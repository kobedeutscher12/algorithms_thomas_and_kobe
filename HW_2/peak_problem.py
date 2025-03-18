"""
Thomas driver and Kobe editor

Problem 1 (20):
A peak element is an element that is strictly greater 
than its neighbors.

Given a 0-indexed integer array nums, find a peak element, 
and return its index. If the array contains multiple peaks, 
return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. 
In other words, an element is always considered to be strictly 
greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.

Constraints: 
nums[i] != nums[i + 1] for all valid i. 
(that means two consecutive numbers are never same)
Your program should contain a function that takes in the input 
(list of numbers) and returns the output (index of a peak).

Description of Algorithm:
Our approach to solving this problem is to start at a random index,
in this case the middle index, and check if it is a peak. If it is not,
then we move to check the larger neighbor. If both neighbors are larger, then
the larger of the two neighbors is checked. This continues until a peak is found.

This algorithm will always find a peak since it moves from the center towards whichever
side is larger. By movin to a larger number, it is guaranteed that the next index being 
checked is larger than at least one neighbor already. It will continue in a direction until
it either reaches a peak, or the end of the list on that side, which is considered a peak since
the only neighbor of that index was determined to be smaller already.

The desired time complexity is acheived by cutting the list in half and moving towards the larger
side, which is most likely to have a peak closer ideally. Even in the worst case, the list will
always be half as large for finding a peak. This effectively gives us O(logn) time.
"""

class PeakFinder():

    def __init__(self, int_list):
        #calculate the start index for the problem
        self.start_idx = len(int_list)//2

        #Quality of life feedback addition
        self.num_of_elements = len(int_list)

    def findPeak(self, start, ints, iters):
        """find a peak to return starting at the middle index"""
        num_of_iter = iters + 1
        cur_idx = start

        while(True):
            left_larger = False
            right_larger = False

            #Check if leftmost index, if not, check if left neighbor is greater
            if cur_idx == 0:
                pass

            elif ints[cur_idx] < ints[cur_idx - 1]:
                left_larger = True

            #Check if rightmost index, if not, check if right neighbor is greater
            if cur_idx == len(ints) - 1:
                pass

            elif ints[cur_idx] < ints[cur_idx + 1]:
                right_larger = True

            #If left was larger and is bigger than the right side, call on the left
            if left_larger and ints[cur_idx - 1] > ints[cur_idx + 1]:
                return self.findPeak(cur_idx - 1, ints, num_of_iter)

            #If right was larger and is bigger than the left side, call on right
            elif right_larger and ints[cur_idx - 1] < ints[cur_idx + 1]:
                return self.findPeak(cur_idx + 1, ints, num_of_iter)
            
            #The other indices weren't larger, so return cur_idx
            else:
                return cur_idx, num_of_iter, self.num_of_elements


def main():
    ex1 = [1, 5, 7, 4]
    ex2 = [2, 5, 6, 9, 3, 4, 1, 2, 1, 6, 8, 10]
    ex3 = [3, 6, 4, 8, 9, 0, 2, 1, 5]
    ex4 = [1, 2, 3, 4, 5, 6, 7]
    ex5 = [5, 4, 3, 2, 1]

    peaker = PeakFinder(ex1)
    result = peaker.findPeak(peaker.start_idx, ex1, 0)
    print(f"Results for ex1: idx = {result[0]}, iters = {result[1]}, n = {result[2]}")

    peaker = PeakFinder(ex2)
    result = peaker.findPeak(peaker.start_idx, ex2, 0)
    print(f"Results for ex2: idx = {result[0]}, iters = {result[1]}, n = {result[2]}")

    peaker = PeakFinder(ex3)
    result = peaker.findPeak(peaker.start_idx, ex3, 0)
    print(f"Results for ex3: idx = {result[0]}, iters = {result[1]}, n = {result[2]}")

    peaker = PeakFinder(ex4)
    result = peaker.findPeak(peaker.start_idx, ex4, 0)
    print(f"Results for ex4: idx = {result[0]}, iters = {result[1]}, n = {result[2]}")

    peaker = PeakFinder(ex5)
    result = peaker.findPeak(peaker.start_idx, ex5, 0)
    print(f"Results for ex5: idx = {result[0]}, iters = {result[1]}, n = {result[2]}")

if __name__ == "__main__":
    main()