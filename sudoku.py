from typing import List


class SudokuBoard:
    """
    http://www.cross-plus-a.com/sudoku.htm
    """

    def __init__(self, size=9):
        self._board = [
            [
                0
                for _ in range(size)
            ]
            for _ in range(size)
        ]

    @property
    def size(self) -> int:
        return len(self._board)

    def get(self, row: int, column: int) -> int:
        return self._board[row][column]

    def get_row(self, row: int) -> List[int]:
        return list(self._board[row])

    def set(self, row: int, column: int, value: int):
        self._board[row][column] = value

    def load(self, input_string: str):
        row = 0
        column = 0

        for value in input_string:
            self.set(row, column, int(value))

            column += 1

            if column % self.size == 0:
                row += 1
                column = 0

    def validate_rows(self) -> bool:
        occurrences = {(i + 1): 0 for i in range(9)}

        for row in range(9):
            for value in self.get_row(row):
                occurrences[value] += 1

            for count in occurrences.values():
                if count != 1:
                    return False

            for i in occurrences:
                occurrences[i] = 0

        return True

    def validate_columns(self) -> bool:
        occurrences = {(i + 1): 0 for i in range(9)}

        for column in range(9):
            for row in range(9):
                value = self.get(row, column)
                occurrences[value] += 1

            for count in occurrences.values():
                if count != 1:
                    return False

            for i in occurrences:
                occurrences[i] = 0

        return True

# Draft/Legacy code below ↓

#
# class SudokuValidationError(Exception):
#     pass
#
# def build_sudoku_board(input_string: str) -> Board:
#     row_idx = 0
#     column_idx = 0
#
#     for number in input_string:
#         board[row_idx][column_idx] = number
#         column_idx += 1
#         if column_idx % 9 == 0:
#             row_idx += 1
#             column_idx = 0
#
#     return board
#
#
# def validate_columns(board: Board):
#     check = {i: 0 for i in range(1,9)}
#
#     for column in board:
#         for number in column:
#             check[number] += 1
#
#         for c in check.values():
#             if c != 1:
#                 raise SudokuValidationError('Invalid column')
#
#         # TODO: reset check dict
#
#
# def validate_rows(board: Board):
#     check = {i: 0 for i in range(1,9)}
#
#     for column_idx in range(0,9):
#         for row_idx in range(0,9):
#             check[board[row_idx][column_idx]] += 1
#
#         for c in check.values():
#             if c != 1:
#                 raise SudokuValidationError('Invalid row')
#
#         # TODO: reset check dict
#
#
# def validate_3x3cell(board: Board):
#     check = {i: 0 for i in range(1,9)}
#
#     cell_row_idx = 0
#     cell_column_idx = 0
#
#     for cell_row_idx in (0, 2, 6):
#         for cell_column_idx in (0, 2, 6):
#
#             for column_idx in range(cell_column_idx, cell_column_idx+3):
#                 for row_idx in range(row_column_idx, row_column_idx+3):
#                     check[board[row_idx][column_idx]] += 1
#
#             for c in check.values():
#                 if c != 1:
#                     raise SudokuValidationError('Invalid 3x3 cell')
#
#             # TODO: reset check dict
#
#
# def validate_sudoku(input_string: str) -> bool:
#     board = build_sudoku_board(input_string)
#
#     validate_columns(board)
#     validate_rows(board)
#     validate_3x3cell(board)
