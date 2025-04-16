'''
Kobe driver and Thomas editor

Problem 2 (10):
This is the interval partitioning problem that we discussed in the class.
You are given a list of intervals where each interval represents the start and end times of a lecture. Your task is to determine the minimum number of classrooms needed so that every lecture can be scheduled without any overlap in the same classroom.
The input to your program will be a variable named intervals which will be a list of lists. Each interval is in the form [start, end]. The intervals are NOT sorted. You are allowed to use library functions for sorting.
Example:
intervals = [[30, 75], [0, 50], [60, 150], [80, 120], [55, 65], [40, 80]]
The output will be 3, which is the minimum number of classrooms required to schedule all lectures.
Explanation:
One possible scheduling could be:
Classroom 1: [0, 50], [55, 65], [80, 120]
Classroom 2: [30, 75] (and possibly another lecture if it fits)
Classroom 3: [40, 80]
Classroom 3: [60, 150] This should be 4 you did not account for [40, 80]

HINT: Look at the interval partitioning part of the lecture slides to implement it using priority queue (min-heap).
This is why I use heapq, it is a sorted list. My original code before looking at this hint used a sort function every iteration
inorder to maintain the smallest endtime at index [0]

Psuedo code:
The implimentation of this function is simple fist the entire array is sorted by earlist start time. 

make another list to keep track of class rooms this will be composed of endtimes

Then you loop through this array
for index in sortedArray:
    if: class room list is empty add the endtime of index to it
    else: There are two cases
        case one: the current index has a start time after the earliest end time in our class room array in this case we can extange these
        case two: the current index has a start time before the earliest end time in our class room array in this case we open a new class room

Using the class heapq will save us from having to sore the class room list each time we iterate through since it will keep the earliest end time at index 0

'''

import heapq

class IntPartition:
    def __init__(self, arrayStartEnd):
        self.arrayStartEnd = arrayStartEnd

    def classRoomsRequired(self):
        sortedByStart = sorted(self.arrayStartEnd, key=lambda x: x[0])  # Sort by start time
        classRooms = []  # This will store the end times of active lectures

        for i in sortedByStart:
            # If classRooms is empty, add the end time of the first class
            if not classRooms:
                heapq.heappush(classRooms, i[1])  
            else:
                # If the earliest ending class is done we will reuse that class room. This <= does allow a class to end and begin right next to eachother not sure if you want <
                if classRooms[0] <= i[0]:  
                    heapq.heappushpop(classRooms, i[1])
                else:
                    heapq.heappush(classRooms, i[1])  #If not add new room


        return len(classRooms)


def main():
    ex1 = [[30, 75], [0, 50], [60, 150], [80, 120], [55, 65], [40, 80]]  # Expected: 4 (There was an error in your example where you did not account for [40, 80])
    ex2 = [[10, 30], [5, 30]]  # Expected: 2 (All overlap)
    ex3 = [[5, 10], [15, 20], [25, 35]]  # Expected: 1 (No overlapping)
    ex4 = [[0, 10], [5, 15], [10, 20], [15, 25]]  # Expected: 2
    ex5 = [[1, 5], [2, 6], [3, 7], [4, 8]]  # Expected: 4 (All overlap)

    print(IntPartition(ex1).classRoomsRequired())
    print(IntPartition(ex2).classRoomsRequired())
    print(IntPartition(ex3).classRoomsRequired())
    print(IntPartition(ex4).classRoomsRequired())
    print(IntPartition(ex5).classRoomsRequired())


if __name__ == "__main__":
    main()
