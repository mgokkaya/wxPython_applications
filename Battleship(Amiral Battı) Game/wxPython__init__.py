#!/usr/bin/python
# -*- coding: utf-8 -*-
import wx, sys
import random
import time
import gtk
import appindicator
import imaplib
import re


class Frame1(wx.Frame):
    ID_LOAD = wx.NewId()


   
    def __init__(self, parent, id, title, size, style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, size=size, style=style)
       
        self.loc = wx.IconLocation(r'/home/muhammed/Desktop/task.ico', 0)
        self.SetIcon(wx.IconFromLocation(self.loc))
        test = TrayIcon()
    
        self.sb = StatusBar(self)
        self.SetStatusBar(self.sb)
        
        self.panel = MainPanel(self) 

        ekran = wx.GridSizer(4, 15, 10, 10)  # rows, cols, vgap, hgap
        middleBox = wx.BoxSizer(wx.HORIZONTAL)
        self.cik = wx.Button(self.panel,1, label="ÇIKIŞ YAP",pos=(800,25),size=(100,50))


        self.liste = []
        for btn in xrange(225):
            
            b = wx.BitmapButton(self.panel, btn, wx.Bitmap('/home/muhammed/Desktop/deniz.png'))
            self.liste.append(b)
            b.SetToolTip(wx.ToolTip(str(btn)))

            ekran.Add(b)
            self.Bind(wx.EVT_BUTTON, self.OnClick,b)
            
        outerSizer = wx.BoxSizer(wx.HORIZONTAL)
        outerSizer.Add(ekran)
        outerSizer.Add(middleBox, 1, wx.EXPAND) 
        self.panel.SetSizer(outerSizer)
        self.matris1=[]
        self.matris2=[]
        self.gemisayac=0
        self.skor=0
        self.Bind(wx.EVT_BUTTON, self.cikisf1, self.cik)


        for i in xrange(0,4):
            x=random.randrange(15) 
            y=random.randrange(15) 
            koordinat=random.randrange(2)
            if koordinat==0:
                if x>12:
                    x=x-i
                    for j in xrange(x,x+i+1):
                        for k in xrange(y,y+1):
                            self.matris1.append(j)
                            self.matris2.append(k)
                        
                else:
                    for j in xrange(x,x+i+1):
                        for k in xrange(y,y+1):
                        
                            self.matris1.append(j)
                            self.matris2.append(k)
                        

            else:
                if y>12:
                    y=y-i
                    for j in xrange(x,x+1):
                        for k in xrange(y,y+i+1):
                            self.matris1.append(j)
                            self.matris2.append(k)
                else:
                    for j in xrange(x,x+1):
                        for k in xrange(y,y+i+1):
                            self.matris1.append(j)
                            self.matris2.append(k)
    
                            
    
            
    def OnClick(self, event):
        #print "konum",(self.matris2[0]*15)+(self.matris1[0])
        #print "konum",(self.matris2[1]*15)+(self.matris1[1])
        #print "konum",(self.matris2[2]*15)+(self.matris1[2])
        #print "konum",(self.matris2[3]*15)+(self.matris1[3])
        #print "konum",(self.matris2[4]*15)+(self.matris1[4])
        #print "konum",(self.matris2[5]*15)+(self.matris1[5])
        #print "konum",(self.matris2[6]*15)+(self.matris1[6])
        #print "konum",(self.matris2[7]*15)+(self.matris1[7])
        #print "konum",(self.matris2[8]*15)+(self.matris1[8])
        #print "konum",(self.matris2[9]*15)+(self.matris1[9])
        self.mesaj = wx.StaticText(self.panel, label="SKOR:"+str(self.skor),size=(150,150), pos=(810, 10))

        #print self.skor


        if (self.matris2[0]*15)+(self.matris1[0])==event.GetId() or (self.matris2[1]*15)+(self.matris1[1])==event.GetId() or (self.matris2[2]*15)+(self.matris1[2])==event.GetId() or (self.matris2[3]*15)+(self.matris1[3])==event.GetId() or (self.matris2[4]*15)+(self.matris1[4])==event.GetId() or (self.matris2[5]*15)+(self.matris1[5])==event.GetId() or (self.matris2[6]*15)+(self.matris1[6])==event.GetId() or (self.matris2[7]*15)+(self.matris1[7])==event.GetId() or (self.matris2[8]*15)+(self.matris1[8])==event.GetId() or (self.matris2[9]*15)+(self.matris1[9])==event.GetId():
            self.SetStatusText("VURULDU    ID:" + str(event.GetId()) )
            self.gemisayac=self.gemisayac+1
            self.skor=int(self.skor+1)
            self.liste[event.GetId()].SetBitmapLabel(wx.Bitmap('/home/muhammed/Desktop/ship-24.png'))
          
            #print "gemi:",self.gemisayac
            if self.gemisayac==10:

                frame4 = Frame4(None, 1, "OYUN BİTTİ ! ",wx.Size(500,760))
                frame4.Show()

                self.Close()



        
        else:
            self.SetStatusText("ORASI BOŞ  ID:"+ str(event.GetId()))
            self.skor=int(self.skor-1)

            self.liste[event.GetId()].SetBitmapLabel(wx.Bitmap('/home/muhammed/Desktop/fire1.png'))

      
    def cikisf1(self,event):
        sys.exit(0)


