import math

def move(x, y, direction_deg, distance):
    rad = direction_deg * math.pi / 180
    x += distance * math.cos(rad)
    y += distance * math.sin(rad)
    return x, y

def normalize(angle):
    angle = angle % 360
    if angle >= 180:
        angle -= 360
    return angle

while True:
    n = int(input())

    if n == 0:
        break
    
    end_x, end_y = 0, 0
    end_coordinates = []

    for i in range(n):
        instructions = input().split()
        x, y = float(instructions[0]), float(instructions[1])
        current_direction = 0

        for j in range(2, len(instructions), 1):
            if instructions[j-1] == 'start':
                current_direction = float(instructions[j])
            elif instructions[j-1] == 'turn':
                current_direction = normalize(current_direction + float(instructions[j]))
            elif instructions[j-1] == 'walk':
                x, y = move(x, y, current_direction, float(instructions[j]))
        
        end_x += x
        end_y += y
        end_coordinates.append((x, y))
    
    end_x /= n
    end_y /= n

    print(end_x, end_y, end=" ")

    worst_dist = -float('inf')
    for pos in end_coordinates:
        worst_dist = max(worst_dist, math.dist((end_x, end_y), pos))
    
    print(worst_dist)