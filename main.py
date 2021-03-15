import wx
import wx.xrc

class MyFrame3 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"tugas pbo 1", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( 20, wx.FONTFAMILY_DECORATIVE, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Colonna MT" ) )
		self.SetBackgroundColour( wx.Colour( 255, 128, 128 ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.MyLabel = wx.StaticText( self, wx.ID_ANY, u"HELLO WX", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.MyLabel.Wrap( -1 )

		bSizer2.Add( self.MyLabel, 0, wx.ALL, 5 )


		bSizer1.Add( bSizer2, 1, wx.ALIGN_CENTER, 5 )

		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Nama :  Aura salsabila", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )

		bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"NIM : 192410101015", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )

		bSizer1.Add( self.m_staticText4, 0, wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass




app = wx.App()
frame =MyFrame3(parent = None)
frame.Show()
app.MainLoop()
