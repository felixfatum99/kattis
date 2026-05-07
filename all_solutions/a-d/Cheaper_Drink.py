def flip(m):
    if any(d in m for d in "23457"):
        return m
    flipped = m[::-1].translate(str.maketrans("69", "96"))
    return min(m, flipped)

n = int(input())
nums = [flip(input().strip()) for _ in range(n)]

for i in range(1, len(nums)):
    key = nums[i]
    j = i - 1
    while j >= 0 and key + nums[j] < nums[j] + key:
        nums[j + 1] = nums[j]
        j -= 1
    nums[j + 1] = key

print("".join(nums))