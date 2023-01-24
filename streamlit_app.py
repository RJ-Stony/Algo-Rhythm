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
    col1, col2, col3 = st.columns(3)
    
    with col1:
        with st.expander('DIJKSTRA'):
            code = '''def hello():
                        print("Hello, Streamlit!")'''
            st.code(code, language='python')

    with col2:
        st.header('Floyd Warshall')
        st.button('This is Floyd Warshall')

    with col3:
        st.header('Bellman Ford')
        st.button('This is Bellman Ford')
