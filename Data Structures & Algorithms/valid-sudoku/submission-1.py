class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #dictionaries are initialized to keep track of duplicates
        rows = {}
        cols = {}
        boxes = {}
        
        for row in range(9):
            for col in range(9):
                value = board[row][col]
                # '//' is flat division where solution's decimal part is disregarded. ex : 5 // 3 = 1.666 but only 1 is considered.
                # also below steps are done to know which among 9 sqares the current value belongs
                box_row = row // 3
                box_col = col // 3

                if value == ".":
                    continue
                # setdefault(key, default) does two things in one line:
                #If key doesn't exist → create it with the default value
                #If key already exists → do nothing, leave it as is
                rows.setdefault(row, set()) 
                cols.setdefault(col, set()) 
                boxes.setdefault((box_row, box_col), set())

                if value in rows[row] or value in cols[col] or value in boxes[(box_row, box_col)]:
                    return False

                rows[row].add(value)
                cols[col].add(value)
                boxes[(box_row, box_col)].add(value)
        return True

## tip : google how the rows and cols and boxes dictionaries look of this problem.