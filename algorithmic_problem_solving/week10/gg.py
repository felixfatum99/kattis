import random 

class crop:
    def __init__(self, samples=100000):
        self.mx = float('inf')
        self._mx = -float('inf')
        self.my = float('inf')
        self._my = -float('inf')
        self.area = 0
        self.crop_circles = []
        self.samples = samples
    
    def add_crop_circle(self, x,  y, r):
        self.crop_circles.append((x, y, r))
        self.update_boundary(x, y, r)

    def update_boundary(self, x, y, r):
        self.mx = min(self.mx, x-r)
        self._mx = max(self._mx, x+r)
        self.my = min(self.my, y-r)
        self._my = max(self._my, y+r)
    
    def calculate_area(self):
        self.area = (self._mx - self.mx) * (self._my - self.my)

    def estimate_area(self):
        estimate = 0
        for _ in range(self.samples):
            estimate += self.inside_crop_circle()
        return (self.area * estimate) / self.samples
    
    def inside_crop_circle(self):
        rx = random.uniform(self.mx, self._mx)
        ry = random.uniform(self.my, self._my)
        for x, y, r in self.crop_circles:
            dx = rx - x
            dy = ry - y
            if dx*dx + dy*dy <= r*r:
                return 1
        return 0

MC = crop()
n = int(input())

for _ in range(n):
    x, y, r = map(int, input().split())
    MC.add_crop_circle(x, y, r)

MC.calculate_area()
print(MC.estimate_area())