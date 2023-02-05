import sys
from typing import List

correct_board_bw = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]
correct_board_wb = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]


def row_col_list_input() -> (int, int, List[List[str]]):
    row, col = map(int, input().split())
    input_board = [input().strip() for _ in range(row)]
    return row, col, input_board


def cut_board(board: List[List[str]], row_index: int, col_index: int) -> List[List[str]]:
    eight_eight_board = [row[col_index:col_index + 8] for row in board[row_index:row_index + 8]]
    return eight_eight_board


def min_counter(board: List[List[str]]):
    count_bw = 0
    count_wb = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != correct_board_bw[i][j]:
                count_bw += 1
            if board[i][j] != correct_board_wb[i][j]:
                count_wb += 1
    return min(count_wb, count_bw)


def solution():
    row, col, input_board = row_col_list_input()
    count_min = sys.maxsize

    for i in range(row - 7):
        for j in range(col - 7):
            extracted_board = cut_board(input_board, i, j)
            count_min = min(count_min, min_counter(extracted_board))
    print(count_min)


solution()
