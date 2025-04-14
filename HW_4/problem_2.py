"""
Thomas driver and Kobe editor

This program solves the staircase problem using dynamic programming. 
This algorithm functions by using bottom up dynamic programming. In our base case, 
the first three f(n)s are defined, and if n is one of these three, they will be 
returned immediately. If not, the next f(n) is calculated using the recurrence relation 
and saved until n is reached and is then returned.
"""

class StaircaseClimbing():

    def __init__(self):
        self.func_dict = {}
        self.func_dict[1] = 1
        self.func_dict[2] = 2
        self.func_dict[3] = 4

    def findN(self, n):
        #Check for a valid input (non-negative int)
        if(n < 0):
            return None
        
        #Return predefined answer if iteration unnecessary
        elif (n < 4):
            return self.func_dict[n]
        
        #Starting place for iteration since 1,2,3 are predefined
        i = 4

        while(i <= n):
            #calculate next entry in the function dictionary using recurrence function
            self.func_dict[i] = self.func_dict[i-3] + self.func_dict[i-2] + self.func_dict[i-1]

            i += 1

        return self.func_dict[n]

def main():
    stairs = StaircaseClimbing()

    print(f"Testing for n = -1. Should return: None. Returns: {stairs.findN(-1)}")
    print(f"Testing for n = 2. Should return: 2. Returns: {stairs.findN(2)}")
    print(f"Testing for n = 5. Should return: 13. Returns: {stairs.findN(5)}")
    print(f"Testing for n = 7. Should return: 44. Returns: {stairs.findN(7)}")
    print(f"Testing for n = 8. Should return: 81. Returns: {stairs.findN(8)}")
    print(f"Testing for n = 9. Should return: 149. Returns: {stairs.findN(9)}")
    print(f"Testing for n = 10. Should return: 274. Returns: {stairs.findN(10)}")

if __name__ == "__main__":
    main()