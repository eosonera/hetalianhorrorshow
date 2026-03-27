####################################################################################
## Dark text tag ######################################################################
####################################################################################

init python:

    renpy.register_textshader(
        "shadow",
        variables="""
        uniform vec4 u__shadow_color;
        uniform vec2 u__offset;
        uniform float u__radius;
        uniform float u__spread;
        uniform vec2 u_model_size;

        varying vec2 v__uv;
        attribute vec2 a_tex_coord;
        """,

        vertex_300="""
        v__uv = a_tex_coord;
        """,

        fragment_300="""
        vec2 texel = 1.0 / u_model_size;
        vec2 base_uv = v__uv + (u__offset / u_model_size);

        float shadow_alpha = 0.0;
        float total = 0.0;

        // Gaussian blur kernel (square, radial falloff)
        for (float x = -u__radius; x <= u__radius; x += 1.0) {
            for (float y = -u__radius; y <= u__radius; y += 1.0) {
                float dist = length(vec2(x, y));
                float weight = exp(-(dist * dist) / (2.0 * u__spread * u__spread));

                vec2 uv = base_uv + vec2(x, y) * texel;
                shadow_alpha += texture2D(tex0, uv).a * weight;
                total += weight;
            }
        }

        shadow_alpha /= total;

        vec4 shadow = vec4(u__shadow_color.rgb,
                        shadow_alpha * u__shadow_color.a);

        vec4 text = texture2D(tex0, v__uv);

        // outline included in shader
        gl_FragColor = shadow * (1.0 - text.a) + text;
        """,

        u__shadow_color="#000000",
        u__offset=(-5.0, -5.0),
        u__radius=9.0,
        u__spread=4.0,
    )




    def dark_text_tag(tag, argument, contents):
        return (
            [(renpy.TEXT_TAG, u"shader=shadow"), (renpy.TEXT_TAG, "color=#767c8a"), (renpy.TEXT_TAG, "outlinecolor=#434959")]
            + contents +
            [(renpy.TEXT_TAG, "/outlinecolor"), (renpy.TEXT_TAG, "/color"), (renpy.TEXT_TAG, u"/shader")]
        )
    config.custom_text_tags["dark"] = dark_text_tag




####################################################################################
## Wrap tiled ######################################################################
####################################################################################

## Wrapping effect adapted from Marquee for Ren'Py by Feniks: https://feniksdev.itch.io/marquee-for-renpy

init -1 python:
    import math
    from renpy.display.render import Render
    from renpy.python import NoRollback

    class WrapTiledDisplayable(NoRollback, renpy.Displayable):
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


####################################################################################
## Shaker ##########################################################################
####################################################################################

init python:
    from renpy.python import NoRollback
    import random

    class Shaker(NoRollback, object):
        def __init__(self, child, dist, interval):
            # Use the child's current placement as the starting point
            self.start = child.get_placement()
            self.dist = dist
            self.interval = interval
            self.child = child

        def __call__(self, t, sizes):
            def fti(x, r):
                if x is None:
                    x = 0
                if isinstance(x, float):
                    return int(x * r)
                else:
                    return x

            xpos, ypos, xanchor, yanchor = [fti(a, b) for a, b in zip(self.start, sizes)]
            xpos -= xanchor
            ypos -= yanchor

            if self.interval > 0:
                step = int(t / self.interval)
            else:
                step = int(t * 1000)

            random.seed(step)  # stable offset during each interval

            nx = xpos + (1.0 - t) * self.dist * (random.random() * 2 - 1)
            ny = ypos + (1.0 - t) * self.dist * (random.random() * 2 - 1)

            return (int(nx), int(ny), 0, 0)


    class ShakeFactory(object):
        def __init__(self, time, dist, interval, properties):
            self.time = time
            self.dist = dist
            self.interval = interval
            self.properties = properties

        def __call__(self, child):
            move = Shaker(child, dist=self.dist, interval=self.interval)
            return renpy.display.motion.Motion(
                move,
                self.time,
                child,
                add_sizes=True,
                **self.properties
            )


    def Shake(time, dist=100.0, interval=0.05, **properties):
        """
        time     = duration of shake (seconds)
        dist     = max displacement in pixels
        interval = fraction of animation duration before new jitter
        """
        return ShakeFactory(time, dist, interval, properties)


define sshake = Shake(time=1, dist=20, interval=0.01)
define sshake1 = Shake(time=1, dist=15, interval=0.01)
define sshake_long = Shake(time=5, dist=9.0, interval=0.005)




#define sshake1 = DiagonalJitterTransform(dist=40, duration=3.0)



