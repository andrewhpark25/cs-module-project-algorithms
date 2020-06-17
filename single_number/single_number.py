'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # first-pass solution
    # array to hold numbers from arr
    no_dups = []
    # iterate through arr, check if number is already in no_dups
    for x in arr:
        if x not in no_dups:
            no_dups.append(x)
    # remove it from array if in no_dups
        else:
            no_dups.remove(x)
    # return the only number left in no_dups after iterating 

    return no_dups[0]

if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")