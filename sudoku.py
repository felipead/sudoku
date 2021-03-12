from typing import List

# http://www.cross-plus-a.com/sudoku.htm
# 957613284483257196612849537178364952524971368369528741845792613291436875736185429
#
# 957613284
# 483257196
# 612849537

# 3x3 cell
# rows
# columns

class SudokuValidationError(Exception):
    pass


Board = List[List[int]]


def build_empty_board() -> Board:
    return [
        [
            None for i in range(0,9)
        ] for i in range(0,9)
    ]


def build_sudoku_board(input_string: str) -> Board:
    board = build_empty_board()

    row_idx = 0
    column_idx = 0

    for number in input_string:
        board[row_idx][column_idx] = number
        column_idx += 1
        if column_idx % 9 == 0:
            row_idx += 1
            column_idx = 0

    return board


def validate_columns(board: Board):
    check = {i: 0 for i in range(1,9)}

    for column in board:
        for number in column:
            check[number] += 1

        for c in check.values():
            if c != 1:
                raise SudokuValidationError('Invalid column')

        # TODO: reset check dict


def validate_rows(board: Board):
    check = {i: 0 for i in range(1,9)}

    for column_idx in range(0,9):
        for row_idx in range(0,9):
            check[board[row_idx][column_idx]] += 1

        for c in check.values():
            if c != 1:
                raise SudokuValidationError('Invalid row')

        # TODO: reset check dict


def validate_3x3cell(board: Board):
    check = {i: 0 for i in range(1,9)}

    cell_row_idx = 0
    cell_column_idx = 0

    for cell_row_idx in (0, 2, 6):
        for cell_column_idx in (0, 2, 6):

            for column_idx in range(cell_column_idx, cell_column_idx+3):
                for row_idx in range(row_column_idx, row_column_idx+3):
                    check[board[row_idx][column_idx]] += 1

            for c in check.values():
                if c != 1:
                    raise SudokuValidationError('Invalid 3x3 cell')

            # TODO: reset check dict


def validate_sudoku(input_string: str) -> bool:
    board = build_sudoku_board(input_string)

    validate_columns(board)
    validate_rows(board)
    validate_3x3cell(board)
