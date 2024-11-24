# Sort binary array in linear time
#
# For
# example,
#
# Input: { 0, 0, 1, 0, 1, 1, 0, 1, 0, 0 }
#
# Output: 0 0 0 0 0 0 1 1 1 1

if __name__ == '__main__':
    input_int_array = [int(x) for x in input("Please enter array of binary : ").split(',')]
    # input_int_array.sort(reverse=False) if using sort method
    input_int_array = [int(x) for x in input_int_array]
    print("array:", input_int_array)
    # if building "binary sort" manually
    countOne = 0
    countZero = 0
    sort = ""
    for i in range(len(input_int_array)):
        if input_int_array[i] > 0:
            countOne = countOne + 1
        else:
            countZero = countZero + 1
    print("zeros count : " + str(countZero))
    print("ones count : " + str(countOne))
    for item0 in range(countZero):
        # noinspection PyTypeChecker,PyUnboundLocalVariable
        sort = sort + " " + "0"
    for item1 in range(countOne):
        # noinspection PyTypeChecker,PyUnboundLocalVariable
        sort = sort + " " + "1"
    # noinspection PyUnboundLocalVariable
    print("RESULT : " + sort)
