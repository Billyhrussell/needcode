# determine 9x9 sudoku board valid

# each row must contain 1-9
# each col must contain 1-9
# each 3x3 must contain 1-9

# 3 maps
# row, col, 3x3
# check if row has all nums
# check if col has all nums
# basically check if there are duplicates?
# import collections
# def check_sudoku(matrix):

#     rows = collections.defaultdict(list)
#     cols = collections.defaultdict(list)
#     box = collections.defaultdict(list)
#     squares = [[set() for x in range(3)] for y in range(3)]

#     for i, row in enumerate(matrix):
#         for x, col in enumerate(row):
#             if col != ".":
#                 cols[x].append(col)


#     for i, row in enumerate(matrix):
#         for x, col in enumerate(row):
#             for j in range(0,3):
#                 box[i].append(row[])

#     for i in range(3):
#         for j in range(3):
#             box[i]

#     print(box)

matrix = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]




def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """

    # create empty set
    rows = [set() for x in range(9)]
    columns = [set() for x in range(9)]
    squares = [[set() for x in range(3)] for y in range(3)]

    print(rows)

    for x in range(9):
        for y in range(9):
            cell_value = board[x][y]

            if cell_value == ".":
                continue
            if cell_value in rows[x] or cell_value in columns[y] or cell_value in squares[x//3][y//3]:
                return False

            rows[x].add(cell_value)
            columns[y].add(cell_value)
            squares[x//3][y//3].add(cell_value)

    print("rows ", rows)
    return True

print(isValidSudoku(matrix))


