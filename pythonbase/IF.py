import random

while True:

    player1 = int(input("请输入你的出拳：(0:石头/1:剪刀/2:布)    "))
    player2 = random.randint(0, 2)

    if (player1 == 0 and player2 == 1) or (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 0):
        print("你赢啦!!!")

        # 显示双方选择
        print(f"\n你出了：{player1}")
        print(f"电脑出了：{player2}")

        break
    elif player1 == player2:
        print("平局！再来一次！")

        # 显示双方选择
        print(f"\n你出了：{player1}")
        print(f"电脑出了：{player2}")

        continue
    else:
        print("你输啦!!!")

        # 显示双方选择
        print(f"\n你出了：{player1}")
        print(f"电脑出了：{player2}")

        break

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
    print(sum)

i = 2
sum = 0
while i <= 100:
    sum += i
    i += 2
    print(sum)

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
    print(sum)

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 2
    print(sum)

for i in range(0, 5):
    print(i)

for i in "123456":
    if i == "4":
        print("不好！")
        break

import random

while True:

    player1 = int(input("请输入你的出拳：(0:石头/1:剪刀/2:布)    "))
    player2 = random.randint(0, 2)

    if (player1 == 0 and player2 == 1) or (player1 == 1 and player2 == 2) or (player1 == 2 and player2 == 0):
        print("你赢啦!!!")

        # 显示双方选择
        print(f"\n你出了：{player1}")
        print(f"电脑出了：{player2}")

        break
    elif player1 == player2:
        print("平局！再来一次！")

        # 显示双方选择
        print(f"\n你出了：{player1}")
        print(f"电脑出了：{player2}")

        continue
    else:
        print("你输啦!!!")

        # 显示双方选择
        print(f"\n你出了：{player1}")
        print(f"电脑出了：{player2}")

        break

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
    print(sum)

i = 2
sum = 0
while i <= 100:
    sum += i
    i += 2
    print(sum)

i = 1
sum = 0
while i <= 100:
    if i % 2 == 0:
        sum += i
    i += 1
    print(sum)

i = 1
sum = 0
while i <= 100:
    sum += i
    i += 2
    print(sum)

for i in range(0, 5):
    print(i)

for i in "123456":
    if i == "4":
        print("不好！")
        break

