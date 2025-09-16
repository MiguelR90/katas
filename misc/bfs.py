from collections import deque


type Graph = dict[str, list[str]]


def bfs(graph: Graph, start: str) -> list[str]:
    if start not in graph:
        return []

    path: list[str] = []
    visited: set[str] = set()

    queue: deque[str] = deque([start])

    while queue:
        current = queue.popleft()
        if current in visited:
            continue

        path.append(current)
        visited.add(current)
        for neighbor in graph[current]:
            queue.append(neighbor)

    return path


def test_bfs():
    """Complex BFS test cases as individual assertions."""

    # Assume bfs(graph, start) returns list of nodes in BFS order

    # Complex tree with multiple levels
    # graph1 = {
    #     "A": ["B", "C", "D"],
    #     "B": ["E", "F"],
    #     "C": ["G"],
    #     "D": ["H", "I"],
    #     "E": [],
    #     "F": [],
    #     "G": [],
    #     "H": [],
    #     "I": [],
    # }
    # assert bfs(graph1, "A") == ["A", "B", "C", "D", "E", "F", "G", "H", "I"]

    # Graph with cycles - should handle gracefully
    graph2 = {
        "A": ["B", "C"],
        "B": ["D"],
        "C": ["D"],
        "D": ["A"],  # Back to A
    }
    result2 = bfs(graph2, "A")
    assert len(result2) == 4
    assert result2[0] == "A"
    assert "B" in result2 and "C" in result2 and "D" in result2

    # Diamond pattern
    graph3 = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}
    assert bfs(graph3, "A") == ["A", "B", "C", "D", "E"]

    # Disconnected components - only reachable nodes
    graph4 = {
        "A": ["B"],
        "B": ["C"],
        "C": [],
        "X": ["Y"],  # Disconnected
        "Y": [],
    }
    assert bfs(graph4, "A") == ["A", "B", "C"]
    assert bfs(graph4, "X") == ["X", "Y"]

    # Wide graph - many children at first level
    graph5 = {
        "root": ["A", "B", "C", "D", "E"],
        "A": [],
        "B": [],
        "C": [],
        "D": [],
        "E": [],
    }
    assert bfs(graph5, "root") == ["root", "A", "B", "C", "D", "E"]

    # Deep graph with single path
    graph6 = {"A": ["B"], "B": ["C"], "C": ["D"], "D": ["E"], "E": ["F"], "F": []}
    assert bfs(graph6, "A") == ["A", "B", "C", "D", "E", "F"]

    # Multiple paths to same node
    graph7 = {"S": ["A", "B"], "A": ["C", "T"], "B": ["T"], "C": ["T"], "T": []}
    result7 = bfs(graph7, "S")
    assert result7[0] == "S"
    assert result7[-1] == "T"
    assert len(result7) == 5

    # Self-loops should be handled
    graph8 = {"A": ["A", "B"], "B": ["C"], "C": []}
    assert bfs(graph8, "A") == ["A", "B", "C"]

    # Bidirectional connections (undirected graph)
    graph9 = {"A": ["B", "C"], "B": ["A", "D"], "C": ["A", "D"], "D": ["B", "C"]}
    result9 = bfs(graph9, "A")
    assert len(result9) == 4
    assert result9[0] == "A"
    assert set(result9) == {"A", "B", "C", "D"}

    # Binary tree structure
    graph10 = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F", "G"],
        "D": ["H", "I"],
        "E": ["J", "K"],
        "F": [],
        "G": [],
        "H": [],
        "I": [],
        "J": [],
        "K": [],
    }
    result10 = bfs(graph10, "A")
    assert result10[:3] == ["A", "B", "C"]  # First level
    assert result10[3:7] == ["D", "E", "F", "G"]  # Second level
    assert len(result10) == 11

    # Numeric nodes with complex connections
    graph11 = {
        "1": ["2", "3", "4"],
        "2": ["5", "6"],
        "3": ["7"],
        "4": ["8", "9", "10"],
        "5": ["11"],
        "6": ["12"],
        "7": [],
        "8": [],
        "9": [],
        "10": [],
        "11": [],
        "12": [],
    }
    result11 = bfs(graph11, "1")
    assert result11[0] == "1"
    assert set(result11[1:4]) == {"2", "3", "4"}  # Level 1
    assert len(result11) == 12

    # Empty graph
    graph12 = {}
    assert bfs(graph12, "A") == []

    # Start node not in graph
    graph13 = {"A": ["B"], "B": []}
    assert bfs(graph13, "Z") == []
