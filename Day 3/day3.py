class TreeNode(object):
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class Code:

    def serialize(self, root):
        result = []

        def depth(node):
            if not node:
                result.append("N")
                return
            result.append(str(node.value))
            depth(node.left)
            depth(node.right)
        return ",".join(result)

    def deserialize(self, data):
        value = data.split(",")
        self.i = 0

        def depth():
            if value[self.i] == "N":
                self.i += 1
                return None
            node = TreeNode(int(value[self.i]))
            self.i += 1
            node.left = depth()
            node.right = depth()
            return node
        return depth()
