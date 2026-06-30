class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s=set()

        for i in range(0,len(board)):
            for j in range(0,len(board)):
                if board[i][j] != "." and board[i][j] in s:
                    return False
                s.add(board[i][j])
            s=set()
        
        for i in range(0,len(board)):
            for j in range(0,len(board)):
                if board[j][i] != "." and board[j][i] in s:
                    return False
                s.add(board[j][i])
            s=set()
        
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):

                s = set()

                for i in range(row, row + 3):
                    for j in range(col, col + 3):

                        if board[i][j] == ".":
                            continue

                        if board[i][j] in s:
                            return False

                        s.add(board[i][j])

        return True