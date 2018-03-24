
ticket = int(input("你有票吗,1是有,0是没有"))#1表示有车票,0表示没有车票

if ticket == 1:
    print("------你有票,你已经能进站检查了")
    danger = int(input("你有危险物吗,几厘米以上"))#cm
    if danger >= 10:
        print("-----不好意思,你带了危险物")
    else:
        print("恭喜你,通过安检,可以上车啦")
        print("终于可以见到我的小可爱了")
else:
    print("没有票救快去买票吧,不要逃票")
