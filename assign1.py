class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []

def deserialize(serialization):
    if not serialization:
        return None

    values = serialization.split(',')
    root_val = values.pop(0)
    if root_val == 'None':
        return None

    root = Node(int(root_val))
    queue = [root]

    while queue and values:
        current = queue.pop(0)
        children_count = int(values.pop(0))

        for _ in range(children_count):
            child_val = values.pop(0)
            if child_val != 'None':
                child = Node(int(child_val))
                current.children.append(child)
                queue.append(child)

    return root

# Example usage:
serialization = "1,3,2,5,None,6,None,2,None,4,None"
root = deserialize(serialization)