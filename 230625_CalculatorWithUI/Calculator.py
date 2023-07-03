from tkinter import ttk
import tkinter as tk

def operations():
    selected = selectedOption.get()
    a = int(input1.get())
    b = int(input2.get())
    out = 0.0

    if (selected == "Addition"):
        out = a + b
    elif (selected == "Substraction"):
        out = a - b
    elif (selected == "Multiplication"):
        out = a * b
    elif (selected == "Division"):
        out = a / b
    else:
        out = -1

    output.set(str(out))
    outputLabel.config(text="Result = %s" % output.get())
    outputLabel.pack(side="left")


def optionSelected(value):
    # print("Selected option:", value)
    selectedOption.set(value)
    print (selectedOption.get())


# Create the main window or root
root = tk.Tk()
# Top text
header = tk.Label(root, text="Calculator", font=("arial", 21, "bold"), padx=20, pady=20)
header.pack()
subHeader = tk.Label(root, text="Made by Edgrant", font=("arial", 7, "bold"), padx=10, pady=10)
subHeader.pack()

# Variable declarations
input1 = tk.StringVar(value="0")
input2 = tk.StringVar(value="0")
output = tk.StringVar(value="0")
selectedOption = tk.StringVar(value="Addition")

# Selection frame
selectionFrame = tk.Frame(root)
selectionFrame.pack()
# Option menu
optionMenu = ttk.OptionMenu(selectionFrame, selectedOption, "Addition", "Addition", "Substraction", "Multiplication", "Division")
optionMenu.pack()
# # retrieve option menu button
# button = ttk.Button(selectionFrame, text="Get Selected Option", command=lambda: optionSelected(selectedOption.get()))
# button.pack()

# number inputs
inputFrame = tk.Frame(root)
inputFrame.pack()
inputFrameLeft = tk.Frame(inputFrame)
inputFrameLeft.pack(side="left")
inputFrameRight = tk.Frame(inputFrame)
inputFrameRight.pack(side="right")
# label 1
numberInput = tk.Label(inputFrameLeft, text="A: ")
numberInput.pack(side="left")
#num 1
entry = ttk.Entry(inputFrameLeft, textvariable=input1)
entry.pack(side="left")

# label 2
numberInput = tk.Label(inputFrameRight, text="B: ")
numberInput.pack(side="left")
#num 2
entry = ttk.Entry(inputFrameRight, textvariable=input2)
entry.pack(side="left")


#output
outputHeader = tk.Label(root, text="\n\nOutput!", font=("arial", 7, "bold"), pady=10)
outputHeader.pack()
# output frame
outputFrame = tk.Frame(root)
outputFrame.pack()
# Create the ttk button
button = ttk.Button(outputFrame, text="Calculate", command=operations)
button.pack()
outputLabel = tk.Label(outputFrame, text="Result = %s" % output.get(), font=("arial", 15, "bold"), pady=10)
outputLabel.pack()


root.mainloop()
