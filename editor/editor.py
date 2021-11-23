from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
import subprocess
import tempfile
import os

ws = Tk()
ws.title('Python Guides')

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
    Result.insert(END,result)
    Result.insert(END,Error)
     

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
editor.config(bg='white', fg='blue', insertbackground='black')
editor.pack()

Result = Text(height=7)
Result.config(bg='black', fg='green')
Result.pack()
 
Menu_option = Menu(ws)

File_option = Menu(Menu_option, tearoff=0)
File_option.add_command(label='Open', command = Openthisfile)
File_option.add_command(label='Save', command = SavethisfileAs)
File_option.add_command(label='SaveAs', command = SavethisfileAs)
File_option.add_command(label='Exit', command = exit)
Menu_option.add_cascade(label='File', menu = File_option)

Compile_option = Menu(Menu_option, tearoff=0)
Compile_option.add_command(label='compile', command = Runthiscode)
Menu_option.add_cascade(label='compile', menu = Compile_option)

def retrieve_input():
    return editor.get("1.0",'end-1c')

ws.config(menu=Menu_option)
ws.mainloop()