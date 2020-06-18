'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):

   # Check cache to see if there is answer, then return it.
    if n == 0:
       return 1
   # check for negative n values
    elif n < 0:
       return 0
   # check if there is cache and init cache if no cache yet
    elif cache and cache[n] > 0:
       return cache[n]
    else:
        if not cache:
           cache = [0 for _ in range(n+1)]
           # save answer to cache
        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)
   
        return cache[n]

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
