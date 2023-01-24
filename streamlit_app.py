# main.py
import streamlit as st
import time

st.title('Algo-Rhythm 🎼')
st.sidebar.header('Algo List')

# Using object notation
add_selectbox = st.sidebar.selectbox(
    'Which algorithm do you want?',
    ('DP, Dynamic Programming', 'Greedy', 'Brute Forcing', 'Sorting',
     'Binary Search', 'BFS, Breadth First Search', 'DFS, Depth First Search',
     'Floyd Warshall')
)


