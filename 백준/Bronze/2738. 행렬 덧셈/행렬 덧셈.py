N, M = map(int, input().split())

arr1 = []
arr2 = []
for i in range(N):
    row = input()
    if len(row)>1:
        arr1.extend(row.split())
    else:
        arr1.append(row)

for i in range(N):
    row = input()
    if len(row)>1:
        arr2.extend(row.split())
    else:
        arr2.append(row)
arr1 = list(map(int, arr1))
arr2 = list(map(int, arr2))

result = [0]*len(arr1)
for i in range(len(arr1)):
    result[i] = arr1[i] + arr2[i]

result = list(map(str, result))
for i in range(N):
    print(' '.join(result[M*i:M*i+M]))