####################################################################################
## Shaker1 ##########################################################################
####################################################################################

init python:
    import random
    from renpy.python import NoRollback

    def jitter_diagonal_func(dist=50, duration=2.0, interval=0.1):
        """
        Returns a Ren'Py transform function that jitters an image
        diagonally up to 'dist' every 'interval' seconds, for 'duration' seconds.
        """

        def f(trans, st, at):
            # st = time since this transform started
            # at = time since this transform was shown on screen

            if st > duration:
                # Reset to normal once duration expires
                trans.xoffset = 0
                trans.yoffset = 0
                return None

            # Work out which "step" we are in
            step = int(st / interval)

            if step % 2 == 0:
                # Random diagonal move
                dx = random.choice([-1, 1]) * random.randint(0, dist)
                dy = random.choice([-1, 1]) * random.randint(0, dist)
                trans.xoffset = dx
                trans.yoffset = dy
            else:
                # Move back to origin
                trans.xoffset = 0
                trans.yoffset = 0

            return interval  # ask Ren'Py to call us again after `interval` seconds

        return f

    
transform jitter_diagonal(dist=50, duration=0.5):
    function jitter_diagonal_func(dist, duration)


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



####################################################################################
## Ripple shader ###################################################################
####################################################################################

transform ripple:
    function RippleShader(amp=0.2, period=30.0, speed=15.0, duration=1)

transform ripple2:
    function RippleShader(amp=1, period=10.0, speed=15.0, duration=1)

