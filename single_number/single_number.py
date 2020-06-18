'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # keep track of counts of particular number
    counts = {}

    # loop through arr to tally up each number
    for i in arr:
        if i in counts:
         del counts[i]
        else:
            counts[i] = 1
            
    # loop through all of the key-value pairs in counts to find the one pair that has value of 1
    for num in counts:
        if counts[num] == 1:
            return num 

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")