"""
Kobe driver and Thomas editor

Problem 3 (25 points): Dynamic Programming - House Robbing (Algorithm + Programming)

Suppose, you are a professional robber planning to rob houses along a street. Each house has some amount of money hidden in it, represented as a non-negative integer. However, you cannot rob two adjacent houses (i.e., if you rob house i, you cannot rob house i+1).
Given an integer array nums representing the amount of money of each house, you need to find the maximum amount of money you can rob tonight without robbing two adjacent houses.
Example 1:
Input: nums = [1, 20, 1, 1, 25]
Output: 45
Explanation: Rob house 2 (20) and house 5 (25) = 45
This is the maximum possible amount without robbing two adjacent houses.


Example 2:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
Find a dynamic programming algorithm to find OPT(n), which is the maximum amount of money you can rob from n houses.
Your solution should include:
Description of your algorithm with Bellman equation showing the subproblems (10 Points).
Discussion of time-complexity.  (5 Points)
Programming: python function that takes an integer array nums (representing the amount of money of each house) as input, and returns the maximum amount of money you can rob tonight. (10)
You should also provide the test cases you have tested this code on. 
HINT: This problem has similarity with the Knapsack problem (with much less difficulty).
"""

class RobbingHouse():
    def __init__(self, house_list):
        self.house_list = house_list
    
    def findMaxMoney(self):
        #Base Cases :) Easy, base case of 2 is inclued 
        n = len(self.house_list)
        if n == 0:
            return 0
        if n == 1:
            return self.house_list[0]
        
        # maxMoney[i] represents maximum money that can be robbed from first i houses
        maxMoney = [0] * n
        maxMoney[0] = self.house_list[0]
        maxMoney[1] = max(self.house_list[0], self.house_list[1])
        
        for i in range(2, n):
            # This is the bellmont equation excluding base cases above. Either we rob the current house
            # and the previous saved or we profit more from robbing the house before and skipping this house.
            maxMoney[i] = max(maxMoney[i-2] + self.house_list[i], maxMoney[i-1])
        
        return maxMoney[n-1]

def main():
    ex1 = [1, 20, 1, 1, 25]
    print(f"ex1\nMaximum money: {RobbingHouse(ex1).findMaxMoney()}\n")
    
    ex2 = [1, 2, 3, 1]
    print(f"ex2\nMaximum money: {RobbingHouse(ex2).findMaxMoney()}\n")
    
    # Additional test cases
    ex3 = [2, 7, 9, 3, 1]
    print(f"ex3\nMaximum money: {RobbingHouse(ex3).findMaxMoney()}\n")
    
    ex4 = []
    print(f"ex4 empty block\nMaximum money: {RobbingHouse(ex4).findMaxMoney()}\n")
    
    ex5 = [5, 6]
    print(f"ex5 two house\nMaximum money: {RobbingHouse(ex5).findMaxMoney()}\n")

if __name__ == "__main__":
    main()