# Amazon Customer Review
#
# Repository: ["mobile","mouse", "moneypot", "monitor", "mousepad"]      mobile, mouse, moneypot, monitor, mousepad
# customerQuery: "mouse"
#
# Output: ["mobile, "moneypot", "monitor"] max 3 output
#           ["mouse", "mousepad"]
#           ["mouse", "mousepad"]
#           ["mouse", "mousepad"]

if __name__ == '__main__':
    input_str_array_repository = [str(x).strip() for x in input("Please enter array of repository : ").split(',')]
    input_str_array_repository = sorted([str(x) for x in input_str_array_repository])
    input_str_query = input("Please enter your query : ")
    print("array repo:", input_str_array_repository)
    print("query:", input_str_query)
    output = []
    queryCompare = input_str_query[0]
    for i in range(1, len(input_str_query)):
        result = ""
        max3Output = []
        queryCompare = queryCompare + input_str_query[i]
        for j in range(len(input_str_array_repository)):
            repoSelected = str(input_str_array_repository[j])
            repoSubstring = str(input_str_array_repository[j]).strip()[0:i + 1]
            print("queryCompare : " + queryCompare)
            print("repoSubstring : " + repoSubstring)
            if queryCompare.lower().strip() == repoSubstring.lower().strip():
                if len(result) != 0:
                    max3Output = result.split(',')
                if len(max3Output) < 3:
                    if len(result) == 0:
                        result = str(input_str_array_repository[j])
                    else:
                        result = result + "," + str(input_str_array_repository[j])
                else:
                    break
        output.append(result)
    for a in range(len(output)):
        print("Suggestion: " + output[a])
