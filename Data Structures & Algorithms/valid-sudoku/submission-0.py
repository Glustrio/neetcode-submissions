class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for i in range(9)]
        col = [set() for i in range(9)]
        box = [set() for i in range(9)]

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                boxIndex = (i // 3) * 3 + (j//3)
                if val != '.':
                    if val in row[i]:
                        return False
                    if val in col[j]:
                        return False
                    if val in box[boxIndex]:
                        return False
                    row[i].add(val)
                    col[j].add(val)
                    box[boxIndex].add(val)
        return True