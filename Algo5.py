# Find maximum length subarray having a given sum
#
# A[] = {5, 6, -5, 5, 3, 5, 3, -2, 0}
# Sum = 8
#
# Subarrays with sum 8 are
#
# {-5, 5, 3, 5}
# {3, 5}
# {5, 3}
#
# The longest subarray is {-5, 5, 3, 5} having length 4

if __name__ == '__main__':
    input_int_array = [int(x) for x in input("Please enter array of integers : ").split(',')]
    input_int_array = [int(x) for x in input_int_array]
    input_sum = input("Please enter sum : ")
    print("array:", input_int_array)
    print("sum:", input_sum)
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
            if summation == int(input_sum):
                resultStr = ""
                for item in tempStore:
                    if len(resultStr) == 0:
                        resultStr = str(item)
                    else:
                        resultStr = resultStr + ", " + str(item)
                result.append(resultStr)
            totalSumFromArray = 0
    final_result = list(dict.fromkeys(result))
    for a in range(len(final_result)):
        print("item length : " + str(len(final_result[a].split(','))))
        print("Item Found No " + str(a + 1) + " : " + str(final_result[a]))
    arrayWithLongestLength = []
    itemLength = 0
    for a in range(len(final_result)):
        if len(final_result[a].split(',')) > itemLength:
            itemLength = len(final_result[a].split(','))
            arrayWithLongestLength.clear()
            arrayWithLongestLength.append(final_result[a])
    # noinspection SpellCheckingInspection
    print("The longest subarray is {" + arrayWithLongestLength[0] + "} having length " + str(itemLength))
