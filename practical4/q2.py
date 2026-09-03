import math

def distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def farthest_point(points):
    farthest = points[0]
    max_dist = math.sqrt(farthest[0]**2 + farthest[1]**2)

    for point in points:
        dist = math.sqrt(point[0]**2 + point[1]**2)
        if dist > max_dist:
            max_dist = dist
            farthest = point

    return farthest, max_dist

points = []

n = int(input("Enter number of points: "))

for i in range(n):
    x = float(input(f"Enter x-coordinate of Point {i+1}: "))
    y = float(input(f"Enter y-coordinate of Point {i+1}: "))
    points.append((x, y))      

print("\nList of Points:", points)

i = int(input("\nEnter first point index (1 to n): ")) - 1
j = int(input("Enter second point index (1 to n): ")) - 1

d = distance(points[i], points[j])
print("Distance between", points[i], "and", points[j], "=", d)

point, dist = farthest_point(points)
print("Farthest Point from Origin:", point)
print("Distance from Origin:", dist)