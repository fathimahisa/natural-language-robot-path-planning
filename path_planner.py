import heapq
from typing import List, Tuple, Dict

Coord = Tuple[int, int]

def heuristic(a: Coord, b: Coord) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def neighbors(pos: Coord):
    x, y = pos
    return [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

def astar(grid: List[List[int]], start: Coord, goal: Coord) -> List[Coord]:
    if start == goal:
        return []
    rows, cols = len(grid), len(grid[0])
    open_heap = []
    heapq.heappush(open_heap, (heuristic(start, goal), 0, start))
    came_from: Dict[Coord, Coord] = {}
    g = {start: 0}
    visited = set()

    while open_heap:
        _, current_g, current = heapq.heappop(open_heap)
        if current in visited:
            continue
        visited.add(current)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        for nx, ny in neighbors(current):
            if not (0 <= nx < rows and 0 <= ny < cols):
                continue
            if grid[nx][ny] == 1:
                continue
            tentative_g = current_g + 1
            if tentative_g < g.get((nx, ny), 10**9):
                g[(nx, ny)] = tentative_g
                came_from[(nx, ny)] = current
                f = tentative_g + heuristic((nx, ny), goal)
                heapq.heappush(open_heap, (f, tentative_g, (nx, ny)))

    return []
