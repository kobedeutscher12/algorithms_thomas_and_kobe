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


Description of Algorithm:
This algorithm checks every possible combination of intervals for validity and then returns the largest number
of intervals it could find. 
'''
class ProblemTwoBruteForce():

    def __init__(self, intervalList):
        #store the input list of tuples
        self.intervals = intervalList

    def overlapChecker(self, tuple1, tuple2):
        """Check if the two given intervals overlap at all"""
        if (tuple1[0] < tuple2[0] and tuple2[0] < tuple1[1]):
            return False
        
        elif (tuple2[0] < tuple1[0] and tuple1[0] < tuple2[1]):
            return False
        
        elif (tuple1[0] < tuple2[1] and tuple2[1] < tuple1[1]):
            return False
        
        elif (tuple2[0] < tuple1[1] and tuple1[1] < tuple2[1]):
            return False
        
        elif (tuple1[0] == tuple2[0] and tuple1[1] == tuple2[1]):
            return False
        
        else:
            return True
        
    def mostIntervalsBrute(self):
        """Find largest set of tuples with brute force"""
        maxSet = 0

        #loop through every interval and check if it overlaps with any others
        for i in self.intervals:
            newSet = {i}
            
            for j in self.intervals:
                
                if self.overlapChecker(i, j):
                    newSet.add(j)
            
            if (len(newSet) > maxSet):
                maxSet = len(newSet)

        return maxSet


def main():
    ex1 = [(1, 3), (2, 5), (4, 6), (6, 8), (7, 9)]
    print(ProblemTwoBruteForce(ex1).mostIntervalsBrute())

if __name__ == "__main__":
    main()