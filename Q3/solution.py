# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 18:52:42 2022

@author: Umer Yasin
"""
# Question 3

def median_arr(merge_arr):

	n = len(merge_arr)

	# If length of array is even
	if n % 2 == 0:
		Quo = n // 2
		first = merge_arr[Quo]
		secound = merge_arr[Quo - 1]
		output = (first + secound) / 2
		return output
		
	# If length of array is odd
	else:
		Quo = n // 2
		output = merge_arr[Quo]
		return output


if __name__ == "__main__":
	
	num1 = [ 1, 2 ]
	num2 = [ 3, 4 ]

	# Concatenating the two arrays
	num3 = num1 + num2

	# Sorting the resultant array
	num3.sort()

	print("Median = ", median_arr(num3))
    
    # Video Link:
    # https://drive.google.com/file/d/1_aKSPnD2Ev21zpd0Ey-PRwMmaob0FIUR/view?usp=sharing
	
        
