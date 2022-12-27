import itchat
from itchat.content import *
import threading
import time
from datetime import datetime

import mytools

'''
重写登录 默认的在linux上登陆不了
或者去改 源码components下的login.py
if isLoggedIn is not None:
    logger.info('Please press confirm on your phone.')
    time.sleep(1)
'''
def mylogin(enableCmdQR):
    loginuuid = itchat.get_QRuuid()
    print("请扫描二维码登录...")
    itchat.get_QR(uuid=loginuuid, enableCmdQR=enableCmdQR)
    waitForConfirm=True
    while 1:
        status = itchat.check_login(loginuuid)
        if status == '200':
            print("Login success!")
            itchat.web_init()
            itchat.show_mobile_login()
            break
        elif status == '201':
            if waitForConfirm:
                print('Please press confirm')
                waitForConfirm = False

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    print(str(datetime.now())+"-好友"+msg.User.RemarkName+":"+msg.text)
    # if str(msg.text).startswith("chat"):
    #     datas = str(msg.text)[7:]
    #     print(datas)
    #     conversation_id = ""
    #     res = mytools.get_chatgpt_once_api(datas)
    #     return res
    if str(msg.text).startswith("验证chat"):
        return "已启动！"
    if str(msg.text).startswith("重置chat"):
        mytools.conversation_id = ""
        mytools.parent_message_id = ""
        del mytools.body["conversation_id"]
        return "重置成功！"
    if str(msg.text).startswith("设置chat"):
        data=str(msg.text).split(" ")[1]
        mytools.headers["Authorization"]=data
        return "设置成功！"
    res = mytools.get_chatgpt_once_api(msg.text)
    return res



@itchat.msg_register(TEXT, isGroupChat=True)
def text_reply(msg):

    # if msg.isAt:
    #     msg.user.send(u'@%s\u2005I received: %s' % (msg.actualNickName, msg.text))
    if str(msg.text).startswith("chat"):
        print(str(datetime.now()) + "-群" + msg.User.NickName + "的" + msg.actualNickName + ":" + msg.text)
        datas = str(msg.text)[5:]
        res = mytools.get_chatgpt_once_api(datas)
        msg.user.send(res)
    if str(msg.text).startswith("重置chat"):
        mytools.conversation_id=""
        mytools.parent_message_id=""
        del mytools.body["conversation_id"]
        msg.user.send("重置成功！")


itchat.auto_login(hotReload=True,enableCmdQR=2)

# mylogin(enableCmdQR=False)
# itchat.get_contact()
# itchat.start_receiving()

itchat.run()