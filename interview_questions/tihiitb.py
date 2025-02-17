# You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents the white color, and character 'B' represents the black color.
# Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the same color.
# Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.
# Example 1:
# Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
# Output: true
# Explanation:
# It can be done by changing the color of the grid[0][2].


def canMakeSquare(grid):
    square_00 = 0
    square_01 = 0
    square_10 = 0
    square_11 = 0
    if grid[0][0] == "B":
        square_00 += 1
    if grid[0][1] == "B":
        square_00 += 1
        square_01 += 1
    if grid[0][2] == "B":
        square_01 += 1
    if grid[1][0] == "B":
        square_00 + 1
        square_10 == 1
    if grid[1][1] == "B":
        square_10 += 1
        square_11 += 1
        square_01 += 1
        square_00 += 1
    if grid[1][2] == "B":
        square_01 += 1
        square_11 += 1
    if grid[2][0] == "B":
        square_10 += 1
    if grid[2][1] == "B":
        square_10 += 1
        square_11 += 1
    if grid[2][2] == "B":
        square_11 += 1
    print(square_00, square_01, square_10, square_11)
    b_square_00 = 4 - square_00
    b_square_01 = 4 - square_01
    b_square_10 = 4 - square_10
    b_square_11 = 4 - square_11
    return 1 in (
        square_00,
        square_01,
        square_10,
        square_11,
        b_square_00,
        b_square_01,
        b_square_10,
        b_square_11,
    ) or 0 in (
        square_00,
        square_01,
        square_10,
        square_11,
        b_square_00,
        b_square_01,
        b_square_10,
        b_square_11,
    )


grid = [["B", "W", "B"], ["B", "W", "W"], ["B", "W", "B"]]
print(canMakeSquare([["B","W","B"],["B","W","W"],["B","W","W"]]))
