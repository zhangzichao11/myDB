import Mydb
from cmd import Cmd

class Client(Cmd):

    def __init(self):
        Cmd.__init__(self)

    @staticmethod
    def do_hello(arg):
        print("do_hello", arg)

    @staticmethod
    def do_exit():
        sys.exit()

    do_EOF = do_exit

if __name__ == "__main__":
   #如果按错数字,继续要求输入
    while True:
        # noinspection PyBroadException
        try:
            number = int(input("查询请按:1  修改请按:2\n删除请按:3  退出程序请按:4\n"))
            client = Client()
            #如果选择了1，走查询模块
            if number == 1:
                #如果查询模块里面的选项选择错误,可以继续选择
                while True:
                    # noinspection PyBroadException
                    try:
                        number1 = int(input("根据id查询,请按:1    根据手机号查询,请按:2    退出查询请按:4\n"))
                        # 输入错误次数的统计
                        count = 0
                        #查询成功后，是否继续查询标志位
                        isReturn = False
                        #如果按1,走通过id查询
                        if number1 == 1:
                            #查询完成后,是否返回查询模块的标志
                            # 如果输入id有误,要求重新输入,,如果错误达到3次,退出循环,从新走查询模块
                            while True:
                                # noinspection PyBroadException
                                try:
                                    userId = int(input("请输入您要查询的id:"))
                                    # noinspection PyCallByClass
                                    Mydb.MysqldbHelper.queryId(Mydb.MysqldbHelper, userId)
                                    #查询完成后,进行操作选择
                                    #如果选择有误,继续选择
                                    while True:
                                        # noinspection PyBroadException
                                        try:
                                            kp= int(input("继续查询,请按:1    退回上级查询模块请按:2\n"))
                                            #查询成功后,如果选择1,退出该选择模块,返回输入id模块,继续进行输入查询
                                            #如果选择2,也退出该选择模块,并根据标志是否退出,并设置是否退出输入模块的标志
                                            if kp == 1:
                                                break
                                            elif kp == 2:
                                                isReturn = True
                                                break
                                            else:print("您选择有误,请重新输入您的选择!")
                                        except:print("您选择有误,请重新输入您的选择!")
                                except:
                                    count=count+1
                                    if count==3:
                                        print("输入已经连续错误3次,请重新选择!\n")
                                        break;
                                    else:
                                        print("输入有误,请重新输入!")
                                #如果为真,退出输入模块,返回查询模块
                                if isReturn:
                                    break
                        #如果选择2,走通过手机号查询
                        elif number1 == 2:
                            # 如果输入有误,要求重新输入,如果错误达到3次,退出循环,从新走查询模块
                            while True:
                                # noinspection PyBroadException
                                try:
                                    phone = int(input("请输入您要查询的手机号:"))
                                    # noinspection PyCallByClass
                                    Mydb.MysqldbHelper.queryPhone(Mydb.MysqldbHelper, phone)
                                    # 如果选择有误,继续选择
                                    while True:
                                        # noinspection PyBroadException
                                        try:
                                            kp = int(input("继续查询,请按:1    退回上级查询模块请按:2\n"))
                                            # 查询成功后,如果选择1,退出该选择模块,返回输入id模块,继续进行输入查询
                                            # 如果选择2,也退出该选择模块,返回输入id模块,并设置是否退出输入模块的标志
                                            if kp == 1:
                                                break
                                            elif kp == 2:
                                                isReturn = True
                                                break
                                            else:
                                                print("您选择有误,请重新输入您的选择!")
                                        except:
                                            print("您选择有误,请重新输入您的选择!")
                                except:
                                    count = count + 1
                                    if count == 3:
                                        print("输入已经连续错误3次,请重新选择!\n")
                                        break;
                                    else:
                                        print("输入有误,请重新输入!")
                                # 如果为真,退出输入模块,返回查询模块
                                if isReturn:
                                    break
                        #如果按4退出该查询模块,继续走总模块流程
                        elif number1 == 4:
                             break
                        else:print("您选择有误,请重新输入您的选择!")
                    except:print("您选择有误,请重新输入您的选择!")
            #如果选择2,走修改模块
            elif number == 2:
                # 输入错误次数的统计
                count=0
                while True:
                    # noinspection PyBroadException
                    try:
                        userId=int(input("输入要修改信息的id:"))
                        # noinspection PyCallByClass
                        Mydb.MysqldbHelper.change(Mydb.MysqldbHelper,userId)
                        #修改执行完成后,退出修改模块
                        break
                    except:
                        #错误达到3次后,退出输入状态，返回上个模块
                        count = count + 1
                        if count == 3:
                            print("输入已经连续错误3次,请重新选择!\n")
                            break
                        else:
                            print("输入信息有误,请重新输入!")
            #如果选择3,走删除模块
            elif number == 3:
                count=0
                while True:
                    # noinspection PyBroadException
                    try:
                        userId=int(input("输入要删除信息的id:"))
                        # noinspection PyCallByClass
                        Mydb.MysqldbHelper.delop(Mydb.MysqldbHelper,userId)
                        # 修改执行完成后,退出修改模块
                        break
                    except:
                        # 错误达到3次后,退出输入状态，返回上个模块
                        count = count + 1
                        if count == 3:
                            print("输入已经连续错误3次,请重新选择!\n")
                            break
                        else:
                            print("输入信息有误,请重新输入!")
            elif number == 4:
                break #这里必须先退出循环后再退出cmd
                client.do_exit()
                client.cmdloop()
            else:print("选择有误,请重新选择!")
        except:
            print("选择有误,请重新选择!")
