from tkinter import *
from tkinter import Button
from tkinter import Text
from tkinter import END
import numpy as np
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
event2canvas = lambda e, c: (c.canvasx(e.x), c.canvasy(e.y))
import os
from tkinter import messagebox
import pickle
from tkinter import font

from PIL import Image
from PIL import ImageTk

main = Tk()
main.title('BREAST App for offline annotating')
w, h = main.winfo_screenwidth(), main.winfo_screenheight()
main.geometry("%dx%d+0+0" % (w, h))
main.state("zoomed")
rows = 0
while rows < 60:
    main.rowconfigure(rows, weight=1)
    main.columnconfigure(rows, weight=1)
    rows += 1
folder = askdirectory(title='Please select a directory')
png_files = [folder + '\\' + f for f in os.listdir(folder) if '.png' in f]
filenames_only = [f for f in os.listdir(folder) if '.png' in f]
# PIL supported image types
img_types = (".png")
# get list of files in folder
flist0 = os.listdir(folder)
# create sub list of image files (no sub folders, no wrong file types)
fnames = [f for f in flist0 if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(img_types)]
File = os.path.join(folder, fnames[0])  # name of first file in list
i = 0

#img = PhotoImage(file=File)
im = Image.open(File)
canvas = Canvas(main, bd=0)
canvas.grid(row=1, column=10, sticky="NSEW",columnspan=57,rowspan=40)
canvas.update()
widthCanvas = canvas.winfo_width()
heightCanvas = canvas.winfo_height()
im2 = im.resize((widthCanvas, heightCanvas), Image.ANTIALIAS)
img = ImageTk.PhotoImage(im2)
canvas.ImageHandel = canvas.create_image(0, 0, image=img, anchor="nw")
casecounter=0
cx_Press = 0
cx_Release = 0
cy_Press = 0
cy_Release = 0
# Create directory
dirName = [folder + '\\' +'Data']

try:
    # Create target Directory
    os.mkdir(dirName[0])
    print("Directory ", dirName, " Created ")
except FileExistsError:
    print("Directory ", dirName, " already exists")


def Next_Image():
    global casecounter
    global canvas
    global img
    global cx_Press, cy_Press
    global cx_Release, cy_Release
    casecounter = casecounter + 1
    if (casecounter <= (len(fnames) - 1)):
        File = os.path.join(folder, fnames[casecounter])
        im = Image.open(File)
        im2 = im.resize((widthCanvas, heightCanvas), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im2)
        #print(width, height)
        canvas.itemconfigure(canvas.ImageHandel, image=img)
    MassSt = var_TypeMassSt.get()
    MassNSD = var_TypeMassNSD.get()
    MassS = var_TypeMassS.get()
    Asy = var_TypeAsy.get()
    Calc = var_TypeCalc.get()
    MassD = var_TypeMassD.get()
    Den = var_Den.get()
    CatClass = var_Class.get()
    Qual = var_Qual.get()
    Arch = var_TypeArch.get()
    VarsToSave = {'MassSt': MassSt, 'MassNSD': MassNSD, 'MassS': MassS, 'Asy': Asy,
                  'Calc': Calc, 'MassD': MassD, 'Den': Den, 'CatClass': CatClass, 'Qual': Qual, 'Arch': Arch,
                  'Annotations': {'cx_Press': cx_Press, 'cx_Release': cx_Release,
                                  'cy_Press': cy_Press, 'cy_Release': cy_Release},
                  'widthCanvas': widthCanvas, 'heightCanvas': heightCanvas}
    fnamepickel=(fnames[casecounter-1][:-3])+'pickle'
    fnamepickel=dirName[0]+'\\'+fnamepickel
    with open(fnamepickel, 'wb') as f:
        pickle.dump(VarsToSave, f)
    var_TypeMassSt.set(False)
    var_TypeMassNSD.set(False)
    var_TypeMassS.set(False)
    var_TypeAsy.set(False)
    var_TypeCalc.set(False)
    var_TypeMassD.set(False)
    var_Den.set(False)
    var_Class.set(False)
    var_Qual.set(False)
    var_TypeArch.set(False)

    canvas.delete('rect')
    orig_color = claButton.cget("background")
    broButton.configure(background=orig_color)
    cx_Press = 0
    cx_Release = 0
    cy_Press = 0
    cy_Release = 0
    i = 0


