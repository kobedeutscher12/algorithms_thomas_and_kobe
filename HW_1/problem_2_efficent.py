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


For each of the solutions, you should provide a description of algorithm
A discussion on how the second solution improved the time complexity.
'''


def main():
    ex1 = [(1, 3), (2, 5), (4, 6), (6, 8), (7, 9)]

if __name__ == "__main__":
    main()