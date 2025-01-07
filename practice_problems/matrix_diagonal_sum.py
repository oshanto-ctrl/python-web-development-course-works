"""
Matrix Diagonal Sum
Problem Statement:
Given a square matrix of size N x N, calculate the sum of the primary and secondary
diagonals.
Input Format:
• The first line contains an integer N, the size of the matrix.
• The next N lines each contain N integers separated by spaces, representing the
matrix.
Output Format:
Output two integers separated by a space:
• The sum of the primary diagonal.
• The sum of the secondary diagonal.
Example:
 Input:
3
1 2 3
4 5 6
7 8 9
Output:
15 15
Explanation:
• Primary diagonal: 1+5+9=15
• Secondary diagonal: 3+5+7=15
"""
def getDiagonalSum(n, arr):
    """ Functiont to calculate primary and secondary diagonal
        values sum of a NxN matrix.
    """
    primary_diagonal_sum = 0
    secondary_digaonal_sum = 0

    for i in range(n):
        primary_diagonal_sum += arr[i][i]
    
    for i in range(n):
        secondary_digaonal_sum += arr[i][n-i-1]

    print(primary_diagonal_sum, " ", secondary_digaonal_sum)

# Take input 
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Call the function
getDiagonalSum(n, arr)



# pass
# for i in range(0, n):
#     for j in range(0, n):
#         print(f"{i}{j}--", end=" ")
#         print(arr[i][j], end=" ")
#     print("")
# print(f"{i}{i}")
# print(f"{arr[i][i]}", end=" ")
# print(f"{arr[i][n-i-1]}", end=" ")
