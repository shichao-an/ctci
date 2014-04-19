from __future__ import print_function
from graph import Graph, GraphNode


def search(g, start, end):
    """DFS search"""
    if start is None or end is None:
        return False
    if not g.nodes:
        return False
    start.visited = True
    for node in start.adjacent:
        if node.visited is False:
            if node == end:
                return True
            else:
                return search(g, node, end)
    return False


def search2(g, start, end):
    """BFS search"""
    if start is None or end is None:
        return False
    if not g.nodes:
        return False
    queue = []
    start.visited = True
    queue.append(start)
    while queue:
        root = queue.pop(0)
        for node in root.adjacent:
            if node.visited is False:
                if node == end:
                    return True
                else:
                    node.visited = True
                queue.append(node)
    return False


def _test():
    pass
    node1 = GraphNode(1)
    node2 = GraphNode(2)
    node3 = GraphNode(3)
    node4 = GraphNode(4)
    node1.adjacent.append(node2)
    node2.adjacent.append(node3)
    node4.adjacent.append(node3)
    graph1 = Graph(node1, node2, node3, node4)
    """
    1 --> 2 --> 3 <-- 4
    """
    assert search(graph1, node1, node4) is False
    graph1.reset()
    assert search(graph1, node2, node3) is True
    graph1.reset()
    assert search2(graph1, node1, node4) is False
    graph1.reset()
    assert search2(graph1, node2, node3) is True
    graph1.reset()


def _print():
    pass


if __name__ == '__main__':
    _test()
    _print()
