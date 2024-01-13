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



