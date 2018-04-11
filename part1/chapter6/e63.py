import wx
from e61 import SketchWindow

class SketchFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, -1, "Sketch Frame", size=(800,600))
        self.sketch = SketchWindow(self, -1)
        self.sketch.Bind(wx.EVT_MOTION, self.OnSketchMotion)
        self.statusbar = self.CreateStatusBar()
        self.statusbar.SetFieldsCount(3)
        self.statusbar.SetStatusWidths([-1,-2,-3])

    def OnSketchMotion(self, event):
        self.statusbar.SetStatusText("Pos:%s"%str((event.GetX(), event.GetY())),0)
        self.statusbar.SetStatusText("Current Pts:%s"%len(self.sketch.curLine),1)
        self.statusbar.SetStatusText("Line Count:%s"%len(self.sketch.lines),2)
        event.Skip()

if __name__ == '__main__':
    app = wx.App()
    frame = SketchFrame(None)
    frame.Show(True)
    app.MainLoop()        
