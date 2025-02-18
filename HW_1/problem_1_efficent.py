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
import math

class Efficient():

    def __init__(self):
        pass
    
    def crossSum(self, numArray, middle, length):
        i = middle
        largestSum = -100000
        currentSum = 0
        while i >= 0:
            currentSum += numArray[i]
            if(currentSum > largestSum): 
                largestSum = currentSum
            i -= 1

        left = largestSum
        i = middle+1
        largestSum = -100000
        currentSum = 0
        while i < length:
            currentSum += numArray[i]
            if(currentSum > largestSum): 
                largestSum = currentSum
            i += 1

        return left + largestSum


    def recursive(self, numArray):
        arrayLength = len(numArray)
        if(arrayLength == 0):
            return None
        elif(arrayLength == 1):
            return numArray[0]
        else:
            middle = (arrayLength)//2
            leftSide = self.recursive(numArray[:middle])
            rightSide = self.recursive(numArray[middle:])
            crossSum = self.crossSum(numArray, middle, arrayLength)
            return max(leftSide, rightSide, crossSum)
            
    

def main():
    ex1 = [-2,1,-3,4,-1,2,1,-5,4]
    ex2 = [1]
    ex3 = [5,4,-1,7,8]
    print(Efficient().recursive(ex1))
    print(Efficient().recursive(ex2))
    print(Efficient().recursive(ex3))

if __name__ == "__main__":
    main()