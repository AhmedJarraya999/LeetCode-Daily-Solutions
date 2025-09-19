class Spreadsheet:
    def __init__(self, rows: int):
        # Dictionary to store only modified cells
        self.cells = {}
        self.rows = rows

    def setCell(self, cell: str, value: int) -> None:
        self.cells[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.cells:
            del self.cells[cell]

    def getValue(self, formula: str) -> int:
        # Formula is always like "=X+Y"
        formula = formula[1:]  # remove '='
        x, y = formula.split("+")
        return self._getOperandValue(x) + self._getOperandValue(y)

    def _getOperandValue(self, operand: str) -> int:
        # Operand can be either a number or a cell reference
        if operand.isdigit():
            return int(operand)
        return self.cells.get(operand, 0)
