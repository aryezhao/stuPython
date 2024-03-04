# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2024/1/21 22:49
# @Function    : for循环
"""
for 循环变量 in 序列：
    重复执行的代码
    ...
"""
str1 = 'shanghai'
for i in str1:
    if i == 'a':
        print('不打印。。。',i)
        continue
    elif i == 'n':
        print('bu da yin...', i)
        continue
    print(i)
