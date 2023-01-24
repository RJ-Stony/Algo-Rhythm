# main.py
import streamlit as st
import time

st.title('_Algo_-**:blue[_Rhythm_]** 🎷')
st.sidebar.header('Algo List')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    'Which algorithm do you want?',
    ('DP, Dynamic Programming', 'Greedy', 'Brute Forcing', 'Sorting', 'Shortest Path',
     'Binary Search', 'BFS, Breadth First Search', 'DFS, Depth First Search')
)

if add_selectbox == 'Shortest Path':
    st.header('Dijkstra')
    with st.expander('Source'):
        code = '''# To implement a priority queue.
import heapq 

def dijkstra(graph, start):
    # To save the distance value from start.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0 # Start value must be 0
    q = []
    
    # To start the search from the start node.
    heapq.heappush(q, [distances[start], start]) 

    while q:
        # Get the node to explore, the distance.
        cur_dis, cur_des = heapq.heappop(q)
        
        # If it's longer than the existing distance, you don't even need to look.
        if distances[cur_des] < cur_dis: 
            continue
        
        for new_des, new_dis in graph[cur_des].items():
            # Distance when going through that node
            dis = cur_dis + new_dis
            
            # Update if less than known distance.
            if dis < distances[new_des]: 
                distances[new_des] = dis
                # Insert into queue to calculate next neighbor distance
                heapq.heappush(q, [dis, new_des])
            
    return distances

n = int(input())
m = int(input())
graph = dict()
for i in range(n+1):
    graph[i] = {}

for _ in range(m):
    dep, des, pri = map(int, input().split())
    if des in graph[dep].keys():
        if graph[dep][des] > pri:
            graph[dep][des] = pri
    else:
        graph[dep][des] = pri

start, end = map(int, input().split())
print(dijkstra(graph, start)[end])'''
        st.code(code, language='python')
        
    st.header('Floyd Warshall')
    with st.expander('Source'):
        code='''# Set 1 billion to mean INF
INF = int(1e9)

n = int(input())
m = int(input())

graph = [[INF] * (n+1) for _ in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1, n+1):
    for b in range(1, n+1):
        if graph[a][b] == INF:
            print(0, end=" ")
        else:
            print(graph[a][b], end=" ")
    print()'''
        st.code(code, language='python')

    st.header('Bellman Ford')
    with st.expander('Source'):
        code='''# Set 1 billion to mean INF
INF = int(1e9)

def bfs(start):
    # Initialize on the start node.
    dist[start] = 0
    # Repeat all n rounds.
    for i in range(n):
        # Every iteration it checks all edges
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # If the distance to another node via the current edge is shorter
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # If the value is updated even in the nth round, there is a negative cycle.
                if i == n - 1:
                    return True
    return False

# Get the number of nodes and the number of edges.
n, m = map(int, input().split())
# Create a list containing information about all edges.
edges = []
# Initialize all shortest distance tables to INF.
dist = [INF] * (n + 1)

# Get all edge information input.
for _ in range(m):
    a, b, c = map(int, input().split())
    # This means that the cost of going from node a to node b is c.
    edges.append((a, b, c))

# Perform Bellman Ford Algorithm.
negative_cycle = bfs(1) # Node 1 is the starting node

if negative_cycle:
    print(-1)
else:
    # Output the shortest distance to go to all other nodes except node 1.
    for i in range(2, n+1):
        # Output -1 if unreachable.
        if dist[i] == INF:
            print(-1)
        # Output distance if reachable.
        else:
            print(dist[i])'''
        st.code(code, language='python')
