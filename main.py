from tkinter import *
from tkinter import filedialog, messagebox
import os
import template
import appTools
import threading
import clipboard


srcPath = "/"
outPath = "/"
entryWidth = 45

baseColor = "#ffffff"
workFrameBg = "#ffffff"
entryBg_a = "#fff"
FontColor_a = "#263238"
selected = "#0081b2"
deselected = "#dddddd"
boxText = "#333333"
DC_mods = ['Config', 'Patch', 'SW Deploy', 'Reports', 'Admin', 'Others']
MDM_mods = ['Android', 'iOS', 'Windows', 'Profiles', 'Admin', 'Others']
currMods = []
activeModName = None
modID = 0


def randomda(newMod, x, i):
    global modID, activeModName
    currMods[modID].config(bg=deselected, fg=boxText)
    newMod.config(bg=selected, fg="#fff")
    activeModName = x
    modID = i

def highlight(mod):
    if mod != currMods[modID]:
        mod.config(bg="#cccccc")

def lowlight(mod):
    if mod != currMods[modID]:
        mod.config(bg=deselected)


def check(event=None):
        if os.path.exists("/Volumes/DCUIRepo/"):
            serverStatus.config(text="Connected!", fg="#558B2F")
            btnconnect.config(text="Share in Cloud", bg="#8ab40b")
            return 1

        elif appTools.checkCon("dcdemo"):
            serverStatus.config(text="Not Connected!", fg="#EE7600")
            btnconnect.config(text="Connect to Server", bg="#0081b2", fg="#ffffff")
            return 2

        elif appTools.checkCon("www.google.com"):
            serverStatus.config(text="Not in ZohoCorp Network!", fg="#EE7600")
            btnconnect.config(text="Share in Cloud", bg="#cccccc", fg="#555555")
            return 3

        else:
            serverStatus.config(text="No Internet Connection!", fg="red")
            btnconnect.config(text="Share in Cloud", bg="#cccccc", fg="#555555")
            return 0


def cloudShare(event=None):
    global srcPath, outPath, activeModName
    status = check()
    if status == 1:
        outPath = "/Volumes/DCUIRepo/Test/DC/" + str(activeModName) + "/" + str(titleName.get()) + "/Iteration1"

        if appTools.copyFiles(srcPath, outPath) == 1:
            generate_HTML(event=None, cloud=1)

        else:
            Notify(opt="F", text="Select Project Directory")

    if status == 2:
        appTools.conServer()

    elif status == 3 or status == 0:
        messagebox.showerror("Error in connection", "Cloud share will only work when you are connected to 'Zoho Corp', 'Zoho Handhelds' or LAN.")


def selDir():

    global srcPath, outPath
    srcPath = outPath = filedialog.askdirectory()
    setEntry()


def setEntry():

    pathEntry.config(state="normal")
    pathEntry.delete(0, END)
    pathEntry.insert(0, str(srcPath))
    pathEntry.config(state="readonly")

    if os.path.isdir(srcPath):
        directory, iteration = os.path.split(srcPath)
        projEntry.delete(0, END)
        projEntry.insert(0, str(os.path.basename(directory)))

    option = appTools.selDevice(srcPath)

    if not option == 1:
        btnMobile.select()

    else:
        btnWeb.select()


def generate_HTML(event=None, cloud=0):
    global srcPath, outPath

    if not (srcPath == "/" or srcPath == ""):
        files = appTools.totalFiles(srcPath)

        if files == 0:
            messagebox.showerror("Cannot find Image Files", "Select the project folder which contains your files inside \"images\" Folder. Coz that's how we Roll Brozz!.")

        else:
            template.HTML(str(titleName.get()), outPath, files, option.get())
            Notify(opt="S", text="Proto Files created Successfully!")

            if autoOpen.get() == 1:
                appTools.previewStory(cloud, outPath.replace('/Volumes/', ''))

    else:
        Notify(opt="F", text="Select Project Directory")


def Notify(opt, text):
    statusMsg.pack(side=BOTTOM, fill=X)

    if opt == "S":
        statusMsg.config(text=text, fg="#000000", bg="#8cc63f", padx=5, pady=5)
    elif opt == "F":
        statusMsg.config(text=text, fg="#ffffff", bg="red", padx=5, pady=5)

    statusMsg.after(3000, statusMsg.pack_forget)


root = Tk()
root.config(bg=baseColor)
title = root.title("STORYBOARD(Beta)")
rootW = root.winfo_screenwidth()
rootH = root.winfo_screenheight()
root.geometry(str(rootW - 400)+"x600+200+200")


titleName = StringVar()
option = IntVar()
autoOpen = IntVar(value=1)
activeMod = IntVar()

# **** Create UI Elements Here ****

detailsFrame = LabelFrame(root, text="Project Details")
dfContent = Frame(detailsFrame)
btnFrame = Frame(root)
btnGrid = Frame(btnFrame)
appTitle = Label(text="STORYBOARD", pady=20, font='Lato 30 bold', bg=baseColor, fg=FontColor_a)

prodTitle = Label(dfContent, text="Select Product                      : ")
prodFrame = Frame(dfContent)
prodDC = Label(prodFrame, text="Mobile Device Mgmt")
prodMDM = Label(prodFrame, text="Desktop Central")

modTitle = Label(dfContent, text="Select Feature Module          :")
modFrame = Frame(dfContent)

projTitle = Label(dfContent, text="Project Title                          : ")
projEntry = Entry(dfContent, textvariable=titleName)
projEntry.insert(0, "Sample Title")