class Frame2(wx.Frame):
    ID_LOAD = wx.NewId()
    def __init__(self, parent, id, title, size, style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, size=size, style=style)
        
        self.loc = wx.IconLocation(r'/home/muhammed/Desktop/favicon.ico', 0)
        
        self.SetIcon(wx.IconFromLocation(self.loc))

        panel = MainPanel(self) 
        
        self.button = wx.Button(panel,1, label="YENİ OYUN",pos=(25,25),size=(200,100))
        
        self.button2 = wx.Button(panel,2, label="HAKKINDA",pos=(25,150),size=(200,100))
        
        self.button3 = wx.Button(panel,3, label="ÇIKIŞ",pos=(25,275),size=(200,100))
        

        middleBox = wx.BoxSizer(wx.HORIZONTAL)
        self.Bind(wx.EVT_BUTTON, self.yenioyun, self.button)
        self.Bind(wx.EVT_BUTTON, self.hakkinda, self.button2)
        self.Bind(wx.EVT_BUTTON, self.cikis, self.button3)
        

        outerSizer = wx.BoxSizer(wx.HORIZONTAL)
        outerSizer.Add(middleBox, 1, wx.EXPAND) 
        panel.SetSizer(outerSizer)

    
            
    def yenioyun(self, event):
        frame = Frame1(None, 1, "AMİRAL BATTI ",wx.Size(900,760))
        frame.Show()
        #return True
        self.Close()
    def hakkinda(self,event):
        frame3 = Frame3(None, 1, "HAKKINDA ",wx.Size(1300,760))
        frame3.Show()
        #self.frasme2.Hide()
        #return True
        self.Close()
    def cikis(self,event):
        self.Close()
        

class Frame3(wx.Frame):
    ID_LOAD = wx.NewId()
    def __init__(self, parent, id, title, size, style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, size=size, style=style)
        
        self.loc = wx.IconLocation(r'/home/muhammed/Desktop/mm.ico', 0)
       
        self.SetIcon(wx.IconFromLocation(self.loc))

        panel = MainPanel2(self) 
        self.yazi = wx.StaticText(panel, label="\t\tAMİRAL BATTI OYUNU\nÇocuk oyunları, genellikle çocukların oynadığı ancak bazen \nyetişkinlerin de eşlik ettiği veya kendi aralarında oynadığı oyunlardır.\n Bazı oyunlar için açık alan gerekirken, diğerleri bina içerisinde \noynanabilir. Tek kişilik çocuk oyunları olduğu gibi onlarca kişi ile \noynanan oyunlar da mevcuttur.\nHollandalı ressam Pieter Bruegel'in Çocuk Oyunları isimli\n eseri, 1560.\nBazı çocuk oyunları evrenseldir ve aşağı yukarı aynı \nkurallarla birçok ülkede oynanır. \nPek çok oyun yüzyıllar öncesinden günümüze ulaşmıştır. \nGünümüzdeki seksek, körebe, ip çekme gibi oyunların Eski Roma döneminde de çocukların \nsevdiği oyunlar olduğu bilinmektedir.\nBazı çocuk oyunları yüzlerce yıldır aynı kalmışken diğerleri\n zaman içerisinde evrim geçirmiş, farklı kurallarla oynanmaya başlamıştır.\nÇocuk oyunları, açık hava oyunları ve ev oyunları şeklinde başlıca iki grupta toplanabilir.\n Kağıt-kalemle oynanan oyunlar, sportif oyunlar, müzikal \noyunlar gibi pek çok oyun grubu vardır.", pos=(10, 10))

        

        
        middleBox = wx.BoxSizer(wx.HORIZONTAL)
        

                    
        outerSizer = wx.BoxSizer(wx.HORIZONTAL)
        outerSizer.Add(middleBox, 1, wx.EXPAND) 
        panel.SetSizer(outerSizer)
