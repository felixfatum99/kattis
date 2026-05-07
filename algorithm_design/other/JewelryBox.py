def volume(l, w, h):
    if l <= 0 or l >= min(w / 2, h / 2):
        return 0  # Return 0 if l is out of bounds
    return l * (w - 2 * l) * (h - 2 * l)

def find_optimal_l(w, h, step=0.00001):
    max_volume = 0
    optimal_l = 0
    l = 0
    while l < min(w / 2, h / 2):
        current_volume = volume(l, w, h)
        if current_volume > max_volume:
            max_volume = current_volume
            optimal_l = l
        l += step
    return max_volume

for i in range(int(input())):
    x, y = map(int, input().split(" "))
    print(find_optimal_l(x, y))

