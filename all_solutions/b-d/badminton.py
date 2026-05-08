def correct_determine_set(a, b):
    # returns correct result based on badminton rules
    if a > 30 or b > 30:
        return "!"
    if a == 30 and b == 30:
        return "!"
    if a == b:
        if a >= 30:
            return "!"
        else:
            return "?"
    diff = abs(a - b)
    if max(a, b) < 21:
        return "?"
    if max(a, b) < 30 and diff == 2:
        return "A" if a > b else "B"
    if max(a, b) == 30:
        return "A" if a > b else "B"
    if max(a, b) > 21 and diff != 2:
        return "?"
    return "?"

def your_determine_set(a, b):
    _max = max(a, b)
    _min = min(a, b)

    if a == b and a == 30:
        return "!"
    elif a == 30 and b == 29:
        return "A"
    elif b == 30 and a == 29:
        return "B"
    elif _max > 21 and (_min < 20 or _max-_min > 2):
        return "!"
    elif a == b:
        return  "?"
    elif a < 21 and b < 21:
        return  "?"
    elif _max > 21 and _max-_min != 2:
        return "?"
    elif _max == 21 and _min == 20:
        return "?"
    elif a >= 21 and b < a:
        return "A"
    elif b >= 21 and a < b:
        return "B"
    elif a > 21 and a-b == 2:
        return "A"
    elif b > 21 and b-a == 2:
        return "B"

# Run over all scores 0–30
wrong = []
for a in range(31):
    for b in range(31):
        yours = your_determine_set(a, b)
        correct = correct_determine_set(a, b)
        if yours != correct:
            wrong.append((a, b, yours, correct))

print(f"Found {len(wrong)} mismatches out of 961 possible single-set scores.\n")
print("Some examples:")
for (a, b, yours, correct) in wrong[:30]:
    print(f"{a:02d}-{b:02d}: yours={yours}, expected={correct}")
