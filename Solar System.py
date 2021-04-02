# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 16:38:20 2020

@author: Karan
"""

#from tkinter import *
import tkinter as tk
from tkinter import StringVar, IntVar
import mysql.connector
from tkinter import messagebox
cn = mysql.connector.connect(user='root',
                             password='',
                             host='localhost',
                             database='project')

command=cn.cursor()
window = tk.Tk()
window.title('Registration form')
window.geometry('800x500')

appliances = tk.Tk()
appliances.geometry("800x800")
appliances.title("Appliances")

prequisites = tk.Tk()
prequisites.title("Prequisites")
prequisites.geometry("800x500")

prequisites1 = tk.Tk()
prequisites1.title("Prequisites")
prequisites1.geometry("800x500")

signUp = tk.Tk()
signUp.title("Sign Up")
signUp.geometry("800x500")

user_name = StringVar(window)
user_email = StringVar(window)
user_password = StringVar(window)
user_conform = StringVar(window)
user_house = StringVar(window)
user_society = StringVar(window)
user_landmark = StringVar(window)
user_pincode = IntVar(window)
user_country = StringVar(window)
user_province = StringVar(window)
user_city = StringVar(window)
signUp_email = StringVar()
signUp_pwd = StringVar()

fan_quantity = StringVar()
lights_quantity = StringVar()
bulbs_quantity = StringVar()
television_quantity = StringVar()
chimney_quantity = StringVar()
blender_quantity = StringVar()
mixture_quantity = StringVar()
juicer_quantity = StringVar()
refrigerator_quantity = StringVar()
homeTheater_quantity = StringVar()
ac_quantity = StringVar()
washingMachine_quantity = StringVar()
phones_quantity = StringVar()
laptop_quantity = StringVar()
pc_quantity = StringVar()

fan_hrs = IntVar()
lights_hrs = IntVar()
bulbs_hrs = IntVar()
television_hrs = IntVar()
chimney_hrs = IntVar()
blender_hrs = IntVar()
mixture_hrs = IntVar()
juicer_hrs = IntVar()
refrigerator_hrs = IntVar()
homeTheater_hrs = IntVar()
ac_hrs = IntVar()
washingMachine_hrs = IntVar()
phones_hrs = IntVar()
laptop_hrs = IntVar()
pc_hrs = IntVar()

class electricAppliances():
    fan=0
    lights=0
    bulbs=0
    television=0
    chimney=0
    blender=0
    mixture=0
    jucier=0
    refrigerator=0
    homeTheater=0
    ac=0
    washingMachine=0
    phones=0
    laptop=0
    pc=0 
    
    def __init__(self,fan_quan,lights_quan,bulbs_quan,television_quan,chimney_quan,blender_quan,
                 mixture_quan,juicer_quan,refrigerator_quan,homeTheater_quan,ac_quan,washingMachine_quan,
                 phones_quan,laptop_quan,pc_quan):
        self.fan=fan_quan
        self.lights=lights_quan
        self.bulbs=bulbs_quan
        self.television=television_quan
        self.chimney=chimney_quan
        self.blender=blender_quan
        self.mixture=mixture_quan
        self.juicer=juicer_quan
        self.refrigerator=refrigerator_quan
        self.homeTheater=homeTheater_quan
        self.ac=ac_quan
        self.washingMachine=washingMachine_quan
        self.phones=phones_quan
        self.laptop=laptop_quan
        self.pc=pc_quan
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.fan,self.lights,self.bulbs,self.television,self.chimney,
                self.blender,self.mixture,self.juicer,self.refrigerator,self.homeTheater,self.ac,self.washingMachine,
                self.phones,self.laptop,self.pc)
        
    def setFan(self,fan_quantity):
        self.fan=fan_quantity
    def setLights(self,lights_quantity):
        self.lights=lights_quantity
    def setBulbs(self,bulbs_quantity):
        self.bulbs=bulbs_quantity
    def setTelevision(self,television_quantity):
        self.television=television_quantity
    def setChimney(self,chimney_quantity):
        self.chimney=chimney_quantity
    def setBlender(self,blender_quantity):
        self.blender=blender_quantity
    def setMixture(self,mixture_quantity):
        self.mixture=mixture_quantity
    def setJuicer(self,juicer_quantity):
        self.juicer=juicer_quantity
    def setRefrigerator(self,refrigerator_quantity):
        self.refrigerator=refrigerator_quantity
    def setHomeTheater(self,homeTheater_quantity):
        self.homeTheater=homeTheater_quantity
    def setAC(self,ac_quantity):
        self.ac=ac_quantity
    def setWashingMachine(self,washingMachine_quantity):
        self.washingMachine=washingMachine_quantity
    def setPhones(self,phones_quantity):
        self.phones=phones_quantity
    def setLaptop(self,laptop_quantity):
        self.laptop=laptop_quantity
    def setpc(self,pc_quantity):
        self.pc=pc_quantity
        
    def getFan(self):
        return self.fan
    def getLights(self):
        return self.lights
    def getBulbs(self):
        return self.bulbs
    def getTelevision(self):
        return self.lights
    def getChimney(self):
        return self.chimney
    def getBlender(self):
        return self.blender
    def getMixture(self):
        return self.mixture
    def getJuicer(self):
        return self.juicer
    def getRefrigerator(self):
        return self.refrigerator
    def getHomeTheater(self):
        return self.homeTheater
    def getAC(self):
        return self.ac
    def getWashingMachine(self):
        return self.washingMachine
    def getPhones(self):
        return self.phones
    def getLaptop(self):
        return self.laptop
    def getpc(self):
        return self.pc

class working_hours:
    fan_wrk=0
    lights_wrk=0
    bulbs_wrk=0
    television_wrk=0
    chimney_wrk=0
    blender_wrk=0
    mixture_wrk=0
    jucie_wrk=0
    refrigerato_wrk=0
    homeTheater_wrk=0
    ac_wrk=0
    washingMachine_wrk=0
    phones_wrk=0
    laptop_wrk=0
    pc_wrk=0 
    
    def __init__(self,fan_hrs,lights_hrs,bulbs_hrs,television_hrs,chimney_hrs,blender_hrs,mixture_hrs,
                  juicer_hrs,refrigerator_hrs,homeTheater_hrs,ac_hrs,washingMachine_hrs,phones_hrs,laptop_hrs,pc_hrs):
        self.fan_wrk=fan_hrs
        self.lights_wrk=lights_hrs
        self.bulbs_wrk=bulbs_hrs
        self.television_wrk=television_hrs
        self.chimney_wrk=chimney_hrs
        self.blender_wrk=blender_hrs
        self.mixture_wrk=mixture_hrs
        self.juicer_wrk=juicer_hrs
        self.refrigerator_wrk=refrigerator_hrs
        self.homeTheater_wrk=homeTheater_hrs
        self.ac_wrk=ac_hrs
        self.washingMachine_wrk=washingMachine_hrs
        self.phones_wrk=phones_hrs
        self.laptop_wrk=laptop_hrs
        self.pc_wrk=pc_hrs
    def __str__(self):
        return "{} {} {} {} {} {} {} {} {} {} {} {} {} {} {}".format(self.fan_wrk,self.lights_wrk,self.bulbs_wrk,
                self.television_wrk,self.chimney_wrk,self.blender_wrk,self.mixture_wrk,self.juicer_wrk
                ,self.refrigerator_wrk,self.homeTheater_wrk,self.ac_wrk,self.washingMachine_wrk,
                self.phones_wrk,self.laptop_wrk,self.pc_wrk)
        
    def setFanHrs(self,fan_hrs):
        self.fan_wrk = fan_hrs
    def setLightsHrs(self,lights_hrs):
        self.lights_wrk=lights_hrs
    def setBulbsHrs(self,bulbs_hrs):
        self.bulbs_wrk=bulbs_hrs
    def setTelevisionHrs(self,television_hrs):
        self.lights_wrk=lights_hrs
    def setChimneyHrs(self,chimney_hrs):
        self.chimney_wrk=chimney_hrs
    def setBlenderHrs(self,blender_hrs):
        self.blender_wrk=blender_hrs
    def setMixtureHrs(self,mixture_hrs):
        self.mixture_wrk=mixture_hrs
    def setJuicerHrs(self,juicer_hrs):
        self.juicer_wrk=juicer_hrs
    def setRefrigeratorHrs(self,refrigerator_hrs):
        self.refrigerator_wrk=refrigerator_hrs
    def setHomeTheaterHrs(self,homeTheater_hrs):
        self.homeTheater_wrk=homeTheater_hrs
    def setACHrs(self,ac_hrs):
        self.ac_wrk=ac_hrs
    def setWashingMachineHrs(self,washingMachine_hrs):
        self.washingMachine_wrk=washingMachine_hrs
    def setPhonesHrs(self,phones_hrs):
        self.phones_wrk=phones_hrs
    def setLaptopHrs(self,laptop_hrs):
        self.laptop_wrk=laptop_hrs
    def setpcHrs(self,pc_hrs):
        self.pc_wrk=pc_hrs
    
    def getFanHrs(self):
        return self.fan_wrk
    def getLightsHrs(self):
        return self.lights_wrk
    def getBulbsHrs(self):
        return self.bulbs_wrk
    def getTelevisionHrs(self):
        return self.lights_wrk
    def getChimneyHrs(self):
        return self.chimney_wrk
    def getBlenderHrs(self):
        return self.blender_wrk
    def getMixtureHrs(self):
        return self.mixture_wrk
    def getJuicerHrs(self):
        return self.juicer_wrk
    def getRefrigeratorHrs(self):
        return self.refrigerator_wrk
    def getHomeTheaterHrs(self):
        return self.homeTheater_wrk
    def getACHrs(self):
        return self.ac_wrk
    def getWashingMachineHrs(self):
        return self.washingMachine_wrk
    def getPhonesHrs(self):
        return self.phones_wrk
    def getLaptopHrs(self):
        return self.laptop_wrk
    def getpcHrs(self):
        return self.pc_wrk

    
        
    
    
#devices = electricAppliances()
#working = working_hours()
prequisites.withdraw()

appliances.withdraw()
signUp.withdraw()
prequisites1.withdraw()


def getAppliances():
    
    devices = electricAppliances(fan_quantity.get(),lights_quantity.get(),bulbs_quantity.get(),television_quantity.get(),
                                    chimney_quantity.get(),blender_quantity.get(),mixture_quantity.get(),juicer_quantity.get(),
                                    refrigerator_quantity.get(),homeTheater_quantity.get(),ac_quantity.get(),
                                    washingMachine_quantity.get(),phones_quantity.get(),laptop_quantity.get(),pc_quantity.get())
    
    working = working_hours(fan_hrs.get(),lights_hrs.get(),bulbs_hrs.get(),television_hrs.get(),chimney_hrs.get(),
                            blender_hrs.get(),mixture_hrs.get(),juicer_hrs.get(),refrigerator_hrs.get(),
                            homeTheater_hrs.get(),ac_hrs.get(),washingMachine_hrs.get(),phones_hrs.get(),laptop_hrs.get(),
                            pc_hrs.get())

    
    
    wrking_hrs = str(working)
    appliance = str(devices)
    
    wrking_hrs = wrking_hrs.split(' ')
    appliance = appliance.split(' ')
    

    devices.setFan(fan_quantity.get())
    devices.setLights(lights_quantity.get())
    devices.setBulbs(bulbs_quantity.get())
    devices.setTelevision(television_quantity.get())
    devices.setChimney(chimney_quantity.get())
    devices.setBlender(blender_quantity.get())
    devices.setMixture(mixture_quantity.get())
    devices.setJuicer(juicer_quantity.get())
    devices.setRefrigerator(refrigerator_quantity.get())
    devices.setHomeTheater(homeTheater_quantity.get())
    devices.setAC(ac_quantity.get())
    devices.setWashingMachine(washingMachine_quantity.get())
    devices.setPhones(phones_quantity.get())
    devices.setLaptop(laptop_quantity.get())
    devices.setpc(pc_quantity.get())
    
    working.setFanHrs(fan_hrs.get())
    working.setLightsHrs(lights_hrs.get())
    working.setBulbsHrs(bulbs_hrs.get())
    working.setTelevisionHrs(television_hrs.get())
    working.setChimneyHrs(chimney_hrs.get())
    working.setBlenderHrs(blender_hrs.get())
    working.setMixtureHrs(mixture_hrs.get())
    working.setJuicerHrs(juicer_hrs.get())
    working.setRefrigeratorHrs(refrigerator_hrs.get())
    working.setHomeTheaterHrs(homeTheater_hrs.get())
    working.setACHrs(ac_hrs.get())
    working.setWashingMachineHrs(washingMachine_hrs.get())
    working.setPhonesHrs(phones_hrs.get())
    working.setLaptopHrs(laptop_hrs.get())
    working.setpcHrs(pc_hrs.get())
       
    list3 = []
    #list4 = []
    
    list3.append(75)
    list3.append(22)
    list3.append(9)
    list3.append(85)
    list3.append(350)
    list3.append(400)
    list3.append(500)
    list3.append(800)
    list3.append(700)
    list3.append(95)
    list3.append(1200)
    list3.append(1150)
    list3.append(95)
    list3.append(300)
    list3.append(100)
    
    '''for i in range(0,10000):
        list4[i] = ((int(wrking_hrs[i])*int(appliance[i])*list3[i])/1000)
        print(list4[i])'''
    print("{} {}".format(wrking_hrs,appliance))


    
def listOfApplicances():
    prequisites.withdraw()
    prequisites1.withdraw()
    appliances.deiconify()
    label0 = tk.Label(appliances,text='Welcome to Solar System Calulator',font=('ariel',16,'bold'))
    label0.place(x=250,y=50)
    
    label1 = tk.Label(appliances,text='Fan',font=('ariel',12))
    label1.place(x=0,y=150)
    text1 = tk.Entry(appliances,textvar=fan_quantity,width=5)
    text1.place(x=80,y=150)
    text11 = tk.Entry(appliances,textvar=fan_hrs,width=5)
    text11.place(x=180,y=150)
    
    label2 = tk.Label(appliances,text='Lights',font=('ariel',12))
    label2.place(x=0,y=200)
    text2 = tk.Entry(appliances,textvar=lights_quantity,width=5)
    text2.place(x=80,y=200)
    text22 = tk.Entry(appliances,textvar=lights_hrs,width=5)
    text22.place(x=180,y=200)
    
    label3 = tk.Label(appliances,text='Bulbs',font=('ariel',12))
    label3.place(x=0,y=500)
    text3 = tk.Entry(appliances,textvar=bulbs_quantity,width=5)
    text3.place(x=80,y=500)
    text33 = tk.Entry(appliances,textvar=bulbs_hrs,width=5)
    text33.place(x=180,y=500)
    
    label4 = tk.Label(appliances,text='Television',font=('ariel',12))
    label4.place(x=0,y=250)
    text4 = tk.Entry(appliances,textvar=television_quantity,width=5)
    text4.place(x=80,y=250)
    text44 = tk.Entry(appliances,textvar=television_hrs,width=5)
    text44.place(x=180,y=250)
    
    label5 = tk.Label(appliances,text='Chimney',font=('ariel',12))
    label5.place(x=0,y=300)
    text5 = tk.Entry(appliances,textvar=chimney_quantity,width=5)
    text5.place(x=80,y=300)
    text55 = tk.Entry(appliances,textvar=chimney_hrs,width=5)
    text55.place(x=180,y=300)
    
    label6 = tk.Label(appliances,text='Blender',font=('ariel',12))
    label6.place(x=0,y=350)
    text6 = tk.Entry(appliances,textvar=blender_quantity,width=5)
    text6.place(x=80,y=350)
    text66 = tk.Entry(appliances,textvar=blender_hrs,width=5)
    text66.place(x=180,y=350)
    
    label7 = tk.Label(appliances,text='Mixture',font=('ariel',12))
    label7.place(x=0,y=400)
    text7 = tk.Entry(appliances,textvar=mixture_quantity,width=5)
    text7.place(x=80,y=400)
    text77 = tk.Entry(appliances,textvar=mixture_hrs,width=5)
    text77.place(x=180,y=400)
    
    label8 = tk.Label(appliances,text='Juicer',font=('ariel',12))
    label8.place(x=300,y=150)
    text8 = tk.Entry(appliances,textvar=juicer_quantity,width=5)
    text8.place(x=440,y=150)
    text88 = tk.Entry(appliances,textvar=juicer_hrs,width=5)
    text88.place(x=540,y=150)
    
    label9 = tk.Label(appliances,text='Refrigerator',font=('ariel',12))
    label9.place(x=300,y=200)
    text9 = tk.Entry(appliances,textvar=refrigerator_quantity,width=5)
    text9.place(x=440,y=200)
    text99 = tk.Entry(appliances,textvar=refrigerator_hrs,width=5)
    text99.place(x=540,y=200)
    
    label10 = tk.Label(appliances,text='Home Theater',font=('ariel',12))
    label10.place(x=300,y=250)
    text10 = tk.Entry(appliances,textvar=homeTheater_quantity,width=5)
    text10.place(x=440,y=250)
    text1010 = tk.Entry(appliances,textvar=homeTheater_hrs,width=5)
    text1010.place(x=540,y=250)
    
    label11 = tk.Label(appliances,text='AC',font=('ariel',12))
    label11.place(x=320,y=300)
    text11 = tk.Entry(appliances,textvar=ac_quantity,width=5)
    text11.place(x=440,y=300)
    text1111 = tk.Entry(appliances,textvar=ac_hrs,width=5)
    text1111.place(x=540,y=300)
    
    label12 = tk.Label(appliances,text='Washing Machine',font=('ariel',12))
    label12.place(x=300,y=350)
    text12 = tk.Entry(appliances,textvar=washingMachine_quantity,width=5)
    text12.place(x=440,y=350)
    text1212 = tk.Entry(appliances,textvar=washingMachine_hrs,width=5)
    text1212.place(x=540,y=350)
    
    label13 = tk.Label(appliances,text='Phones',font=('ariel',12))
    label13.place(x=300,y=400)
    text13 = tk.Entry(appliances,textvar=phones_quantity,width=5)
    text13.place(x=440,y=400)
    text1313 = tk.Entry(appliances,textvar=phones_hrs,width=5)
    text1313.place(x=540,y=400)
    
    label14 = tk.Label(appliances,text='Laptops',font=('ariel',12))
    label14.place(x=300,y=450)
    text14 = tk.Entry(appliances,textvar=laptop_quantity,width=5)
    text14.place(x=440,y=450)
    text1414 = tk.Entry(appliances,textvar=laptop_hrs,width=5)
    text1414.place(x=540,y=450)
    
    label15 = tk.Label(appliances,text='PC',font=('ariel',12))
    label15.place(x=0,y=450)
    text15 = tk.Entry(appliances,textvar=pc_quantity,width=5)
    text15.place(x=80,y=450)
    text1515 = tk.Entry(appliances,textvar=pc_hrs,width=5)
    text1515.place(x=180,y=450)
    
    label16 = tk.Label(appliances,text='Quantity',font=('ariel',14,'bold'),width=10)
    label16.place(x=40,y=100)
    
    label17 = tk.Label(appliances,text='Working-hrs',font=('ariel',14,'bold'),width=10)
    label17.place(x=150,y=100)
    
    label18 = tk.Label(appliances,text='Quantity',font=('ariel',14,'bold'),width=10)
    label18.place(x=400,y=100)
    
    label19 = tk.Label(appliances,text='Working-hrs',font=('ariel',14,'bold'),width=10)
    label19.place(x=510,y=100)
    
    next_btn = tk.Button(appliances,text='Next',width=25, command = getAppliances)
    next_btn.place(x=250,y=600)
    #appliances.mainloop()

def registration():
    window.destroy()
    prequisites.deiconify()

    
    name = user_name.get()
    try:
        if name=="":
            messagebox.showerror("Name Error"," Please enter your name")
            raise Exception("Please enter your name.")
    except Exception as e:
        print(e)
    email = user_email.get()
    try:
        if email=="":
            messagebox.showerror("mail error","Please enter email id")
            raise Exception("Please enter your email ID.")
        elif '@' not in email:
            messagebox.showerror("Invalid email","Please enter valid email id")
            raise Exception("Please enter valid email ID.")
        elif '.' not in email:
            messagebox.showerror("invalid email","Please enter valid email id")
            raise Exception("Please enter valid email ID.")
    except Exception as e:
        print(e)
        
    password = user_password.get()
    conform_pwd = user_conform.get()
    try:
        if password!=conform_pwd:
            messagebox.showerror("Password error","Please enter password again")
            password.insert('')
            conform.insert('')
            raise Exception("Please enter password again")
    except Exception as e:
        print(e)
            
    house = user_house.get()
    try:
        if house == "":
            messagebox.showerror("Dwelling Error","Please enter your house name")
            raise Exception("Please enter society name.")
    except Exception as e:
        print(e)
    society = user_society.get()
    try:
        if society=="":
            messagebox.showerror("Error","Please enter your society name")
            raise Exception("Please enter your street name.")
    except Exception as e:
            print(e)
    landmark = user_landmark.get()
    try:
        if landmark=="":
            messagebox.showerror("Landmark","Please enter a landmark")
            raise Exception("Please enter landmark.")
    except Exception as e:
        print(e)
    pincode = user_pincode.get()
    try:
        if len(str(pincode))<6 or len(str(pincode)>6):
            messagebox.showerror("Pincode Error","Please enter valid pincode")
            raise Exception("Please enter valid pincode.")
    except Exception as e:
        print(e)
    country = user_country.get()
    try:
        if country=="":
            messagebox.showerror("Country not selected","Please select a country")
            raise Exception("Please enter your country name.")
    except Exception as e:
        print(e)
    province = user_province.get()
    try:
        if province == '':
            messagebox.showerror("Province not selected","Please enter a state/province")
            raise Exception("Please eneter Province")
    except Exception as e:
        print(e)
    city = user_city.get()
    try:
        if city == "":
            messagebox.showerror("City not selected","Please select a city")
            raise Exception("Please select City")
    except Exception as e:
        print(e)
    
    command=cn.cursor()
    insertQuery = ("INSERT INTO registration VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
    record = (str(name),str(email),str(password),str(house),str(society),str(landmark),str(pincode),
              str(country),str(province),str(city))
    command.execute(insertQuery,record)
    cn.commit()
        
        
        
    label1 = tk.Label(prequisites,text='Welcome to Solar System Calulator',font=('TimesNewRoman',22,'bold'),width=35)
    label1.place(x=100,y=0)
        
    label2 = tk.Label(prequisites,text='Please follow the following instructions for better outcome of your calaulation:',
                      width=60,font=('TimesNewRoman',16,'bold'))
    label2.place(x=0,y=100)
        
    label3=tk.Label(prequisites,text='->Make a list of electrical appliances in your home.',font=('TimesNewRoman',12,'bold'),width = 38)
    label3.place(x=0,y=150)
        
    label4=tk.Label(prequisites,text='->Please give correct quantities of appliances in your home.',font=('TimesNewRoman',12,'bold'),width = 45)
    label4.place(x=0,y=194)
    
    label5=tk.Label(prequisites,text='->Please write the working hours of appliances too.',font=('TimesNewRoman',12,'bold'),width = 36)
    label5.place(x=0,y=172)
    
    label6=tk.Label(prequisites,text='->Please give correct information about area of your home.',font=('TimesNewRoman',12,'bold'),width = 44)
    label6.place(x=0,y=216)
    next_button = tk.Button(prequisites,text='Next',font=('TimesNewRoman',10,'bold'),width=15,command=listOfApplicances)
    next_button.place(x=325,y=400)
        
    #prequisites.mainloop()



def checkDetails():
    prequisites1.deiconify()
    signup_email = email.get()
    signup_pwd = password.get()
    cmd = cn.cursor()
    myQuery = ("SELECT Email,Password FROM registration")
    cmd.execute(myQuery)
    for record in command:
        if str(record[0]) == signup_email and str(record[1]) == signup_pwd:
            flag=1
            break
        else:
            continue
    if flag == 1:
        signUp.withdraw()
        label1 = tk.Label(prequisites1,text='Welcome to Solar System Calulator',font=('TimesNewRoman',22,'bold'),width=35)
        label1.place(x=100,y=0)
            
        label2 = tk.Label(prequisites1,text='Please follow the following instructions for better outcome of your calaulation:',
                          width=60,font=('TimesNewRoman',16,'bold'))
        label2.place(x=0,y=100)
            
        label3=tk.Label(prequisites1,text='->Make a list of electrical appliances in your home.',font=('TimesNewRoman',12,'bold'),width = 38)
        label3.place(x=0,y=150)
            
        label4=tk.Label(prequisites1,text='->Please give correct quantities of appliances in your home.',font=('TimesNewRoman',12,'bold'),width = 45)
        label4.place(x=0,y=194)
    
        label5=tk.Label(prequisites1,text='->Please write the working hours of appliances too.',font=('TimesNewRoman',12,'bold'),width = 36)
        label5.place(x=0,y=172)
        
        label6=tk.Label(prequisites1,text='->Please give correct information about area of your home.',font=('TimesNewRoman',12,'bold'),width = 44)
        label6.place(x=0,y=216)
        next_button = tk.Button(prequisites1,text='Next',font=('TimesNewRoman',10,'bold'),width=15,command=listOfApplicances)
        next_button.place(x=325,y=400)
def signup():
    window.withdraw()
    signUp.deiconify()
    label1 = tk.Label(signUp, text='Email ID', width = 15)
    label1.place(x=270,y=100)
    email = tk.Entry(signUp, textvar=signUp_email,width = 25)
    email.place(x=350,y=100)

    label2 = tk.Label(signUp,text = 'Password', width = 25)
    label2.place(x=240, y= 150)
    password = tk.Entry(signUp, textvar = signUp_pwd, width = 15)
    password.place(x=357,y=150)
    button1 = tk.Button(signUp,text='Log in', width = 10,font=('TimesNewRoman',10,'bold'),command= checkDetails)
    button1.place(x=350, y= 250)

label1 = tk.Label(window,text='Name:',font = ('TimesNewRoman',12,'bold'))
label1.place(x=50,y=47)
name = tk.Entry(window,textvar = user_name, width = 25)
name.place(x=110,y=51)

label2 = tk.Label(window,text='Email:',font = ('TimesNewRoman',12,'bold'))
label2.place(x=500,y=47)
email = tk.Entry(window,textvar = user_email, width = 25)
email.place(x=560,y=51)

label3 = tk.Label(window,text='Password:',font = ('TimesNewRoman',12,'bold'))
label3.place(x=20,y=100)
password = tk.Entry(window,textvar = user_password, width = 25)
password.place(x=110,y=100)

label4 = tk.Label(window,text='Conform Password:',font = ('TimesNewRoman',12,'bold'))
label4.place(x=400,y=100)
conform = tk.Entry(window,textvar = user_conform, width = 25)
conform.place(x=560,y=100)


label5 = tk.Label(window, text='House name:', font=('TimesNewRoman', 12, 'bold'))
label5.place(x=00,y=153)
house = tk.Entry(window,textvar = user_house,width = 35)
house.place(x=110,y=153)

label6 = tk.Label(window,text='Society name:', font=('TimesNewRoman', 12, 'bold'))
label6.place(x=450, y=153)
society = tk.Entry(window,textvar=user_society,width=25)
society.place(x=560, y=153)
#window.destroy()
label7 = tk.Label(window, text='Landmark:', font=('TimesNewRoman', 12, 'bold'))
label7.place(x=20,y=206)
landmark = tk.Entry(window, textvar = user_landmark,width=25)
landmark.place(x=110,y=206)

label8 = tk.Label(window, text='Pincode:', font=('TimesNewRoman', 12, 'bold'))
label8.place(x=480,y=206)
pincode=tk.Entry(window,textvar = user_pincode, width=25)
pincode.place(x=560,y=206)

label9 = tk.Label(window, text='Country:', font=('TimesNewRoman', 12, 'bold'))
label9.place(x=20,y=259)
countries = ['India','Sri-Lanka','Bhutan','America','Canada','Norway','Vietnam','Russia','Germany']
country_list = tk.OptionMenu(window,user_country,*countries)
user_country.set("Select Country")
country_list.config(width=20)
country_list.place(x=110,y=259)

label10 = tk.Label(window, text='Province:', font=('TimesNewRoman', 12, 'bold'))
label10.place(x=480,y=259)
province = ['Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat',
            'Haryana','Himachal Pradesh', 'Jharkhand','Karnataka','	Kerala','Madhya Pradesh',
            'Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan',
            'Sikkim','Tamil Nadu','Telangana','Tripura','Uttar Pradesh','Uttarakhand','	West Bengal']
province_list = tk.OptionMenu(window,user_province,*province)
user_province.set("Select State")
province_list.config(width=20)
province_list.place(x=570,y=259)


label11 = tk.Label(window, text='City:', font=('TimesNewRoman', 12, 'bold'))
label11.place(x=20,y=312)
city = ['Ahmedabad','Jamnagar','Junagadh','Kutchh','Rajkot','Surat','	Vadodara/Baroda',
            'Bhuj','Champaner', 'Chotta Udepur','Dabhoi','Dharampur','Gondal',
            'Idar','Lakhpat','Mandvi','Morbi','Patan','Porbandar','Wankaner']
city_list = tk.OptionMenu(window,user_city,*city)
user_city.set("Select City")
city_list.config(width=20)
city_list.place(x=110,y=312)

login = tk.Button(window,text = 'Sign Up', width=12, bg = 'white', fg = 'black', command = registration)
login.place(x=400,y=400)

signup = tk.Button(window, text = 'Login',width = 12, bg = 'white', fg = 'black', command = signup)
signup.place(x=300,y=400)
window.mainloop()

