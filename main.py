from tkinter import *
from tkinter import messagebox, colorchooser, font, filedialog
import os
import webbrowser
import get_feedback as gfb
import get_report as grt
import clock
import calculator


# global variables for changing the text area's font, size etc.
name = 'Arial'
size = 12
file = None
font_list = [name, size]


# Initial widgets
root = Tk()
root.title("* Untitled  -  Notepad")
root.minsize(422, 233)
root.geometry("888x555")


# Define the text area
text_area = Text(root, font=font_list, undo=True)
text_area.pack(expand=True, fill='both')

# Make Scrollbar
scroll = Scrollbar(text_area)
scroll.pack(side='right', fill='y')
scroll.config(command=text_area.yview)
text_area.config(yscrollcommand=scroll.set)


# Logic's or functions for command

def new_file(*args):
    '''this function just erase all text from text_area'''
    global text_area
    content = text_area.get(1.0, END)
    if content != '\n':
        save_change = messagebox.askquestion(
            'Save Change', 'Do you want to save change?')

        if save_change == 'yes':
            save()
        text_area.delete(1.0, END)

    root.title('* Untitled  -  Notepad')


def open_file(*args):
    '''for open a file'''
    global file

    file = filedialog.askopenfilename(
        defaultextension='.txt',
        filetypes=[
            ('All Files', '*.*'), ('Text Documents',
                                   '*.txt'), ('Python File', '*.py')
        ])

    if file == '':
        file = None
    else:
        root.title(os.path.basename(file) + '  -  Notepad')
        text_area.delete(1.0, END)

        f = open(file, 'r')
        text_area.insert(1.0, f.read())

        f.close()


def save(*args):
    '''if file exist, this function simply save the changes. else this function ask for saving.'''
    global file

    if file == None:
        file = filedialog.asksaveasfilename(
            initialfile='Untitled.txt',
            defaultextension='.txt',
            filetypes=[
                ('All Files', '*.*'), ('Text Document',
                                       '*.txt'), ('Python File', '*.py')
            ]
        )

        if file == '':
            file = None
        else:
            f = open(file, 'w')
            f.write(text_area.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + '  -  Notepad')

    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()


def save_as(*args):
    '''every time ask for saving to a new file.'''
    global file

    file = filedialog.asksaveasfilename(
        initialfile='Untitled.txt',
        defaultextension='.txt',
        filetypes=[
            ('All Files', '*.*'), ('Text Document',
                                   '*.txt'), ('Python File', '*.py')
        ]
    )

    if file == '':
        file = None
    else:
        f = open(file, 'w')
        f.write(text_area.get(1.0, END))
        f.close()

        root.title(os.path.basename(file) + '  -  Notepad')


def save_all():
    messagebox.showerror('Error', 'No such file or directory!')


def share(*args):
    ans = messagebox.askquestion('Share', 'Share on facebook?')

    if ans == 'yes':
        webbrowser.open('facebook.com')


def exit_editor(*args):
    ans = messagebox.askquestion('Exit', 'Are you sure to Exit?')

    if ans == 'yes':
        root.destroy()


def undo(*args):
    try:
        text_area.edit_undo()  # just i defined undo=True in text_area
    except:  # this undo and redo method show error when nothing to undo and redo.
        messagebox.showerror('Error', 'Nothing to Undo!')


def redo(*args):
    try:
        text_area.edit_redo()
    except:
        messagebox.showerror('Error', 'Nothinh to Redo!')



def cut(*args):
    text_area.event_generate("<<Cut>>")


def copy(*args):
    text_area.event_generate("<<Copy>>")


def paste(*args):
    text_area.event_generate("<<Paste>>")


def expand_editor():
    root.geometry('1400x700')


def resize_editor():
    root.geometry('888x555')


def change_bg():
    '''this function ask for changing color, and change'''
    color = colorchooser.askcolor()
    text_area.config(bg=color[1])


def font_color():
    '''ask for change color of font'''
    color = colorchooser.askcolor()
    text_area.config(fg=color[1])


def select_font(font_name):
    '''this function simply change the font name, the others are not change'''
    global text_area, font_list
    font_list[0] = font_name

    text_area.config(font=font_list)


def f_size(size):
    '''change only the size from font_list.'''
    global text_area, font_list
    font_list[1] = size

    text_area.config(font=font_list)


def bold_text(*args):
    '''get bold text without changing other'''
    global font_list

    if len(font_list) == 3:
        font_list.pop()

    font_list.append('bold')
    text_area.config(font=font_list)


def italic_text(*args):
    '''get italic text without change others'''
    global font_list

    if len(font_list) == 3:
        font_list.pop()

    font_list.append('italic')
    text_area.config(font=font_list)


def underline_text():
    '''for underline'''
    global font_list

    if len(font_list) == 3:
        font_list.pop()

    font_list.append('underline')
    text_area.config(font=font_list)


def qv_clock(*args):
    '''this is imported class, this function open a window to show time'''
    clock.main()


