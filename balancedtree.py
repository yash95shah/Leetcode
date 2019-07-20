def isBalanced(root):
    root_N = Node(root, left=None, right=None)
    if calculateHeight(root_N) > -1:
        return True
    else:
        return False


def calculateHeight(root):
    if root is None: return 0

    h1 = calculateHeight(root.left)
    h2 = calculateHeight(root.right)

    if h1 == -1 or h2 == -1: return -1


if abs(h1 - h2) > 1:
    return -1
else:
    return Math.max(h1 + 1, h2 + 1)
