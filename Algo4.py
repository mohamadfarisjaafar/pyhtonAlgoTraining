# Find the duplicate element in a limited range array
#
# Input: {1, 2, 3, 4, 4}
# Output: The
# duplicate
# element is 4
#
# Input: {1, 2, 3, 4, 2 , 1}
# Output: The
# duplicate
# element is 2, 1

if __name__ == '__main__':
    input_int_array = [int(x) for x in input("Please enter array of binary : ").split(',')]
    input_int_array = [int(x) for x in input_int_array]
    print("array:", input_int_array)
    result = []
    statement = ""
    for i in range(len(input_int_array) - 1):
        for j in range(i + 1, len(input_int_array)):
            if input_int_array[i] == input_int_array[j]:
                result.append(input_int_array[i])
    for item in result:
        if len(statement) == 0:
            statement = str(item) + statement
        else:
            statement = statement + ", " + str(item)
    print("element is : " + statement)
