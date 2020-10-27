import os
from tkinter import *
from tkinter import messagebox
from colorama import Fore

MAIN_DIR = "/Users/your_name..."
font = ('Sans serif', 35)
# IMAGE .psd, .ai, .xcf, .cdr, .tiff or .tif, .bmp, .jpg, .jpeg, .gif, .png, .raw
# VIDEO .webm, .mpg, .ogg, .mp4, .avi, .mov
# AUDIO .wav, .aiff, .au, .mp4, .mp3, .mpeg
extensions = (".jpg",".png","jpeg")
status = True
executed = False

def check(path):
	if len(path) == 0:
		return False

	if path[0] != "/":
		path = "/" + path
		path = MAIN_DIR + path
		if os.path.exists(path):
			return path
		else:
			return False

	elif path[0] == "/":
		path = MAIN_DIR + path
		if os.path.exists(path):
			return path
		else:
			return False
	else:
		return False
	

def start():
	global status
	global extensions
	global executed


	folder_to_track = path_from_input.get()
	destination_folder = path_to_input.get()

	folder_to_track = check(folder_to_track)
	destination_folder = check(destination_folder)

	if folder_to_track == False or destination_folder == False:
		print(Fore.RED + '[*] Stopped')
		messagebox.showwarning(title="Warning", message="Invalid input")
		path_from_input.delete(0,'end')
		path_to_input.delete(0,'end')
	else:
		if status:
			print(Fore.GREEN + "[*] Running...")
			executed = True
			info_lbl["text"] = "Active"
			info_lbl["fg"] = "green"
			for file in os.listdir(folder_to_track):
				if file.endswith(extensions):
					src = folder_to_track + '/' + file
					new_destination = destination_folder + '/' + file
					os.rename(src, new_destination)
					print(Fore.YELLOW + '[+] Transfered')
			window.after(3000, start) # timeout for 3 secs


def stop():
	global executed
	if not executed:
		messagebox.showwarning(title="Warning", message="Invalid input")
	else:	
		print(Fore.RED + '[*] Stopped')
		info_lbl["text"] = "Not Active"
		info_lbl["fg"] = "red"

		global status
		status = False

def restart():
	global executed
	if not executed:
		messagebox.showwarning(title="Warning", message="Invalid input")
	else:
		print(Fore.BLUE + '[*] Restarting')

		global status
		status = True

window = Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
dimension = str(width//2) + "x" + str(height//2-400)
window.title("File Handler")
window.geometry(dimension)

path_from_lbl = Label(master=window, text="Enter folder to track", font=font, padx=40)
path_from_input = Entry(master=window, width=30)

path_to_lbl = Label(master=window, text="Enter destination folder", font=font)
path_to_input = Entry(master=window, width=30)

submit_btn = Button(master=window, text="Run", height=2, width=10, command=start)
stop_btn = Button(master=window, text="Stop", height=2, width=10, command=stop)
res_btn = Button(master=window, text="Restart", height=2, width=10, command=restart)

info_lbl = Label(master=window, text="Not Active", font=('Sans serif', 24), fg="red")

path_from_lbl.grid(column=0, row=0)
path_from_input.grid(column=0, row=1)
path_to_lbl.grid(column=1, row=0)
path_to_input.grid(column=1, row=1)
submit_btn.grid(column=2, row=0)
stop_btn.grid(column=2, row=1)
res_btn.grid(column=2, row=2)
info_lbl.grid(column=1,row=2)

window.mainloop()

