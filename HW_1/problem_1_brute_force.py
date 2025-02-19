'''
Kobe driver and Thomas editor

Given an integer array nums, find the subarray with the largest sum, and return its sum. A subarray is a contiguous non-empty sequence of elements within an array.
Your program should contain a function that takes in the input and returns the output.

Description of Algorithum:
This is the brute force algorithum, it solves the problem in O(n^2) time.
It does this by starting on one end of the array, this is the first loop, this point in this case i is the start point.
It then works through the whole array adding all numbers to the currentSub. If at any point in this loop currentSub is larger
than largestSub it updates largest some. After that cycle finished for all of j, i the start point is then moved forward 
one spot and the cycle is repeated.
'''

class BruteForce():

    def __init__(self, numArray):
        self.numArray = numArray

    def isBigger(self, num1, num2):
        if(num1 > num2):
            return True
        else:
            return False 

    def largestSubArray(self):
        lengthArray = len(self.numArray)
        largestSub = -100000
        currentSub = 0
        if(lengthArray > 0) :
            largestSub = self.numArray[0]
        else:
            return None
        for i in range(lengthArray):
            currentSub = self.numArray[i]
            if(self.isBigger(currentSub, largestSub)):
                largestSub = currentSub 
            for j in range(i+1, lengthArray):
                currentSub += self.numArray[j]
                if(self.isBigger(currentSub, largestSub)):
                    largestSub = currentSub 
        return largestSub


def main():
    ex1 = [-2,1,-3,4,-1,2,1,-5,4]
    ex2 = [1]
    ex3 = [5,4,-1,7,8]
    print(BruteForce(ex1).largestSubArray())
    print(BruteForce(ex2).largestSubArray())
    print(BruteForce(ex3).largestSubArray())

if __name__ == "__main__":
    main()