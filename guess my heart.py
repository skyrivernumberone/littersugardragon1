import random
secret = random.randint(1,10)

print('----------------game-----------------')
temp = input('来猜猜我现在心里想的数')
guess = int(temp)
x = 3
while guess!= secret and x>0:
    temp = input("好伤心，竟然猜不到我的心，再给你一次机会")
    guess = int(temp)
    x += -1
    if guess == secret:
        print('艹，你是我的蛔虫么？')
        print('略略略，猜对了也没有奖')
    else:
        if guess<secret:
            print("嘿！小了小了")
            print('哦豁，小笨蛋')
            print('我心里想得肯定是你啦')
        else:
            print("哟！大了大了~~")
            print('哦豁，小笨蛋')
            print('我心里想得肯定是你啦')
    print("滚蛋吧！")
else:
    print('艹，你是我的蛔虫么？')
    print('略略略，猜对了也没有奖')
    
print("game over!")