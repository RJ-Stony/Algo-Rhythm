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
        code = '''import heapq    # 우선순위 큐 구현을 위함

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}    # start로 부터의 거리 값을 저장하기 위함
    distances[start] = 0  # 시작 값은 0이어야 함
    q = []
    heapq.heappush(q, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

    while q:
        cur_dis, cur_des = heapq.heappop(q)  # 탐색 할 노드, 거리를 가져옴.

        if distances[cur_des] < cur_dis:   # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue
        
        for new_des, new_dis in graph[cur_des].items():
            dis = cur_dis + new_dis # 해당 노드를 거쳐 갈 때 거리
            if dis < distances[new_des]:   # 알고 있는 거리 보다 작으면 갱신
                distances[new_des] = dis
                heapq.heappush(q, [dis, new_des])   # 다음 인접 거리를 계산 하기 위해 큐에 삽입
            
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
    st.button('This is Floyd Warshall')

    st.header('Bellman Ford')
    st.button('This is Bellman Ford')
