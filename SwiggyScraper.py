import requests as rq
import bs4
import csv
from tkinter import messagebox
class swiggy_scraper(common_ui):
    def __init__(self):
        self.url = 'https://www.swiggy.com/'
        super().__init__()
    def extract(self):
        try:
            self.inp = self.et.get().strip()
            self.url += self.inp
            self.data = rq.get(self.url)
            self.soup = bs4.BeautifulSoup(self.data.text, 'html.parser')
            #print(self.data)
            self.data = self.soup.findAll('a', {'class': '_1j_Yo'})
            #print(self.data[0]['href'])
            self.res_det = []
            for d in self.data[:5]:
                self.res = list()
                self.new = "https://www.swiggy.com" + d['href']
                self.data = rq.get(self.new)
                self.soup = bs4.BeautifulSoup(self.data.text, 'html.parser')
                self.data = self.soup.find('div', {'class': 'OEfxz'})
                self.res.append(self.data.text)
                self.data = self.soup.find('div', {'class': 'Gf2NS _2Y6HW'})
                self.res.append(self.data.text)
                self.data = self.soup.find('div', {'class': '_3Plw0 JMACF'})
                self.res.append(self.data.text)
                self.data = self.soup.find('div', {'class': '_2l3H5'})
                self.res.append(self.data.text)
                self.data = self.soup.find('div', {'class': 'jTy8b'})
                self.res.append(self.data.text)
                self.res_det.append(self.res)
            for i in self.res_det:
                print(i)
            with open("swiggyData.csv", 'w') as f:
                writer = csv.writer(f)
                writer.writerow(self.res_det)
        except:
            messagebox.showinfo('Caution', 'Network/Input Error')
        
    def uicomponents(self):
        self.l1 = Label(self.root, text = 'Swiggy Recommendation Scraper', fg = 'black', bg = 'orange', font = ('Courier 30 bold'))
        self.l1.place(x = 200, y = 10, width = 700, height = 50)
        self.img = ImageTk.PhotoImage(Image.open("C:\\Users\\abhis\\Learn Code Online\\DAY-17\\assets\\swiggyit.jpg"))
        self.l2 = Label(self.root, image = self.img)
        self.l2.place(x = 100, y = 75, width = 1000, height = 580)
        self.l3 = Label(self.root, text = 'CITY', fg = 'white', bg = '#f57c00', font = ('Courier 30 bold'))
        self.l3.place(x = 200, y = 680, width = 200, height = 60)
        self.et = Entry(self.root, fg = 'white', bg = '#f57c00', font = ('Courier 20 bold'))
        self.et.place(x = 410, y = 680, width = 500, height = 60)
        Button(self.root, text = 'OK', fg = 'black', bg = '#f57c00', command = self.extract, font = ('Courier 15 bold')).place(x = 550, y = 750, width = 50, height = 40)
        
        

obj = swiggy_scraper()
