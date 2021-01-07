versionnumber = ('当前为用户登录2.0版本:Currently  user login version2.0\n')
language_choice = ('\nyou can choose Chinese or English ,input C or E\n你可以输入C或者E，选择中文或英语语言\n')
hint2 = ('\nWelcome to our website\nif you have count:','Please input "1"','\nif you did not have count;','please input "2"Can help you create your own account','\nif you want to quit','you can input"3"','\n')
hint1 = ('\n欢迎登陆我们的网站\n','如果你有账号:''请输入 "1"\n','如果你没有账号;','请输入 "2",可以帮助你注册一个账号\n','如果你想退出网站','请输入"3"\n','\n')



def star():
    print(versionnumber)
    print(language_choice)
def star_nextstep(comd):
    if comd=='C':
        print("当前为中文")
        def hint_1():
            for hint in hint1:
                print(hint)
    elif comd =="E":
        print('Currently in English')
        for hint in hint2:
            print(hint2)
    else:
        print('输入有误（input error）')
        chooselanguage = (input('请选择(please choose:):')
star()
chooselanguage = (input('请选择(please choose:):'))
star_nextstep(chooselanguage)