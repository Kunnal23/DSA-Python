from collections import deque

def addEdge(adj,u,v):
    adj[u].append(v)
    adj[v].append(u)

def printGraph(adj):
    for l in adj:
        print(l)

def BFS(adj,s):
    visited = [False]*len(adj)
    q=deque()
    q.append(s)
    visited[s] = True
    while q:
        s = q.popleft()
        print(s, end = " ")
        for u in adj[s]:
            if visited[u] == False:
                q.append(u)
                visited[u]= True
                

adj = [[] for i in range(4)]
addEdge(adj,0,1)
addEdge(adj,0,2)
addEdge(adj,1,2)
addEdge(adj,1,3)
printGraph(adj)
BFS(adj,0)