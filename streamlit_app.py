# main.py
import streamlit as st
import time

st.title('Algo-Rhythm 🎼')
st.sidebar.header('Algo List')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    'Which algorithm do you want?',
    ('DP, Dynamic Programming', 'Greedy', 'Brute Forcing', 'Sorting', 'Shortest Path',
     'Binary Search', 'BFS, Breadth First Search', 'DFS, Depth First Search')
)

if add_selectbox == 'Shortest Path':
    st.header('DIJKSTRA')
    with st.expander('Source'):
        code = '''import heapq # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph} # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0 # 시작 값은 0이어야 함
    q = []
    heapq.heappush(q, [distances[start], start]) # 시작 노드부터 탐색 시작 하기 위함.

    while q:
        cur_dis, cur_des = heapq.heappop(q) # 탐색 할 노드, 거리를 가져옴.

        if distances[cur_des] < cur_dis: # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        
        for new_des, new_dis in graph[cur_des].items():
            dis = cur_dis + new_dis # 해당 노드를 거쳐 갈 때 거리
            if dis < distances[new_des]: # 알고 있는 거리 보다 작으면 갱신
                distances[new_des] = dis
                heapq.heappush(q, [dis, new_des]) # 다음 인접 거리를 계산 하기 위해 큐에 삽입
            
    return distances

n=int(input())
m=int(input())
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
        code='''INF = int(1e9)

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
        code='''# 벨만 포드 알고리즘 소스코드
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

def bf(start):
    # 시작 노드에 대해서 초기화
    dist[start] = 0
    # 전체 n번의 라운드(round)를 반복
    for i in range(n):
        # 매 반복마다 "모든 간선"을 확인하며
        for j in range(m):
            cur = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]
            # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if dist[cur] != INF and dist[next_node] > dist[cur] + cost:
                dist[next_node] = dist[cur] + cost
                # n번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
                if i == n - 1:
                    return True
    return False

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 모든 간선에 대한 정보를 담는 리스트 만들기
edges = []
# 최단 거리 테이블을 모두 무한으로 초기화
dist = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    edges.append((a, b, c))

# 벨만 포드 알고리즘을 수행
negative_cycle = bf(1)  # 1번 노드가 시작 노드

if negative_cycle:
    print(-1)
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        # 도달할 수 없는 경우, -1을 출력
        if dist[i] == INF:
            print(-1)
        # 도달할 수 있는 경우 거리를 출력
        else:
            print(dist[i])'''
        st.code(code, language='python')
