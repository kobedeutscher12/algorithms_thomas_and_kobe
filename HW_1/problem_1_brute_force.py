'''
Kobe driver and Thomas editor

Given an integer array nums, find the subarray with the largest sum, and return its sum. A subarray is a contiguous non-empty sequence of elements within an array.
Your program should contain a function that takes in the input and returns the output.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4], Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1], Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8], Output: 23

Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
You should provide:
Two programming solutions to the problem (in two separate .py files):
A brute force approach which checks every possible combination of sub arrays and their sum.
A more efficient solution which reduces the time complexity significantly.


For each of the solutions, you should provide a description of algorithm
A discussion on how the second solution improved the time complexity.
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
        largestSub = 0
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