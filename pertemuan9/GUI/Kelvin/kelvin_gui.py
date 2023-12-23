# File-1
class Kelvin:
  def __init__(self, suhu):
    self.suhu = suhu

  def get_kelvin(self):
    val = self.suhu
    return val
    
  def get_celcius(self):
    val = float(self.suhu) - 273.15
    return val
  
  def get_reamur(self):
    val = (4/5) * (float(self.suhu) - 273.15)
    return val
  
  def get_fahrenheit(self):
    val = (9/5 * (float(self.suhu) - 273.15)) + 32
    return val

# File-2
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W
from kelvin import *
class FrmKelvin:
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES) 
        Label(mainFrame, text='Kelvin:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Reamur:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=0, column=1, padx=5, pady=5)  

        self.txtCelcius = Entry(mainFrame) 
        self.txtCelcius.grid(row=2, column=1, padx=5, pady=5) 

        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=3, column=1, padx=5, pady=5) 

        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=4, column=1, padx=5, pady=5) 

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)
        
    def onHitung(self):
        K = Kelvin(int(self.txtKelvin.get()))

        C = K.get_celcius()
        self.txtCelcius.delete(0,END)
        self.txtCelcius.insert(END,str(C))

        R = K.get_reamur()
        self.txtReamur.delete(0,END)
        self.txtReamur.insert(END,str(R))

        F = K.get_fahrenheit()
        self.txtFahrenheit.delete(0,END)
        self.txtFahrenheit.insert(END,str(F))
               
    def onKeluar(self, event=None):
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmKelvin(root, "Program Konversi Suhu Fahrenheit")
    root.mainloop() 