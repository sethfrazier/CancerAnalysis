import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

#Creating the GUI window
root = Tk()
root.title("Relationship between Cancer and Nitrate Levels")
root.geometry("1050x800")
root.configure(background="papaya whip")

# #Section for the map display
imagePath = ImageTk.PhotoImage(Image.open(r"C:\Users\sfrazier\Desktop\Geog777\cancerAnalysis-master\cancerAnalysis-master\olsResults.png")) 
#imagePath = imagePath.resize((250,250), image.ANTIALIAS)
mapDisplay = Label(root,image = imagePath, bg="black")
mapDisplay.grid(columnspan=4,padx=50)
#Image.ANTIALIAS

# #Create a new frame
execute = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, bg="gray72")
execute.grid(row=5, column=0, sticky=W, padx=50, pady=20)


# #Title for the execution frame
executeTitle = Text(execute, width=20, height=1, wrap=WORD)
executeTitle.insert(INSERT, "Execute Analysis")
executeTitle.config(state=DISABLED)
executeTitle.configure(font=("Baskerville Old Face", "13"))
executeTitle.grid(row=6, column=0, sticky=W)

# #Instructions for the user
executeLabel = Label(execute, text="Enter a Power Value:", font=("Baskerville Old Face", "10"))
executeLabel.grid(row=7, column=0)

# #Create the power entry box
powerEntry = Entry(execute, bg="white")
powerEntry.grid(row=8, columnspan=2)

# #Create the buttons to either run the analysis or get help about the analysis
executeHelp = Button(execute, text="Help") #command=idwHelp)
executeHelp.grid(row=9)

# #Create a new frame for the spatial unit
units = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, bg="gray72")
units.grid(row=5, column=1, sticky=W, padx=50, pady=20)

# #Title for the spatial units frame
unitsTitle = Text(units, width=25, height=1, wrap=WORD)
unitsTitle.insert(INSERT, "Choose a Spatial Unit:")
unitsTitle.config(state=DISABLED)
unitsTitle.configure(font=("Gill Sans", "11"))
unitsTitle.grid(row=6, column=1)

# #Create the radiobuttons
unitVar = IntVar()
unitVar.set(1)
tracts = Radiobutton(units, text="Census Tracts", font=("Baskerville Old Face", "10"), variable=unitVar, value=1)
blocks = Radiobutton(units, text="Counties", font=("Baskerville Old Face", "11"), variable=unitVar, value=2, width=10)
unitsHelp = Button(units, text="Help")#, command=censusHelp)
tracts.grid(row=7, column=1)
blocks.grid(row=8, column=1)
unitsHelp.grid(row=9, columnspan=3)


# #Create a new frame for the different map displays
displays = Frame(root, highlightbackground="black", highlightcolor="black", highlightthickness=1, bg="gray72")
displays.grid(row=5, column=2, padx=50, pady=20)

# #Title for the map displays
displaysTitle = Text(displays, width=25, height=1, wrap=WORD)
displaysTitle.insert(INSERT, "Choose a map display:")
displaysTitle.config(state=DISABLED)
displaysTitle.configure(font=("Baskerville Old Face", "13"))
displaysTitle.grid(row=6, column=2)

# #Create the buttons to determine the map display
idwDisplay = Button(displays, text="IDW")#, command=displayIDW)
olsDisplay = Button(displays, text="Regression")#, command=displayOLS)
idwDisplay.config(state=DISABLED)
olsDisplay.config(state=DISABLED)
idwDisplay.grid(row=7, columnspan=3)
olsDisplay.grid(row=8, columnspan=3)

# #Create the buttons to run the script and to download the map
run = Frame(root, highlightbackground="black", highlightcolor="black", bg="papaya whip")
run.grid(row=5, column=3)
runButton = Button(run, text="Run")#, command=idw)
runButton.grid(row=5)
downloadButton = Button(run, text="Download")#, command=downloadMaps)
downloadButton.config(state=DISABLED)
downloadButton.grid(row=6)


root.mainloop()

##def calculate(*args):
##    try:
##        value = float(feet.get())
##        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
##    except ValueError:
##        pass
###top = Tk()
####top.geometry("100x100")
####def hellowCallBack():
####    msg = messagebox.showinfo("hello Python", "Hello World")
####
####B= Button(top, text="Hello", command = hellowCallBack)
####B.place(x=50,y=50)
##
####L1 = Label(top, text = "User Name")
####L1.pack( side = LEFT)
####E = Entry(top, bd=5)
####E.pack(side = RIGHT)
##
##root = Tk()
##root.title("Feet to Meters")
####root.title("Relationship between Cancer and Nitrate Levels")
####root.geometry("1050x800")
####root.configure(background="papaya whip")
##
##
##frame = ttk.Frame(root, padding="3 3 12 12")
##frame.grid(column=0, row=0, sticky=(N, W, E, S))
###frame.pack()
##Button(root, text="hello World").grid()
##root.columnconfigure(0, weight=1)
##root.rowconfigure(0, weight=1)
##
##feet = StringVar()
##meters = StringVar()
##
##feet_entry = ttk.Entry(frame, width=7, textvariable=feet)
##feet_entry.grid(column=2, row=1, sticky=(W, E))
##ttk.Label(frame, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
##ttk.Button(frame, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)
##
##ttk.Label(frame, text="feet").grid(column=3, row=1, sticky=W)
##ttk.Label(frame, text="is equivalent to").grid(column=1, row=2, sticky=E)
##ttk.Label(frame, text="meters").grid(column=3, row=2, sticky=W)
##for child in frame.winfo_children(): child.grid_configure(padx=5, pady=5)
##feet_entry.focus()
##root.bind('<Return>', calculate)
###tkMessageBox.showinfo("Download Complete", "The map download has completed. Navigate to the selected folder to see the results.")
##
##
##root.mainloop()
