import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._PCShellF = System.Windows.Forms.PictureBox()
		self._AISpookyBOOF = System.Windows.Forms.PictureBox()
		self._PCShellB = System.Windows.Forms.PictureBox()
		self._AISpookyBOOB = System.Windows.Forms.PictureBox()
		self._PCShellF.BeginInit()
		self._AISpookyBOOF.BeginInit()
		self._PCShellB.BeginInit()
		self._AISpookyBOOB.BeginInit()
		self.SuspendLayout()
		# 
		# PCShellF
		# 
		self._PCShellF.Location = System.Drawing.Point(12, 12)
		self._PCShellF.Name = "PCShellF"
		self._PCShellF.Size = System.Drawing.Size(50, 75)
		self._PCShellF.TabIndex = 0
		self._PCShellF.TabStop = False
		# 
		# AISpookyBOOF
		# 
		self._AISpookyBOOF.Location = System.Drawing.Point(79, 12)
		self._AISpookyBOOF.Name = "AISpookyBOOF"
		self._AISpookyBOOF.Size = System.Drawing.Size(92, 109)
		self._AISpookyBOOF.TabIndex = 1
		self._AISpookyBOOF.TabStop = False
		# 
		# PCShellB
		# 
		self._PCShellB.Location = System.Drawing.Point(12, 93)
		self._PCShellB.Name = "PCShellB"
		self._PCShellB.Size = System.Drawing.Size(50, 75)
		self._PCShellB.TabIndex = 2
		self._PCShellB.TabStop = False
		# 
		# AISpookyBOOB
		# 
		self._AISpookyBOOB.Location = System.Drawing.Point(79, 127)
		self._AISpookyBOOB.Name = "AISpookyBOOB"
		self._AISpookyBOOB.Size = System.Drawing.Size(92, 109)
		self._AISpookyBOOB.TabIndex = 3
		self._AISpookyBOOB.TabStop = False
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gray
		self.ClientSize = System.Drawing.Size(996, 608)
		self.Controls.Add(self._AISpookyBOOB)
		self.Controls.Add(self._PCShellB)
		self.Controls.Add(self._AISpookyBOOF)
		self.Controls.Add(self._PCShellF)
		self.Name = "MainForm"
		self.Text = "finalproj"
		self._PCShellF.EndInit()
		self._AISpookyBOOF.EndInit()
		self._PCShellB.EndInit()
		self._AISpookyBOOB.EndInit()
		self.ResumeLayout(False)

