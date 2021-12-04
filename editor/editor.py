from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import tempfile
import os

ws = Tk()
ws.title('Code Editor')

Cpath = ''

def Runthiscode():
    global Cpath
    # if Cpath == '':
    #     SaveMessage = Toplevel()
    #     message = Label(SaveMessage, text="Save this File")
    #     message.pack()
    #     return
    fd, path = tempfile.mkstemp()
    try:
        with os.fdopen(fd, 'w') as tmp:
            # do stuff with temp file
            tmp.write(retrieve_input())
    finally:
        pass
    
    Command = f'python ./interpreter/interpreter.py --file {path}'
    process = subprocess.Popen(Command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    result, Error = process.communicate()
    
    # Clear and display new output
    Result.configure(state='normal')
    Result.delete('1.0', END)
    Result.insert(END,result)
    
    # setting color to everythin after result (error msgs) to red
    numLines = float(Result.index(END))-1.1
    if str(result) == "b''":
        Result.configure(foreground='red')
    else:
        Result.tag_add('errorText', str(numLines), END)
        Result.tag_config('errorText', foreground='red')
    
    Result.insert(END,Error)
    Result.configure(state='disabled')
    

def Openthisfile():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        global Cpath
        Cpath = path

def SavethisfileAs():
    global gpath
    if Cpath =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = Cpath    
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)

editor = Text()
editor.config(bg='white', fg='blue', insertbackground='black',undo=True,state=NORMAL)
editor.pack()

Font_tuple = ("Courier New", 11, "bold")

Result = Text(height=7)
Result.config(bg='black', fg='light green',font=Font_tuple,state=NORMAL)
Result.pack()

def help_appear():
    global help
    help = Toplevel(ws)
    help.title("Help")
    help.geometry("500x500")
    help.config(bg="white")

    # scrollbar = Scrollbar(help)
    # scrollbar.pack( side = RIGHT, fill = Y )

    # help text
    helpTxt = "This application aims at teaching children to program a simple math algorithm by " \
    "indroducing to the logic used in programming. There are multiple built-in keywords that need to be used with " \
        "accordance to this application's synthax, just as in actual code editors. \n\n\nHere are examples of all the "\
            "keywords (with placeholder numbers): \n\nadd 2 to 3 (output: 5)\n\nremove 2 from 3 (output: 1)\n\nmultiply 5 by 5 "\
                "(output: 25)\n\ndivide 10 by 2 (output: 5)\n\nmodulo 10 by 3 (output: 1, gives remainder of 10/3 division)\n\n"\
                    "set X to 3 (output: makes user-made variable X equal to 3)\n\nget X (outputs the value of X to the console)\n\n"\
                        "if X is less than 10 add 2 to 3 (adds 2 to 3 if variable X is less than 10, and if X is more than 10, it "\
                            "skips the addition)\n\nKeywords if, true, false, to, from & by are used in between the above keywords\n"
    help_label = Label(help, text=helpTxt,bg="white", wraplength=450, font=("Verdana", 10), anchor=NE, justify='left', pady=10)

    help_label.pack()

help_btn = Button(ws, text='Help', command=help_appear)
help_btn.pack(side='left',padx=12,pady=12)
run_btn = Button(text='Run', command=Runthiscode)
run_btn.pack(side='left',padx=12,pady=12)
exit_btn = Button(text='Exit', command=exit)
exit_btn.pack(side='left',padx=12,pady=12)
undo_btn = Button(text='Undo', command=editor.edit_undo)
undo_btn.pack(side='left',padx=12,pady=12)
redo_btn = Button(text='Redo', command=editor.edit_redo)
redo_btn.pack(side='left',padx=12,pady=12)

Menu_option = Menu(ws)

File_option = Menu(Menu_option, tearoff=0)
File_option.add_command(label='Open', command = Openthisfile)
File_option.add_command(label='Save', command = SavethisfileAs)
File_option.add_command(label='Save As', command = SavethisfileAs)
Menu_option.add_cascade(label='File', menu = File_option)

Compile_option = Menu(Menu_option, tearoff=0)
Compile_option.add_command(label='compile', command = Runthiscode)
Menu_option.add_cascade(label='compile', menu = Compile_option)




def retrieve_input():
    return editor.get("1.0",'end-1c')

ws.config(menu=Menu_option)
ws.mainloop()