#void traverse(vector<vector<int>>& adj, int node, vector<int>& visited, vector<int>& result) {
#    visited[node] = 1;
#    result.push_back(node);
#    for (int neighbor : adj[node]) {
#        if (!visited[neighbor]) {
#            traverse(adj, neighbor, visited, result);
#        }
#    }
#}

#vector<int> dfs(vector<vector<int>>& adj, int start) {
#    vector<int> visited(adj.size(), 0);
#    vector<int> result;
#    
#    traverse(adj, start, visited, result);
#    return result;
#}

def traverse(adj: list[list[int]], node: int, visited: list[int], result: list[int]) -> None:
    visited[node] = 1
    result.append(node)
    for neighbor in adj[node]:
        if not visited[neighbor]:
            traverse(adj, neighbor, visited, result)

def dfs(adj: list[list[int]], start: int) -> list[int]:
    """Return the DFS visit order from start.

    Python lists are mutable, so the helper updates visited and result
    without C++ reference parameters.
    """
    visited = [0] * len(adj)
    result = []
    
    traverse(adj, start, visited, result)
    return result
