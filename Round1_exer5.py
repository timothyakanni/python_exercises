n = int(input())
k = int(input())

count = k

first = []
result = []
for num in range(1, n):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
            first.append(num,)
            if (count % k == 0):
                result.append(num,)
            count = count + 1


print(*result, sep=" ")
print(*first, sep=" ")
