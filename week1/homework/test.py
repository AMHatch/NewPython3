 Hunters Solution. 

a = [12, 3, 1, 2, -6, 5, -8, 6]
a.sort()
solution = []
for i in range(0, (len(a) -1)):
    l = i +1
    r = len(a) - 1
    while l < r:
        ce = a[i]
        left = a[l]
        right = a[r]
        if (ce + left + right == 0):
            current_zero = []
            current_zero.append(ce)
            current_zero.append(left)
            current_zero.append(right)
            solution.append(current_zero)
            l += 1
        elif (ce + left + right > 0):
            r -= 1
        else:
            l += 1
print(solution)

