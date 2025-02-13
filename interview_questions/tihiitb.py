# You are given a 2D matrix grid of size 3 x 3 consisting only of characters 'B' and 'W'. Character 'W' represents the white color, and character 'B' represents the black color.
# Your task is to change the color of at most one cell so that the matrix has a 2 x 2 square where all cells are of the same color.
# Return true if it is possible to create a 2 x 2 square of the same color, otherwise, return false.
# Example 1:
# Input: grid = [["B","W","B"],["B","W","W"],["B","W","B"]]
# Output: true
# Explanation:
# It can be done by changing the color of the grid[0][2].


def canMakeSquare(grid) -> bool:
    count_black_00 = 0
    count_black_01 = 0
    count_black_10 = 0
    count_black_11 = 0

    if grid[0][0] == "B":
        count_black_00 += 1

    if grid[0][1] == "B":
        count_black_00 += 1
        count_black_01 += 1

    if grid[0][2] == "B":
        count_black_01 += 1

    if grid[1][0] == "B":
        count_black_00 += 1
        count_black_10 += 1

    if grid[1][1] == "B":
        count_black_10 += 1
        count_black_11 += 1
        count_black_00 += 1
        count_black_01 += 1

    if grid[1][2] == "B":
        count_black_11 += 1
        count_black_01 += 1

    if grid[2][0] == "B":
        count_black_10 += 1

    if grid[2][1] == "B":
        count_black_11 += 1
        count_black_10 += 1

    if grid[2][2] == "B":
        count_black_11 += 1

    white_00 = 4 - count_black_00
    white_01 = 4 - count_black_01
    white_10 = 4 - count_black_10
    white_11 = 4 - count_black_11

    return 1 in (
        count_black_00,
        count_black_01,
        count_black_10,
        count_black_11,
        white_00,
        white_01,
        white_10,
        white_11,
    ) or 0 in (
        count_black_00,
        count_black_01,
        count_black_10,
        count_black_11,
        white_00,
        white_01,
        white_10,
        white_11,
    )