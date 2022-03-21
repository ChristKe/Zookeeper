# put your python code here
desk = 2
group_a = abs(int(input()))
group_b = abs(int(input()))
group_c = abs(int(input()))
classroom_a = (group_a // desk) + (group_a % desk)
classroom_b = (group_b // desk) + (group_b % desk)
classroom_c = (group_c // desk) + (group_c % desk)
print(classroom_a + classroom_b + classroom_c)
