"""
Thomas driver and Kobe editor

2D Matrix Problem

This program acheives the desired O(m+n) time complexity by searching the matrix from
[m-2][n-2] downwards across the diagonal until a number less than the target is found.
The algorithm then checks the previous row and column for the target number. Protocols are
in place to prevent the program from going out of bounds and it is capable of handling
non square matrices using the same method as well. The program will have to check every
part of one column and one row in the worst case which is equal to m+n searches.
"""

class MatrixIntFinder():

    def findInt(self, matrix, target):
        """find specified int in a list of lists"""
        rows = len(matrix)
        cols = len(matrix[0])

        row_dist_from_corner = 1
        col_dist_from_corner = 1
        cur = matrix[self.nextIndex(rows, row_dist_from_corner)][self.nextIndex(cols, col_dist_from_corner)]

        while(cur >= target):
            if cur == target:
                return (self.nextIndex(rows, row_dist_from_corner), self.nextIndex(cols, col_dist_from_corner))
            if(rows - row_dist_from_corner - 1 != 0):
                row_dist_from_corner += 1

            if(cols - col_dist_from_corner - 1 != 0):
                col_dist_from_corner += 1

            cur = matrix[self.nextIndex(rows, row_dist_from_corner)][self.nextIndex(cols, col_dist_from_corner)]

        return self.searchRowCol(matrix, target, self.nextIndex(rows, row_dist_from_corner-1), self.nextIndex(cols, col_dist_from_corner-1))

    def nextIndex(self, dim_length, distance):
        """
        Helper that prevents dist_from_corner from allowing
        an out of bounds index call
        """
        if dim_length > distance:
            return dim_length - distance - 1
        
        return 0
        
    def searchRowCol(self, matrix, target, row, col):
        """
        Helper that searches a specific row and column set for the target
        value
        """
        for i in range(0, row+1):
            if(matrix[i][col]) == target:
                return (i, col)
            
        for j in range(0, col+1):
            if(matrix[row][j]) == target:
                return(row, j)
            
        return self.searchRowCol(matrix, target, row+1, col+1)

def main():
    finder = MatrixIntFinder()

    ex1 = [[1, 3, 5], [2, 4, 6]]
    ex2 = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    ex3 = [[1, 30, 55, 76, 90], [3, 34, 57, 77, 92], [6, 36, 60, 80, 93], [15, 40, 65, 83, 96], [21, 47, 71, 88, 99]]

    print("TESTS FOR EX1")
    print(finder.findInt(ex1, 2))
    print(finder.findInt(ex1, 1))
    print(finder.findInt(ex1, 6))
    print("TESTS FOR EX2")
    print(finder.findInt(ex2, 7))
    print(finder.findInt(ex2, 3))
    print(finder.findInt(ex2, 4))
    print("TESTS FOR EX3")
    print(finder.findInt(ex3, 34))
    print(finder.findInt(ex3, 71))
    print(finder.findInt(ex3, 36))


if __name__ == "__main__":
    main()