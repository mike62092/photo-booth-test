from tkinter import *
from tkinter import ttk
from time import sleep
from picamera import PiCamera
from datetime import datetime
import time

def capture_photo():
	data = datetime.datetime.now()
	camera = PiCamera()
	camera.resolution = (1024, 768)
	camera.start_preview()
	#Camera warm-up time
	sleep(5)
	camera.capture('data.jpg')

root = Tk()
root.title("AshAck Photo Cube")
root.geometry("800x480") # Fullscreen for a 5-inch screen
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="AisAck").grid(column=0, row=0)
ttk.Button(frm, text="Take Photo!", command=capture_photo).grid(column=1, row=0)
#ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
root.mainloop()
