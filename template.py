from string import Template
from shutil import copyfile


def htmlTemplate(titleName, device, thisFile, nextFile):

    fadeScript = "$(document).ready(function(){ \n \
                  $('body').css('display', 'none');\n \
                  $('body').fadeIn(400);\n \
                  });"

    f = open('base.html', "r")
    f = f.read()

    temp = Template(f)

    return temp.substitute(titleName=titleName, deviceType=device, thisFile=thisFile, nextFile=nextFile, fadeScript=fadeScript)


def HTML(titleName, path, length, type):
    device = ''

    if type == 1:
        device = "webUI"

    elif type == 2:
        device = "mobileUI"

    for i in range(1, length + 1):

        if i == 1:

            f = open(path + "/index.html", "w+")
            f.write(htmlTemplate(titleName, device, str(i), str(i+1)))

        elif i == length:

            f = open(path + "/" + str(i) + ".html", "w+")
            f.write(htmlTemplate(titleName, device, str(i), "end"))

        else:

            f = open(path + "/" + str(i) + ".html", "w+")
            f.write(htmlTemplate(titleName, device, str(i), str(i + 1)))

        copyfile('review.js', path + '/review.js')
        copyfile('end.html', path + '/end.html')

    return 1
