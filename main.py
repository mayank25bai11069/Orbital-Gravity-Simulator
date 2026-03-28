import math
import matplotlib.pyplot as plt
import matplotlib.animation as animation

G = 0.5
time_step = 0.1

class CelestialBody:
    def __init__(self, name, mass, x, y, vx, vy, color, size):
        self.name = name
        self.mass = mass
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.size = size
        self.trail_x = []
        self.trail_y = []

    def get_pull(self, other):
        dx = other.x - self.x
        dy = other.y - self.y
        dist = math.sqrt(dx**2 + dy**2)

        if dist == 0:
            return 0, 0

        f = G * self.mass * other.mass / (dist**2)
        angle = math.atan2(dy, dx)
        return math.cos(angle) * f, math.sin(angle) * f

    def update_vel(self, all_bodies):
        sum_fx = 0
        sum_fy = 0
        for b in all_bodies:
            if b != self:
                fx, fy = self.get_pull(b)
                sum_fx += fx
                sum_fy += fy

        self.vx += (sum_fx / self.mass) * time_step
        self.vy += (sum_fy / self.mass) * time_step

    def move(self):
        self.x += self.vx * time_step
        self.y += self.vy * time_step
        
        self.trail_x.append(self.x)
        self.trail_y.append(self.y)
        
        if len(self.trail_x) > 50:
            self.trail_x.pop(0)
            self.trail_y.pop(0)

sun = CelestialBody("Sun", 1000, 0, 0, 0, 0, 'yellow', 300)
p1 = CelestialBody("Planet A", 10, 50, 0, 0, 2.5, 'cyan', 50)
p2 = CelestialBody("Planet B", 5, -80, 0, 0, -2.0, 'red', 30)
rogue = CelestialBody("Rogue Planet", 300, 150, 150, -4.5, -4.5, 'white', 80)
system = [sun, p1, p2, rogue]

fig, ax = plt.subplots(figsize=(8, 8))
fig.canvas.manager.set_window_title('Gravity Engine')
ax.set_facecolor('black')

dots = ax.scatter([], [], s=[], c=[])
lines = [ax.plot([], [], color=b.color, alpha=0.6)[0] for b in system]

ax.set_xlim(-150, 150)
ax.set_ylim(-150, 150)
ax.set_xticks([])
ax.set_yticks([])

def run_frame(frame):
    for b in system:
        b.update_vel(system)
        
    for b in system:
        b.move()

    dots.set_offsets(list(zip([b.x for b in system], [b.y for b in system])))
    dots.set_sizes([b.size for b in system])
    dots.set_color([b.color for b in system])
    
    for index, b in enumerate(system):
        lines[index].set_data(b.trail_x, b.trail_y)
        
    return dots, *lines

sim = animation.FuncAnimation(fig, run_frame, frames=200, interval=20, blit=True)
plt.show()