graph = { 
 '5' : ['3','7'], 
 '3' : ['2', '4'], 
 '7' : ['8'], 
 '2' : [], 
 '4' : ['8'], 
 '8' : [] 
} 
visited = [] 
queue = [] 
dfs_visited = set() 
def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m,end = " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)




def dfs(dfs_visited,graph,node):
    if node not in dfs_visited:
        print(node,end = " ")
        dfs_visited.add(node)

        for neighbour in graph[node]:
            dfs(dfs_visited,graph,neighbour)


bfs(visited, graph, '3')
print("\n")
dfs(dfs_visited,graph,'3') 