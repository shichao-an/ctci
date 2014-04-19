class GraphNode(object):
    def __init__(self, data):
        self.data = data
        self.visited = False
        self.adjacent = []


class Graph(object):
    def __init__(self, *nodes):
        self.nodes = nodes
        self.reset()

    def reset(self):
        # Initialize states of all node
        for node in self.nodes:
            node.visited = False
