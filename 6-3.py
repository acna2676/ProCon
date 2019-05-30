import math

class Point:
    def __init__(self, x_ini, y_ini):
        self.x = x_ini
        self.y = y_ini

def koch(n, a, b):
    if n == 0:
        return 0

    th = math.pi * 60.0 / 180.0
    s = Point(0,0)
    t = Point(0,0)
    u = Point(0,0)
    s.x = (2.0 * a.x + 1.0 * b.x) / 3.0
    s.y = (2.0 * a.y + 1.0 * b.y) / 3.0
    t.x = (1.0 * a.x + 2.0 * b.x) / 3.0
    t.y = (1.0 * a.y + 2.0 * b.y) / 3.0
    u.x = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
    u.y = (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y

    koch(n-1, a, s)
    print(s.x, s.y)
    koch(n-1, s, u)
    print(t.x, t.y)
    koch(n-1, u, t)
    print(u.x, u.y)
    koch(n-1, t, b)


n = int(input())

a = Point(0,0)
b = Point(100,0)

print(a.x, a.y)
koch(n, a, b)
print(b.x, b.y)

