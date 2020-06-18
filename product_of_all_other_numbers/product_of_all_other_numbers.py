'''
Input: a List of integers
Returns: a List of integers
'''
def product_of_all_other_numbers(arr):
    # multiply everything that comes before on the way up and everything that come after on way back

        # set result to list of 1s that's the length of arr
        result = [1] * len(arr)
        # instantiate product that tells everything multiplied before the number
        product = 1

        # keep track of index
        for i in range(len(arr)):
             # multiply result array by product and set it to the element
            result[i] *= product
            # product multiplies by the element in num
            product *= arr[i] 
        # reset product to 1 
        product = 1
        # do same as first for loop but go through array backwards
        for i in range(len(arr) - 1, -1, -1):
            result[i] *= product
            product *= arr[i] 
        
        return result

if __name__ == '__main__':
    # Use the main function to test your implementation
    # arr = [1, 2, 3, 4, 5]
    arr = [2, 6, 9, 8, 2, 2, 9, 10, 7, 4, 7, 1, 9, 5, 9, 1, 8, 1, 8, 6, 2, 6, 4, 8, 9, 5, 4, 9, 10, 3, 9, 1, 9, 2, 6, 8, 5, 5, 4, 7, 7, 5, 8, 1, 6, 5, 1, 7, 7, 8]

    print(f"Output of product_of_all_other_numbers: {product_of_all_other_numbers(arr)}")
