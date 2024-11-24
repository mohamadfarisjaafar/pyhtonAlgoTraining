# Print all subarrays with 0 sum
# Input: {4, 2, -3, -1, 0, 4}

# Subarrays
# with zero - sum are
#
# {-3, -1, 0, 4}
# {0}
#
# Input: {3, 4, -7, 3, 1, 3, 1, -4, -2, -2}
#
# Subarrays
# with zero - sum are
#
# {3, 4, -7}
# {4, -7, 3}
# {-7, 3, 1, 3}
# {3, 1, -4}
# {3, 1, 3, 1, -4, -2, -2}
# {3, 4, -7, 3, 1, 3, 1, -4, -2, -2}

if __name__ == '__main__':
    input_int_array = [int(x) for x in input("Please enter array of integers : ").split(',')]
    input_int_array = [int(x) for x in input_int_array]
    print("array:", input_int_array)
    result = []
    totalSumFromArray = 0
    for i in range(len(input_int_array) - 1):
        tempStore = []
        for j in range(i + 1, len(input_int_array)):
            if len(tempStore) == 0:
                tempStore.append(input_int_array[i])
            for item in tempStore:
                totalSumFromArray = int(item) + totalSumFromArray
            print("totalSumFromArray : " + str(totalSumFromArray))
            summation = totalSumFromArray + input_int_array[j]
            print("summation " + str(summation))
            tempStore.append(input_int_array[j])
            if summation == 0:
                resultStr = ""
                for item in tempStore:
                    if len(resultStr) == 0:
                        resultStr = str(item)
                    else:
                        resultStr = resultStr + ", " + str(item)
                result.append(resultStr)
            totalSumFromArray = 0

    for a in range(len(result)):
        print("Item Found No " + str(a+1) + " : " + str(result[a]))