class Frame4(wx.Frame):
    ID_LOAD = wx.NewId()
    def __init__(self, parent, id, title, size, style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, size=size, style=style)
        
        self.loc = wx.IconLocation(r'/home/muhammed/Desktop/favicon.ico', 0)
        
        self.SetIcon(wx.IconFromLocation(self.loc))

        panel = MainPanel(self) 
       
        self.button = wx.Button(panel,1, label="YENİ OYUN",pos=(25,25),size=(200,100))
        
        self.button2 = wx.Button(panel,2, label="HAKKINDA",pos=(25,150),size=(200,100))
        
        self.button3 = wx.Button(panel,3, label="ÇIKIŞ",pos=(25,275),size=(200,100))
        

        middleBox = wx.BoxSizer(wx.HORIZONTAL)
        self.Bind(wx.EVT_BUTTON, self.yenioyun, self.button)
        self.Bind(wx.EVT_BUTTON, self.hakkinda, self.button2)
        self.Bind(wx.EVT_BUTTON, self.cikis, self.button3)


        

        outerSizer = wx.BoxSizer(wx.HORIZONTAL)
        outerSizer.Add(middleBox, 1, wx.EXPAND) 
        panel.SetSizer(outerSizer)

    
            
    def yenioyun(self, event):
        frame = Frame1(None, 1, "AMİRAL BATTI ",wx.Size(900,760))
        frame.Show()
        #return True
        self.Close()
    def hakkinda(self,event):
        frame3 = Frame3(None, 1, "HAKKINDA ",wx.Size(1300,760))
        frame3.Show()
        #self.frasme2.Hide()
        self.Close()
    def cikis(self,event):
        self.Close()
        menu.Destroy()

class TrayIcon():

    def __init__(self):
        self.ind = appindicator.Indicator("trayicon","/home/muhammed/Desktop/notfica.png",appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        

        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
        self.menu = gtk.Menu()
        self.start_item=gtk.MenuItem("BAŞLAT")
        self.start_item.connect("activate",self.start)
        self.start_item.show()
        self.menu.append(self.start_item)

        self.quit_item = gtk.MenuItem("ÇIKIŞ")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def main(self):
        gtk.main()
    def start(self):
        frame = Frame1(None, 1, "AMİRAL BATTI ",wx.Size(900,760))
        frame.Show()
        #pass
    def quit(self, widget):
        sys.exit(0)


class StatusBar(wx.StatusBar):
    
    def __init__(self, parent):
        super(StatusBar, self).__init__(parent)

        self.SetFieldsCount(2)
        self.SetStatusText('AMİRAL BATTI AÇILDI :D')
        self.SetStatusWidths([-1, 200])
        
        self.icon = wx.StaticBitmap(self, bitmap=wx.Bitmap('/home/muhammed/Desktop/deniz.png'))
        self.Bind(wx.EVT_SIZE,self.iconp())
    def iconp(self):
        
        konum = self.GetFieldRect(1)

        self.icon.SetPosition((konum.x, konum.y))




class MyApp(wx.App):
    def OnInit(self):
        self.frame2=Frame2(None, 1 ,  "BAŞLAMA EKRANI", wx.Size(300,400))
        self.frame2.Show()
        return True

def main(argv=None):
    if argv is None:
        argv = sys.argv
    app = MyApp(0)
    app.MainLoop()
    test = TrayIcon()
    test.main()

class MainPanel(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.arkaplan)

    def arkaplan(self, evt):
       
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("/home/muhammed/Desktop/fon1.jpg")
        dc.DrawBitmap(bmp, 0, 0)
class MainPanel2(wx.Panel):
    
    def __init__(self, parent):
        
        wx.Panel.__init__(self, parent=parent)
        self.SetBackgroundStyle(wx.BG_STYLE_CUSTOM)
        self.frame = parent

        sizer = wx.BoxSizer(wx.VERTICAL)
        hSizer = wx.BoxSizer(wx.HORIZONTAL)

        self.SetSizer(hSizer)
        self.Bind(wx.EVT_ERASE_BACKGROUND, self.arkaplan)

    def arkaplan(self, evt):
       
        dc = evt.GetDC()

        if not dc:
            dc = wx.ClientDC(self)
            rect = self.GetUpdateRegion().GetBox()
            dc.SetClippingRect(rect)
        dc.Clear()
        bmp = wx.Bitmap("/home/muhammed/Desktop/p3.jpg")
        dc.DrawBitmap(bmp, 0, 0)
if __name__ == '__main__':
        main()
