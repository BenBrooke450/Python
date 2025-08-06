

"""
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.



Example 1:
Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

Example 2:
Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.

Example 3:
Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16

"""

def numberOfSubarrays(nums: list[int], k: int) -> int:
    # Step 1: Convert each number to 1 if odd, 0 if even
    nums = [1 if x % 2 != 0 else 0 for x in nums]

    t = 0  # Counter for valid subarrays
    prefix_sum = {0: 1}  # Dictionary to store prefix sums
    current_sum = 0  # Running sum of odd counts

    for n in nums:
        current_sum = current_sum + n

        # Check if there's a previous prefix sum equal to current_sum - k
        if (current_sum - k) in prefix_sum:
            print(prefix_sum)
            print(current_sum - k)
            print(prefix_sum[current_sum - k])

            t = t + prefix_sum[current_sum - k]

        # Update the prefix_sum dictionary
        if current_sum in prefix_sum:
            prefix_sum[current_sum] = prefix_sum[current_sum] + 1
        else:
            prefix_sum[current_sum] = 1

    return t

#print(numberOfSubarrays(nums = [1,1,2,1,1], k = 3))
#print(numberOfSubarrays(nums = [2,4,6], k = 1))
print(numberOfSubarrays(nums = [2,2,2,1,2,2,1,2,2,2], k = 2))



import numpy as np
def numberOfSubarrays(nums: list[int], k: int) -> int:
    t = 0
    nums = np.array([ 1 if x % 2 != 0 else 0 for x in nums])
    print(nums)


    for x in np.arange(k+1, len(nums)+1):
        for i in np.arange(len(nums)-x+1):

            if sum(nums[i:i + x]) == k:
                t = t + 1

    return t













import numpy as np
def numberOfSubarrays(nums: list[int], k: int) -> int:
    t = 0
    nums = np.array(nums)

    for x in np.arange(k, len(nums)+1):
        for i in np.arange(len(nums)-x+1):
            if np.sum(1 for x in nums[i:i + x] if x % 2 != 0) == k:
                t = t + 1

    return t









