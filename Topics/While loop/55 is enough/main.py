# put your code here
count = 0
total = 0
target = 55
n = int(input())

while n != target:
    count += 1
    total += n
    n = int(input())

print(count)
print(total)
print(round(total / count))