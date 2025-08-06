def max_fish(grid: list[list[int]]) -> int:
    n: int = len(grid)
    m: int = len(grid[0])

    def dfs(r: int, c: int, visited: set[tuple[int, int]] | None = None) -> int:
        if not grid[r][c]:
            return 0

        if visited is None:
            visited = set()

        visited.add((r, c))

        search: list[int] = []
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and (nr, nc) not in visited:
                search.append(dfs(nr, nc, visited))

        return grid[r][c] + max(search)

    ans = [dfs(r, c) for r in range(n) for c in range(m) if grid[r][c]]
    return max(ans, default=0)


def test():
    assert max_fish([[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]) == 7
    assert max_fish([[1, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 1]]) == 1


test()
