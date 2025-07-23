import streamlit as st
import numpy as np

st.set_page_config(page_title="Glow Tic-Tac-Toe ✨", layout="centered")

st.markdown("""
    <style>
    .title {
        text-align: center;
        color: #FF4B4B;
        font-size: 40px;
        font-weight: bold;
    }
    .game-cell button {
        height: 100px !important;
        font-size: 40px !important;
    }
    </style>
    <div class='title'>🌟 Tic-Tac-Toe Glow ✨</div>
""", unsafe_allow_html=True)

# Session state setup
if 'board' not in st.session_state:
    st.session_state.board = [''] * 9
    st.session_state.winner = None

# Winning combinations
def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),
            (0,3,6), (1,4,7), (2,5,8),
            (0,4,8), (2,4,6)]
    for i, j, k in wins:
        if board[i] == board[j] == board[k] and board[i] != '':
            return board[i], (i, j, k)
    if '' not in board:
        return 'Draw', ()
    return None, ()

# Minimax algorithm
def minimax(board, is_maximizing):
    result, _ = check_winner(board)
    if result == '⭕': return 1
    if result == '❌': return -1
    if result == 'Draw': return 0

    if is_maximizing:
        best = -np.inf
        for i in range(9):
            if board[i] == '':
                board[i] = '⭕'
                score = minimax(board, False)
                board[i] = ''
                best = max(score, best)
        return best
    else:
        best = np.inf
        for i in range(9):
            if board[i] == '':
                board[i] = '❌'
                score = minimax(board, True)
                board[i] = ''
                best = min(score, best)
        return best

# AI move
def ai_move():
    best = -np.inf
    move = None
    for i in range(9):
        if st.session_state.board[i] == '':
            st.session_state.board[i] = '⭕'
            score = minimax(st.session_state.board, False)
            st.session_state.board[i] = ''
            if score > best:
                best = score
                move = i
    if move is not None:
        st.session_state.board[move] = '⭕'

# Display board
winner, win_combo = check_winner(st.session_state.board)
cols = st.columns(3)
for i in range(3):
    for j in range(3):
        idx = 3 * i + j
        cell = st.session_state.board[idx]
        glow_style = "background-color: #00FFCC;" if idx in win_combo else ""
        with cols[j]:
            if st.button(cell or " ", key=idx, help="Click to play!", use_container_width=True):
                if st.session_state.board[idx] == '' and not winner:
                    st.session_state.board[idx] = '❌'
                    winner, _ = check_winner(st.session_state.board)
                    if not winner:
                        ai_move()
                        winner, win_combo = check_winner(st.session_state.board)

# Show result
if winner:
    if winner == 'Draw':
        st.warning("🤝 It's a draw! You're almost as smart as the AI.")
    elif winner == '❌':
        st.balloons()
        st.success("🎉 Wow! You defeated the AI! You’re a legend!")
    else:
        st.error("💀 Oops! AI won again. Try harder, human!")

# Reset
if st.button("🔁 Restart Game"):
    st.session_state.board = [''] * 9
    st.session_state.winner = None
    st.rerun()
