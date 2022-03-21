deposit = int(input())
b_er = 700000
count = 0
t = 7.1
while deposit <= b_er:
    y = ((deposit * t) / 100)
    deposit += + y
    count += 1
print(count)