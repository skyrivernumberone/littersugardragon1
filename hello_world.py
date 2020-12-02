versionnumber = 'v0.0.0.1'

count = {
    'cpu':{'countname':'cpu',
            'password':'121'},
    'gpu':{'countname':'gpu',
            'password':'121'}}

funzondict = {"'log in':":'log to system',"'sign':":'sign a count',"'sys':":'log in to system backstage',"'exit':":'exit the system'}

startcommond = ['log in','sign','sys','exit']

startinfo = ['\nhello to use our system\n','if you have count.',"please input 'log in'.\n","if you didn't have count ","please input 'sign' to register a count to login\n",'\n']

def start_info():
    print(versionnumber)
    for startinf in startinfo:
        print(startinf)
#log in function
def log_in(com_opt):
    if com_opt == 'log in':
        print('reload module,please wait a moment.')
        print('\ndone\n')
        countname = input('please input your countname: ')
        while countname not in count:
            print('\n\ncount can not found,')
            print('please input again.\n\n')
            countname = input('please input your countname: ')
        else:
            password = input('please input your password.')
            countinfo = count.get(countname)
            cotpas = countinfo.get('password')
            while password != cotpas:
                print('password were wrong,please input again.')
                password = input('please input your password.')
            else:
                print('log successful.')
                print('loading main system.')
    print('--------cross line--------')
#start menu
def start_menu():
    com_opt = input('Command options : ')
    while com_opt not in startcommond:
        print('\ncommond not found')
        com_opt = input('Command options : ')
    log_in(com_opt)
    sign(com_opt)
    sys(com_opt)
    if com_opt == 'exit':
        pass
#functional zone
def function_zone():
    print('Available options：\n')
    print('--------cross line--------')
    for funzoncmd,funzoninfo in funzondict.items():
        print(funzoncmd,end='')
        print(funzoninfo)
    print('--------cross line--------\n')
#sign
def sign(com_opt):
    if com_opt == 'sign':
        print('\nwait a moment ~~~\n')
        signname = input('please input your countname,\njust include 0~9,A~Z,a~z,\nand the len only support less than 5 str.: ')
        signnamelen =len(signname) 
        signnamestr = signname.isalnum()
        while signnamelen > 5 or signnamelen < 2 or signnamestr == False:
            if signnamelen >5 :
                print('\ncountname is too long.\n')
            elif signnamestr == False:
                print('\ncan not identification string.\n')
            elif signnamelen < 2:
                print('\ncountname is too short.\n')
            signname = input('please input your countname,\njust include 0~9,A~Z,a~z,\nand the len only support less than 5 str.: ')
            signnamelen = len(signname)
            signnamestr = signname.isalnum()
        print('\nsuccess\n')
        signpass = input('please input your count password,\nthe len only support less than 5 str. ')
        signpasslen = len(signpass)
        while signpasslen >5 or signpasslen < 2:
            if signpasslen >5:
                print('\npassword is too long.\n')
            elif signpasslen <2:
                print('\npassword is too short.\n')
            signpass = input('please input your count password,\nthe len only support less than 5 str. ')
            signpasslen = len(signpass)
        signname = "'"+signname+"'"
        signpass = "'"+signpass+"'" 
        count[signname] = {'countname':signname,'password':signpass}
        print('\nsign successful\n')
        print('have a good time.')
        print('\nloading system.\n\n')
        function_zone()
        start_menu()
#sys
def sys(com_opt):
    while com_opt == 'sys':
        syscmd = input("S:\\")
        while syscmd == 'change data':
            sysdata = input("S:\\data")
            while sysdata == 'versionnumber':
                print(1)
            while sysdata == 'count':
                print(2)
            while sysdata == 'funzondict':
                print(3)
            while sysdata == 'startcommond':
                print(4)
            while sysdata == 'startinfo':
                print(5)
            if sysdata == 'exit':
                pass
        if syscmd == 'exit':
            break




'''
start
'''
#start info
start_info()
function_zone()
#start menu
com_opt = input('Command options : ')
while com_opt not in startcommond:
    print('\ncommond not found')
    com_opt = input('Command options : ')
else:
    print('\ndone,please wait a moment\n')
log_in(com_opt)
sign(com_opt)
sys(com_opt)
if com_opt == 'exit':
    pass




