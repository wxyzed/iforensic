from tkinter import *
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import event_logger
import getpass
from datetime import datetime
#DEVELOPED BY Mark Arvin
root = Tk()
root.title("Evidence Management")
width = 700
height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="#6666ff")
#============================VARIABLES===================================
ITEM = StringVar()
DESCRIPTION = StringVar()
GENDER = StringVar()
QUANITITY = StringVar()
RELEASEDBY = StringVar()
RECEIVEDBY = StringVar()
#============================METHODS=====================================
def Database():
    conn = sqlite3.connect("pythontut.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER NOT NULL  PRIMARY KEY AUTOINCREMENT, item TEXT, description TEXT, gender TEXT, quanitity TEXT, releasedby TEXT, receivedby TEXT)")
    cursor.execute("SELECT * FROM `member` ORDER BY `item` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data))
    cursor.close()
    conn.close()
def SubmitData():
    if  ITEM.get() == "" or DESCRIPTION.get() == "" or GENDER.get() == "" or QUANITITY.get() == "" or RELEASEDBY.get() == "" or RECEIVEDBY.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `member` (item, description, gender, quanitity, releasedby, receivedby) VALUES(?, ?, ?, ?, ?, ?)", (str(ITEM.get()), str(DESCRIPTION.get()), str(GENDER.get()), int(QUANITITY.get()), str(RELEASEDBY.get()), str(RECEIVEDBY.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `item` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        ITEM.set("")
        DESCRIPTION.set("")
        GENDER.set("")
        QUANITITY.set("")
        RELEASEDBY.set("")
        RECEIVEDBY.set("")
        now = datetime.now()
        x = getpass.getuser()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        f = open("hash.txt", "a+")
        f.write("Evidence added By {} On {}\n".format(x, dt_string))
        print("Hash saved successfully, please check hash.txt file")
def UpdateData():
    if GENDER.get() == "":
       result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree.delete(*tree.get_children())
        conn = sqlite3.connect("pythontut.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `member` SET `item` = ?, `description` = ?, `gender` =?, `quanitity` = ?,  `releasedby` = ?, `receivedby` = ? WHERE `mem_id` = ?", (str(ITEM.get()), str(DESCRIPTION.get()), str(GENDER.get()), str(QUANITITY.get()), str(RELEASEDBY.get()), str(RECEIVEDBY.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `item` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        ITEM.set("")
        DESCRIPTION.set("")
        GENDER.set("")
        QUANITITY.set("")
        RELEASEDBY.set("")
        RECEIVEDBY.set("")
def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    ITEM.set("")
    DESCRIPTION.set("")
    GENDER.set("")
    QUANITITY.set("")
    RELEASEDBY.set("")
    RECEIVEDBY.set("")
    ITEM.set(selecteditem[1])
    DESCRIPTION.set(selecteditem[2])
    QUANITITY.set(selecteditem[4])
    RELEASEDBY.set(selecteditem[5])
    RECEIVEDBY.set(selecteditem[6])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()
    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Evidence", font=('arial', 16), bg="orange",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="Item", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="Description", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="Quanitity", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="Released By", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="Received By", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)
    #===================ENTRY===============================
    item = Entry(ContactForm, textvariable=ITEM, font=('arial', 14))
    item.grid(row=0, column=1)
    description = Entry(ContactForm, textvariable=DESCRIPTION, font=('arial', 14))
    description.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    quanitity = Entry(ContactForm, textvariable=QUANITITY,  font=('arial', 14))
    quanitity.grid(row=3, column=1)
    releasedby = Entry(ContactForm, textvariable=RELEASEDBY,  font=('arial', 14))
    releasedby.grid(row=4, column=1)
    receivedby = Entry(ContactForm, textvariable=RECEIVEDBY,  font=('arial', 14))
    receivedby.grid(row=5, column=1)
    #==================BUTTONS==============================
    btn_updatecon = Button(ContactForm, text="Update", width=50, command=UpdateData)
    btn_updatecon.grid(row=6, columnspan=2, pady=10)
#fn1353p
def DeleteData():
    if not tree.selection():
       result = tkMessageBox.showwarning('', 'Please Select Something First!', icon="warning")
    else:
        result = tkMessageBox.askquestion('', 'Are you sure you want to delete this record?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            conn = sqlite3.connect("pythontut.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
def AddNewWindow():
    global NewWindow
    ITEM.set("")
    DESCRIPTION.set("")
    GENDER.set("")
    QUANITITY.set("")
    RELEASEDBY.set("")
    RECEIVEDBY.set("")
    NewWindow = Toplevel()
    NewWindow.title("Contact List")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    RadioGroup = Frame(ContactForm)
    Male = Radiobutton(RadioGroup, text="Male", variable=GENDER, value="Male",  font=('arial', 14)).pack(side=LEFT)
    Female = Radiobutton(RadioGroup, text="Female", variable=GENDER, value="Female",  font=('arial', 14)).pack(side=LEFT)
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Adding New Evidence", font=('arial', 16), bg="#66ff66",  width = 300)
    lbl_title.pack(fill=X)
    lbl_firstname = Label(ContactForm, text="item", font=('arial', 14), bd=5)
    lbl_firstname.grid(row=0, sticky=W)
    lbl_lastname = Label(ContactForm, text="description", font=('arial', 14), bd=5)
    lbl_lastname.grid(row=1, sticky=W)
    lbl_gender = Label(ContactForm, text="Gender", font=('arial', 14), bd=5)
    lbl_gender.grid(row=2, sticky=W)
    lbl_age = Label(ContactForm, text="quanitity", font=('arial', 14), bd=5)
    lbl_age.grid(row=3, sticky=W)
    lbl_address = Label(ContactForm, text="releasedby", font=('arial', 14), bd=5)
    lbl_address.grid(row=4, sticky=W)
    lbl_contact = Label(ContactForm, text="receivedby", font=('arial', 14), bd=5)
    lbl_contact.grid(row=5, sticky=W)
    #===================ENTRY===============================
    firstname = Entry(ContactForm, textvariable=ITEM, font=('arial', 14))
    firstname.grid(row=0, column=1)
    lastname = Entry(ContactForm, textvariable=DESCRIPTION, font=('arial', 14))
    lastname.grid(row=1, column=1)
    RadioGroup.grid(row=2, column=1)
    age = Entry(ContactForm, textvariable=QUANITITY,  font=('arial', 14))
    age.grid(row=3, column=1)
    address = Entry(ContactForm, textvariable=RELEASEDBY,  font=('arial', 14))
    address.grid(row=4, column=1)
    contact = Entry(ContactForm, textvariable=RECEIVEDBY,  font=('arial', 14))
    contact.grid(row=5, column=1)
    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData)
    btn_addcon.grid(row=6, columnspan=2, pady=10)
#============================FRAMES======================================
Top = Frame(root, width=500, bd=1, relief=SOLID)
Top.pack(side=TOP)
Mid = Frame(root, width=500,  bg="#6666ff")
Mid.pack(side=TOP)
MidLeft = Frame(Mid, width=100)
MidLeft.pack(side=LEFT, pady=10)
MidLeftPadding = Frame(Mid, width=370, bg="#6666ff")
MidLeftPadding.pack(side=LEFT)
MidRight = Frame(Mid, width=100)
MidRight.pack(side=RIGHT, pady=10)
TableMargin = Frame(root, width=500)
TableMargin.pack(side=TOP)
#============================LABELS======================================
lbl_title = Label(Top, text="Chain of Custody", font=('arial', 16), width=500)
lbl_title.pack(fill=X)

#============================ENTRY=======================================
#============================BUTTONS=====================================
btn_add = Button(MidLeft, text="+ Add New Evidence", bg="#66ff66", command=AddNewWindow)
btn_add.pack()
btn_delete = Button(MidRight, text="DELETE", bg="red", command=DeleteData)
btn_delete.pack(side=RIGHT)
#============================TABLES======================================
scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
tree = ttk.Treeview(TableMargin, columns=("MemberID", "item", "description", "Gender", "quanitity", "releasedby", "receivedby"), height=400, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('item', text="Item", anchor=W)
tree.heading('description', text="Description of item", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('quanitity', text="Quanitity", anchor=W)
tree.heading('releasedby', text="Released By", anchor=W)
tree.heading('receivedby', text="Received By", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=90)
tree.column('#5', stretch=NO, minwidth=0, width=80)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)
#============================INITIALIZATION==============================
if __name__ == '__main__':
    Database()
    root.mainloop()
