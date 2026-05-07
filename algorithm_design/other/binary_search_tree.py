class binary_search_tree():
    def __init__(self, value) -> None:
        self.value = value
        self.l = None
        self.r = None
    
    def add(self, y, d):
        current_node = self
        depth = d
        while current_node is not None:
            if current_node.value >= y:
                if current_node.l is None:
                    current_node.l = binary_search_tree(y)
                    return depth
                else:
                    current_node = current_node.l
            else:
                if current_node.r is None:
                    current_node.r = binary_search_tree(y)
                    return depth
                else:
                    current_node = current_node.r
            depth+=1

n = int(input())
depth = 0
y = int(input())
bst = binary_search_tree(y)
print(0)
for i in range(n-1):
    y = int(input())
    depth += bst.add(y, 1)
    print(depth)