init python:
    renpy.register_shader("ripple", variables="""
        uniform float u_shader_time;
        uniform vec2 u_wave_period;
        uniform vec2 u_wave_amp;
        uniform vec2 u_wave_speed;
        uniform float u_intensity;
        uniform vec2 u_center;
        uniform vec2 u_resolution;
        
        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
    """, vertex_200="""
        v_coords = a_tex_coord;
    """, fragment_300="""
        // Convert center position from screen coordinates to UV coordinates
        vec2 center_uv = u_center / u_resolution;
        vec2 to_uv = v_coords - center_uv;
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
            self.start_time = None

        def __call__(self, trans, st, at):
            if self.start_time is None:
                self.start_time = st
            
            elapsed = st - self.start_time
            
            if elapsed >= self.duration:
                # Clear the shader
                trans.shader = None
                trans.mesh = False
                return None  # Stop the transition
            
            if self.first_time or trans.shader != 'ripple':
                trans.shader = 'ripple'
                trans.mesh = True
                trans.u_shader_time = 0.0
                trans.u_wave_period = self.period
                trans.u_wave_amp = self.amp
                trans.u_wave_speed = self.speed
                trans.u_center = ((config.screen_width/2), (config.screen_height/2))
                trans.u_resolution = (config.screen_width, config.screen_height)
                self.first_time = False

            fade_in_time = 0.3
            fade_out_time = 0.3
            t = min(elapsed, self.duration)

            # intensity
            if t < fade_in_time:
                intensity = t / fade_in_time
            elif t > self.duration - fade_out_time:
                intensity = max(0.0, (self.duration - t) / fade_out_time)
            else:
                intensity = 1.0
            trans.u_intensity = intensity

            # clamp shader time
            trans.u_shader_time = t

            # Return a small interval to keep the transition running
            return 0.01




####################################################################################
## Squares ################################################
####################################################################################

init python:
    import random

    class SquareScatter(renpy.display.transition.Transition):
        """
        A transition that divides the old screen into true squares,
        scatters them semi-randomly with a fade-out effect, and reveals the new screen beneath.
        """

        def __init__(self, time=1.0, grid=12, dist=100, old_widget=None, new_widget=None, **properties):

            super(SquareScatter, self).__init__(time, **properties)

            self.time = float(time)
            self.grid = grid
            self.dist = dist

            self.old_widget = old_widget
            self.new_widget = new_widget

            self._random_offsets = None
            self.events = False

        def __call__(self, old_widget, new_widget):
            new_trans = SquareScatter(time=self.time, grid=self.grid, dist=self.dist)
            new_trans.old_widget = old_widget
            new_trans.new_widget = new_widget
            return new_trans

        def render(self, width, height, st, at):

            if st >= self.time:
                self.events = True
                return renpy.render(self.new_widget, width, height, st, at)

            old_r = renpy.render(self.old_widget, width, height, st, at)
            new_r = renpy.render(self.new_widget, width, height, st, at)

            rv = renpy.display.render.Render(width, height)

            # ensure true squares
            cell_size = int(min(width, height) // self.grid)
            cols = int((width + cell_size - 1) // cell_size)
            rows = int((height + cell_size - 1) // cell_size)

            progress = st / self.time

            # Draw new image first
            rv.blit(new_r, (0, 0))

            # number of active squares shrinks over time
            max_squares = cols * rows
            active_squares = int(max_squares * (1 - progress))

            # Lazy init cells
            if not hasattr(self, "_cells"):
                self._cells = [(gx, gy) for gx in range(cols) for gy in range(rows)]
                random.shuffle(self._cells)
                self._last_shuffle = st

            if st - self._last_shuffle > 0.07:
                random.shuffle(self._cells)
                self._last_shuffle = st

            for gx, gy in self._cells[:active_squares]:
                x = gx * cell_size
                y = gy * cell_size
                w = min(cell_size, width - x)
                h = min(cell_size, height - y)

                # jump, but keep dx/dy per cell stable between reshuffles
                if not hasattr(self, "_offsets"):
                    self._offsets = {}
                if (gx, gy) not in self._offsets or st - self._last_shuffle < 0.05:
                    self._offsets[(gx, gy)] = (
                        random.randint(-self.dist, self.dist),
                        random.randint(-self.dist, self.dist)
                    )
                dx, dy = self._offsets[(gx, gy)]

                sx = int(x + dx * progress)
                sy = int(y + dy * progress)

                subsurf = old_r.subsurface((x, y, w, h))
                rv.blit(subsurf, (sx, sy))

            renpy.redraw(self, 0)
            return rv


####################################################################################
## Old film shader ###################################################################
####################################################################################

transform old_film_distort_x:
    function OldFilmShader(intensity=4, stretch=0.2, speed=2.0, period=10, direction="x", duration=1)

transform old_film_distort_x1:
    function OldFilmShader(intensity=2, stretch=0.2, speed=10.0, period=4, direction="x", duration=1)

init python:
    renpy.register_shader("old_film", variables="""
        uniform float u_shader_time;
        uniform float u_intensity;
        uniform float u_stretch;
        uniform float u_speed;
        uniform float u_vertical;  // 1.0 = vertical, 0.0 = horizontal
        uniform vec2 u_resolution;
        uniform float u_wave_freq;

        uniform sampler2D tex0;
        attribute vec2 a_tex_coord;
        varying vec2 v_coords;
    """, vertex_200="""
        v_coords = a_tex_coord;
    """, fragment_300="""
        vec2 uv = v_coords;

        float wave = sin((u_vertical > 0.5 ? uv.y : uv.x) * u_wave_freq + u_shader_time * u_speed);

        if(u_vertical > 0.5) {
            uv.y += wave * u_stretch * u_intensity;
            uv.x = mix(uv.x, 0.5 + (uv.x - 0.5) * 0.9, u_intensity);
        } else {
            uv.x += wave * u_stretch * u_intensity;
            uv.y = mix(uv.y, 0.5 + (uv.y - 0.5) * 0.9, u_intensity);
        }

        gl_FragColor = texture2D(tex0, uv);
    """)

    def advance_shader_time(trans, st, at):
        trans.u_shader_time = at
        return 0

    class OldFilmShader(object):
        """
        Old film stretch effect with wobble.
        """
        def __init__(self, intensity=1.0, stretch=0.2, speed=2.0, period=10, direction="x", duration=2.0):
            self.intensity = intensity
            self.stretch = stretch
            self.speed = speed
            self.direction = direction
            self.duration = duration
            self.period = period
            self.first_time = True
            self.start_time = None

        def __call__(self, trans, st, at):
            if self.start_time is None:
                self.start_time = st

            elapsed = st - self.start_time
            if elapsed >= self.duration:
                trans.shader = None
                trans.mesh = False
                return None

            if self.first_time or trans.shader != 'old_film':
                trans.shader = 'old_film'
                trans.mesh = True
                trans.u_shader_time = 0.0
                trans.u_stretch = self.stretch
                trans.u_speed = self.speed
                trans.u_wave_freq = self.period
                trans.u_vertical = 1.0 if self.direction.lower() == "x" else 0.0
                trans.u_resolution = (config.screen_width, config.screen_height)
                self.first_time = False

            # Fade in/out intensity
            fade_in_time = 0.3
            fade_out_time = 0.3
            t = min(elapsed, self.duration)
            if t < fade_in_time:
                intensity = t / fade_in_time
            elif t > self.duration - fade_out_time:
                intensity = max(0.0, (self.duration - t) / fade_out_time)
            else:
                intensity = 1.0
            trans.u_intensity = intensity * self.intensity

            trans.u_shader_time = t
            return 0.01


