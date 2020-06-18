'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''


def sliding_window_max(nums, k):

        result = [0] * (len(nums) - k + 1)
        result[0] = max(nums[:k])
        for i in range(1, len(nums) - k + 1):
                if nums[i-1] == result[i-1]:
                    result[i] = max(nums[i:i + k])
                else:
                    result[i] = max(result[i-1], nums[i+k-1])

        return result
    
    
            


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
