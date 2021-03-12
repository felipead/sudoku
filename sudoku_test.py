from typing import List

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

    def test_load_input_string(self):
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
