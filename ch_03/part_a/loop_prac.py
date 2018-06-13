
arr = [2,3,5,7,2,7,83,4,7,4]
print("Lenght > ", len(arr))
count = 0

# Loop 10 times
# for item in arr:
#     count += 1
#     print(item)

print("Count >> ", count)

num = len(arr) - 1
pos = 0
while num >= 0:
    print(arr[pos])
    pos = pos + 1
    num = num - 1
