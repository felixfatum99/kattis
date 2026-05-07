class Node:
    def __init__(self, value="", children=None, index=None, is_root=False):
        self.is_root = is_root
        self.value = value
        self.children = [] if children is None else children
        self.index = index     

class SuffixTree:
    def __init__(self):
        self.root = Node("", is_root=True)

    def _lcp(self, a, b):
        k = 0
        while k < len(a) and k < len(b) and a[k] == b[k]:
            k += 1
        return k

    def insert(self, word):
        word = word + "$"

        for i in range(len(word), -1, -1):
            suffix = word[i:]
            parent = self.root

            while True:
                if suffix == "":
                    break

                child = None
                for ch in parent.children:
                    if ch.value and ch.value[0] == suffix[0]:
                        child = ch
                        break

                if child is None:
                    parent.children.append(Node(suffix, [], i))
                    break

                edge = child.value
                k = self._lcp(edge, suffix)

                if k == len(edge):
                    parent = child
                    suffix = suffix[k:]
                    continue

                common = edge[:k]
                edge_rem = edge[k:]
                suf_rem = suffix[k:]

                mid = Node(common, [], None)

                parent.children.remove(child)
                parent.children.append(mid)

                child.value = edge_rem
                mid.children.append(child)

                if suf_rem:
                    mid.children.append(Node(suf_rem, [], i))
                else:
                    mid.index = i
                break
    
    def lrs_length(self):
        best = 0

        def dfs(node, depth):
            nonlocal best

            leaf_count = 1 if node.index is not None else 0

            for child in node.children:
                add = len(child.value.replace("$", ""))
                leaf_count += dfs(child, depth + add)

            if leaf_count >= 2:
                best = max(best, depth)

            return leaf_count

        dfs(self.root, 0)
        return best



input()
tree = SuffixTree()
tree.insert(input())
print(tree.lrs_length())
