import json

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def serialize(self):
        return json.dumps({
            "value": self.value,
            "left": "<PUT YOUR CODE TO CALCULATE THIS>",
            "right": "<PUT YOUR CODE TO CALCULATE THIS>"
        })

    @classmethod
    def deserialize(self, string):
        return "Memes"

node = Node(
    100,
    Node(50, Node(40), Node(60, Node(55))),
    Node(101)
)

print(result = node.serialize())
print(Node.deserialize(result)) # --> should be identical to the tree above

# Might be cheating to use json library.. try to do it yourself. 