i_quantity = int(input())
f_quantity = int(input())
h_l = 12
n = 0
while i_quantity >= f_quantity:
    i_quantity = i_quantity // 2
    n += 1
print(n * h_l)