deviceTitle = Label(dfContent, text="Create Storyboard for           : ")
btnWeb = Radiobutton(dfContent, text='web', variable=option, value=1, indicatoron=0)
btnWeb.select()

btnMobile = Radiobutton(dfContent, text='mobile', variable=option, value=2, indicatoron=0)

pathTitle = Label(dfContent, text="Source Directory                   : ")
pathEntry = Entry(dfContent, text=srcPath)

btnChooseDir = Button(dfContent, text='Dir..', command=selDir)

autoCheck = Checkbutton(root, text="Open in browser after Export", variable=autoOpen)
autoCheck.select()

statusMsg = Label(root)
emptyStatus = statusMsg.config(text="", bg=baseColor)

btnGenerate = Label(btnGrid, text='Generate Files')
btnconnect = Label(btnGrid, text='Share in Cloud')
openPaint = Label(btnGrid, text='Open Editor')

statusBar = Frame(root, bg="#eeeeee")
svrStatFrame = Frame(statusBar, bg="#eeeeee")
serverTitle = Label(svrStatFrame, text="Server connection Status : ", font='Lato 12 bold', bg="#eeeeee")
serverStatus = Label(svrStatFrame, text="UNKNOWN", font='Lato 12 bold', bg="#eeeeee")


# **** UI Elements Configuration Here ****

detailsFrame.config(padx=15, pady=15, bg=workFrameBg, fg=FontColor_a)

prodTitle.config(pady=20, padx=5, bg=workFrameBg, fg=FontColor_a)
prodDC.config(padx=10, pady=5, bg=selected, fg="#fff")
prodMDM.config(padx=10, pady=5, bg=deselected, fg=boxText)

modTitle.config(pady=20, padx=5, bg=workFrameBg, fg=FontColor_a)

projTitle.config(pady=20, padx=5, bg=workFrameBg, fg=FontColor_a)
projEntry.config(bg=entryBg_a, fg=FontColor_a, width=entryWidth)

deviceTitle.config(pady=20, padx=5, bg=workFrameBg, fg=FontColor_a)

pathTitle.config(padx=5, pady=20, bg=workFrameBg, fg=FontColor_a)
pathEntry.config(bg=entryBg_a, fg=FontColor_a, width=entryWidth)

autoCheck.config(padx=5, pady=15)
btnGenerate.config(padx=20, pady=5, bg="#FF1744", fg="#ffffff", cursor="hand", highlightbackground="#ffffff", highlightthickness=8)
btnconnect.config(padx=20, pady=5, bg="#333333", fg="#ffffff", cursor="hand", highlightbackground="#ffffff", highlightthickness=8)
openPaint.config(padx=20, pady=5, bg="#ccc", fg="#000000", cursor="hand", highlightbackground="#ffffff", highlightthickness=8)

btnconnect.bind('<Button-1>', cloudShare)
btnGenerate.bind('<Button-1>', generate_HTML)
openPaint.bind('<Button-1>', appTools.openApp)


# **** Layout All Elements Here ****
df_X = 0

prodTitle.grid(row=df_X, column=0, sticky=W)
prodFrame.grid(row=df_X, column=1, sticky=W)
prodDC.pack(side=LEFT)
prodMDM.pack(side=LEFT)
df_X += 1
modTitle.grid(row=df_X, column=0, sticky=W)

modFrame.grid(row=df_X, column=1, sticky=W)


def modList(prod=MDM_mods):
    for i, x in enumerate(prod):
        mod = Label(modFrame, text=str(x), padx=10, pady=5, bg=deselected, fg=boxText)
        currMods.append(mod)
        mod.grid(row=0, column=i)
        mod.bind('<Button-1>', lambda e, i=i, x=x: randomda(currMods[i], x, i))
        mod.bind('<Enter>', lambda e, i=i: highlight(currMods[i]))
        mod.bind('<Leave>', lambda e, i=i: lowlight(currMods[i]))

    randomda(currMods[0], prod[0], 0)

modList()

df_X += 1
pathTitle.grid(row=df_X, column=0, sticky=W)
pathEntry.grid(row=df_X, column=1, sticky=W)
btnChooseDir.grid(row=df_X, column=2, sticky=W)
df_X += 1
projTitle.grid(row=df_X, column=0, sticky=W)
projEntry.grid(row=df_X, column=1, columnspan=2, sticky=W)
df_X += 1
deviceTitle.grid(row=df_X, column=0, sticky=W)
btnWeb.grid(row=df_X, column=1, sticky=W)
btnMobile.grid(row=df_X, column=1)

appTitle.pack(fill=X)
detailsFrame.pack(fill=X)
dfContent.pack()
autoCheck.pack()
btnGenerate.grid(row=0, column=0)
btnconnect.grid(row=0, column=1)
# openPaint.grid(row=0, column=2)
btnGrid.pack()
btnFrame.pack(fill=X)

statusBar.pack(side=BOTTOM, fill=X)

svrStatFrame.pack(side=LEFT)
serverTitle.pack(side=LEFT)
serverStatus.pack(side=LEFT)


def loopCheck():
    fff = threading.Timer(2.0, loopCheck)
    try:
        fff.start()
        check()

    except:
        fff.cancel()

def pbpaste():
    global srcPath, outPath
    text = clipboard.paste()

    try:
        if os.path.isdir(text):
            srcPath = outPath = text
            setEntry()

    except:
        srcPath = outPath = ' '

loopCheck()
pbpaste()

root.mainloop()