def qv_calculator(*args):
    '''imported function, this will called a simple GUI canculator for simple calculations'''
    calculator.main()


def welcome(*args):
    messagebox.showinfo(
        'Welcome message', 'Welcome to simple notepad, this is a simple notepad made with Python(Tkinter).')


def documentation():
    messagebox.askokcancel('Unavailable', 'Sorry, documentation not ready.')


def website():
    ans = messagebox.askokcancel('Website', "Open developer's website?")
    if ans == True:
        webbrowser.open('https://mdshakib007.github.io/')


def tutorial():
    messagebox.showwarning(
        'Unavailable', 'Sorry, there is no tutorial at this moment!')


def source_code(*args):
    webbrowser.open('https://github.com/mdshakib007/Tkinter-Projects')


def github():
    webbrowser.open('https://github.com/mdshakib007')


def report(*args):
    '''this is also imported. this is just call a window so that user can report an issue and automatically stored in a database(mysql)'''
    grt.main()


def feedback(*args):
    '''same like report.'''
    gfb.main()


def update():
    messagebox.showwarning(
        'Update', 'You are using the letest version of Text Editor.')


def about(*args):
    messagebox.showinfo(
        'Info', 'This is a simple & opensource text editor. If any issue, please report.')


# Bind keyboard shortcuts to menu items
root.bind("<Control-n>", new_file)   # Ctrl + N for new file
root.bind("<Control-o>", open_file)  # Ctrl + O for open file
root.bind("<Control-s>", save)       # Ctrl + S for save
root.bind("<Alt-s>", share)          # Alt + S for share
root.bind("<Control-q>", exit_editor)# Ctrl + Q for exit editor
root.bind("<Control-z>", undo)       # Ctrl + Z for undo
root.bind("<Control-y>", redo)       # Ctrl + Y for redo
root.bind("<Control-x>", cut)        # Ctrl + X for cut
root.bind("<Control-c>", copy)       # Ctrl + C for copy
root.bind("<Control-v>", paste)      # Ctrl + V for paste
root.bind("<Escape>", exit_editor)   # Escape key for exit editor
root.bind("<Control-b>", bold_text)  # get bolded text
root.bind("<Control-i>", italic_text)# italic text 
root.bind("<Alt-c>", qv_clock)       # and so on.....
root.bind("<Alt-a>", qv_calculator) 
root.bind("<Control-w>", welcome)
root.bind("<Control-F2>", source_code)
root.bind("<Control-r>", report)
root.bind("<Control-f>", feedback)
root.bind("<Control-a>", about)


main_menu = Menu(root)  # this is main menu
# This is 'File' menu
file_menu = Menu(main_menu, tearoff=0)
file_menu.add_command(label='New Text File',
                      accelerator='Ctrl+N', command=new_file)
file_menu.add_command(label='New file', accelerator='Ctrl+N', command=new_file)
file_menu.add_command(label='Open file...',
                      accelerator='Ctrl+O', command=open_file)
file_menu.add_command(label='Open Recent',
                      accelerator='Ctrl+O', command=open_file)
file_menu.add_separator()
file_menu.add_command(label='Save', accelerator='Ctrl+S', command=save)
file_menu.add_command(label='Save As...',
                      accelerator='Ctrl+S', command=save_as)
file_menu.add_command(label='Save All', command=save_all)
file_menu.add_separator()
file_menu.add_command(label='Share', accelerator='Alt+S', command=share)
file_menu.add_separator()
# this is built in command.
file_menu.add_command(label='Exit', accelerator='Ctrl+Q', command=exit_editor)
# configuring the 'File' menu
main_menu.add_cascade(label='File', menu=file_menu, font='Arial 13')

# 'Edit' menu
edit_menu = Menu(main_menu, tearoff=0)
edit_menu.add_command(label='Undo', command=undo, accelerator='Ctrl+Z')
edit_menu.add_command(label='Redo', command=redo, accelerator='Ctrl+Y')
edit_menu.add_separator()
edit_menu.add_command(label='Cut', command=cut, accelerator='Ctrl+X')
edit_menu.add_command(label='Copy', command=copy, accelerator='Ctrl+C')
edit_menu.add_command(label='Paste', command=paste, accelerator='Ctrl+V')
edit_menu.add_separator()
edit_menu.add_command(label='Expand', command=expand_editor)
edit_menu.add_command(label='Resize', command=resize_editor)
edit_menu.add_separator()
edit_menu.add_command(label='Exit Editor',
                      command=exit_editor, accelerator='Ctrl+Q')

# configuring 'Edit' menu
main_menu.add_cascade(label='Edit', menu=edit_menu, font='Arial 13')

# 'Selection' menu
selection_menu = Menu(main_menu, tearoff=0)
selection_menu.add_command(label='Change Background', command=change_bg)
selection_menu.add_command(label='Font Color', command=font_color)
selection_menu.add_separator()
# sub menu(for font)
font_menu = Menu(selection_menu, tearoff=0)

