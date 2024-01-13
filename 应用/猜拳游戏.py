# @Organization: 上海商业智能信息科技有限公司
# @Author      : Kevin
# @Time        : 2023/11/27 22:30
# @Function    : 猜拳游戏
"""
1. 出拳
    玩家：手动输入
    电脑：1.固定：剪刀；2，随机
2.  判断输赢
    2.1 判断获胜
    2.2 平局
    2.3 电脑获胜
"""
# 1. 出拳
# 玩家
player = int(input('请出拳：0--石头；1--剪刀；2--布：'))
# 电脑
computer = 1

# 2. 判断输赢
# 玩家获胜
if((player == 0) and (computer == 1)) or ((player == 1) and (computer == 2)) or ((player == 2) and (computer == 0)):
    print("玩家获胜。。。。。。")

# 平局
elif player == computer:
    print("平局，再来一局")

else:
    print('电脑获胜')