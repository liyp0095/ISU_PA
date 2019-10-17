import wx

WHITE_COLOR = (255,255,255)

class MoveCircle():

    def __init__(self, parent):
        self.parent=parent
        self.parameters = [36,36,30]
        self.advance=3
        self.parent.Bind(wx.EVT_PAINT, self.on_paint)
        self.timer = wx.Timer(self.parent)
        self.parent.Bind(wx.EVT_TIMER, self.on_timer, self.timer)
        self.timer.Start(100)

    def on_paint(self, event=None):
        dc = wx.PaintDC(self.parent)
        dc.SetBrush(wx.Brush("blue"))
        dc.DrawCircle(*self.parameters)

    def on_timer(self, event):
        self.parameters[0] += self.advance
        # print(self.parameters)
        if self.parameters[0] < 36 or self.parameters[0] > 210:
            self.advance *= -1
        self.parent.Refresh()


if __name__ == "__main__":
    app = wx.App()
    title = "Circle"
    frame = wx.Frame(None, wx.ID_ANY, title, size=(250, 200))
    MoveCircle(frame)
    frame.Show(True)
    app.MainLoop()
