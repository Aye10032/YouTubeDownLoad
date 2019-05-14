import json
import os
import win32api
from shutil import copy2

import wx


# --------------------------------- 资源文件位置设置 ---------------------------------
basedir = ""

VERSION = 'V3.2.1'
RES_PATH = 'res'
CONFIG_PATH = 'res/config.json'
TEMP_PATH = 'res/temp.json'
ARIA2C = 'aria2c.exe'
ARIA2C_PATH = basedir + '/res/aria2c.exe'
LOGO_PATH = basedir + '/res/logo.ico'
LICENCE_PATH = basedir + '/res/LICENCE'
HELP_PATH = basedir + "/res/HELP"
SEARCH_PATH = basedir + "/res/search.png"
COPY_PATH = basedir + "/res/copy.png"
LINK_PATH = basedir + "/res/link.png"
PLAY_PATH = basedir + "/res/play.png"

# --------------------------------- 前置检查部分开始 ---------------------------------
if not os.path.exists(ARIA2C):
    copy2(ARIA2C_PATH, os.getcwd())

if not os.path.exists(RES_PATH):
    os.makedirs('res')
if not os.path.exists(CONFIG_PATH):
    default_config = {
        "name": "",
        "ipaddress": "http://127.0.0.1:1080",
        "useProxy": True,
        "xiancheng": "4",
        "token": "5460f6d462bc3067e27a3fbc8d732799339a7f85",
        "single_language": "en",
        "multilanguage": False,
        "notimeline": False,
        "videopro": True
    }
    with open(CONFIG_PATH, 'w+') as conf:
        json.dump(default_config, conf, indent=4)

if not os.path.exists(TEMP_PATH):
    default_config = {}
    with open(TEMP_PATH, 'w+') as conf:
        json.dump(default_config, conf, indent=4)
# --------------------------------- 前置检查部分结束 ---------------------------------
with open(CONFIG_PATH, 'r') as conf:
    config = json.load(conf)

with open(TEMP_PATH, 'r') as conf2:
    config2 = json.load(conf2)

if not os.path.exists('Download_Video'):
    os.mkdir('Download_Video')

if not os.path.exists('res'):
    os.mkdir('res')

format_code, extension, resolution, format_note, file_size = [], [], [], [], []

rootdir = 'Download_Video'
list = os.listdir(rootdir)
filelist = []

class bucky(wx.Frame):
    # 获取当前文件路径
    current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")


    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'Frame aka window', size=(300, 200))

        panel = wx.Panel(self)
        button = wx.Button(panel, label='exit', pos=(130, 10), size=(60, 60))

        self.Bind(wx.EVT_BUTTON, self.closebutton, button)

    def closebutton(self, event):
        path = 'Download_Video\\Showstopper 1141'
        templist = os.listdir(path)
        for i in templist:
            if i.__contains__('.mp4'):
                win32api.ShellExecute(0, 'open', self.father_path +'\\'+ path +'\\'+ i, '', '', 1)
                print(self.father_path +'\\'+ path +'\\'+ i)



if __name__ == '__main__':
    app = wx.App()
    frame = bucky(parent=None, id=-1)
    frame.Show()
    app.MainLoop()
