import json
import os
import socket
import tkinter
import tkinter.messagebox
from threading import Thread
import threading

#初始化弹窗
root = tkinter.Tk()
root.withdraw()
root.wm_attributes('-topmost',1)

#获取实时IP地址
def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip

#将IP地址写入json文件

filename = 'config.json'
with open(filename, 'r') as f:
    data = json.load(f)
    data['server'] = get_host_ip() # <--- 添加实时ip地址.

os.remove(filename)
with open(filename, 'w') as f:
    json.dump(data, f, indent=4)


#读取json端口/密码

filename = 'config.json'
with open(filename, 'r') as f:
    data = json.load(f)
    a = data['password']
    b = data['server_port']
    c = data['method']

def runserver():
    os.system('shadowsocks-server.bat')
def talk():
    tkinter.messagebox.showinfo("提示","你的ip地址是" + get_host_ip()+"\n你的端口号是"+str(b)+"\n你的密码是" + a + "\n加密方式是"+ c +"\n请勿关闭cmd窗口")
    

#主程序
netopen = threading.Thread(target=runserver)#, daemon=True)

if __name__=='__main__':
    
    netopen.start()

if netopen.is_alive() == True:
    #弹窗显示
    talk()
    tkinter.messagebox.showinfo("欢迎","开启成功,如需退出请关闭cmd窗口")
if  netopen.is_alive() == False:
    tkinter.messagebox.showinfo("退出","服务已退出，请检查配置")

    






            
    


