class Solution(object):
    def rotate(self, matrix):
        # 0,0 == 2,0
        # 0,1 == 1,0
        # 0,2 == 0,0
        # --------
        # 1,1 = 3,1
        # 1,2 = 2,1
        # 1,3 = 1,1
        # --------
        # 2,1 = 3,2
        # 2,2 = 2,2
        # 2,3 = 1,2

        # n = len(matrix)
        # matrix1 = matrix
        # for i in range(n):
        #     for j in range(n):
        #         if j == 0:
        #             matrix[i][j] = matrix1[2][i]
        #         if j == 1:
        #             matrix[i][j] = matrix1[1][i]
        #         if j == 2:
        #             matrix[i][j] = matrix1[0][i]
        # return matrix

        n = len(matrix)

        # Step 1: Transpose the matrix
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Step 2: Reverse each row
        for row in matrix:
            row.reverse()






        