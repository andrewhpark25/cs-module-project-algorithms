'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):

    count = 0 # Counting non-zeroes

   # Traverse array and swap non-zero element at index 'count' with element at index 'i'


    for i in range(0, len(arr)):
        if arr[i] != 0:
            arr[count], arr[i] = arr[i], arr[count]
            count += 1
   

    return arr
    


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")