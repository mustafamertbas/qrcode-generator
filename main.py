from tkinter import *
from tkinter import messagebox
import os
import pyqrcode

#Made with @mustafamret / @mustafamret.dev
#Bu proje @mustafamret / @mustafamret.dev tarafından yapılmıştır.

window = Tk()
window.title("QR Code Oluşturucu")


#Karekod oluştur
def generate():
    if len(Subject.get())!=0 :
        global qr,photo
        qr = pyqrcode.create(Subject.get())
        photo = BitmapImage(data = qr.xbm(scale=8))
    else:
        messagebox.showinfo("Hata!", "Lütfen linki girin!")
    try:
        showcode()
    except:
        pass

#Oluşturan Karekodu göster
def showcode():
    imageLabel.config(image = photo)
    subLabel.config(text=Subject.get())

#Oluşturulan Karekodu belirtilen yere kaydet veya belirtlien klasörü oluştur
def save():
    dir = os.getcwd() + "\\QR Kodlarım"
    if not os.path.exists(dir):
        os.makedirs(dir)
    try:
        if len(name.get())!=0:
            qr.png(os.path.join(dir,name.get()+".png"),scale=8)
        else:
            messagebox.showinfo("Hata!", "Lütfen isim belirleyin!")
    except:
        messagebox.showinfo("Başarılı!", "QR Kodun Başarıyla Oluşturuldu!")

#Link belirtilmesi için başlık oluştur
Sub = Label(window,text="Linki Girin")
Sub.grid(row =0,column =0,sticky=N+S+W+E)

#Link belirtilmesi için metin alanı oluştur
Subject = StringVar()
SubEntry = Entry(window,textvariable = Subject)
SubEntry.grid(row =0,column =1,sticky=N+S+W+E)

#İsim belirtilmesi için başlık oluştur
FName = Label(window,text="İsim Belirleyin")
FName.grid(row =1,column =0,sticky=N+S+W+E)

#İsim belirtilmesi için metin alanı oluştur
name = StringVar()
nameEntry = Entry(window,width=50,textvariable = name)
nameEntry.grid(row =1,column =1,sticky=N+S+W+E)

#Karekodu oluşturmak için tuş ekle
button = Button(window,text = "QR Kodu Oluştur",width=15,command = generate)
button.grid(row =0,column =3,sticky=N+S+W+E)

#Oluşturulan karekodu ekrana yansıt
imageLabel = Label(window)
imageLabel.grid(row =2,column =1,sticky=N+S+W+E)

#Oluşturulan karekodun adresini aşağısına yaz
subLabel = Label(window,text="")
subLabel.grid(row =3,column =1,sticky=N+S+W+E)

#Karekodu kaydetmek için buton ekle
saveB = Button(window,text="PNG Olarak Kaydet",width=15,command = save)
saveB.grid(row =1,column =3,sticky=N+S+W+E)


window.mainloop()
