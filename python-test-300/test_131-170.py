# 131
fruits = ["사과", "귤", "수박"]
for i in fruits:
    print(i)

# 132
for i in fruits:
    print("#####")

# 133
for i in ["A", "B", "C"]:
    print(i)

print("A")
print("B")
print("C")

# 134
for i in ["A", "B", "C"]:
    print("출력:", i)

print("출력:", "A")
print("출력:", "B")
print("출력:", "C")

# 135
for i in ["A", "B", "C"]:
    b = i.lower()
    print("변환:", b)

a = "A"
low_a = a.lower()
print("변환:", low_a)
b = "B"
low_b = b.lower()
print("변환:", low_b)
c = "C"
low_c = c.lower()
print("변환:", low_c)

# 136
num1 = 10
print(num1)
num2 = 20
print(num2)
num3 = 30
print(num3)

nums = [10, 20, 30]
for num in nums:
    print(num)

# 137
print(10)
print(20)
print(30)

for num in [10, 20, 30]:
    print(num)

# 138
print(10)
print("-------")
print(20)
print("-------")
print(30)
print("-------")

for i in [10, 20, 30]:
    print(i)
    print("-------")

# 139
print("++++")
print(10)
print(20)
print(30)

print("++++")
for i in [10, 20, 30]:
    print(i)

# 140
print("-------")
print("-------")
print("-------")
print("-------")

for i in [1, 2, 3, 4]:
    print("-------")

# 141
nums = [100, 200, 300]

for i in nums:
    print(i + 10)

# 142
menu = ["김밥", "라면", "튀김"]

for m in menu:
    print("오늘의 메뉴:", m)

# 143
stocks = ["SK하이닉스", "삼성전자", "LG전자"]

for name in stocks:
    print(len(name))

# 144
animals = ['dog', 'cat', 'parrot']

for name in animals:
    print(name, len(name))

# 145
for name in animals:
    print(name[0])

# 146
num = [1, 2, 3]

for i in num:
    print("3 x", i)

# 147
for i in num:
    print("3 x {} = {}".format(i, 3 * i))

# 148
str = ["가", "나", "다", "라"]

for s in str[1:]:
    print(s)

# 149
for s in str[::2]:
    print(s)

# 150
for s in str[::-1]:
    print(s)


