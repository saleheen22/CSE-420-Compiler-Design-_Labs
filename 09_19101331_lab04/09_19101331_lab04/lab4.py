file1 = open('input.txt', "r") # It will open the input  file and read
lines = file1.readlines() # It will read all the lines of the file
methods = []               # for storing the methods name
return_type = []           # for storing the return type

for lin in lines:          # This loop will iterate all the lines stored in lines variable

    k = 0  # for getting the index of the return type string from line_list
    if lin.strip() == "public static void main(String [] args)":    # here lin.strip() will remove white space and first we are checking have we reached the last portion of the code

        break                                                      # if we have reached the last portion of the code it will break the loop
    else:
        line_list = lin.strip().split(' ')                        # It will split the lines into a list if get any space and line_list is a list

        for j in line_list:                                  # Now we are iteration the list through j
            k = k + 1
            if "(" in j:                                     # to check if we have got any opeing paranthesis for a mehtod. That means we have got a method
                # print('something')
                method = j[0:j.index('(')]
                # the methods name stays always before the parenthesis. As we splitted the lines on the basis of white space, there is no white space befor the parenthesis and the name.
                #So, the name of the methods is in the same index of which the ( is in. Here j is a string which is actually a member of that line_list. We have to take the name of the methods.
                #That's why we sliced the string till the ( to take only the name of the mehtod and saved it to a variable method



                methods.append(method + lin[lin.index('('):])
                # we have to get the full name of the method which contains the arguments as well. So, we got the partial name before.
                # In the lin variable the full name is there. lin.index('(') by this we go to the index of the ( in the lin variable.
                # Now we slice the second part of the methods name which starts form ( and ends in ) by " lin[lin.index('('):] " this
                # after that we are adding two parts of the mehtod name and appending it in methods list

                return_type.append(line_list[k - 2])
                # this will append the return type which is in the index k-2 in the line_list list. why k-2 because the return type always stays before the
                # name of the mehtod. k is always 2 step ahead for counting purpose. That's why k-2... k-1 for array/ list indexing .. we know that
                # and another -1, because return type stays before the method name.

print('Mehtods:')
for i in range(len(methods)):
    print("{}, return type: {}".format(methods[i].strip(), return_type[i]))

