



init python:
    import random

    class RiverFactory(NoRollback):

        def __setstate__(self, state):
            self.start = 0
            vars(self).update(state)
            self.init()

        def __init__(self, image, count, xspeed, yspeed, border, start, fast,
                    xspawn=(0,0), yspawn=(0,0), ybottom=None):
            self.image = renpy.easy.displayable(image)
            self.count = count
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.fast = fast
            self.xspawn = xspawn
            self.yspawn = yspawn
            self.ybottom = ybottom  # 👈 new bottom boundary
            self.init()

        def init(self):
            self.starts = [random.uniform(0, self.start) for _ in range(self.count)]
            self.starts.append(self.start)
            self.starts.sort()

        def create(self, particles, st):

            def ranged(n):
                if isinstance(n, tuple):
                    return random.uniform(n[0], n[1])
                else:
                    return n

            if (st == 0) and not particles and self.fast:
                rv = []
                for _i in range(self.count):
                    rv.append(RiverParticle(self.image,
                                            ranged(self.xspeed),
                                            ranged(self.yspeed),
                                            self.border,
                                            st,
                                            random.uniform(0, 100),
                                            fast=True,
                                            xspawn=self.xspawn,
                                            yspawn=self.yspawn,
                                            ybottom=self.ybottom))
                return rv

            if particles is None or len(particles) < self.count:
                if particles and st < self.starts[len(particles)]:
                    return None

                return [RiverParticle(self.image,
                                    ranged(self.xspeed),
                                    ranged(self.yspeed),
                                    self.border,
                                    st,
                                    random.uniform(0, 100),
                                    fast=False,
                                    xspawn=self.xspawn,
                                    yspawn=self.yspawn,
                                    ybottom=self.ybottom)]

        def predict(self):
            return [self.image]


    class RiverParticle(NoRollback):

        def __init__(self, image, xspeed, yspeed, border, start, offset,
                    fast, xspawn=(0,0), yspawn=(0,0), ybottom=None):
            if xspeed == 0 and yspeed == 0:
                xspeed = 50  # avoid stuck particles

            self.image = image
            self.xspeed = xspeed
            self.yspeed = yspeed
            self.border = border
            self.start = start
            self.offset = offset
            self.xspawn = xspawn
            self.yspawn = yspawn
            self.ybottom = ybottom

            sw = renpy.config.screen_width
            sh = renpy.config.screen_height

            # Spawn position within given ranges
            self.xstart = random.uniform(xspawn[0], xspawn[1])
            self.ystart = random.uniform(yspawn[0], yspawn[1])

            if fast:
                self.xstart = random.uniform(xspawn[0], xspawn[1])
                self.ystart = random.uniform(yspawn[0], yspawn[1])

        def update(self, st):
            to = st - self.start

            xpos = self.xstart + to * self.xspeed
            ypos = self.ystart + to * self.yspeed

            sw = renpy.config.screen_width
            sh = renpy.config.screen_height

            # remove when fully offscreen horizontally
            if xpos > sw + self.border or xpos < -self.border:
                return None

            # remove when below bottom boundary
            bottom_limit = self.ybottom if self.ybottom is not None else sh
            if ypos > bottom_limit + self.border or ypos < -self.border:
                return None

            return int(xpos), int(ypos), to + self.offset, self.image


    def River(d,
            count=80,
            border=50,
            xspeed=(100, 300),   # horizontal flow range
            yspeed=(-20, 20),    # vertical wobble range
            start=0,
            fast=False,
            xspawn=(0, 800),     # spawn x-range
            yspawn=(400, 450),   # spawn y-range
            ybottom=None):       # optional bottom boundary
        """
        Creates a river effect using particles with x/y spawn ranges and bottom boundary.
        """
        return Particles(RiverFactory(image=d,
                                    count=count,
                                    border=border,
                                    xspeed=xspeed,
                                    yspeed=yspeed,
                                    start=start,
                                    fast=fast,
                                    xspawn=xspawn,
                                    yspawn=yspawn,
                                    ybottom=ybottom))



