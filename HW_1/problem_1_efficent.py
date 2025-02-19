'''
Kobe driver and Thomas editor

Given an integer array nums, find the subarray with the largest sum, and return its sum. A subarray is a contiguous non-empty sequence of elements within an array.
Your program should contain a function that takes in the input and returns the output.

This second problem goes about solving it recursively. I believe this makes it O(nlogn) time.
It does this through a divide and concoure. The simplest way to think about this is that there are three spots in which the
longest sub array can exist. It is either in the left side, the right side, or some crossing spot between the two side.
To solve this the array is broken in half L and R. the function recursive will return the largest sum either L, R, or CR.
This process is repeated down to the lowest iteration which is a array of length 1 or 0. the children return their max sum
of the three catagories (L, R, and CR) and thus by dividing we are able to lessen the complexity from cycling through the entire
array to breaking it down into smaller sections. 
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