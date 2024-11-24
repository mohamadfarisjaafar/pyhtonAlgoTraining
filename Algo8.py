# Input:
#
# Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#
# Output:
#
#  [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# Write a Python program to get a list, sorted in increasing order
# by the last element in each tuple from a given list of non-empty tuples.

def compare(inputlist):
    temp_list = []
    checked = 1
    print(type(inputlist))
    while bool(checked):
        counter = 0
        if len(inputlist) != len(temp_list):
            for x in inputlist:
                if len(temp_list) == 0:
                    temp_list.append(x)
                    counter = counter + 1
                else:
                    existingValue = temp_list[counter-1]
                    if existingValue[1] > x[1]:
                        temp_list.pop(counter-1)
                        temp_list.append(x)
                        temp_list.append(existingValue)
                        counter = counter + 1
                        checked = 1
                    else:
                        temp_list.append(x)
                        counter = counter + 1
                        checked = 0
        else:
            inputlist = temp_list
            temp_list = []
            for x in inputlist:
                if len(temp_list) == 0:
                    temp_list.append(x)
                    counter = counter + 1
                else:
                    existingValue = temp_list[counter - 1]
                    if existingValue[1] > x[1]:
                        temp_list.pop(counter - 1)
                        temp_list.append(x)
                        temp_list.append(existingValue)
                        counter = counter + 1
                        checked = 1
                    else:
                        temp_list.append(x)
                        counter = counter + 1
                        checked = 0

if __name__ == "__main__":
    compare([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
    print("H")
