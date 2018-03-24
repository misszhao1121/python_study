sex = input("你是男还是女")

if sex == "女":
        color = input("你白吗？")
        money = input("你有钱吗？")
        beautiful = input("你长得漂亮吗？")

        if color == "白" and money > "10000" and beautiful == "漂亮":
            print("你是一个白富美")
        #python是通过代码快来确定语句范围的
        else:
            print("你还需要一些成长才能成为白富美")
else:
        
        color = input("你高吗？")
        money = input("你有钱吗？")
        beautiful = input("你长得帅吗？")

        if color == "高" and money > "10000" and beautiful == "帅":
            print("你是一个高富帅")
        #python是通过代码快来确定语句范围的
        else:
            print("你还需要一些成长才能成为高富帅")

