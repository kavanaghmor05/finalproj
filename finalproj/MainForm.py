import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._AISpookyBOO = System.Windows.Forms.PictureBox()
		self._CompOn1 = System.Windows.Forms.PictureBox()
		self._CompOn2 = System.Windows.Forms.PictureBox()
		self._CompOn3 = System.Windows.Forms.PictureBox()
		self._ShellPCStill = System.Windows.Forms.PictureBox()
		self._ShellPcM1 = System.Windows.Forms.PictureBox()
		self._ShellPcM2 = System.Windows.Forms.PictureBox()
		self._AISpookyBOO.BeginInit()
		self._CompOn1.BeginInit()
		self._CompOn2.BeginInit()
		self._CompOn3.BeginInit()
		self._ShellPCStill.BeginInit()
		self._ShellPcM1.BeginInit()
		self._ShellPcM2.BeginInit()
		self.SuspendLayout()
		# 
		# AISpookyBOO
		# 
		self._AISpookyBOO.Location = System.Drawing.Point(79, 12)
		self._AISpookyBOO.Name = "AISpookyBOO"
		self._AISpookyBOO.Size = System.Drawing.Size(92, 109)
		self._AISpookyBOO.TabIndex = 1
		self._AISpookyBOO.TabStop = False
		# 
		# CompOn1
		# 
		self._CompOn1.Location = System.Drawing.Point(177, 12)
		self._CompOn1.Name = "CompOn1"
		self._CompOn1.Size = System.Drawing.Size(37, 33)
		self._CompOn1.TabIndex = 4
		self._CompOn1.TabStop = False
		# 
		# CompOn2
		# 
		self._CompOn2.Location = System.Drawing.Point(220, 12)
		self._CompOn2.Name = "CompOn2"
		self._CompOn2.Size = System.Drawing.Size(37, 33)
		self._CompOn2.TabIndex = 5
		self._CompOn2.TabStop = False
		# 
		# CompOn3
		# 
		self._CompOn3.Location = System.Drawing.Point(263, 12)
		self._CompOn3.Name = "CompOn3"
		self._CompOn3.Size = System.Drawing.Size(37, 33)
		self._CompOn3.TabIndex = 6
		self._CompOn3.TabStop = False
		# 
		# ShellPCStill
		# 
		self._ShellPCStill.Location = System.Drawing.Point(12, 12)
		self._ShellPCStill.Name = "ShellPCStill"
		self._ShellPCStill.Size = System.Drawing.Size(61, 58)
		self._ShellPCStill.TabIndex = 7
		self._ShellPCStill.TabStop = False
		# 
		# ShellPcM1
		# 
		self._ShellPcM1.Location = System.Drawing.Point(12, 76)
		self._ShellPcM1.Name = "ShellPcM1"
		self._ShellPcM1.Size = System.Drawing.Size(61, 58)
		self._ShellPcM1.TabIndex = 8
		self._ShellPcM1.TabStop = False
		# 
		# ShellPcM2
		# 
		self._ShellPcM2.Location = System.Drawing.Point(12, 140)
		self._ShellPcM2.Name = "ShellPcM2"
		self._ShellPcM2.Size = System.Drawing.Size(61, 58)
		self._ShellPcM2.TabIndex = 9
		self._ShellPcM2.TabStop = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gray
		self.ClientSize = System.Drawing.Size(900, 750)
		self.Controls.Add(self._ShellPcM2)
		self.Controls.Add(self._ShellPcM1)
		self.Controls.Add(self._ShellPCStill)
		self.Controls.Add(self._CompOn3)
		self.Controls.Add(self._CompOn2)
		self.Controls.Add(self._CompOn1)
		self.Controls.Add(self._AISpookyBOO)
		self.Name = "MainForm"
		self.Text = "finalproj"
		self._AISpookyBOO.EndInit()
		self._CompOn1.EndInit()
		self._CompOn2.EndInit()
		self._CompOn3.EndInit()
		self._ShellPCStill.EndInit()
		self._ShellPcM1.EndInit()
		self._ShellPcM2.EndInit()
		self.ResumeLayout(False)

