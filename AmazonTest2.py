# Amazon Fresh Promo

# Input 1 :
# codeList= [[apple, apple], [banana, anything, banana]]
# shoppingCart= [apple, orange, banana, orange, banana]

# output:
# false

# Input 2 :
# codeList= [[apple, apple], [banana, anything, banana]]    apple, apple    banana, anything, banana
# shoppingCart= [apple, apple, strawberry, banana, orange, banana]    apple, apple, strawberry, banana, orange, peach

# output:
# true

if __name__ == '__main__':
    input_str_array_codeList = []
    while input("Please enter Y to exit or click Enter to proceed: ") != "Y":
        input_str_array_codeList.append(input("Please enter array of code list : "))
    input_str_array_shoppingCart = [str(x).strip() for x in input("Please enter your shopping cart : ").split(',')]
    input_str_array_shoppingCart = [str(x) for x in input_str_array_shoppingCart]
    print("array code list:", input_str_array_codeList)
    print("shopping cart:", input_str_array_shoppingCart)
    exist = False
    tempStr = ""
    codeListExist = False
    innerLoopCounter = 0
    startConcurrent = False
    status = True
    for i in range(len(input_str_array_codeList)):
        tempArray = []
        if status:
            codeList = input_str_array_codeList[i]
            codeListLength = len(codeList.split(','))
            codeListLengthCounter = 0
            for j in range(len(input_str_array_shoppingCart)):
                if codeListLengthCounter <= codeListLength:
                    codeListValue = codeList.split(',')[codeListLengthCounter].strip().lower()
                    shoppingCartValue = input_str_array_shoppingCart[innerLoopCounter].strip().lower()
                    if input_str_array_shoppingCart[innerLoopCounter].strip().lower() == codeList.split(',')[codeListLengthCounter].strip().lower() or codeList.split(',')[codeListLengthCounter].strip().lower() == "anything":
                        tempArray.append(input_str_array_shoppingCart[innerLoopCounter])
                        codeListLengthCounter = codeListLengthCounter + 1
                        startConcurrent = True
                    else:
                        if startConcurrent:
                            status = False
                            break
                innerLoopCounter = innerLoopCounter + 1
                if len(tempArray) == codeListLength:
                    startConcurrent = False
                    break
        else:
            break
    if status:
        print(True)
    else:
        print(False)
