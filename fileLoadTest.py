import os

import wx

rootdir = 'Download_Video'
list = os.listdir(rootdir)
filelist = []
for i in range(0, len(list)):
    path = os.path.join(rootdir, list[i])
    if not os.path.isfile(path):
        filelist.append(i)


class bucky(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'test', size=(300, 200),
                          style=wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX | wx.SYSTEM_MENU)
        panel = wx.Panel(self)

        menubar = wx.MenuBar()
        first = wx.Menu()
        load = wx.Menu()
        first.Append(-1, '加载', load)
        save = first.Append(-1, '保存')
        menubar.Append(first, '文件')

        for i in filelist:
            load.Append(-1, i)

        self.SetMenuBar(menubar)


if __name__ == '__main__':
    app = wx.App()
    frame = bucky(parent=None, id=-1)
    frame.Show()
    frame.Center()
    app.MainLoop()
