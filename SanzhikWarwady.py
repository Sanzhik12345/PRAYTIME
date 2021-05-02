import urllib.request
from tkinter import *
from bs4 import BeautifulSoup
from tkinter import messagebox
root = Tk()
root["bg"] = "white"
root.title("Prayer time")
root.geometry("250x200")
Label(root, text="Please enter the name of city:", font="Arial 11", bg="white").pack(pady=5)
city= Entry(root, width=40)
city.pack()
def time():
     s = str(city.get())
     search = f'{s}'
     url = f"https://namaz.today/city/={search}"
     source = urllib.request.urlopen(url).read()
     features="html.parser"
     soup = BeautifulSoup(source, features)
     Fajr_time = soup.find("div", class_="columns small-up-2 large-up-6 medium-up-3 time-block").find_all("span")
     Tulu_time = soup.find("div", class_="columns small-up-2 large-up-6 medium-up-3 time-block").find_all("span")
     Zuhr_time = soup.find("div", class_="columns small-up-2 large-up-6 medium-up-3 time-block").find_all("span")
     Asr_time = soup.find("div", class_="columns small-up-2 large-up-6 medium-up-3 time-block").find_all("span")
     Maghrib_time = soup.find("div", class_="columns small-up-2 large-up-6 medium-up-3 time-block").find_all("span")
     Isha_time = soup.find("div", class_="columns small-up-2 large-up-6 medium-up-3 time-block").find_all("span")
     time = Fajr_time[0].text
     time1 = Tulu_time[4].text
     time2 = Zuhr_time[8].text
     time3 = Asr_time[12].text
     time4 = Maghrib_time[16].text
     time5 = Isha_time[20].text
     messagebox.showinfo("Prayer time in city "+ s," Fajr time " + time +'\n'+ " Tulu time " + time1 +'\n'+ " Zuhr time " + time2 +'\n'+ " Asr time " + time3 +'\n'+ " Maghrib time " + time4 +'\n'+ " Isha time " + time5+'\n'+ "" +'\n'+" Suhoor " + time +'\n'+" Iftar " + time4)
     city.delete(0, END)
Button(root, text="search",command=time, bg="white", width=10, font="Arial 9 ").pack(pady=10)
root.mainloop()