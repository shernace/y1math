# Generate multiples of 3 from 1 to 80

START = 1
END = 80
num = 3

for i in range(START, END+1):
  if i % num == 0:
    print(i, end=' ')
