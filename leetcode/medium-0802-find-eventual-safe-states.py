def safe_nodes(graph: list[list[int]]) -> list[int]:
    def is_safe(node: int, visited: set[int] | None = None) -> bool:
        # node is terminal
        if not graph[node]:
            return True

        # convenient initialization
        if visited is None:
            visited = set()

        visited.add(node)

        # node is not terminal so check neighbors for cycles or unsafe nodes
        for neighbor in graph[node]:
            if neighbor in visited:
                return False

            if not is_safe(neighbor, visited):
                return False

        return True

    return [n for n in range(len(graph)) if is_safe(n)]


def test():
    assert safe_nodes([[1, 2], [2, 3], [5], [0], [5], [], []]) == [2, 4, 5, 6]
    assert safe_nodes([[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]) == [4]


test()
