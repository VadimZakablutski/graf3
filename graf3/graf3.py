from tkinter import*
from module import*
from tkinter.messagebox import*
from tkinter.ttk import*
userr=loe_failist_listisse("users.txt")
passww=loe_failist_listisse("passwords.txt")
log=Tk()
log.geometry("300x100")
log.title("Авторизация")
def append():
    global login1
    global psw1
    Label(text="Придумайте\nЛогин:").grid(row=0,column=0)
    login1=Entry(width=30)
    login1.grid(row=0,column=1,columnspan=3)
    Label(text="Придумайте\nПароль:").grid(row=1,column=0)
    psw1=Entry(width=30)
    psw1.grid(row=1,column=1,columnspan=3)
    Button(text="Выход",command=Exit2).grid(row=2,column=1)
    Button(text="Подтвердить",command=append).grid(row=2,column=3)
    if psw1.get=="" or login1.get=="":
        showerror(title="Error",message="Пароль или логин не может быть пустотой!")
    else:
        showinfo(title="OK",message="Пароль принят и добавлен в базу данных!")
        userr.append(login1)
        passww.append(psw1)
def Reg():
    log.destroy()
    reg=Tk()
    reg.geometry("300x100")
    reg.title("Регистрация")
    Label(text="Придумайте\nЛогин:").grid(row=0,column=0)
    login1=Entry(width=30)
    login1.grid(row=0,column=1,columnspan=3)
    Label(text="Придумайте\nПароль:").grid(row=1,column=0)
    psw1=Entry(width=30)
    psw1.grid(row=1,column=1,columnspan=3)
    Button(text="Выход",command=Exit2).grid(row=2,column=1)
    Button(text="Подтвердить",command=append).grid(row=2,column=3)
    
def Login():
    user=login.get()
    passw=psw.get()
    if (user not in userr) or (passw not in passww):
        showerror(title="Error",message="Пароль или логин неверен!")
        Reg()
    else:
        showinfo(title="OK",message="Добро пожаловать!")

def Exit2():
    if askyesno("Выход","Выйти?"):
         Reg.destroy()
def Exit():
    if askyesno("Выход","Выйти?"):
        log.destroy()

Label(text="Логин:").grid(row=0,column=0)
login=Entry(width=30)
login.grid(row=0,column=1,columnspan=3)
Label(text="Пароль:").grid(row=1,column=0)
psw=Entry(width=30)
psw.grid(row=1,column=1,columnspan=3)
Button(text="Регистрация",command=Reg).grid(row=2,column=0)
Button(text="Выход",command=Exit).grid(row=2,column=2)
Button(text="Вход",command=Login).grid(row=2,column=3)



log.mainloop()