def Previous_Image():
    global casecounter
    global canvas
    global img
    global cx_Press, cy_Press
    global cx_Release, cy_Release
    casecounter = casecounter - 1
    if (casecounter >= 0):
        File = os.path.join(folder, fnames[casecounter])
        im = Image.open(File)
        im2 = im.resize((widthCanvas, heightCanvas), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im2)
        canvas.itemconfigure(canvas.ImageHandel, image=img)
        #print(img.width())
    MassSt = var_TypeMassSt.get()
    MassNSD = var_TypeMassNSD.get()
    MassS = var_TypeMassS.get()
    Asy = var_TypeAsy.get()
    Calc = var_TypeCalc.get()
    MassD = var_TypeMassD.get()
    Den = var_Den.get()
    CatClass = var_Class.get()
    Qual = var_Qual.get()
    Arch = var_TypeArch.get()
    VarsToSave = {'MassSt': MassSt, 'MassNSD': MassNSD, 'MassS': MassS, 'Asy': Asy,
                  'Calc': Calc, 'MassD': MassD, 'Den': Den, 'CatClass': CatClass, 'Qual': Qual, 'Arch': Arch,
                  'Annotations': {'cx_Press': cx_Press, 'cx_Release': cx_Release,
                                  'cy_Press': cy_Press, 'cy_Release': cy_Release},
                  'widthCanvas': widthCanvas, 'heightCanvas': heightCanvas}
    fnamepickel = (fnames[casecounter+1][:-3]) + 'pickle'
    fnamepickel = dirName[0] + '\\' + fnamepickel
    with open(fnamepickel, 'wb') as f:
        pickle.dump(VarsToSave, f)
    var_TypeMassSt.set(False)
    var_TypeMassNSD.set(False)
    var_TypeMassS.set(False)
    var_TypeAsy.set(False)
    var_TypeCalc.set(False)
    var_TypeMassD.set(False)
    var_Den.set(False)
    var_Class.set(False)
    var_Qual.set(False)
    var_TypeArch.set(False)

    canvas.delete('rect')
    orig_color = claButton.cget("background")
    broButton.configure(background=orig_color)
    cx_Press = 0
    cx_Release = 0
    cy_Press = 0
    cy_Release = 0
    i = 0

def unbindANDsave_coordinate():
    global cx_Press, cy_Press
    global cx_Release, cy_Release
    global broButton
    canvas.unbind("<ButtonRelease-1>")
    canvas.unbind("<ButtonPress-1>")
    broButton.configure(bg="green")

def unbindANDDelete_coordinate():
    global cx_Press, cy_Press
    global cx_Release, cy_Release
    global broButton
    canvas.unbind("<ButtonRelease-1>")
    canvas.unbind("<ButtonPress-1>")
    answer = messagebox.askyesno("Question", "Do you like to delete all annotations?")
    orig_color = claButton.cget("background")
    broButton.configure(background=orig_color)
    if (answer):
        cx_Press = 0
        cx_Release = 0
        cy_Press = 0
        cy_Release = 0
        canvas.delete('rect')

def printcoords_Press(event):
    global cx_Press, cy_Press
    global i
    cx, cy = event2canvas(event, canvas)
    cx_Press = np.append(cx_Press, cx)
    cy_Press = np.append(cy_Press, cy)

def printcoords_Release(event):
        global cx_Release, cy_Release
        global cx_Press, cy_Press
        global i
        cx, cy = event2canvas(event, canvas)
        cx_Release = np.append(cx_Release, cx)
        cy_Release = np.append(cy_Release, cy)
        #print("(%d, %d) / (%d, %d)" % (cx, cy, cx_Release[i + 1], cy_Release[i + 1]))
        canvas.create_rectangle(cx_Press[i+1], cy_Press[i+1], cx_Release[i+1], cy_Release[i+1],
                                outline="#f50", tag='rect')
        i = i+1

def save_coordinate():
    global cx_Press, cy_Press
    global cx_Release, cy_Release
    global i
    i = 0
    cx_Press = 0
    cx_Release = 0
    cy_Press = 0
    cy_Release = 0
    canvas.bind("<ButtonPress-1>",printcoords_Press)
    canvas.bind("<ButtonRelease-1>", printcoords_Release)

