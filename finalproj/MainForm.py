import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		resources = System.Resources.ResourceManager("finalproj.MainForm", System.Reflection.Assembly.GetEntryAssembly())
		self._AISpookyBOO = System.Windows.Forms.PictureBox()
		self._ShellPCStill = System.Windows.Forms.PictureBox()
		self._ShellPCM1 = System.Windows.Forms.PictureBox()
		self._ShellPCM2 = System.Windows.Forms.PictureBox()
		self._timermonst = System.Windows.Forms.Timer(self._components)
		self._timerwalk = System.Windows.Forms.Timer(self._components)
		self._timergame = System.Windows.Forms.Timer(self._components)
		self._groupBox1 = System.Windows.Forms.GroupBox()
		self._movecontr = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._timerhuh = System.Windows.Forms.Timer(self._components)
		self._Count1 = System.Windows.Forms.Label()
		self._Count2 = System.Windows.Forms.Label()
		self._Count3 = System.Windows.Forms.Label()
		self._AISpookyBOO.BeginInit()
		self._ShellPCStill.BeginInit()
		self._ShellPCM1.BeginInit()
		self._ShellPCM2.BeginInit()
		self._groupBox1.SuspendLayout()
		self.SuspendLayout()
		# 
		# AISpookyBOO
		# 
		self._AISpookyBOO.BackColor = System.Drawing.Color.Transparent
		self._AISpookyBOO.Location = System.Drawing.Point(79, 12)
		self._AISpookyBOO.Name = "AISpookyBOO"
		self._AISpookyBOO.Size = System.Drawing.Size(92, 109)
		self._AISpookyBOO.TabIndex = 1
		self._AISpookyBOO.TabStop = False
		# 
		# ShellPCStill
		# 
		self._ShellPCStill.BackColor = System.Drawing.Color.Transparent
		self._ShellPCStill.BackgroundImage = resources.GetObject("ShellPCStill.BackgroundImage")
		self._ShellPCStill.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._ShellPCStill.Location = System.Drawing.Point(12, 12)
		self._ShellPCStill.Name = "ShellPCStill"
		self._ShellPCStill.Size = System.Drawing.Size(61, 58)
		self._ShellPCStill.TabIndex = 7
		self._ShellPCStill.TabStop = False
		# 
		# ShellPCM1
		# 
		self._ShellPCM1.BackColor = System.Drawing.Color.Transparent
		self._ShellPCM1.BackgroundImage = resources.GetObject("ShellPCM1.BackgroundImage")
		self._ShellPCM1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._ShellPCM1.Location = System.Drawing.Point(12, 76)
		self._ShellPCM1.Name = "ShellPCM1"
		self._ShellPCM1.Size = System.Drawing.Size(61, 58)
		self._ShellPCM1.TabIndex = 8
		self._ShellPCM1.TabStop = False
		# 
		# ShellPCM2
		# 
		self._ShellPCM2.BackColor = System.Drawing.Color.Transparent
		self._ShellPCM2.BackgroundImage = resources.GetObject("ShellPCM2.BackgroundImage")
		self._ShellPCM2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._ShellPCM2.Location = System.Drawing.Point(12, 140)
		self._ShellPCM2.Name = "ShellPCM2"
		self._ShellPCM2.Size = System.Drawing.Size(61, 58)
		self._ShellPCM2.TabIndex = 9
		self._ShellPCM2.TabStop = False
		# 
		# timerwalk
		# 
		self._timerwalk.Tick += self.TimerwalkTick
		# 
		# timergame
		# 
		self._timergame.Tick += self.TimergameTick
		# 
		# groupBox1
		# 
		self._groupBox1.BackColor = System.Drawing.Color.Linen
		self._groupBox1.Controls.Add(self._label2)
		self._groupBox1.Controls.Add(self._label1)
		self._groupBox1.Controls.Add(self._movecontr)
		self._groupBox1.Location = System.Drawing.Point(728, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(144, 109)
		self._groupBox1.TabIndex = 10
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Controls"
		self._groupBox1.Enter += self.GroupBox1Enter
		# 
		# movecontr
		# 
		self._movecontr.Font = System.Drawing.Font("SimSun", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._movecontr.Location = System.Drawing.Point(6, 13)
		self._movecontr.Name = "movecontr"
		self._movecontr.Size = System.Drawing.Size(128, 32)
		self._movecontr.TabIndex = 0
		self._movecontr.Text = "To move use W-A-S-D"
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("SimSun", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(6, 51)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(128, 22)
		self._label1.TabIndex = 1
		self._label1.Text = "To interact use Z"
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Chiller", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(6, 64)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(128, 32)
		self._label2.TabIndex = 2
		self._label2.Text = "Good Luck!"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# Count1
		# 
		self._Count1.BackColor = System.Drawing.Color.Transparent
		self._Count1.Location = System.Drawing.Point(116, 153)
		self._Count1.Name = "Count1"
		self._Count1.Size = System.Drawing.Size(669, 77)
		self._Count1.TabIndex = 11
		# 
		# Count2
		# 
		self._Count2.BackColor = System.Drawing.Color.Transparent
		self._Count2.Location = System.Drawing.Point(108, 317)
		self._Count2.Name = "Count2"
		self._Count2.Size = System.Drawing.Size(669, 77)
		self._Count2.TabIndex = 12
		# 
		# Count3
		# 
		self._Count3.BackColor = System.Drawing.Color.Transparent
		self._Count3.Location = System.Drawing.Point(116, 503)
		self._Count3.Name = "Count3"
		self._Count3.Size = System.Drawing.Size(669, 77)
		self._Count3.TabIndex = 13
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gray
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self.ClientSize = System.Drawing.Size(884, 711)
		self.Controls.Add(self._Count3)
		self.Controls.Add(self._Count2)
		self.Controls.Add(self._Count1)
		self.Controls.Add(self._groupBox1)
		self.Controls.Add(self._ShellPCM2)
		self.Controls.Add(self._ShellPCM1)
		self.Controls.Add(self._ShellPCStill)
		self.Controls.Add(self._AISpookyBOO)
		self.DoubleBuffered = True
		self.Name = "MainForm"
		self.Text = "finalproj"
		self.Load += self.MainFormLoad
		self._AISpookyBOO.EndInit()
		self._ShellPCStill.EndInit()
		self._ShellPCM1.EndInit()
		self._ShellPCM2.EndInit()
		self._groupBox1.ResumeLayout(False)
		self.ResumeLayout(False)


	def GroupBox1Enter(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def TimergameTick(self, sender, e):
		pass
	def TimerwalkTick(self, sender, e):
		Still = self._ShellPCStill
		M1 = self._ShellPCM1
		M2 = self._ShellPCM2
		
	def MainFormKeyDown(self, sender, e):
		walkin = self._timerwalk
		
		
		
		if e.KeyCode == Keys.W:
			walkin.Enabled = True
			Still.Visible = False
			Still and M1 and M2
			if walkin = 0:
				M1.Visible = True
				M2.Visible = False
				
			if walkin = 50:
				M2.Visible = True
				M1.Visible = False
		
		if e.KeyCose == Keys.S:
			walkin.Enabled = True
			Still.Visible = False
			if walkin = 0:
				M1.Visible = True
				M2.Visible = False
				
			if walkin = 50:
				M2.Visible = True
				M1.Visible = False
				
		if e.KeyCode == Keys.A:
			walkin.Enabled = True
			Still.Visible = False
			if walkin = 0:
				M1.Visible = True
				M2.Visible = False
				
			if walkin = 50:
				M2.Visible = True
				M1.Visible = False
				
		if e.KeyCode == Keys.D:
			walkin.Enabled = True
			Still.Visible = False
			if walkin = 0:
				M1.Visible = True
				M2.Visible = False
				
			if walkin = 50:
				M2.Visible = True
				M1.Visible = False
								