array = [12, 3, 1, 2, -6, 5, -8, 6]
array.sort()
answer = []

for i in range(len(array) -1) : # for index in the array not exceeding the length of the array
    il = i + 1                  # left integer is the current element plus one
    ir = len(array) -1          # right integer is the length of the array, so the last element in the array.
    while il < ir :             # while the left is less than the right, i.e. they dont cross.
        ce = array[i]           # the common element is  the far left of the array, current integer bing processed
        left = array[il]        # index of arry to be one index to the right of the common element being processed
        right = array[ir]       # index of the array at the far right, or the end of the array being processed.
        if ce + left + right == 0: # if the 3 integers sum zerom then:
            zeros = []             # list to store numbers that sum zero
            zeros.append(ce)                
            zeros.append(left)
            zeros.append(right)
            answer.append(zeros)
            il+=1                     # move process to the integer in the next index to the right of current
        elif ce + left + right > 0:   # if sum is greater than zero,
            ir-=1                     # move process to the integer in the next index to the left of current
        else:
            il+=1                     # move process to the integer in the next index to the right of current
    
print(answer)
