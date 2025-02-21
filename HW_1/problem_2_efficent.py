#Thomas driver and Kobe editor
'''
Problem 2 (10):
Given a set of intervals, find the maximum number of intervals that do not overlap. All the intervals are represented in a list of tuples. Each interval is represented as a pair (start, end).
For example:
Input: intervals = [(1, 3), (2, 5), (4, 6), (6, 8), (7, 9)], output 3.
Explanation: The maximum number of non-overlapping intervals that can be scheduled is 3, achieved by selecting (1,3), (4,6), and (6,8)
You should provide:
Two solutions to the problem (in two separate .py files):
A brute force approach which checks all possible subsets of intervals and checks if they are non-overlapping.
A more efficient solution which reduces the time complexity significantly.


This algorithm improves upon our brute force algorithm by approaching the problem by sorting by ascending order based
on the end of each interval. Sorting takes O(n*logn) time (we used merge sort) and this allows for a much simpler
process in finding the max possible set of intervals. With the intervals sorted by their ends, we can safely include
the first interval to have an ending which maximizes our potential for future intervals as it leaves as much space as
possible. The rest of the program only needs to go through the sorted list of intervals once, adding any intervals 
with a larger start value than the last added end value. Since the next start value above the last end value will be
in ascending order based on the end of the interval, this always finds the smallest possible interval that maximizes space
for the others in the list. Since the creation of the actual list of intervals takes O(n) time which is less than
O(n*logn), the time complexity of this solution is O(n*logn)
'''
class ProblemTwoEfficient():

    def __init__(self, intervalList):
        #store the input list of tuples
        self.intervals = intervalList

    def sortTuplesByEnd(self):
        """Sorts the intervals by their end in ascending order"""
        self.mergeSort(0, len(self.intervals) - 1)

    def mergeSort(self, left, right):
        """helper for sorting with merge sort"""
        if left < right:
            mid = (left + right) // 2

            self.mergeSort(left, mid)
            self.mergeSort(mid + 1, right)
            self.merge(left, mid, right)

    def merge(self, left, mid, right):
        """helper for merge sort merging"""
        n1 = mid - left + 1
        n2 = right - mid

        L = self.intervals[left : left + n1]
        R = self.intervals[mid + 1: mid + 1 + n2]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if L[i][1] <= R[j][1]:
                self.intervals[k] = L[i]
                i += 1
            else:
                self.intervals[k] = R[j]
                j += 1
            k += 1

        while i < n1:
            self.intervals[k] = L[i]
            i += 1
            k += 1

        while j < n2:
            self.intervals[k] = R[j]
            j += 1
            k += 1

        
    def mostIntervalsEfficient(self):
        """Find largest set of tuples"""
        self.sortTuplesByEnd()
        print(self.intervals)

        lastNonOverlapping = self.intervals[0]
        intervalSet = {self.intervals[0]}
        for i in self.intervals:
            if i[0] >= lastNonOverlapping[1]:
                intervalSet.add(i)
                lastNonOverlapping = i
                print(intervalSet)

        return len(intervalSet)
        


def main():
    ex1 = [(1, 3), (2, 5), (4, 6), (6, 8), (7, 9)]
    ex2 = [(4,5),(4,6)]
    ex3 = [(2,5),(6,8),(3,10),(1,2),(7,9),(4,7)]
    
    print(ProblemTwoEfficient(ex1).mostIntervalsEfficient())
    print(ProblemTwoEfficient(ex2).mostIntervalsEfficient())
    print(ProblemTwoEfficient(ex3).mostIntervalsEfficient())

if __name__ == "__main__":
    main()