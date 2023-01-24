# main.py
import streamlit as st
import time

# Using object notation
add_selectbox = st.sidebar.selectbox(
    'Which algorithm do you want?',
    ('DP, Dynamic Programming', 'Greedy', 'Brute Forcing', 'Sorting',
     'Binary Search', 'BFS, Breadth First Search', 'DFS, Depth First Search')
)
