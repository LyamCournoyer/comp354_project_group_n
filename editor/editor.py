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
    
    # TODO: Change color for errors
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

    ## placeholder for help text
    help_label = Label(help, text="hello here is help",bg="white")
    ## TODO: Add more info for the help screen, including usage examples
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