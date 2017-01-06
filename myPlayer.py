# Luiz Henrique de Freitas Almeida
# 06/01/2017
# My music player using python + pygame + tkinter

import Tkinter, tkFileDialog
import pygame

class Application:
	def __init__(self,master):
		self.master = master
		master.title("My Player")
		pygame.mixer.init()
		self.stateButton = False
		
		self.openButton = Tkinter.Button(master, text="Open File", command=self.openFile)
		self.openButton.pack()

		self.pauseButton = Tkinter.Button(master, text=u'\u25B6' + "/" + u'\u23F8', command=self.changeButton)
		self.pauseButton.pack()

	# Open music file
	def openFile(self):
		filename = tkFileDialog.askopenfile()
		pygame.mixer.music.load(filename)
		pygame.mixer.music.play()
	
	# Change button state (pause/unpause music)
	def changeButton(self):
		if(self.stateButton):
			self.unpauseMusic()
			self.stateButton = False
		else:
			self.pauseMusic()
			self.stateButton = True

	# Pause music
	def pauseMusic(self):
		pygame.mixer.music.pause()

	# Unpause music
	def unpauseMusic(self):
		pygame.mixer.music.unpause()
		
	
root = Tkinter.Tk()
app = Application(root)
root.mainloop()