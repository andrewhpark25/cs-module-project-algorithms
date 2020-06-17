'''
Input: a List of integers
Returns: a List of integers
'''
def moving_zeroes(arr):
    # Your code here
    
    # arrays to hold non-0s and 0s
    nonZeroes = []
    zeroes = []

    # iterate through arr and append non-0s to nonZeroes array
    for i in arr:
        if i != 0:
            nonZeroes.append(i)
            # append 0s to zeroes array
        else:
            zeroes.append(i)
            # join them in new array newArr
    newArr = nonZeroes + zeroes
    
    return newArr


if __name__ == '__main__':
    # Use the main function here to test out your implementation
    arr = [0, 3, 1, 0, -2]

    print(f"The resulting of moving_zeroes is: {moving_zeroes(arr)}")