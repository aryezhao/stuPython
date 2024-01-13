# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2024/1/13 14:32
# @Function    : 随机数

"""
步骤：
    1.导入模块
    import random
    2.使用这个模块中的功能
    random.randint()
"""
import random
# num = random.randint(0, 200)
# print(num)

# 1. 出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布：'))
# 电脑
computer = random.randint(0, 2)

# 2. 判断输赢
# 玩家获胜
if((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print("玩家获胜。。。。。。")

# 平局
elif player == computer:
    print("平局，再来一局")

else:
    print('电脑获胜')
