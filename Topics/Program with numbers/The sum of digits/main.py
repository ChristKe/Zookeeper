# put your python code here
number = int(input())
fn = (number // 100) + (number % number)
sn = (number // 10)
ln = number % 10
sun = (fn + (sn % 10) + ln)
print(sun)