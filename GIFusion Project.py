#!/usr/bin/env python
# coding: utf-8

# Python Problem: Reverse Integer

# In[ ]:


class Solution:
    def reverse(self, x: int) -> int:
        # Define the 32-bit signed integer range
        m = -2**31  # Minimum value for a 32-bit signed integer
        n = 2**31 - 1  # Maximum value for a 32-bit signed integer
        
        # Initialize an empty list to collect digits
        l = []
        x1 = ""
        
        # Check if the input number is non-negative
        if x >= 0:
            # Convert number to string to process each digit
            b = str(x)
            # Append each digit to the list
            for a in b:
                l.append(str(a))
            # Reverse the list of digits
            l.reverse()
            # Build the reversed number from the list
            for a in l:
                x1 += a
        else:
            # Handle negative numbers
            b = str(x)
            # Loop through each character in the string representation
            for a in b:
                try:
                    # Try converting the character to an integer
                    int(a)
                    # Append digit characters to the list
                    l.append(a)
                except:
                    # Ignore non-digit characters like the minus sign
                    continue
            # Reverse the list of digit characters
            l.reverse()
            # Build the reversed number string
            x2 = ""
            for a in l:
                x2 += a
            # Convert the reversed string to an integer and apply the negative sign
            x1 = -abs(int(x2))
        
        # Check if the reversed number is within the 32-bit signed integer range
        if m <= int(x1) <= n:
            return int(x1)  # Return the reversed number if within range
        else:
            return 0  # Return 0 if the reversed number is out of range


# 

# SQL Problem: Sort Array by Increasing Frequency

# In[ ]:


class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        num1 = set(nums)  # Get unique elements from nums
        l = []
        l2 = []
        l3 = []
        dictionary = dict()
        
        # Build a dictionary to count the frequency of each number
        for a in num1:
            count = 0
            for b in nums:
                if a == b:
                    count += 1
            dictionary[a] = count

        # Sort nums based on frequency and then by value in decreasing order
        l = sorted(nums, key=lambda x: (dictionary[x], -x))

        return l

