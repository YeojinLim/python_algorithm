# 1
print("\n1) "+("-"*30))
num = int(input("학생 번호 : "))
leader = ((num - 1) // 10) * 10 + 1
print("팀장 번호 :", leader)

# 2
print("\n2) "+("-"*30))
num = int(input("숫자 : "))
if num % 2 == 0:
    print("짝수")
else:
    print("홀수")

# 3
print("\n3) "+("-"*30))
num = int(input("숫자 : "))
if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("0")

# 4
print("\n4) "+("-"*30))
age1 = int(input("첫 번째 나이 : "))
age2 = int(input("두 번째 나이 : "))
if 20 <= age1 <= 29 and 20 <= age2 <= 29:
    print("출입 가능")
else:
    print("출입 불가")

# 5
print("\n5) "+("-"*30))
for i in range(1, 51):
    if i % 5 == 0:
        print(i)

# 6        
print("\n6) "+("-"*30))
total = 0
for i in range(1, 11):
    if i % 2 == 1:
        total += i
print(total)

# 7
print("\n7) "+("-"*30))
for year in range(2014, 2501):
    if year % 400 == 0:
        print(year)
    elif year % 4 == 0 and year % 100 != 0:
        print(year)

# 8
print("\n8) "+("-"*30))
num = int(input("숫자 : "))
is_prime = True
if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print("소수")
else:
    print("소수가 아님")

# 9
print("\n9) "+("-"*30))
count = 0
for num in range(3, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count += 1
print(count)

# 10
print("\n10) "+("-"*30))
for i in range(1, 6):
    print("*" * i)


# 11
print("\n11) "+("-"*30))
for i in range(5):
    print(" " * i + "*" + " " * (8 - 2 * i) + "*")

for i in range(4, -1, -1):
    print(" " * i + "*" + " " * (8 - 2 * i) + "*")

# 12
print("\n12) "+("-"*30))
for dan in range(2, 10):
    for i in range(1, 10):
        print(f" {dan} * {i} = {dan*i:2}", end=" | ")
    print()

# 13
print("\n12) "+("-"*30))
for i in range(1, 10):
    for dan in range(2, 10):
        print(f" {dan} * {i} = {dan*i:>2}", end=" | ")
    print("",end="\n") # print()

# f"{x:2}"    # 폭 2, 우측정렬(기본)
# f"{x:<2}"   # 좌측정렬
# f"{x:^2}"   # 가운데정렬
# f"{x:>2}"   # 우측정렬(명시)
# f"{x:02}"   # 빈칸 대신 0으로 채움