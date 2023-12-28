import tkinter as tk
from tkinter import filedialog
from tkinter import *
import os, shutil, sys, zipfile
import io, base64

lcDir = ""

vanillaFiles = ["Lethal Company.exe", "nvngx_dlss.dll", "NVUnityPlugin.dll", "UnityCrashHandler64.exe", "UnityPlayer.dll"]
vanillaFolders = ["Lethal Company_Data", "MonoBleedingEdge"]

def check_folder_name(folder_path):
    folder_name = os.path.basename(folder_path)
    return folder_name == "Lethal Company"

def open_folder():
    global lcDir
    folder_path = filedialog.askdirectory(title = "Select your Lethal Company folder")
    lcDir = folder_path
    folder_path_var.set(folder_path)

    if os.path.exists(f"{lcDir}\\Lethal Company.exe"):
        mainLabel.config(text = "Looks good, get cleaning!")
        resetButton.config(state = 'normal')
    
    else:
        mainLabel.config(text = "\"Lethal Company.exe\" not found")
        resetButton.config(state = 'disabled')

def reset_mods():
    if os.path.exists(lcDir):
        global vanillaFiles, vanillaFolders
        allFiles = os.listdir(lcDir)
        rmvd = []
        resultString = f"Removed: "

        # Removes all unwanted files
        for i in allFiles:
            if i not in vanillaFiles:
                try:
                    os.remove(os.path.join(lcDir,i))
                    rmvd.append(i)
                except FileNotFoundError:
                    None
                except PermissionError:
                    None
        
        for i in allFiles:
            if i not in vanillaFolders:
                try:
                    shutil.rmtree(os.path.join(lcDir, i))
                    rmvd.append(i)
                except FileNotFoundError:
                    None
                except PermissionError:
                    None
                except NotADirectoryError:
                    None
        if len(rmvd) < 1:
            rmvd.append('Nothing :)')
        mainLabel.config(text = f"{resultString} {str(rmvd)}")

root = tk.Tk()
root.title("LC Reseter")
root.geometry('350x150')
root.minsize(350, 150)
root.maxsize(450, 150)

mainLabel = tk.Label(root, text = "Thanks for using this tool!")
mainLabel.pack(pady=10)

folder_path_var = tk.StringVar()
folder_path_label = tk.Label(root, text = "Selected Folder:",)
folder_path_label.pack(pady = 5)
folder_path_text = tk.Entry(root, textvariable=folder_path_var, state='readonly', width=50,)
folder_path_text.pack(pady=5)

buttonFrame = tk.Frame(root)
openButton = tk.Button(buttonFrame, text = "Open Folder", command=open_folder)
openButton.grid(row=1, column=0)
resetButton = tk.Button(buttonFrame, text = "Reset Game", state = 'disabled', command=reset_mods)
resetButton.grid(row=1, column=1, padx= 5)
buttonFrame.pack(pady=10)

root.mainloop()