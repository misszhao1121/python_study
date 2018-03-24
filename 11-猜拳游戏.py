import random
def boxgame():  
    boxing = input("请输入:剪刀(0)\t石头(1)\t布(2)")
    computer = random.randint(0, 2)
    
    if boxing == 0:
        if computer == 1:
            print("输了,不要走,决战到天亮!")
        elif computter == 2:
            print("赢了,算你运气好,不要走继续来!")
        else:
            print("嘿嘿,砸门这次是平手!!")
    elif boxing == 1: 
        if computer == 2:
            print("输了,不要走,决战到天亮!")
        elif computer == 0:
            print("赢了了,不要走,决战到天亮!")
        else:
            print("平手,不要走,决战到天亮!")
    else:
        if computer == 0:
            print("赢了,不要走,决战到天亮")
        elif computer == 1:
            print("我也是石头,平局")
        else:
            print("输了,不要走,再来一盘")
    return boxgame();
boxgame()
