# def odd_even(range):            # odd_even(fucntion) "range" = parameter
#     for num in range(1,2001,1):     # invoking the function by passing an argument in "range"
#         if num %2 != 0:
#             print "number is", num, "this is an odd number"
#         elif num %2 == 0:
#             print "number is", num, "this is an even number"

# odd_even(range) # a functional call is equal to whatever that function returns

a = [2,4,10,16]
# def multiply(x, n):
#     b = []
#     for i in a:
#         b.append(i*n)
#     print b
# multiply([2,4,10,16], 5)


def layered_multiples(arr,multiplier):  #array(list), multiplier(number)
    new_array = []
    for x in arr:   # x is an index within each element(2,4,5) of the array
        tempArr = []    # contains the multiplier with ones(1)

        for i in range(0,x):    # i runs through the array starting from 0 to the same range as x first 'for loop'
            tempArr.append(1)
        new_array.append(tempArr)
    return new_array        # storing the new values from the for loops.
x = layered_multiples([2,4,5],3)
print x
        

# output
#[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
    
