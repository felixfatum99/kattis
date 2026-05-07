n = int(input())
print("Gomes:")
for i in range(n):
    list = [int(x) for x in input().split()]
    list_ordered = sorted(list)
    list_ordered_reversed = sorted(list, reverse=True)
    print("Ordered" if list == list_ordered or list == list_ordered_reversed  else "Unordered")