init python:
    import random, math

    class DustFactory(NoRollback):

        def __init__(self, image, count, xradius, yradius, center, speed=(0.5, 1.5), start=0, fast=False):
            self.image = renpy.easy.displayable(image)
            self.count = count
            self.xradius = xradius
            self.yradius = yradius
            self.center = center  # (x_center, y_center)
            self.speed = speed
            self.start = start
            self.fast = fast
            self.init()

        def init(self):
            self.starts = [random.uniform(0, self.start) for _ in range(self.count)]
            self.starts.append(self.start)
            self.starts.sort()

        def create(self, particles, st):

            def ranged(n):
                if isinstance(n, tuple):
                    return random.uniform(n[0], n[1])
                else:
                    return n

            if (st == 0) and not particles and self.fast:
                return [DustParticle(self.image,
                                    self.center,
                                    self.xradius,
                                    self.yradius,
                                    ranged(self.speed),
                                    random.uniform(0, 360),
                                    st,
                                    fast=True) for _ in range(self.count)]

            if particles is None or len(particles) < self.count:
                if particles and st < self.starts[len(particles)]:
                    return None

                return [DustParticle(self.image,
                                    self.center,
                                    self.xradius,
                                    self.yradius,
                                    ranged(self.speed),
                                    random.uniform(0, 360),
                                    st,
                                    fast=False)]

        def predict(self):
            return [self.image]


    class DustParticle(NoRollback):

        def __init__(self, image, center, xradius, yradius, speed, angle, start, fast):
            self.image = image
            self.cx, self.cy = center
            self.xradius = xradius
            self.yradius = yradius
            self.speed = speed  # degrees per second
            self.angle = angle  # starting angle in degrees
            self.start = start

            if fast:
                self.angle = random.uniform(0, 360)

        def update(self, st):
            t = st - self.start
            theta = math.radians((self.angle + self.speed * t) % 360)

            x = self.cx + self.xradius * math.cos(theta)
            y = self.cy + self.yradius * math.sin(theta)

            return int(x), int(y), t, self.image


    def Dust(d,
            count=20,
            xradius=100,
            yradius=50,
            center=None,
            speed=(20, 60),
            start=0,
            fast=False):

        # Set default center at runtime
        if center is None:
            sw = renpy.config.screen_width
            sh = renpy.config.screen_height
            center = (sw // 2, sh // 2)

        return Particles(DustFactory(image=d,
                                    count=count,
                                    xradius=xradius,
                                    yradius=yradius,
                                    center=center,
                                    speed=speed,
                                    start=start,
                                    fast=fast))




init python:
    import random, math

    class RadiateFactory(NoRollback):

        def __init__(self, image, count, speed=(100, 300), border=50, start=0, fast=False, center=None):
            self.image = renpy.easy.displayable(image)
            self.count = count
            self.speed = speed
            self.border = border
            self.start = start
            self.fast = fast

            if center is None:
                self.center = (renpy.config.screen_width // 2, renpy.config.screen_height // 2)
            else:
                self.center = center

            self.init()

        def init(self):
            self.starts = [random.uniform(0, self.start) for _ in range(self.count)]
            self.starts.append(self.start)
            self.starts.sort()

        def create(self, particles, st):

            def ranged(n):
                if isinstance(n, tuple):
                    return random.uniform(n[0], n[1])
                else:
                    return n

            if (st == 0) and not particles and self.fast:
                return [RadiateParticle(self.image,
                                        self.center,
                                        ranged(self.speed),
                                        random.uniform(0, 360),
                                        st,
                                        fast=True) for _ in range(self.count)]

            if particles is None or len(particles) < self.count:
                if particles and st < self.starts[len(particles)]:
                    return None

                return [RadiateParticle(self.image,
                                        self.center,
                                        ranged(self.speed),
                                        random.uniform(0, 360),
                                        st,
                                        fast=False)]

        def predict(self):
            return [self.image]


    class RadiateParticle(NoRollback):

        def __init__(self, image, center, speed, angle, start, fast):
            self.image = image
            self.cx, self.cy = center
            self.speed = speed
            self.angle = math.radians(angle)  # random direction
            self.start = start

            if fast:
                # Start a bit away from center
                dist = random.uniform(0, 30)
                self.cx += math.cos(self.angle) * dist
                self.cy += math.sin(self.angle) * dist

        def update(self, st):
            t = st - self.start

            x = self.cx + math.cos(self.angle) * self.speed * t
            y = self.cy + math.sin(self.angle) * self.speed * t

            sw = renpy.config.screen_width
            sh = renpy.config.screen_height

            if x < -100 or x > sw + 100 or y < -100 or y > sh + 100:
                return None  # particle has exited screen

            return int(x), int(y), t, self.image


    def Radiate(d,
                count=30,
                speed=(150, 300),
                border=50,
                start=0,
                fast=False,
                center=None):
        """
        Radiates particles outward from the center.
        `d` - particle sprite (spark, dust puff, etc.)
        """
        return Particles(RadiateFactory(image=d,
                                        count=count,
                                        speed=speed,
                                        border=border,
                                        start=start,
                                        fast=fast,
                                        center=center))



