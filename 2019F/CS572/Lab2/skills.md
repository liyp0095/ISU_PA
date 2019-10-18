<script type="text/javascript" async
src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?
config=TeX-MML-AM_CHTML"
</script>

## wxPython

- When you're not in a paint event, use wxClientDC instead.

https://groups.google.com/forum/#!msg/wx-users/_6GCTegdpuI/zftOPa7oCgAJ
https://docs.wxwidgets.org/trunk/classwx_client_d_c.html

```python
    dc = wx.PaintDC(self)
    dc = wx.ClientDC(self)
    dc.SetPen(wx.Pen('#04d4d4', 3, wx.SOLID))
    dc.SetBrush(wx.Brush('#f0f0f0', wx.TRANSPARENT))
```


## errors

tkinter errors on macos

https://bugs.python.org/issue37833

https://github.com/pyinstaller/pyinstaller/issues/4334


$ \sum_{\forall i}{x_i^{2}} $