font_menu.add_command(label='Arial', accelerator='Default',
                      command=lambda: select_font('Arial'))
font_menu.add_command(label='Calibri',
                      command=lambda: select_font('Calibri'))
font_menu.add_command(label='Courier New', accelerator='New',
                      command=lambda: select_font('Courier'))
font_menu.add_command(label='Garamond',
                      command=lambda: select_font('Garamond'))
font_menu.add_command(label='Georgia',
                      command=lambda: select_font('Georgia'))
font_menu.add_command(label='Helvetica',
                      command=lambda: select_font('Helvetica'))
font_menu.add_command(label='monospace', accelerator='Pro',
                      command=lambda: select_font('monospace'))
font_menu.add_command(label='Serif',
                      command=lambda: select_font('Serif'))
font_menu.add_command(label='Verdana',
                      command=lambda: select_font('Verdana'))
font_menu.add_command(label='Tahoma', command=lambda: select_font(
    'Tahoma'))  # english submenu ends
font_menu.add_separator()
font_menu.add_command(label='SolaimanLipi', accelerator='বাংলা')
font_menu.add_command(label='Nikosh', accelerator='বাংলা',)
font_menu.add_command(label='Siyamrupali', accelerator='বাংলা')
font_menu.add_command(label='Vrinda Lohit Bengali', accelerator='বাংলা')
font_menu.add_command(label='Mukti Narrow', accelerator='বাংলা')
font_menu.add_command(label='Kalpurush', accelerator='বাংলা')  # submenu ends
selection_menu.add_cascade(label='Font', menu=font_menu)

# Font Size
font_size = Menu(selection_menu, tearoff=0)

font_size.add_command(label='8', command=lambda: f_size(8))
font_size.add_command(label='9', command=lambda: f_size(9))
font_size.add_command(label='10', command=lambda: f_size(10))
font_size.add_command(label='11', command=lambda: f_size(11))
font_size.add_command(label='12', command=lambda: f_size(12))
font_size.add_command(label='14', command=lambda: f_size(14))
font_size.add_command(label='15', command=lambda: f_size(15))
font_size.add_command(label='16', command=lambda: f_size(16))
font_size.add_command(label='18', command=lambda: f_size(18))
font_size.add_command(label='20', command=lambda: f_size(20))
font_size.add_command(label='22', command=lambda: f_size(22))
font_size.add_command(label='25', command=lambda: f_size(25))
font_size.add_command(label='27', command=lambda: f_size(27))
font_size.add_command(label='30', command=lambda: f_size(30))
font_size.add_command(label='35', command=lambda: f_size(35))
font_size.add_command(label='40', command=lambda: f_size(40))
font_size.add_command(label='46', command=lambda: f_size(46))
font_size.add_command(label='50', command=lambda: f_size(50))
font_size.add_command(label='60', command=lambda: f_size(60))  # size

selection_menu.add_cascade(label='Size', menu=font_size)

selection_menu.add_separator()
selection_menu.add_command(
    label='Bold', command=bold_text, accelerator='Ctrl+B')
selection_menu.add_command(
    label='Italic', command=italic_text, accelerator='Ctrl+I')
selection_menu.add_command(label='Underline', command=underline_text)
selection_menu.add_separator()
selection_menu.add_command(
    label='Close', command=exit_editor, accelerator='Ctrl+Q')

main_menu.add_cascade(label='Selection', menu=selection_menu, font='Arial 13')


# 'Tools' menu
tools_menu = Menu(main_menu, tearoff=0)

tools_menu.add_command(label='Clock', command=qv_clock, accelerator='Alt+C')
tools_menu.add_command(label='Quick Calculation', command=qv_calculator, accelerator='Alt+A')
tools_menu.add_separator()
tools_menu.add_command(label='Quick Exit', command=exit, accelerator='Ctrl+Q')

main_menu.add_cascade(menu=tools_menu, label='Tools', font='Arial 13')

# 'Help' menu
help_menu = Menu(main_menu, tearoff=0)

help_menu.add_command(label='Welcome', command=welcome, accelerator='Ctrl+W')
help_menu.add_command(label='Documentation', command=documentation)
help_menu.add_separator()
help_menu.add_command(label='Website', command=website)
help_menu.add_command(label='Tutorial', command=tutorial)
help_menu.add_command(label='Source Code', command=source_code, accelerator='Ctrl+F2')
help_menu.add_command(label='GitHub', command=github)
help_menu.add_separator()
help_menu.add_command(label='Report An Issue', command=report, accelerator='Ctrl+R')
help_menu.add_command(label='Give Feedback', command=feedback, accelerator='Ctrl+F')
help_menu.add_separator()
help_menu.add_command(label='Check For Updates', command=update)
help_menu.add_separator()
help_menu.add_command(label='About', command=about, accelerator='Ctrl+A')

main_menu.add_cascade(label='Help', menu=help_menu, font='Arial 13')
root.config(menu=main_menu)


root.mainloop()
