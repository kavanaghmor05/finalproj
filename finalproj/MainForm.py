import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._AISpookyBOO = System.Windows.Forms.PictureBox()
		self._CompOn1 = System.Windows.Forms.PictureBox()
		self._CompOn2 = System.Windows.Forms.PictureBox()
		self._CompOn3 = System.Windows.Forms.PictureBox()
		self._ShellPCStill = System.Windows.Forms.PictureBox()
		self._ShellPCM1 = System.Windows.Forms.PictureBox()
		self._ShellPcM2 = System.Windows.Forms.PictureBox()
		self._timerAI = System.Windows.Forms.Timer(self._components)
		self._timerwalk = System.Windows.Forms.Timer(self._components)
		self._timertbd = System.Windows.Forms.Timer(self._components)
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._AISpookyBOO.BeginInit()
		self._CompOn1.BeginInit()
		self._CompOn2.BeginInit()
		self._CompOn3.BeginInit()
		self._ShellPCStill.BeginInit()
		self._ShellPCM1.BeginInit()
		self._ShellPcM2.BeginInit()
		self._groupBox1.SuspendLayout()
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
		self._ShellPCStill.Click += self.ShellPCStillClick
		# 
		# ShellPCM1
		# 
		self._ShellPCM1.Location = System.Drawing.Point(12, 76)
		self._ShellPCM1.Name = "ShellPCM1"
		self._ShellPCM1.Size = System.Drawing.Size(61, 58)
		self._ShellPCM1.TabIndex = 8
		self._ShellPCM1.TabStop = False
		# 
		# ShellPcM2
		# 
		self._ShellPcM2.Location = System.Drawing.Point(12, 140)
		self._ShellPcM2.Name = "ShellPcM2"
		self._ShellPcM2.Size = System.Drawing.Size(61, 58)
		self._ShellPcM2.TabIndex = 9
		self._ShellPcM2.TabStop = False
		# 
		# timerAI
		# 
		self._timerAI.Tick += self.Timer1Tick
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.SeaShell
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._label3)
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Location = System.Drawing.Point(735, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(153, 96)
		self._groupBox1.TabIndex = 10
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Controls"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("MS Gothic", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(6, 16)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(141, 23)
		self._label1.TabIndex = 11
		self._label1.Text = "To walk use w-a-s-d"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("MS Gothic", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 41)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(141, 23)
		self._label2.TabIndex = 11
		self._label2.Text = "To interact use z"
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.Font = System.Drawing.Font("Chiller", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(32, 64)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(87, 23)
		self._label3.TabIndex = 12
		self._label3.Text = "Good luck!"
		self._label3.Click += self.Label3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gray
		self.ClientSize = System.Drawing.Size(900, 750)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._ShellPcM2)
		self.Controls.Add(self._ShellPCM1)
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
		self._ShellPCM1.EndInit()
		self._ShellPcM2.EndInit()
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)

		

	def Timer1Tick(self, sender, e):
		pass
	
		if ___ :
			self._timerwalk = True
			self._ShellPCStill.Visible = False
			self._ShellPCM1.Visible = True
			if self._timerwalk = ___ and self._PCM1.Visible = True:
				self._ShellPCM1.Visible = False
				self._ShellPCM2.Visible = True
	

	def ShellPCStillClick(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass