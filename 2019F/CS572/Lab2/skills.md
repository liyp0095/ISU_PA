
## wxPython

- When you're not in a paint event, use wxClientDC instead.

https://groups.google.com/forum/#!msg/wx-users/_6GCTegdpuI/zftOPa7oCgAJ
https://docs.wxwidgets.org/trunk/classwx_client_d_c.html

```python
    # dc = wx.PaintDC(self)
    dc = wx.ClientDC(self)
    dc.SetPen(wx.Pen('#04d4d4', 3, wx.SOLID))
    dc.SetBrush(wx.Brush('#f0f0f0', wx.TRANSPARENT))
```


## errors

tkinter errors on macos

https://bugs.python.org/issue37833

https://github.com/pyinstaller/pyinstaller/issues/4334


## python argparser

https://docs.python.org/2/library/argparse.html


## online implementation by others

https://draughts.github.io/

## Submodule

https://git-scm.com/book/zh/v2/Git-%E5%B7%A5%E5%85%B7-%E5%AD%90%E6%A8%A1%E5%9D%97

>其中有 DbConnector 目录，不过是空的。 你必须运行两个命令：git submodule init 用来初始化本地配置文件，而 git submodule update 则从该项目中抓取所有数据并检出父项目中列出的合适的提交。
