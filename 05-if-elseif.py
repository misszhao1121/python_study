#从标准输入获取用户输入
def period():  
    num = int(input("请输入周1-7:"))
    #python里面变量的类型是根据输入的东西来判断所以需要转换成int
    #对用户的输入进行判断
    if num == 1:
         print("今天是周一")
         period();
    elif num == 2:
         print("今天是周二")
         period();
    elif num == 3:
         print("今天是周三")
         period();
    elif num == 4:
         print("今天是周四")
         period();
    elif num == 5:
         print("今天是周五")
         period();
    elif num == 6:
         print("今天是周六")
         period();
    elif num == 7:
         print("今天是周日")
         period();
    else:
        print("退出程序!!!!!!!!!!")
        quit()
period()
