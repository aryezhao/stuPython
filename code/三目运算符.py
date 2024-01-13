# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2024/1/13 14:43
# @Function    : 三目运算符或三元表达式

"""
语法如下：
    条件成立执行的表达式    if 条件  else 条件不成立执行的表达式
"""
a = 1
b = 2
c = a if a > b else b
print(c)

# 需求：有两个变量：比较大小，如果变量1 大于 变量2 执行 变量1 - 变量2；否则 变量2 - 变量1
aa = 22
bb = 4
cc = aa - bb if aa > bb else bb - aa
print(cc)
