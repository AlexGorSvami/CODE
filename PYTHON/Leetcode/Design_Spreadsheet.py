class Spreadsheet:

    def __init__(self, rows: int):
        self.cells = [[0] * 26 for _ in range(rows)]

    def setCell(self, cell: str, value: int) -> None:
        row = int(cell[1:]) - 1 
        col = ord(cell[0]) - ord('A')
        self.cells[row][col] = value 

    def resetCell(self, cell: str) -> None:
        row = int(cell[1:]) - 1 
        col = ord(cell[0]) - ord('A')
        self.cells[row][col] = 0 

    def getValue(self, formula: str) -> int:
        x, y = formula[1:].split('+')
        if x[0].isalpha():
            row1 = int(x[1:]) - 1 
            col1 = ord(x[0]) - ord('A')
            x_value = self.cells[row1][col1]
        else:
            x_value = int(x)
        if y[0].isalpha():
            row2 = int(y[1:]) - 1 
            col2 = ord(y[0]) - ord('A')
            y_value = self.cells[row2][col2]
        else:
            y_value = int(y)
        return x_value + y_value 


