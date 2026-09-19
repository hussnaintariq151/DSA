# Given an array of integers nums and an integer target, return indices of the two numbers such that they add 
# up to target. 
# You may assume that each input would have exactly one solution, and you may not use the same element 
# twice.

# Brute Force

class Solution:
    def hashsumbrute(self, nums, target):
        for i in range(len(nums)):
           for j in range(i+1, nums):
               if nums[i] + nums[j] == target:
                  return [i,j] 
        
        return []

# Hash map

class Solution:
    def twosumhash(self, nums, target):
        seen = {}

        for i,num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            
            seen[num] = i
        
        return []

# Problems
# Arbisoft Real-Style Question 
# SETTING: Arbisoft Test Gorilla — 90 min, 3 problems. 
# PROBLEM (Real): 
# An e-commerce cart system. Aik user ke cart mein items hain jinke prices di gayi hain. Aur ek promo code hai 
# jo un items ka pair identify karta hai jinka total EXACTLY promo amount ke barabar hai — us pair pe discount 
# lag jata hai. 
# Ek PromoValidator class banayein jo: 
# 1. Cart mein promo pair identify kare (indices return kare) 
# 2. Multiple valid pairs mein se first found return kare 
# 3. Agar valid pair nahi hai — return None 
# Constraint: Cart size up to 10K items. Optimize for speed. 

prices = [100, 250, 150, 300]
target = 400

class Solution3:
    def promo_validator(self,prices,promo_amount):
        seen = {}

        for i,price in enumerate(prices):
            complement = promo_amount - price
            if complement in seen:
                return [seen[complement],i]
            
            seen[price] = i
        
        return None
    
# Devsinc Real-Style Question 
# SETTING: Devsinc 2nd round — manager coding karwa raha hai. 
# PROBLEM: 
# Manager ne board pe likha: 
# "Given expenses = [200, 150, 300, 450, 100], find two expenses that add up to 550. Return their indices."

class Solution:
    def runningsumdevsinc(self, expenses, target):
        seen = {}

        for i,expense in enumerate(expenses):
            complement = target - expense
            if complement in seen:
                return [seen[complement], i]
            seen[expense] = i
        return []