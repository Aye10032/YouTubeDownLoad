import os

import wx

rootdir = 'Download_Video'
list = os.listdir(rootdir)
filelist = []

menuBar = None
for i in range(0, len(list)):
    path = os.path.join(rootdir, list[i])
    if not os.path.isfile(path):
        filelist.append(list[i])

#关于这个方法的self 应该是会默认传进来一个self是一个
# CommandEvent对象应该只能得到按钮的id 不知道怎么直接拿出按钮对象
def print_menuitem_name(self):
    #调用全局的变量menuBar
    print(menuBar.FindItemById(self.Id).Name)

class bucky(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'test', size=(300, 200),
                          style=wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU)
        panel = wx.Panel(self)

        _menubar = wx.MenuBar()
        first = wx.Menu()
        load = wx.Menu()
        for i in filelist:
            but_1 = load.Append(-1, i)
            self.Bind(wx.EVT_MENU, print_menuitem_name, but_1)
        first.Append(-1, '加载', load)
        save = first.Append(-1, '保存')
        _menubar.Append(first, '文件')
        self.SetMenuBar(_menubar)


if __name__ == '__main__':
    app = wx.App()
    frame = bucky(parent=None, id=-1)
    frame.Show()
    frame.Center()
    #将当前的MenuBar放在全局
    menuBar = frame.MenuBar
    app.MainLoop()
