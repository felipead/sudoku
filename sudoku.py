from typing import List, Dict


class SudokuBoard:
    def __init__(self, size=9):
        self._board = [
            [0 for _ in range(size)]
            for _ in range(size)
        ]

    @property
    def size(self) -> int:
        return len(self._board)

    def get(self, row: int, column: int) -> int:
        return self._board[row][column]

    def get_row(self, row: int) -> List[int]:
        return list(self._board[row])

    def set(self, row: int, column: int, element: int):
        self._board[row][column] = element

    def load(self, input_string: str):
        row = 0
        column = 0

        for element in input_string:
            self.set(row, column, int(element))

            column += 1

            if column % self.size == 0:
                row += 1
                column = 0

    def validate_rows(self) -> bool:
        occurrences = self._new_occurrences_map()

        for row in range(self.size):
            for element in self.get_row(row):
                self._register_occurrence(occurrences, element)

            if not self._check_occurrences(occurrences):
                return False

            self._reset_occurrences(occurrences)

        return True

    def validate_columns(self) -> bool:
        occurrences = self._new_occurrences_map()

        for column in range(self.size):
            for row in range(self.size):
                element = self.get(row, column)
                self._register_occurrence(occurrences, element)

            if not self._check_occurrences(occurrences):
                return False

            self._reset_occurrences(occurrences)

        return True

    def validate_cells(self) -> bool:
        occurrences = self._new_occurrences_map()
        cell_indexes = self._build_cell_indexes()

        for column in cell_indexes:
            for row in cell_indexes:

                for column_offset in range(3):
                    for row_offset in range(3):
                        element = self.get(row + row_offset, column + column_offset)
                        self._register_occurrence(occurrences, element)

                if not self._check_occurrences(occurrences):
                    return False

                self._reset_occurrences(occurrences)

        return True

    def _new_occurrences_map(self) -> Dict[int, int]:
        return {(i + 1): 0 for i in range(self.size)}

    @staticmethod
    def _register_occurrence(occurrences: Dict[int, int], element: int):
        occurrences[element] += 1

    @staticmethod
    def _check_occurrences(occurrences: Dict[int, int]) -> bool:
        for count in occurrences.values():
            if count != 1:
                return False

        return True

    @staticmethod
    def _reset_occurrences(occurrences: Dict[int, int]):
        for i in occurrences:
            occurrences[i] = 0

    def _build_cell_indexes(self):
        return [
            (i * 3)
            for i in range(self.size // 3)
        ]
