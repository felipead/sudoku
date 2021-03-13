from typing import List

from parameterized import parameterized

from sudoku import SudokuBoard


def printable_row(row: List[int]) -> str:
    return ''.join([str(i) for i in row])


class TestSudokuBoard:

    def test_build_empty_9x9_board(self):
        board = SudokuBoard()
        assert board.size == 9
        for row in range(9):
            for column in range(9):
                assert board.get(row, column) == 0

    def test_load_input_string_representing_a_9x9_board(self):
        input_string = (
            '957613284'
            '483257196'
            '612849537'
            '178364952'
            '524971368'
            '369528741'
            '845792613'
            '291436875'
            '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert printable_row(board.get_row(0)) == '957613284'
        assert printable_row(board.get_row(1)) == '483257196'
        assert printable_row(board.get_row(2)) == '612849537'
        assert printable_row(board.get_row(3)) == '178364952'
        assert printable_row(board.get_row(4)) == '524971368'
        assert printable_row(board.get_row(5)) == '369528741'
        assert printable_row(board.get_row(6)) == '845792613'
        assert printable_row(board.get_row(7)) == '291436875'
        assert printable_row(board.get_row(8)) == '736185429'

    def test_validate_rows_when_all_rows_are_valid(self):
        input_string = (
            '957613284'
            '483257196'
            '612849537'
            '178364952'
            '524971368'
            '369528741'
            '845792613'
            '291436875'
            '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert board.validate_rows() is True

    @parameterized.expand([
        ['123456788'],
        ['111111111'],
        ['178364953']
    ])
    def test_validate_rows_when_a_row_is_invalid(self, invalid_row):
        input_string = (
                '957613284' +
                '483257196' +
                '612849537' +
                invalid_row +
                '524971368' +
                '369528741' +
                '845792613' +
                '291436875' +
                '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert board.validate_rows() is False

    def test_validate_columns_when_all_columns_are_valid(self):
        input_string = (
            '957613284'
            '483257196'
            '612849537'
            '178364952'
            '524971368'
            '369528741'
            '845792613'
            '291436875'
            '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert board.validate_columns() is True

    def test_validate_columns_when_a_column_is_invalid(self):
        input_string = (
            '957613284'
            '483257196'
            '612849537'
            '178364952'
            '524791368'  # <= swapping values from the fifth row in the fourth column
            '369528741'
            '845792613'
            '291436875'
            '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert board.validate_columns() is False

    def test_validate_3x3_cells_when_all_cells_are_valid(self):
        input_string = (
            '957613284'
            '483257196'
            '612849537'
            '178364952'
            '524971368'
            '369528741'
            '845792613'
            '291436875'
            '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert board.validate_cells() is True

    def test_validate_3x3_cells_when_all_one_cell_is_not_valid(self):
        bogus = '8'
        input_string = (
                '957613284'
                '483257196'
                '612849537'
                '178364952'
                '5249' + bogus + '1368' +
                '369528741'
                '845792613'
                '291436875'
                '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert board.validate_cells() is False

    def test_validate_a_board_that_is_completely_valid(self):
        input_string = (
            '957613284'
            '483257196'
            '612849537'
            '178364952'
            '524971368'
            '369528741'
            '845792613'
            '291436875'
            '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert board.validate() is True

    def test_validate_a_board_that_is_invalid(self):
        input_string = (
            '957613284'
            '483257196'
            '612849537'
            '178634952'
            '524971368'
            '369528741'
            '845792613'
            '291436875'
            '736185429'
        )
        board = SudokuBoard()
        board.load(input_string)

        assert board.validate() is False
