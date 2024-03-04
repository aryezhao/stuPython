# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2024/3/4 8:20
# @Function    : 退出循环的方式


str1 = 'hello world'
for i in str1:
    if i == 'w':
        print('当前是w字母')
        break
    print(i)
else:
    print('循环正常结束之后执行的代码')