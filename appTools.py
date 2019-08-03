import socket
import os
import webbrowser
import shutil
from PIL import ImageTk, Image

def openApp(event):
    os.system("open /Applications/StoryBoard.app")


def conServer():
    os.system('open smb://dcdemo')


def checkCon(url):
    try:
        socket.gethostbyname(url)
        return True
    except:
        return False


def reframeTo(type, link):

    if type == "browser":
        link = link.replace(' ', '%20')

    elif type == "macTerminal":
        link = link.replace(' ', '\ ')

    return link


def selDevice(srcPath):
    if not (srcPath == "/" or srcPath == ""):
        try:
            tempImg = Image.open(srcPath + "/images/2.png")
            temp = ImageTk.PhotoImage(tempImg)

            if temp.width() < 1000 and temp.height() > temp.width():
                tempImg.close()
                return 2

            else:
                tempImg.close()
                return 1

        except:
            pass


def previewStory(cloud, outPath):

    if cloud == 1:
        webbrowser.open((reframeTo("browser", ("dcdemo:6060/" + outPath)) + "/index.html"), autoraise=True)

    else:
        webbrowser.open((reframeTo("browser", ("file:///Volumes/" + outPath)) + "/index.html"), new=2, autoraise=True)
        # os.system("open " + (reframeTo("macTerminal", outPath) + "/index.html"))


def totalFiles(srcPath):
    global total
    total = 0
    try:
        for file in os.listdir(srcPath + "/images"):
            if file.endswith(".png") or file.endswith(".jpg"):
                total = total + 1

        return total

    except:
        return 0


def copyFiles(srcPath, outPath):
    if not (srcPath == "/" or srcPath == ""):
        try:
            shutil.copytree(srcPath + "/images", outPath + "/images/")
            return 1

        except FileExistsError:
            shutil.rmtree(outPath)
            shutil.copytree(srcPath + "/images", outPath + "/images/")
            return 1

    else:
        return 0
