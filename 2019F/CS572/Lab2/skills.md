
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
