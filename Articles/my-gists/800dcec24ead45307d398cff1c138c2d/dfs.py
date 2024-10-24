def dfs(graph, node, visited):
    if not visited[node]:
        visited[node] = True
        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs(graph, neighbor, visited)
