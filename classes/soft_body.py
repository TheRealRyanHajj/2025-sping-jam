import pygame, math
from util.grefs import grefs

class Vertex:
    def __init__(self, cords):
        self.x, self.y = cords
        self.oldx, self.oldy = cords
        self.accx = self.accy = 0
        self.radius = 1

    def apply_force(self, fx, fy):
        self.accx += fx
        self.accy += fy

    def update(self, dt):
        vx, vy = self.x - self.oldx, self.y - self.oldy
        self.oldx, self.oldy = self.x, self.y
        dt2 = dt * dt
        self.x += vx + self.accx * dt2
        self.y += vy + self.accy * dt2
        self.accx = self.accy = 0

    def get_normal(self, mask, offset):
        x, y = int(self.x - offset[0]), int(self.y - offset[1])
        try:
            dx = -mask.get_at((x - 1, y)) + mask.get_at((x + 1, y))
            dy = -mask.get_at((x, y - 1)) + mask.get_at((x, y + 1))
        except IndexError:
            return (0, -1)
        mag = math.hypot(dx, dy)
        return (dx / mag, dy / mag) if mag else (0, -1)

    def collide_and_bounce(self, mask, surface_offset=(0, 0), restitution=0.9, friction=0.8):
        x, y = int(self.x - surface_offset[0]), int(self.y - surface_offset[1])
        if not (0 <= x < mask.get_size()[0] and 0 <= y < mask.get_size()[1]):
            return
        if not mask.get_at((x, y)):
            return

        vx, vy = self.x - self.oldx, self.y - self.oldy
        self.x, self.y = self.oldx, self.oldy

        nx, ny = self.get_normal(mask, surface_offset)
        tx, ty = -ny, nx

        v_dot_n = vx * nx + vy * ny
        v_dot_t = vx * tx + vy * ty

        self.oldx = self.x - (-v_dot_n * nx * restitution + v_dot_t * tx * friction)
        self.oldy = self.y - (-v_dot_n * ny * restitution + v_dot_t * ty * friction)

    def draw(self, surf):
        if math.isfinite(self.x) and math.isfinite(self.y):
            pygame.draw.circle(surf, (0, 0, 255), (int(self.x), int(self.y)), self.radius)


class Spring:
    def __init__(self, a: Vertex, b: Vertex, length, stiffness=0.01):
        self.a = a
        self.b = b
        self.length = length
        self.lengthSmall = length
        self.lengthBig = length * 2
        self.stiffness = stiffness

    def update(self):
        dx, dy = self.b.x - self.a.x, self.b.y - self.a.y
        dist = math.hypot(dx, dy)
        if dist == 0:
            return
        percent = (self.length - dist) / dist * 0.5 * self.stiffness
        ox, oy = dx * percent, dy * percent
        self.a.x -= ox
        self.a.y -= oy
        self.b.x += ox
        self.b.y += oy

    def get_color(self):
        dx, dy = self.b.x - self.a.x, self.b.y - self.a.y
        delta = math.hypot(dx, dy) - self.length
        if delta > 0.2:
            return (0, min(255, int(delta * 200)), 0)
        elif delta < -0.2:
            return (min(255, int(-delta * 200)), 0, 0)
        return None

    def goBig(self, is_big):
        self.length = self.lengthBig if is_big else self.lengthSmall


class SoftBody:
    def __init__(self, cords, radius=50, num_points=200):
        self.dt = grefs["TimeMachine"].dt
        self.isBig = False
        self.x = cords[0]
        self.y = cords[1]

        angle_step = 2 * math.pi / num_points
        self.vertexs = [
            Vertex((
                cords[0] + math.cos(i * angle_step) * radius,
                cords[1] + math.sin(i * angle_step) * radius
            )) for i in range(num_points)
        ]

        self.springs = [
            Spring(self.vertexs[i], self.vertexs[j], 
                   math.hypot(self.vertexs[i].x - self.vertexs[j].x,
                              self.vertexs[i].y - self.vertexs[j].y))
            for i in range(num_points) for j in range(i + 1, num_points)
        ]

    def update(self):
        for v in self.vertexs:
            v.apply_force(0, 1000)
            v.collide_and_bounce(grefs["Level"].collideMask, (grefs["Camera"].offsetX,grefs["Camera"].offsetY))
            v.update(self.dt)

        for _ in range(5):
            for s in self.springs:
                s.update()
    
        # Recalculate center position in world coordinates
        self.x = sum(v.x for v in self.vertexs) / len(self.vertexs)
        self.y = sum(v.y for v in self.vertexs) / len(self.vertexs)


    def draw(self, window):
        cam = grefs["Camera"]
        points = [(v.x - cam.offsetX, v.y - cam.offsetY) for v in self.vertexs]
        pygame.draw.polygon(window, (125, 255, 125), points)

    def apply_velocity(self, dx=0, dy=0):
        for v in self.vertexs:
            v.oldx -= dx
            v.oldy -= dy

    def toggleBig(self):
        self.isBig = not self.isBig
        for spring in self.springs:
            spring.goBig(self.isBig)