def OnDouble(event):
    global casecounter
    global canvas
    global img
    global cx_Press, cy_Press
    global cx_Release, cy_Release
    widget = event.widget
    selection = widget.curselection()
    value = widget.get(selection[0])
    MassSt = var_TypeMassSt.get()
    MassNSD = var_TypeMassNSD.get()
    MassS = var_TypeMassS.get()
    Asy = var_TypeAsy.get()
    Calc = var_TypeCalc.get()
    MassD = var_TypeMassD.get()
    Den = var_Den.get()
    CatClass = var_Class.get()
    Qual = var_Qual.get()
    Arch = var_TypeArch.get()
    VarsToSave = {'MassSt': MassSt, 'MassNSD': MassNSD, 'MassS': MassS, 'Asy': Asy,
                  'Calc': Calc, 'MassD': MassD, 'Den': Den, 'CatClass': CatClass, 'Qual': Qual, 'Arch': Arch,
                  'Annotations': {'cx_Press': cx_Press, 'cx_Release': cx_Release,
                                  'cy_Press': cy_Press, 'cy_Release': cy_Release},
                  'widthCanvas': widthCanvas, 'heightCanvas': heightCanvas}
    fnamepickel = (fnames[casecounter][:-3]) + 'pickle'
    fnamepickel = dirName[0] + '\\' + fnamepickel
    with open(fnamepickel, 'wb') as f:
        pickle.dump(VarsToSave, f)
    casecounter = selection[0]
    if (casecounter <= (len(fnames) - 1)):
        File = os.path.join(folder, fnames[casecounter])
        im = Image.open(File)
        im2 = im.resize((widthCanvas, heightCanvas), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(im2)
        canvas.itemconfigure(canvas.ImageHandel, image=img)
    var_TypeMassSt.set(False)
    var_TypeMassNSD.set(False)
    var_TypeMassS.set(False)
    var_TypeAsy.set(False)
    var_TypeCalc.set(False)
    var_TypeMassD.set(False)
    var_Den.set(False)
    var_Class.set(False)
    var_Qual.set(False)
    var_TypeArch.set(False)
    canvas.delete('rect')
    orig_color = claButton.cget("background")
    broButton.configure(background=orig_color)
    cx_Press = 0
    cx_Release = 0
    cy_Press = 0
    cy_Release = 0
    var_TypeMassSt.set(False)
    var_TypeMassNSD.set(False)
    var_TypeMassS.set(False)
    var_TypeAsy.set(False)
    var_TypeCalc.set(False)
    var_TypeMassD.set(False)
    var_Den.set(False)
    var_Class.set(False)
    var_Qual.set(False)
    var_TypeArch.set(False)
    canvas.delete('rect')
    orig_color = claButton.cget("background")
    broButton.configure(background=orig_color)
    cx_Press = 0
    cx_Release = 0
    cy_Press = 0
    cy_Release = 0
    i = 0

helv36= font.Font(family='Helvetica', size=12)
helv46= font.Font(family='Helvetica', size=13, weight='bold')

nextButton = Button(main, text='Next', height=1, width=10,command=Next_Image,font=helv36)
nextButton.grid(row=48, column=0, sticky="W", padx=20)
nextButton.configure(bg="pale green")
x0 = nextButton.winfo_y()
#print(x0)
preButton = Button(main, text='Previous', height=1, width=10, command=Previous_Image,font=helv36)
preButton.grid(row=50, column=0, sticky="W", padx=20)
preButton.configure(bg="tomato")
L0 = Label(main, text=" ", justify='center',font=helv46)
L0.grid(row=56, column=10, sticky="NW")
canvas.config(scrollregion=canvas.bbox(ALL))
claButton = Button(main, text='Annotate', height=1, width=10, command=save_coordinate,font=helv36)
claButton.grid(row=48, column=10, sticky="NSEW")
L000 = Label(main, text=" ", justify='center',font=helv46)
L000.grid(row=49, column=10, sticky="NSEW")
broButton = Button(main, text='Done', height=1, width=10, command=unbindANDsave_coordinate,font=helv36)
broButton.grid(row=50, column=10, sticky="NSEW")
L0000 = Label(main, text=" ", justify='center',font=helv46)
L0000.grid(row=51, column=10, sticky="NW")
L05 = Label(main, text=" ", justify='center',font=helv46)
L05.grid(row=47, column=10, sticky="NW")
delButton = Button(main, text='Delete', height=1, width=5, command=unbindANDDelete_coordinate,font=helv36)
delButton.grid(row=52, column=10, sticky="NSEW")
var_Den = IntVar()
Ltemp = Label(main, text="  ", justify='center',font=helv46)
Ltemp.grid(row=49, column=11, sticky="NSEW")
L1 = Label(main, text="Density", justify='center',font=helv46)
L1.grid(row=48, column=12, sticky="NW")
RDen1 = Radiobutton(main, text="A", variable=var_Den, value=1,font=helv36)
RDen1.grid(row=49, column=12, sticky="NSEW",columnspan=1,rowspan=1)
RDen2 = Radiobutton(main, text="B", variable=var_Den, value=2,font=helv36)
RDen2.grid(row=50, column=12, sticky="NSEW",columnspan=1,rowspan=1)
RDen3 = Radiobutton(main, text="C", variable=var_Den, value=3,font=helv36)
RDen3.grid(row=51, column=12, sticky="NSEW",columnspan=1,rowspan=1)
RDen3 = Radiobutton(main, text="D", variable=var_Den, value=4,font=helv36)
RDen3.grid(row=52, column=12, sticky="NSEW",columnspan=1,rowspan=1)
Ltemp2 = Label(main, text="  ", justify='center',font=helv46)
Ltemp2.grid(row=49, column=13, sticky="NSEW")
L2 = Label(main, text="Image Quality", justify='center',font=helv46)
L2.grid(row=48, column=14, sticky="NW")
var_Qual = IntVar()
RQ1 = Radiobutton(main, text="Pass", variable=var_Qual, value=1,font=helv36)
RQ1.grid(row=49, column=14, sticky="W")
RQ2 = Radiobutton(main, text="Poor Positioning", variable=var_Qual, value=2,font=helv36)
RQ2.grid(row=50, column=14, sticky="W")
RQ3 = Radiobutton(main, text="Outdated Technology", variable=var_Qual, value=3,font=helv36)
RQ3.grid(row=51, column=14, sticky="W")
Ltemp3 = Label(main, text="  ", justify='center',font=helv46)
Ltemp3.grid(row=49, column=15, sticky="NSEW")
L3 = Label(main, text="Case Category", justify='center',font=helv46)
L3.grid(row=48, column=16, sticky="NW")
var_Class = IntVar()
R1 = Radiobutton(main, text="Actionable Sign", variable=var_Class, value=1,font=helv36)
R1.grid(row=49, column=16, sticky="W",columnspan=1,rowspan=1)
R2 = Radiobutton(main, text="Non-actionable Sign", variable=var_Class, value=2,font=helv36)
R2.grid(row=50, column=16, sticky="W",columnspan=1,rowspan=1)
R3 = Radiobutton(main, text="Without Visible Sign", variable=var_Class, value=3,font=helv36)
R3.grid(row=51, column=16, sticky="W",columnspan=1,rowspan=1)
Ltemp4 = Label(main, text="  ", justify='center',font=helv46)
Ltemp4.grid(row=49, column=17, sticky="NSEW")
L4 = Label(main, text="Type", justify='center', font=helv46)
L4.grid(row=48, column=18, sticky="E")
var_TypeMassD = IntVar()
RType1 = Checkbutton(main, text="Discrete Mass", variable=var_TypeMassD,font=helv36)
RType1.grid(row=49, column=18, sticky="W")
var_TypeCalc = IntVar()
RType1 = Checkbutton(main, text="Calcifications", variable=var_TypeCalc,font=helv36)
RType1.grid(row=50, column=18, sticky="W")
var_TypeArch = IntVar()
RType2 = Checkbutton(main, text="Architectural distortion", variable=var_TypeArch,font=helv36)
RType2.grid(row=51, column=18, sticky="W")
var_TypeAsy = IntVar()
RType3 = Checkbutton(main, text="Asymmetry", variable=var_TypeAsy,font=helv36)
RType3.grid(row=52, column=18, sticky="W")
var_TypeMassS = IntVar()
RType5 = Checkbutton(main, text="Spiculated Mass", variable=var_TypeMassS,font=helv36)
RType5.grid(row=49, column=19, sticky="W")
var_TypeMassNSD = IntVar()
RType6 = Checkbutton(main, text="NSD", variable=var_TypeMassNSD,font=helv36)
RType6.grid(row=50, column=19, sticky="W")
var_TypeMassSt = IntVar()
RType7 = Checkbutton(main, text="Stellate", variable=var_TypeMassSt,font=helv36)
RType7.grid(row=51, column=19, sticky="W")
TPathRep = Text(main, height=10, width=40)
TPathRep.grid(row=48, column=48, sticky="NW",columnspan=35,rowspan=10)
fnametxt=(fnames[casecounter][:-3])+'txt'
dirNamePathReport = [folder + '\\' +'PathReport']
fnametxt=dirNamePathReport[0]+'\\'+fnametxt
PathReportInfo = open(fnametxt, "r")
TPathRep.insert(END,PathReportInfo.readlines())
listbox = Listbox(main, selectmode=SINGLE, height=45, width=27)
helv26= font.Font(family='Helvetica', size=12)
L5 = Label(main, text="All cases in this batch", justify='center', font=helv26)
L5.grid(row=0, column=0, sticky="E")
listbox.grid(column=0, row=1, columnspan=3, rowspan=20, sticky="W")
L6 = Label(main, text=" ", justify='center', font=helv26)
L6.grid(row=0, column=2, sticky="E")
'''xx0, yy0, xx1, yy1 = canvas.ImageHandel.coord()
print(xx0, yy0, xx1, yy1)'''
for x in range(len(fnames)):
    listbox.insert(END, fnames[x])
listbox.bind('<Double-Button>', OnDouble)
main.mainloop()
