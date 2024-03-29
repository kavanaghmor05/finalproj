﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.AIup = 0
		self.AIdown = 0
	
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
		self._wow = System.Windows.Forms.Label()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._timerques1 = System.Windows.Forms.Timer(self._components)
		self._Count1 = System.Windows.Forms.Label()
		self._Count2 = System.Windows.Forms.Label()
		self._Count3 = System.Windows.Forms.Label()
		self._comp1 = System.Windows.Forms.Button()
		self._comp2 = System.Windows.Forms.Button()
		self._comp3 = System.Windows.Forms.Button()
		self._compback = System.Windows.Forms.Label()
		self._compques1 = System.Windows.Forms.Label()
		self._compans1 = System.Windows.Forms.TextBox()
		self._compques2 = System.Windows.Forms.Label()
		self._compques3 = System.Windows.Forms.Label()
		self._compans2 = System.Windows.Forms.TextBox()
		self._compans3 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._compex = System.Windows.Forms.Button()
		self._timerques2 = System.Windows.Forms.Timer(self._components)
		self._timerques3 = System.Windows.Forms.Timer(self._components)
		self._label3 = System.Windows.Forms.Label()
		self._Door = System.Windows.Forms.Button()
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
		self._AISpookyBOO.BackgroundImage = resources.GetObject("AISpookyBOO.BackgroundImage")
		self._AISpookyBOO.Location = System.Drawing.Point(401, 12)
		self._AISpookyBOO.Name = "AISpookyBOO"
		self._AISpookyBOO.Size = System.Drawing.Size(92, 111)
		self._AISpookyBOO.TabIndex = 1
		self._AISpookyBOO.TabStop = False
		# 
		# ShellPCStill
		# 
		self._ShellPCStill.BackColor = System.Drawing.Color.Transparent
		self._ShellPCStill.BackgroundImage = resources.GetObject("ShellPCStill.BackgroundImage")
		self._ShellPCStill.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._ShellPCStill.Location = System.Drawing.Point(12, 641)
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
		self._ShellPCM1.Location = System.Drawing.Point(12, 577)
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
		self._ShellPCM2.Location = System.Drawing.Point(63, 25)
		self._ShellPCM2.Name = "ShellPCM2"
		self._ShellPCM2.Size = System.Drawing.Size(61, 58)
		self._ShellPCM2.TabIndex = 9
		self._ShellPCM2.TabStop = False
		self._ShellPCM2.Click += self.ShellPCM2Click
		# 
		# timermonst
		# 
		self._timermonst.Tick += self.TimermonstTick
		# 
		# timerwalk
		# 
		self._timerwalk.Interval = 20
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
		self._groupBox1.Controls.Add(self._wow)
		self._groupBox1.Location = System.Drawing.Point(728, 12)
		self._groupBox1.Name = "groupBox1"
		self._groupBox1.Size = System.Drawing.Size(144, 138)
		self._groupBox1.TabIndex = 10
		self._groupBox1.TabStop = False
		self._groupBox1.Text = "Controls"
		self._groupBox1.Enter += self.GroupBox1Enter
		# 
		# wow
		# 
		self._wow.Font = System.Drawing.Font("SimSun", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._wow.Location = System.Drawing.Point(0, 13)
		self._wow.Name = "wow"
		self._wow.Size = System.Drawing.Size(128, 43)
		self._wow.TabIndex = 0
		self._wow.Text = "Ask Mr.Szelogowski about his AI!"
		self._wow.Click += self.MovecontrClick
		# 
		# label1
		# 
		self._label1.Font = System.Drawing.Font("SimSun", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(0, 51)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(144, 43)
		self._label1.TabIndex = 1
		self._label1.Text = """To interact click
Press escape to close the game!"""
		self._label1.Click += self.Label1Click
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Chiller", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(22, 103)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(99, 32)
		self._label2.TabIndex = 2
		self._label2.Text = "Good Luck!"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._label2.Click += self.Label2Click
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
		# comp1
		# 
		self._comp1.BackColor = System.Drawing.Color.SteelBlue
		self._comp1.BackgroundImage = resources.GetObject("comp1.BackgroundImage")
		self._comp1.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._comp1.ForeColor = System.Drawing.Color.Transparent
		self._comp1.Location = System.Drawing.Point(237, 153)
		self._comp1.Name = "comp1"
		self._comp1.Size = System.Drawing.Size(90, 77)
		self._comp1.TabIndex = 14
		self._comp1.UseVisualStyleBackColor = False
		self._comp1.Click += self.Comp1Click
		# 
		# comp2
		# 
		self._comp2.BackColor = System.Drawing.Color.SteelBlue
		self._comp2.BackgroundImage = resources.GetObject("comp2.BackgroundImage")
		self._comp2.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._comp2.ForeColor = System.Drawing.Color.Transparent
		self._comp2.Location = System.Drawing.Point(363, 317)
		self._comp2.Name = "comp2"
		self._comp2.Size = System.Drawing.Size(90, 77)
		self._comp2.TabIndex = 15
		self._comp2.UseVisualStyleBackColor = False
		self._comp2.Click += self.Comp2Click
		# 
		# comp3
		# 
		self._comp3.BackColor = System.Drawing.Color.SteelBlue
		self._comp3.BackgroundImage = resources.GetObject("comp3.BackgroundImage")
		self._comp3.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self._comp3.ForeColor = System.Drawing.Color.Transparent
		self._comp3.Location = System.Drawing.Point(679, 503)
		self._comp3.Name = "comp3"
		self._comp3.Size = System.Drawing.Size(98, 77)
		self._comp3.TabIndex = 16
		self._comp3.UseVisualStyleBackColor = False
		self._comp3.Click += self.Comp3Click
		# 
		# compback
		# 
		self._compback.BackColor = System.Drawing.Color.MediumSlateBlue
		self._compback.Location = System.Drawing.Point(152, 63)
		self._compback.Name = "compback"
		self._compback.Size = System.Drawing.Size(576, 465)
		self._compback.TabIndex = 17
		self._compback.Click += self.CompbackClick
		# 
		# compques1
		# 
		self._compques1.BackColor = System.Drawing.Color.FloralWhite
		self._compques1.Font = System.Drawing.Font("Comic Sans MS", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._compques1.Location = System.Drawing.Point(178, 84)
		self._compques1.Name = "compques1"
		self._compques1.Size = System.Drawing.Size(275, 100)
		self._compques1.TabIndex = 18
		self._compques1.Text = " "
		self._compques1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# compans1
		# 
		self._compans1.Font = System.Drawing.Font("Comic Sans MS", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._compans1.Location = System.Drawing.Point(459, 87)
		self._compans1.Name = "compans1"
		self._compans1.Size = System.Drawing.Size(249, 97)
		self._compans1.TabIndex = 19
		# 
		# compques2
		# 
		self._compques2.BackColor = System.Drawing.Color.FloralWhite
		self._compques2.Font = System.Drawing.Font("Comic Sans MS", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._compques2.Location = System.Drawing.Point(178, 197)
		self._compques2.Name = "compques2"
		self._compques2.Size = System.Drawing.Size(275, 100)
		self._compques2.TabIndex = 20
		self._compques2.Text = " "
		self._compques2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# compques3
		# 
		self._compques3.BackColor = System.Drawing.Color.FloralWhite
		self._compques3.Font = System.Drawing.Font("Comic Sans MS", 20.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._compques3.Location = System.Drawing.Point(178, 308)
		self._compques3.Name = "compques3"
		self._compques3.Size = System.Drawing.Size(275, 100)
		self._compques3.TabIndex = 21
		self._compques3.Text = " "
		self._compques3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# compans2
		# 
		self._compans2.Font = System.Drawing.Font("Comic Sans MS", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._compans2.Location = System.Drawing.Point(459, 200)
		self._compans2.Name = "compans2"
		self._compans2.Size = System.Drawing.Size(249, 97)
		self._compans2.TabIndex = 22
		# 
		# compans3
		# 
		self._compans3.Font = System.Drawing.Font("Comic Sans MS", 48, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._compans3.Location = System.Drawing.Point(459, 311)
		self._compans3.Name = "compans3"
		self._compans3.Size = System.Drawing.Size(249, 97)
		self._compans3.TabIndex = 23
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkSlateGray
		self._button1.Font = System.Drawing.Font("Comic Sans MS", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.ForeColor = System.Drawing.Color.Chartreuse
		self._button1.Location = System.Drawing.Point(178, 412)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(275, 106)
		self._button1.TabIndex = 24
		self._button1.Text = "Answer"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkSlateGray
		self._button2.Font = System.Drawing.Font("Comic Sans MS", 27.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.ForeColor = System.Drawing.Color.Red
		self._button2.Location = System.Drawing.Point(459, 412)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(249, 106)
		self._button2.TabIndex = 25
		self._button2.Text = "Hint"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# compex
		# 
		self._compex.BackColor = System.Drawing.Color.Red
		self._compex.ForeColor = System.Drawing.Color.Maroon
		self._compex.Location = System.Drawing.Point(706, 63)
		self._compex.Name = "compex"
		self._compex.Size = System.Drawing.Size(22, 23)
		self._compex.TabIndex = 26
		self._compex.Text = "X"
		self._compex.UseVisualStyleBackColor = False
		self._compex.Click += self.CompexClick
		# 
		# timerques2
		# 
		self._timerques2.Tick += self.Timerques2Tick
		# 
		# timerques3
		# 
		self._timerques3.Tick += self.Timerques3Tick
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Linen
		self._label3.Location = System.Drawing.Point(12, 89)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(89, 109)
		self._label3.TabIndex = 27
		# 
		# Door
		# 
		self._Door.BackColor = System.Drawing.Color.Peru
		self._Door.Font = System.Drawing.Font("Comic Sans MS", 9.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._Door.Location = System.Drawing.Point(1, 605)
		self._Door.Name = "Door"
		self._Door.Size = System.Drawing.Size(26, 104)
		self._Door.TabIndex = 28
		self._Door.Text = """D
o
o
r"""
		self._Door.UseVisualStyleBackColor = False
		self._Door.Click += self.DoorClick
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Gray
		self.BackgroundImage = resources.GetObject("$this.BackgroundImage")
		self.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
		self.ClientSize = System.Drawing.Size(884, 711)
		self.Controls.Add(self._Door)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._compex)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._compans3)
		self.Controls.Add(self._compans2)
		self.Controls.Add(self._compques3)
		self.Controls.Add(self._compques2)
		self.Controls.Add(self._compans1)
		self.Controls.Add(self._compques1)
		self.Controls.Add(self._compback)
		self.Controls.Add(self._comp3)
		self.Controls.Add(self._comp2)
		self.Controls.Add(self._comp1)
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
		self.PerformLayout()


	def GroupBox1Enter(self, sender, e):
		pass

	def Label1Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		self._compback.Visible = False
		self._compques1.Visible = False
		self._compans1.Visible = False
		self._compques2.Visible = False
		self._compans2.Visible = False
		self._compques3.Visible = False
		self._compans3.Visible = False
		self._button1.Visible = False
		self._button2.Visible = False
		self._compex.Visible = False
		self._AISpookyBOO.Visible = False
		self._timerques1.Enabled = False
		self._timerques2.Enabled = False
		self._timerques3.Enabled = False
		self._timermonst.Enabled = False
		self._label3.Visible = False
		Still = self._ShellPCStill
		M1 = self._ShellPCM1
		M2 = self._ShellPCM2
		M1.Visible = False
		M2.Visible = True
		Still.Visible = False
		
	

	def TimergameTick(self, sender, e):
		if ShellPCStill.Right >= Count1.Left and ShellPCStill.Bottom >= Count1.Top and ShellPCStill.Top <= Count1.Bottom and ShellPCStill.Left <= Count1.Right:
			pass
	def TimerwalkTick(self, sender, e):
		pass
		
	def MainFormKeyDown(self, sender, e):
		walkin = self._timerwalk
		Still = self._ShellPCStill
		M1 = self._ShellPCM1
		M2 = self._ShellPCM2
		
		
		
		if e.KeyCode == Keys.W:
			self.flagright = False
			walkin.Enabled = True
			
		if e.KeyCode == Keys.S:
			self.flagright = True
			walkin.Enabled = True
			
				
		if e.KeyCode == Keys.A:
			walkin.Enabled = True
			
				
		if e.KeyCode == Keys.D:
			walkin.Enabled = True
			
			
		#if flagd == True:
			#ShellPCStill.Top += 5
		#if flagd == False:
			#ShellPCStill.Top -= 5
		#if ShellPCStill.Top <= 10:
			#tmr.Enabled = False
		#if ShellPCStill.Bottom >= self.Height - 50:
			#tmr.Enabled = False
			
								

	def Comp1Click(self, sender, e):
		self._compback.Visible = True
		self._compques1.Visible = True
		self._compans1.Visible = True
		self._compques2.Visible = True
		self._compans2.Visible = True
		self._compques3.Visible = True
		self._compans3.Visible = True
		self._button1.Visible = True
		self._button2.Visible = True
		self._compex.Visible = True
		self._compques1.Text = "one plus one equals"
		self._compques2.Text = "Name the continent"
		self._compques3.Text = "How to pronounce Szelogowski"
		

	def CompbackClick(self, sender, e):
		pass

	def CompbackClick(self, sender, e):
		pass

	def CompexClick(self, sender, e):
		self._compback.Visible = False
		self._compques1.Visible = False
		self._compans1.Visible = False
		self._compques2.Visible = False
		self._compans2.Visible = False
		self._compques3.Visible = False
		self._compans3.Visible = False
		self._button1.Visible = False
		self._button2.Visible = False
		self._compex.Visible = False

	def Button1Click(self, sender, e):
		if str(self._compans1.Text) == "1+1=" and str(self._compans2.Text) == "Pangea" and str(self._compans3.Text) == "Suh-Zell-Go-wisk-ee":
			self._timerques1.Enabled = True
			self._compback.Visible = False
			self._compques1.Visible = False
			self._compans1.Visible = False
			self._compques2.Visible = False
			self._compans2.Visible = False
			self._compques3.Visible = False
			self._compans3.Visible = False
			self._button1.Visible = False
			self._button2.Visible = False
			self._compex.Visible = False
			self._compans1.Text = ""
			self._compans2.Text = ""
			self._compans3.Text = ""
			
		elif str(self._compans1.Text) == "Fish" and str(self._compans2.Text) == "read" and str(self._compans3.Text) == "correct":
			self._timerques2.Enabled = True
			self._compback.Visible = False
			self._compques1.Visible = False
			self._compans1.Visible = False
			self._compques2.Visible = False
			self._compans2.Visible = False
			self._compques3.Visible = False
			self._compans3.Visible = False
			self._button1.Visible = False
			self._button2.Visible = False
			self._compex.Visible = False
			self._compans1.Text = ""
			self._compans2.Text = ""
			self._compans3.Text = ""
			
		elif str(self._compans1.Text) == "also correct" and str(self._compans2.Text) == "True" and str(self._compans3.Text) == "wrong":
			self._timerques3.Enabled = True
			self._compback.Visible = False
			self._compques1.Visible = False
			self._compans1.Visible = False
			self._compques2.Visible = False
			self._compans2.Visible = False
			self._compques3.Visible = False
			self._compans3.Visible = False
			self._button1.Visible = False
			self._button2.Visible = False
			self._compex.Visible = False
			self._compans1.Text = ""
			self._compans2.Text = ""
			self._compans3.Text = ""
			
		else:
			Application.Exit()

	def Comp2Click(self, sender, e):
		self._compback.Visible = True
		self._compques1.Visible = True
		self._compans1.Visible = True
		self._compques2.Visible = True
		self._compans2.Visible = True
		self._compques3.Visible = True
		self._compans3.Visible = True
		self._button1.Visible = True
		self._button2.Visible = True
		self._compex.Visible = True
		self._compques1.Text = "bees are"
		self._compques2.Text = "read or read"
		self._compques3.Text = "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo"

	def Comp3Click(self, sender, e):
		self._compback.Visible = True
		self._compques1.Visible = True
		self._compans1.Visible = True
		self._compques2.Visible = True
		self._compans2.Visible = True
		self._compques3.Visible = True
		self._compans3.Visible = True
		self._button1.Visible = True
		self._button2.Visible = True
		self._compex.Visible = True
		self._compques1.Text = "Colorless green ideas sleep furiously"
		self._compques2.Text = "All generlizations are false, including this one"
		self._compques3.Text = "Has anyone really bean far even as decided to use even go want to do look more like?"

	def Button2Click(self, sender, e):
		if self._compques1.Text == "bees are" and self._compques2.Text == "read or read" and self._compques3.Text == "Buffalo buffalo Buffalo buffalo buffalo buffalo Buffalo buffalo":
			MessageBox.Show("Buffalo")
		
		elif self._compques1.Text == "Colorless green ideas sleep furiously" and self._compques2.Text == "All generlizations are false, including this one" and self._compques3.Text == "Has anyone really bean far even as decided to use even go want to do look more like?":
			MessageBox.Show("Some of these are correct and some are not?")
		
		elif self._compques1.Text == "one plus one equals" and self._compques2.Text == "Name the continent" and self._compques3.Text == "How to pronounce Szelogowski":
			MessageBox.Show("Those symbol buttons look shiny, don't they?")
		
		
	

	def TimermonstTick(self, sender, e):
		pass

	def MovecontrClick(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def ShellPCM2Click(self, sender, e):
		self._label3.Visible = True
		self._label3.Text = "Szelogowski:  The AI has taken form! The power of music was too strong! Shut it down with the questions!"

	def Timerques3Tick(self, sender, e):
		if self._timerques1.Enabled == True and self._timerques2.Enabled == True and self._timerques3.Enabled == True:
			self._label3.Visible = True
			self._AISpookyBOO.Visible = False
			self._label3.Text = "Szelogowski:  You did it! Wait this is after hours, LEAVE! There is no prize!"

	def DoorClick(self, sender, e):
		Application.Exit()

	def Timerques2Tick(self, sender, e):
		if self._timerques1.Enabled == True and self._timerques2.Enabled == True:
			self._label3.Visible = True
			self._AISpookyBOO.Visible = True
			self._label3.Text = "Szelogowski:  The AI escaped! QUICKLY!"