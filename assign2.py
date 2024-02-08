class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def postorder_traversal(root):
    if not root:
        return []

    result = []
    for child in root.children:
        result.extend(postorder_traversal(child))

    result.append(root.val)
    return result

# Example usage:
def build_tree(nodes):
    if not nodes:
        return None

    root_val = nodes.pop(0)
    root = Node(val=root_val)
    stack = [root]

    while stack and nodes:
        current_node = stack.pop()

        children_count = int(nodes.pop(0))
        current_node.children = [Node(val=int(nodes.pop(0))) for _ in range(children_count)]
        stack.extend(reversed(current_node.children))

    return root

# Example usage:
nodes = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
root = build_tree(nodes)
output = postorder_traversal(root)

print("Postorder Traversal Output:", output)