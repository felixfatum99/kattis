from collections import deque

def generate_knight_moves():
    """Generates all possible knight moves on a chessboard."""
    return [(2, 1), (2, -1), (-2, 1), (-2, -1), 
            (1, 2), (1, -2), (-1, 2), (-1, -2)]

def is_valid_position(x, y):
    """Checks if a position is valid on the 8x8 chessboard."""
    return 0 <= x < 8 and 0 <= y < 8

def algebraic_notation(x, y):
    """Converts board coordinates to algebraic notation."""
    return f"{chr(x + ord('a'))}{y + 1}"

def knight_moves_from_position(start):
    """Computes the maximum knight jumps for all positions on the board."""
    knight_moves = generate_knight_moves()
    start_x, start_y = ord(start[0]) - ord('a'), int(start[1]) - 1
    
    # BFS to calculate distances
    queue = deque([(start_x, start_y, 0)])  # (x, y, distance)
    visited = set()
    max_distance = 0
    distance_map = {}
    
    while queue:
        x, y, dist = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        distance_map[(x, y)] = dist
        max_distance = max(max_distance, dist)
        
        for dx, dy in knight_moves:
            nx, ny = x + dx, y + dy
            if is_valid_position(nx, ny) and (nx, ny) not in visited:
                queue.append((nx, ny, dist + 1))
    
    # Find positions that take the maximum number of jumps
    max_jump_positions = [algebraic_notation(x, y) for (x, y), d in distance_map.items() if d == max_distance]
    return max_distance, sorted(max_jump_positions)

def generate_chessboard_knight_dict():
    """Generates a dictionary of knight's longest paths on a chessboard."""
    chessboard = {}
    for x in range(8):
        for y in range(8):
            position = algebraic_notation(x, y)
            chessboard[position] = knight_moves_from_position(position)
    return chessboard

def sort_positions_by_jumps(knight_dict):
    """Sorts positions by the number of jumps and then alphabetically."""
    sorted_positions = sorted(
        knight_dict.items(),
        key=lambda item: (-item[1][0], item[0])  # Sort by jumps (desc) then alphabetically
    )
    return sorted_positions

knight_dict = generate_chessboard_knight_dict()

sorted_knight_positions = sort_positions_by_jumps(knight_dict)

n = int(input())
for _ in range(n):
    position = input()
    res = ""
    for l in sorted_knight_positions:
        if l[0] == position:
            res = 
    print(knight_dict[position][0], " ".join(map(str, knight_dict[position][1])))

