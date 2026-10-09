from collections import deque
from typing import Any


def bfs(graph: dict[Any, list[Any]], start: Any) -> list[Any]:
    """
    Perform Breadth-First Search (BFS) on a graph starting from `start` node.
    Returns the list of visited nodes in the traversal order.

    Differences from C++ implementation:
    1. Python leverages `collections.deque` with O(1) `popleft()` and `append()`,
       whereas C++ relies on `std::queue<T>`.
    2. In Python, adjacency lists and visited sets handle arbitrary hashable node types
       without explicit template definitions such as `std::unordered_map<int, std::vector<int>>`.
    3. Checking whether a node is visited uses the idiomatic `if neighbor not in visited:`
       on a `set`, which is much cleaner than C++ iterator checks (`visited.find(v) == visited.end()`).
    """
    if start is None:
        return []

    visited: set[Any] = {start}
    visit_order: list[Any] = []
    queue: deque[Any] = deque([start])

    while queue:
        current = queue.popleft()
        visit_order.append(current)

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return visit_order
