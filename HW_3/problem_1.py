"""
Thomas driver and Kobe editor

2D Matrix Problem

This program acheives the desired O(m+n) time complexity by searching the matrix starting at [m][1].
If the number is larger the program moves right 1 and if the number is smaller the program moves up.
In the worst case it goes all the way up and then all the way right achieving the O(m+n) time.
"""

class MatrixIntFinder():

    def findInt(self, matrix, target):
        """find specified int in a list of lists"""
        rows = len(matrix)-1
        cols = 0

        while(True):
            #Ensure we haven't step out of the array
            if(cols > (len(matrix[0])-1) or rows < 0):
                return None
            cur = matrix[rows][cols]
            #Check if this is the number
            if(target == cur):
                return (rows, cols)

            #Decide if we step up or to the right
            if(target < cur):
                rows -= 1
            if(target > cur):
                cols += 1

        return 

def main():
    finder = MatrixIntFinder()

    ex1 = [[1, 3, 5], 
           [2, 4, 6]]
    ex2 = [[1, 4, 7], 
           [2, 5, 8], 
           [3, 6, 9]]
    ex3 = [[1, 30, 55, 76, 90], 
           [3, 34, 57, 77, 92], 
           [6, 36, 60, 80, 93], 
           [15, 40, 65, 83, 96], 
           [21, 47, 71, 88, 99]]

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
    print(finder.findInt(ex3, 0))


if __name__ == "__main__":
    main()