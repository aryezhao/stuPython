# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2024/1/13 22:06
# @Function    : break和continue的应用

# break：当某些条件成立，退出整个循环
i = 1
while i <= 5:
    if i == 4:
        print('eat full,not eat')
        break
    print(f'eat {i} apple')
    i += 1

# continue：当条件成立，退出当前一次循环，继而执行下一次循环
n = 1
while n <= 5:
    if n == 3:
        print('eat bad,not eat')
        n += 1
        continue

    print(f'eat {n} apple')
    n += 1
