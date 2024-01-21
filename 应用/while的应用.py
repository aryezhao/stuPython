# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2024/1/13 15:25
# @Function    : while的应用

# 应用一：计算1-100的累加和
n = 1
result = 0
while n <= 100:
    result += n
    n += 1

print(result)

# 应用二：计算1-100偶数累加和
# 方法1：累加计算
x = 0
result1 = 0
while x <= 100:
    result1 += x
    x += 2

print(result1)

# 方法2：计数器控制
z = 1
result2 = 0
while z <= 100:
    if z % 2 == 0:
        result2 += z
    z += 1
print(result2)

# 应用三：打印 *  正方形
j = 0
while j < 5:
    # 一行星星的开始
    i = 0
    while i < 5:
        # 一行内的星星不能换行，取消print默认结束符\n
        print('*', end='')
        i += 1
    # 一行星星的结束，换行显示下一行
    print()
    j += 1

# 应用三：打印 *  正三角形
p = 0
while p < 5:
    q = 0
    while q <= p:
        print('*', end='')
        q += 1
    print()
    p += 1
print('-------- 应用三：打印 *  倒三角形 ----------')
# 应用三：打印 *  倒三角形
p = 0
while p < 5:
    q = 5
    while q > p:
        print('*', end='')
        q -= 1
    print()
    p += 1

print('-------- 应用四：打印 九九乘法表 ----------')
a = 1
while a <= 9:
    b = 1
    while b <= a:
        print(f'{b} * {a} = {a *b}\t', end='')
        b += 1
    print()
    a += 1


