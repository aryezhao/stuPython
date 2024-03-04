# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2024/3/4 8:09
# @Function    : while ... else ... break
"""
所谓else指的是循环正常结束之后要执行的代码，即如果是break终止循环的情况，else下方缩进的代码将不执行
"""

i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print('输出次循环')
    i += 1
else:
    print('输出最终循环体')