
####################################################################################
## Shaker ##########################################################################
####################################################################################

init python:
    import math

    class Shaker(object):
    
        anchors = {
            'top' : 0.0,
            'center' : 0.5,
            'bottom' : 1.0,
            'left' : 0.0,
            'right' : 1.0,
            }
    
        def __init__(self, start, child, dist):
            if start is None:
                start = child.get_placement()
            #
            self.start = [ self.anchors.get(i, i) for i in start ]  # central position
            self.dist = dist    # maximum distance, in pixels, from the starting point
            self.child = child
            
        def __call__(self, t, sizes):
            # Float to integer... turns floating point numbers to
            # integers.                
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

            xpos = xpos - xanchor
            ypos = ypos - yanchor
            
            nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
            ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

            return (int(nx), int(ny), 0, 0)
    
    def _Shake(start, time, child=None, dist=100.0, **properties):

        move = Shaker(start, child, dist=dist)
    
        return renpy.display.layout.Motion(move,
                    time,
                    child,
                    add_sizes=True,
                    **properties)

    Shake = renpy.curry(_Shake)

    sshake = Shake((0, 0, 0, 0), 1.0, dist=15)


transform shake_delay:
    time 1.5
    sshake


####################################################################################
## Ripple shader ######################################################################
####################################################################################

transform ripple:
    function RippleShader(amp=2.0, period=30.0, speed=5.0, duration=1.0)

init python:
    renpy.register_shader("ripple", variables="""
        uniform float u_shader_time;
        uniform vec2 u_wave_period;
        uniform vec2 u_wave_amp;
        uniform vec2 u_wave_speed;
        uniform float u_intensity;
        
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
    """, vertex_200="""
        v_coords = a_tex_coord;
    """, fragment_300="""
        vec2 center = vec2(0.5, 0.5); 
        vec2 to_uv = v_coords - center;
        float dist = length(to_uv);
        
        // ripple wave (intensity fades in/out externally)
        float wave = sin(u_wave_period.x * dist - u_shader_time * u_wave_speed.x);
        float offset = wave * u_wave_amp.x * 0.01 * u_intensity;

        vec2 new_pos = v_coords + normalize(to_uv) * offset;
        gl_FragColor = texture2D(tex0, new_pos);
    """)

    def advance_shader_time(trans, st, at):
        trans.u_shader_time = at
        return 0

    class RippleShader(object):
        """
        Creates a ripple effect that fades in, ripples a few times, then fades out.
        """
        def __init__(self, amp=5.0, period=40.0, speed=8.0, duration=2.0):
            self.amp = (float(amp), float(amp))
            self.period = (float(period), float(period))
            self.speed = (float(speed), float(speed))
            self.duration = duration
            self.first_time = True

        def __call__(self, trans, st, at):
            if self.first_time or trans.shader != 'ripple':
                trans.shader = 'ripple'
                trans.mesh = True
                trans.u_shader_time = 0.0
                trans.u_wave_period = self.period
                trans.u_wave_amp = self.amp
                trans.u_wave_speed = self.speed
                self.first_time = False

            # Fade in for first 0.3s, stay at 1.0, fade out at end
            fade_in_time = 0.3
            fade_out_time = 0.3
            t = min(at, self.duration)
            if t < fade_in_time:
                intensity = t / fade_in_time
            elif t > self.duration - fade_out_time:
                intensity = max(0.0, (self.duration - t) / fade_out_time)
            else:
                intensity = 1.0

            trans.u_intensity = intensity
            return advance_shader_time(trans, st, at)

####################################################################################
## Wrap tiled ######################################################################
####################################################################################

init python:
    import math
    from renpy.display.render import Render

    class WrapTiledDisplayable(renpy.Displayable):
        def __init__(self, child, speed_x=0.0, speed_y=0.0, init_x=0.0, init_y=0.0, **kwargs):
            super().__init__(**kwargs)
            self.child = renpy.displayable(child)
            self.speed_x = speed_x
            self.speed_y = speed_y
            self.offset_x = init_x
            self.offset_y = init_y
            self.last_st = 0

        def render(self, width, height, st, at):
            # Get transformed child render every frame (accounts for zoom/rotate)
            child_render = renpy.render(self.child, width, height, st, at)
            img_w, img_h = child_render.get_size()
            img_w = max(1, img_w)
            img_h = max(1, img_h)

            delta = st - self.last_st
            self.last_st = st

            sw, sh = renpy.config.screen_width, renpy.config.screen_height

            # Positive speed moves right/down
            self.offset_x = (self.offset_x - self.speed_x * delta) % img_w
            self.offset_y = (self.offset_y - self.speed_y * delta) % img_h

            rv = Render(sw, sh)

            start_x = -self.offset_x
            start_y = -self.offset_y

            # Tile fully across screen
            y = start_y
            while y < sh:
                x = start_x
                while x < sw:
                    rv.blit(child_render, (x, y))
                    x += img_w
                y += img_h

            renpy.redraw(self, 0)
            return rv

    def WrapTiled(child=None, speed_x=0.0, speed_y=0.0, init_x=0.0, init_y=0.0, **properties):
        return WrapTiledDisplayable(child, speed_x=speed_x, speed_y=speed_y,
                                    init_x=init_x, init_y=init_y)



    dust2 = WrapTiled("images/vfx/dust.png", speed_x=7.8, speed_y=2, init_x=146.0, init_y=41.0)

    #wrapmist = WrapTiled("images/vfx/mist.png", speed_x=30, speed_y=20)
    #wrapmist1 = WrapTiled("images/vfx/mist.png", speed_x=20, speed_y=50, init_x=0.0, init_y=200.0)

    

####################################################################################
## Non Looping Transition Animation ################################################
####################################################################################

init python:
    class NonLoopAnimation(renpy.display.anim.TransitionAnimation):
        def render(self, width, height, st, at):
            if self.anim_timebase:
                t = at
            else:
                t = st

            total_time = sum(self.delays)

            if t >= total_time:
                image = self.images[-1]
                im = renpy.display.render.render(image, width, height, t, at)
                width, height = im.get_size()
                rv = renpy.display.render.Render(width, height)
                rv.blit(im, (0, 0))
                return rv

            for image, prev, delay, trans in zip(self.images, self.prev_images, self.delays, self.transitions):
                if t < delay:
                    if not renpy.game.less_updates:
                        renpy.display.render.redraw(self, delay - t)

                    if trans and (self.anim_timebase and at >= self.delays[0]):
                        image = trans(old_widget=prev, new_widget=image)

                    im = renpy.display.render.render(image, width, height, t, at)
                    width, height = im.get_size()
                    rv = renpy.display.render.Render(width, height)
                    rv.blit(im, (0, 0))
                    return rv
                else:
                    t -= delay

            return renpy.display.render.Render(0, 0)


