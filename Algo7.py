# Input:
#
# X[] = [ 1, 4, 7, 8, 10 ]
# Y[] = [2, 3, 9]
#
# Output:
#
# X[] = {1, 2, 3, 4, 7}
# Y[] = {8, 9, 10}

# Write a Python program to get a list, sorted in increasing order
# by the last element in each tuple from a given list of non-empty tuples.
def merge(X, Y):
 
    m = len(X)
    n = len(Y)
 
    # Consider each element `X[i]` of list `X[]` and ignore the element if it is
    # already in the correct order; otherwise, swap it with the next smaller
    # element, which happens to be the first element of `Y[]`.
    for i in range(m):
        print(i)
        # compare the current element of `X[]` with the first element of `Y[]`
        if X[i] > Y[0]:
 
            # swap `X[i] with `Y[0]`
            temp = X[i]
            X[i] = Y[0]
            Y[0] = temp
 
            first = Y[0]
 
            # move `Y[0]` to its correct position to maintain the sorted
            # order of `Y[]`. Note: `Y[1…n-1]` is already sorted
            k = 1
            while k < n and Y[k] < first:
                Y[k - 1] = Y[k]
                k = k + 1
 
            Y[k - 1] = first
 
 
if __name__ == '__main__':
 
    X = [2, 3, 9] 
    Y = [1, 4, 7, 8, 10]
 
    merge(X, Y)
 
    print("X:", X)
    print("Y:", Y)
