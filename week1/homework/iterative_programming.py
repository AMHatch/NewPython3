# #1 1. Multiply Vectors
# Given two lists of numbers of the same length, create a new list by multiplying the pairs of 
# numbers in corresponding positions in the two lists. Example:

# [2, 4, 5] x [2, 3, 6] = [4, 12, 30]

# list1 = [2,4,5]
# list2 = [2,3,6]
# list3 = []
# index = 0
# while index < len(list1):                          #While index is less than the length of the list, multipy list1[index] by list2[index]
#     list3.append(list1[index] * list2[index])      #multipy list1[index] by list2[index]
#     index+=1                                       # increment index up one
# print(list3) 

# #2 2. Matrix Addition
# Given two two-dimensional lists of numbers of the size 2x2 two dimensional list is represented
#  as an list of lists:

# [ [2, -2],
#    [5, 3] ]
# Calculate the result of adding the two matrices.
#  The number in each position in the resulting matrix should be the sum of the numbers
#  in the corresponding addend matrices.
#  Example: to add

# 1 3
# 2 4
# and
# 5 2
# 1 0
# results in
# 6 5
# 3 4

# matrix1 = [[1,3],[2,4],]
# matrix2 = [[5,2],[1,0],]
# final_matrix=[]
# index0 = 0
# while index0 < len(matrix1):                                                 #While index is less than the length of matrix1,
#     matrix3 = []                                                            # really should be called a list, since we're using it to add to another list to create a matrix
#     index1 = 0                                                              
#     while index1 < len(matrix1):                                            #While index1 is less than the length of matrix1,
#         matrix3.append(matrix1[index0][index1] + matrix2[index0][index1])     # we're adding the value of matrix1[0,0](in this case '1') to the value of matrix2[0,0](5) and appending it to list matrix3
#         index1+=1                                                           # incrementing the value of index1 by 1 so the next loop does matrix1[0,1]+matrix2[0,1]
#     index0 += 1                                         # incrementing the value of index0 by 1 so the next loop does matrix1[1,0]+matrix2[1,0] and matrix1[1,1]+matrix2[1,1]
#     final_matrix.append(matrix3)                        # appending the results of the inner while loop to final_matrix, will look like:
# print(final_matrix)                                                 # [[loop one,increment index1 for loop two],[loop three after incrementing index0,increment index1 for loop 4]]

#3. use your solution in Matrix Addition, 
# and extend it to work for a pair of matrices of any size,
#  as long as they have the same size.
# [[1,5,4],[2,3,6],[4,8,9]]
# [[2,9,3],[4,8,1],[5,7,6]]


# tried it with a while loop. having trouble getting it to work. see for loop below.  

#                                                               <<<<<REVISIT>>>>>>>

# matrix1 = [[1,5,4],[2,3,6],[4,8,9]]
# matrix2 = [[2,9,3],[4,8,1],[5,7,6]]

# final_matrix=[]

# index = 0
# while index < len(matrix1):
#     matrix3 = []
#     index0 = 0
#     while index0 < len(matrix1):
#         final_inner = 0
#         index1 = 0
#         while index1 < len(matrix1):
#             matrix1_inner = matrix1[index1]
#             matrix2_inner = matrix2[index0]
#             final_inner = matrix1_inner[index0] * matrix2_inner[index1]
#             index1+=1
#         matrix3.append(final_inner)
#         index0 += 1
#     final_matrix.append(matrix3)
#     index +=1
# print(final_matrix) 

#                    >>>>>>Definately need clarification on this<<<<<<<<<<    
# matx1 = [[1,5,4],[2,3,6],[4,8,9]]
# matx2 = [[2,9,3],[4,8,1],[5,7,6]]

# final_matx = []

# for indexA in range(len(matx1)):                                # for indexA in the range of the lenght of matx1 so :(0,1,2)
#     matx3 = []                                                  # like above, really should be a list since its being wiped after 3 indices
#     for indexB in range(len(matx1)):                            # for indexb in the range of the lenght of matx1 so :(0,1,2)
#         inner_matx = 0                                          #values being saved to be appended to matx3
#         for indexC in range(len(matx1)):                        # for indexc in the range of the lenght of matx1 so :(0,1,2)
#             matx1_index = matx1[indexC]                         # matx1_index is the mutable indexA of matx1 being saved to be used in equation.|  
#             matx2_index = matx2[indexB]                         # matx2_index is the mutable indexB of matx2 being saved to be used in equation.|     
#             inner_matx += matx1_index[indexB] + matx2_index[indexC]           
#         matx3.append(inner_matx)
#     final_matx.append(matx3)

# print(final_matx)

#4
# Given a list of numbers or strings, create a new list containing the same elements as the first list,
#  except with any duplicate values removed. Print the list.

# for i in list1:
#     if i not in list1:
#         list2.append(i)
# print(list2)

    # 5 L337 5P43K

# my_string = input('Give me a phrase!').upper()
# my_list = list(my_string)
# letter_list = ['A','E','G','I','O','S','T']
# number_list = ['4','3','6','1','0','5','7']

# for i in my_list:
#     # print(i)                                         # i is then letter in the input
#     if i in letter_list:
#         i_of_letter = letter_list.index(i)
#         # print(i_of_letter)                           # i_of _letter is the index of the letters in letter_list that match between the 
#         # input list and letter list
#         value = number_list[i_of_letter]
#                                          # value of the index in number list given from letter list.
#         orig_index = my_list.index(i) # index of the orignial list (my list) that needs to be replaced with the value from number list.
#         my_list[orig_index] = number_list[i_of_letter]   # this is the value of the orignial list that has been replaced by the numbers from number list. 
# result =''.join(my_list)
# print(result)

    #6 Given a word as a string, 
    # print the result of extending any long vowels to the length of 5.

# myInput = input("Give me a word with a long vowel : ")
# vowels = ['ee', 'aa','ii','oo','uu','yy']

# final= ''

# for i in range(len(myInput)):
#     x = myInput[i:i+2]
#     if x in vowels:
#         final += myInput[i] * 4
#     else:
#         final += myInput[i]
# print(final)

# 7 caesar cypher
# code = 'Lbh zhfg hayrnea jung lbh unir yrnearq'
# code = code.lower()
# alph ='abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
# key = 13
# result = ''

# for i in code:
#     if i in alph:
#         letter_index = alph.index(i)
#         new_index = letter_index + key
#         decode = alph[new_index]
#         result += decode
#     else:
#         result += i
# print(result)








