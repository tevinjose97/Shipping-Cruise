import getpass
import os
import pickle
import time


id=0
x=0
m=0
class passengers:
    
    def __init__(self):
        self.name=None
        self.mobile_no=None
        self.email=None
        self.username=None
        self.password=None
        self.pass_t_id=[]
        self.b_no=[]
        self.t_bill=[]
        self.t_ref=[]
        self.money=0
        self.security_ques=None
        self.security_pas=None
       
    def storedata(self):
        print '-------------------------------Customer Details-------------------------------'
        self.name=raw_input('Enter Your Name- ')
        stat=0
        self.mobile_no=raw_input('Enter Your Mobile Number- ')
        while stat==0:
            if len(self.mobile_no)!=10:
                print 'Inavlid Mobile Number'
                self.mobile_no=raw_input('Please Enter Valid Mobile Number- ')
            else:
                stat=1
        self.email=raw_input('Enter Your Email ID- ')
        pos=0
        while pos==0:
            c_a=0
            c_dot=0
            for ch in self.email:
                if ch=='@':
                    c_a=c_a+1
                elif ch=='.':
                    c_dot=c_dot+1
            if '@' in self.email and '.' in self.email and c_a==1 and c_dot==1:
                mail=list(self.email.split('@'))
                ma=mail[1].split('.')

                if len(mail[0])>=1 and len(ma[0])>=1 and len(ma[1])>=2:
                    pos=1
                else:
                    print 'Invalid Email ID'
                    self.email=raw_input('Please Enter a Valid Email ID- ')
                
            else:
                print 'Invalid Email ID'
                self.email=raw_input('Please Enter a Valid Email ID- ')
                
        self.money=input('Enter An Amount To Be Stored In The Account [>3000]- ')
        status=0
        while status==0:
            if self.money<3000:
                print 'Minimum Amount Not Met'
                self.money=input('Please Enter A Valid Amount [>3000]- ')
            elif self.money>100000:
                print 'Amount Too Large To Store'
                self.money=input('Please Enter A Valid Amount [>3000]- ')
            else:
                status=1
        print 

    def display_pas(self):
        print '-------------------------------Customer Details-------------------------------'
        print
        print 'Customer Name : '+self.name
        print 'Customer Mobile : '+self.mobile_no
        print 'Customer Email : '+self.email
        print 'Account Balance :  '+str(self.money)+'$'
        print
        print '-------------------------------------------------------------------------------------'

def forgot_password():

    status=0
    while status==0:        
        username=raw_input('Enter Username- ')
        f=open("passenger.dat","rb")
        p=passengers()
        st=1
        try:            
            while True:
                
                p= pickle.load(f)
                if p.username==username:
                    status=1
                    st=0
                    print
                    ans=raw_input(p.security_ques+'- ')
                    print
                    if ans.lower()==p.security_pas.lower():
                        print 'Password : '+p.password
                        print
                    else:
                        print 'Wrong Answer'
                        print                        
                    break
                       
        except EOFError:
            f.close()
            
        if status==0 and st==1:
            os.system('cls')
            print '\nIncorrect Username'
            print'--------------------Choose The Following--------------------'
            print '1)Retry Username'
            print '2)Exit To Main Menu'
            print
            c=input('Enter Your Choice (Number)- ')
            
            if c==1:
                pass
            elif c==2:
                break
            else:
                print 'Invalid Entry'
  
                
def security():
    status=0
    while status==0:
        print 'Pick Your Security Question'
        print
        print '----------------------------Security Questions----------------------------'
        print '1)What is the last name of the teacher who gave you your first failing grade?'
        print '2)What is the name of your first pet?'
        print '3)What is the name of the first beach you visited?'
        print '4)What was your favorite place to visit as a child?'
        print '5)What was the make and model of your first car?'
        print '6)What was your maternal grandfather\'s first name?'
        print '7)In what city or town does your nearest sibling live?'
        print '8)Any Other (Custom)'
        print
        c=input('Enter Your Choice (Number)- ')
        if c==1:
            security_ques='What is the last name of the teacher who gave you your first failing grade?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            status=1
            os.system('cls')
        elif c==2:
            security_ques='What is the name of your first pet?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            status=1
            os.system('cls')
        elif c==3:
            security_ques='What is the name of the first beach you visited?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            status=1
            os.system('cls')
        elif c==4:
            security_ques='What was your favorite place to visit as a child?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            status=1
            os.system('cls')
        elif c==5:
            security_ques='What was the make and model of your first car?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            status=1
            os.system('cls')
        elif c==6:
            security_ques='What was your maternal grandfather\'s first name?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            status=1
            os.system('cls')
        elif c==7:
            security_ques='In what city or town does your nearest sibling live?'
            print
            security_pas=raw_input('Enter Answer For The Security Question- ')
            status=1
            os.system('cls')
        elif c==8:
            security_ques=raw_input('Enter A Question Of Your Choice (Without \'?\')- ')
            print
            security_ques=security_ques+'?'
            security_pas=raw_input('Enter The Answer For The Security Question- ')
            status=1
            os.system('cls')
        else:
            os.system('cls')
            print 'Invalid Entry'
        print

    return ([security_ques,security_pas])
        
def pas_t_id(user):
    global id 
    global x
    f=open('passenger.dat','rb')
    s=passengers()
    status=0
    i=1
    while status==0:
        s=pickle.load(f)
        x=0
        if s.username==user:
            if s.pass_t_id==[]:
                x=1
                print '\nYou Do Not Have Any Bookings\n'
                break
            for j in range(len(s.pass_t_id)):
                id=s.pass_t_id[j]
                f1=open('trip_details.dat','rb')
                try:
                    while True:
                        sh= pickle.load(f1)
                        if sh.trip_id==id:
                            print 'Booking '+str(i)
                            i=i+1
                            sh.display()
                                       
                except EOFError:
                    f1.close()        

            status=1

        else:
            status=0
    f.close()        
    
def change_password(user,pas):

    stat=0
    
    while stat==0:
        print
        password=raw_input('Enter Old Password- ')                
        if password==pas:
            stat=1
            new_pass=raw_input('Enter New Password- ')
            sta=0
            while sta==0:
                confirm_pass=raw_input('Re-Enter (Confirm) Your New Password- ')                
                if confirm_pass==new_pass:
                    sta=1
                    print '\nYour New Password Is Confirmed\n'

                else:
                    print '\nYour New Password Is Not Confirmed\n'
                    sta=0
            
        else:
            print '\nThe Password You Gave Was Incorrect'
            stat=0
    
    f1=open("passenger.dat","rb")
    f2=open("newfile.dat","wb")
    s=passengers()

    try:
        while True:
            s= pickle.load(f1)
            if s.username==user:
                s.password=new_pass
            pickle.dump(s,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove("passenger.dat")
    os.rename("newfile.dat","passenger.dat")
    
def edit_pas(user):
    
    f1=open("passenger.dat","rb")
    f2=open("newfile.dat","wb")
    s=passengers()

    try:
        while True:
            s= pickle.load(f1)
            if s.username==user:
                print '-----------------------------------Edit Details-----------------------------------'
                print '1)Customer Name\n2)Customer Mobile\n3)Customer Email\n4)Account Balance\n5)All Details'
                print
                ch=input('Enter Your Choice (Number)- ')
                os.system('cls')
                if ch==1:
                    s.name=raw_input('Enter New Name- ')
                elif ch==2:
                    stat=0
                    s.mobile_no=raw_input('Enter New Mobile Number- ')
                    while stat==0:
                        if len(s.mobile_no)!=10:
                            print 'Inavlid Mobile Number'
                            s.mobile_no=raw_input('Enter New Mobile Number- ')
                        else:
                            stat=1
                elif ch==3:
                    s.email=raw_input('Enter New Email- ')
                    pos=0
                    c_a=0
                    c_dot=0
                    for ch in s.email:
                        if ch=='@':
                            c_a=c_a+1
                        elif ch=='.':
                            c_dot=c_dot+1
                            
                    if '@' in s.email and '.' in s.email and c_a==1 and c_dot==1:                        
                        mail=list(s.email.split('@'))
                        ma=mail[1].split('.')
                        if len(mail[0])>=1 and len(ma[0])>=1 and len(ma[1])>=2:
                            pos=1                                                   
                        else:
                            print 'Invalid Email ID'
                            s.email=raw_input('Please Enter Valid Email ID- ')
                    else:
                        print 'Invalid Email ID'
                        s.email=raw_input('Please Enter Valid Email ID- ')
                        
                elif ch==4:
                    status=0
                    s.money=input('Enter An Amount To Be Stored In The Account [>3000]- ')
                    while status==0:
                        if s.money<3000:
                            print 'Minimum Amount Not Met'
                            s.money=input('Enter An Amount To Be Stored In The Account [>3000]- ')
                        elif s.money>100000:
                            print 'Amount Too Large To Store'
                            s.money=input('Enter An Amount To Be Stored In The Account [>3000]- ')
                        else:
                            status=1
                elif ch==5:
                    s.storedata()
                    
                else:
                    print 'Invalid Entry'
                    
            pickle.dump(s,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove("passenger.dat")
    os.rename("newfile.dat","passenger.dat")
    
def disp_pas():
    f=open('passenger.dat','rb')
    s=passengers()
    try:
        i=1
        while True:
            s= pickle.load(f)
            print 'Customer '+str(i)
            s.display_pas()
            i=i+1
            
    except EOFError:
        f.close()  

def del_pass():
    pos=0
    while pos==0:
        f=open('passenger.dat','rb')
        i=1
        try:
            while True:
                s= pickle.load(f)
                print 'Customer '+str(i)
                s.display_pas()
                i=i+1
            
        except EOFError:
            f.close()        
        print
        n=i
        c=input('Enter Your Choice (Number)- ')
        
        if c in range(1,n):
            f=open('passenger.dat','rb')

            i=1
            while i<c:
                s=pickle.load(f)
                i=i+1        
            s=pickle.load(f)
            user=s.username
            f.close()
    
            f1=open("passenger.dat","rb")
            f2=open("newfile.dat","wb")
    
            try:
                while True:
                    s= pickle.load(f1)
                    if s.username!=user:
                        pickle.dump(s,f2)
      
            except EOFError:
                f1.close()
                f2.close()
            os.remove("passenger.dat")
            os.rename("newfile.dat","passenger.dat")
            print
            print 'User Account Deleted\n'
            pos=1
            
        else:
            print 'Invalid Entry'

def disp_pass(user):

    f=open('passenger.dat','rb')  
    status=0
    while status==0:
        s=pickle.load(f)
        if s.username==user:
            s.display_pas()
            status=1

    f.close()
    
def sign_in():
    print '----------------------------------Login----------------------------------'
    x=0
    username='sfdag'
    password='sdg'
    pos=0
    status=0
    while status==0:
        
        username=raw_input('Enter Username- ')
        f=open("passenger.dat","rb")
        p=passengers()
        st=1
        try:            
            while True:
                p= pickle.load(f)
                if p.username==username:
                    status=1
                    stat=0
                    while stat==0:
                        password=getpass.getpass('Enter Password:')
                        if p.password==password:
                            os.system('cls')
                            print
                            print 'You Are Signed In- '
                            print p.name
                            print
                            stat=1
                            st=0
                            status=1                                                    
                        else:
                            stat=0
                            os.system('cls')
                            print '\nIncorrect Password'
                            print '--------------------Choose The Following--------------------'
                            print '1)Change Username'
                            print '2)Retry Password'
                            print '3)Exit And Return To Main Menu'
                            print
                            c=input('Enter Your Choice (Number)- ')
                            if c==1:
                                stat=1
                                status=0
                                st=0
                            elif c==2:
                                stat=0
                            elif c==3:
                                stat=1
                                status=0
                                st=0
                                x=1                           
                            else:
                                print 'Invalid Entry'
                    if stat==1:
                        break
                else:
                    status=0
                        
        except EOFError:
            f.close()
        if x==1:
            pos=1
            break
        if status==0 and st==1:
            os.system('cls')
            print '\nIncorrect Username'
            print'--------------------Choose The Following--------------------'
            print '1)Retry Username'
            print '2)Exit To Main Menu'
            print
            c=input('Enter Your Choice (Number)- ')
            if c==1:
                pass
            elif c==2:
                pos=1
                break
            else:
                print 'Invalid Entry'

    return([username,password,pos])


def sign_up():
    
    print '----------------------------Login Details----------------------------'
    status=1
    while status==1:
        username=raw_input('Create A Username- ')
        f=open("passenger.dat","rb")
        p=passengers()
        
        try:            
            while True:
                p= pickle.load(f)
                if p.username==username:
                    os.system('cls')
                    print 'Username Is Taken'
                    status=1
                    break
                else:
                    status=0
                    
        except EOFError:
            f.close()
        
    password=raw_input('Create (Enter) A Password- ')
    stat=0
    
    while stat==0:
        confirm_pass=raw_input('Re-Enter (Confirm) Your Password- ')                
        if confirm_pass==password:
            os.system('cls')
            stat=1
            print '\nYour Password Is Confirmed'
            print 'Account Created'
            print 'Username : '+username
            print 'Password : '+password
            print
            
        else:
            stat=0
            print '\nPassword Not Confirmed\n'

    return([username,password])

def add_member(user,pas):
    
    f=open("passenger.dat","ab")    
    p=passengers()
    secure=list(security())
    p.security_ques=secure[0]
    p.security_pas=secure[1]
    p.storedata()
    p.username=user
    p.password=pas
    pickle.dump(p,f)
    f.close()
    
class trip_details:

    def __init__(self):
        self.admin_user='royalcruise'
        self.admin_pass='royal123'
        self.date=None
        self.trip_id=None
        self.ship_name=None
        self.from_l=None
        self.to_l=None
        self.facilities=[]
        self.len_cruise=0
        self.t_std_rooms=80
        self.t_clb_rooms=50
        self.t_sui_rooms=30
        self.a_std_rooms=80
        self.a_clb_rooms=50
        self.a_sui_rooms=30
        self.f_pass=0
        self.f_std=0
        self.f_clb=0
        self.f_sui=0

    def input_data(self):
        self.ship_name=raw_input('Enter Ship Name- ')
        self.date=raw_input('Enter Date Of Trip (DD\MM\YY)- ')
        self.from_l=raw_input('Enter Departure Location- ')
        self.to_l=raw_input('Enter Destination- ')
        self.facilities=[raw_input('Enter Facility 1- '),raw_input('Enter Facility 2- ')]
        self.len_cruise=input('Enter Number Of Days- ')
        self.t_std_rooms=input('Enter Number Of Standard Rooms- ')
        self.t_clb_rooms=input('Enter Number Of Club Rooms- ')
        self.t_sui_rooms=input('Enter Number Of Suite Rooms- ')
        self.f_pass=input('Enter Admission Fee Per Passenger- ')
        self.f_std=input('Enter Fare Per Standard Room- ')
        self.f_clb=input('Enter Fare Per Club Room- ')
        self.f_sui=input('Enter Fare Per Suite Room- ')
        self.trip_id=self.date[0]+self.date[1]+self.date[3]+self.ship_name+self.date[4]+self.date[6]+self.date[7]
        self.a_std_rooms=self.t_std_rooms
        self.a_clb_rooms=self.t_clb_rooms
        self.a_sui_rooms=self.t_sui_rooms        

    def display(self):
        
        print '-------------------------------Ship Details-------------------------------'
        print
        print 'ID :',self.trip_id
        print 'Ship Name :',self.ship_name
        print 'Date Of Trip :',self.date
        print 'Departure Location :',self.from_l
        print 'Destination :',self.to_l
        print 'Facilities :'+self.facilities[0]+','+self.facilities[1]
        print 'Number Of Days :',self.len_cruise
        print 'Total Number Of Standard Rooms :',self.t_std_rooms
        print 'Total Number Of Club Rooms :',self.t_clb_rooms
        print 'Total Number Of Suite Rooms :',self.t_sui_rooms
        print 'Number Of Available Standard Rooms :',self.a_std_rooms
        print 'Number Of Available Club Rooms :',self.a_clb_rooms
        print 'Number Of Available Suite Rooms :',self.a_sui_rooms
        print 'Admission Fee Per Passenger : '+str(self.f_pass)+'$'
        print 'Fare Per Standard Room : '+str(self.f_std)+'$'
        print 'Fare Per Club Room : '+str(self.f_clb)+'$'
        print 'Fare Per Suite Room : '+str(self.f_sui)+'$'
        print
        print'--------------------------------------------------------------------------'

def create_ship():
    
    f=open("trip_details.dat","wb")    
    n=input("Enter Number Of Ships (To Be Created)- ")
    s=trip_details()
    for i in range(n):
        s.input_data()
        pickle.dump(s,f)
    f.close()


def add_ship():
    
    f=open("trip_details.dat","ab")    
    n=input("Enter Number Of Ships (To Be Added)- ")
    s=trip_details()
    for i in range(n):
        print 'Ship '+str(i+1)
        print '--------------------------------------------------------------------------'
        s.input_data()
        pickle.dump(s,f)
    f.close()
    print '\n'

def display_ship():
    
    f=open('trip_details.dat','rb')
    i=1
    try:
        while True:
            s= pickle.load(f)
            print 'Ship '+str(i)
            s.display()
            i=i+1
            
    except EOFError:
        f.close()        

    
def del_ship():
    global id 

    display_ship() 
    f=open('trip_details.dat','rb')
    print
    c=input('Enter Your Choice (Number)- ')
    os.system('cls')
    i=1
    while i<c:
        s=pickle.load(f)
        i=i+1        
    s=pickle.load(f)
    id=s.trip_id
    f.close()
    
    f1=open("trip_details.dat","rb")
    f2=open("newfile.dat","wb")
    
    try:
        while True:
            s= pickle.load(f1)
            if s.trip_id!=id:
                pickle.dump(s,f2)
      
    except EOFError:
        f1.close()
        f2.close()
    os.remove("trip_details.dat")
    os.rename("newfile.dat","trip_details.dat")

def edit_ship():
    
    global id
    display_ship()
    f=open("trip_details.dat","rb")
    s=trip_details()
    cou=0
    try:
        while True:
            s=pickle.load(f)
            cou=cou+1
    except EOFError:
        f.close()

    f=open('trip_details.dat','rb')
    print
    c=input('Enter Your Choice (Number)- ')    
    while c in (range(1,(cou+1))):
        os.system('cls')
        i=1
        while i<c:
            s=pickle.load(f)
            i=i+1        
        s=pickle.load(f)
        id=s.trip_id
        f.close()
        f1=open("trip_details.dat","rb")
        f2=open("newfile.dat","wb")
        s=trip_details()
        try:
            while True:
                s= pickle.load(f1)
                if s.trip_id==id:
                    s.input_data() 
                pickle.dump(s,f2)
            
        except EOFError:
            f1.close()
            f2.close()
        os.remove("trip_details.dat")
        os.rename("newfile.dat","trip_details.dat")

    else:
        print 'Invalid Entry'

def book_room(user):
    global id
    
    no_passengers=input('Enter Number Of Passengers [Children < 3yrs :Free Admission]- ')
    b_std=raw_input('Enter Number Of Standard Rooms To Be Booked- ')
    if b_std=='0' or b_std=='':
        b_std=0
    else:
        b_std=int(b_std)
    b_clb=raw_input('Enter Number Of Club Rooms To Be Booked- ')
    if b_clb=='0' or b_clb=='':
        b_clb=0
    else:
        b_clb=int(b_clb)
    b_sui=raw_input('Enter Number Of Suite Rooms To Be Booked- ')
    if b_sui=='0' or b_sui=='':
        b_sui=0
    else:
        b_sui=int(b_sui)
    receipt(b_std,b_clb,b_sui,no_passengers,user)
    ch=raw_input('Do You Want To Confirm Booking (y/n)- ')
    os.system('cls')    
    if ch.lower()=='y':
        t_bil=t_bill(b_std,b_clb,b_sui,no_passengers,user)
        t_reff=t_ref(b_std,b_clb,b_sui,user)
        chk=check_amnt(t_bil,user)
        if chk==0:
            print '\nInsufficient Amount'
            print '\nBooking Not Confirmed\n'
        elif chk==1:
            update_rooms(b_std,b_clb,b_sui)
            update_b_no(b_std,b_clb,b_sui,user)
            update_t_bill(t_bil,t_reff,user)
            update_pass_t_id(user)
            print '\nBooking Confirmed\n'
            
    else:
        print '\nBooking Not Confirmed\n'

def check_amnt(t_bill,user):
    f=open("passenger.dat","rb")
    s=passengers()
    try:
        while True:
            s= pickle.load(f)
            if s.username==user:
                if s.money<t_bill:
                    return (0)
                else:
                    return (1)
            
    except EOFError:
        f.close()
def t_bill(b_std,b_clb,b_sui,no_passengers,user):
    global id 
    f=open('passenger.dat','rb')
    s=passengers()
    status=0
    while status==0:
        s=pickle.load(f)
        if s.username==user:
            f1=open('trip_details.dat','rb')
            try:
                while True:
                    sh= pickle.load(f1)
                    if sh.trip_id==id:
                        t_bill=sh.f_pass*no_passengers+b_std*sh.f_std+b_clb*sh.f_clb+b_sui*sh.f_sui
                        return (t_bill)
            except EOFError:
                    f1.close()        
            status=1

        else:
            status=0
    f.close()
    
def t_ref(b_std,b_clb,b_sui,user):
    global id 
    f=open('passenger.dat','rb')
    s=passengers()
    status=0
    while status==0:
        s=pickle.load(f)
        if s.username==user:
            f1=open('trip_details.dat','rb')
            try:
                while True:
                    sh= pickle.load(f1)
                    if sh.trip_id==id:
                        t_ref=b_std*sh.f_std+b_clb*sh.f_clb+b_sui*sh.f_sui
                        return (t_ref)
            except EOFError:
                    f1.close()        
            status=1

        else:
            status=0
    f.close()
    
def receipt(b_std,b_clb,b_sui,no_passengers,user):
    os.system('cls')
    lcltime = time.asctime( time.localtime(time.time()) )
    global id 
    f=open('passenger.dat','rb')
    s=passengers()
    status=0
    while status==0:
        s=pickle.load(f)
        if s.username==user:
            f1=open('trip_details.dat','rb')
            try:
                while True:
                    sh= pickle.load(f1)
                    if sh.trip_id==id:
                        t_bill=sh.f_pass*no_passengers+b_std*sh.f_std+b_clb*sh.f_clb+b_sui*sh.f_sui
                        print '\n                        Royal Cruises Enterprises LTD'
                        print '----------------------------------RECEIPT-----------------------------------'
                        print '\t   Customer Name: '+s.name+'\t         '+lcltime
                        print '\t   Ship Name : '+sh.ship_name
                        print '\t   Departure Location : '+sh.from_l
                        print '\t   Destination : '+sh.to_l
                        print '\t   Date Of Departure : '+sh.date
                        print '\t   Number Of Standard Rooms : '+str(b_std)
                        print '\t   Number Of Club Rooms : '+str(b_clb)
                        print '\t   Number Of Suite Rooms : '+str(b_sui)
                        print '\t   '+str(no_passengers)+'x'+str(sh.f_pass)+'='+str(sh.f_pass*no_passengers)+'$'
                        print '\t   '+str(b_std)+'x'+str(sh.f_std)+'='+str(b_std*sh.f_std)+'$'
                        print '\t   '+str(b_clb)+'x'+str(sh.f_clb)+'='+str(b_clb*sh.f_clb)+'$'
                        print '\t   '+str(b_sui)+'x'+str(sh.f_sui)+'='+str(b_sui*sh.f_sui)+'$'
                        print '-----------------------------------------------------------------------------'
                        print '\t   TOTAL : '+str(t_bill)+'$'
                        print '-----------------------------------------------------------------------------'                        
            
            except EOFError:
                    f1.close()        
            status=1

        else:
            status=0
    f.close()

def update_rooms(b_std,b_clb,b_sui):
    global id    
    f1=open("trip_details.dat","rb")
    f2=open("newfile.dat","wb")
    s=trip_details()

    try:
        while True:
            s= pickle.load(f1)
            if s.trip_id==id:
                s.a_std_rooms=s.t_std_rooms-b_std 
                s.a_clb_rooms=s.t_clb_rooms-b_clb
                s.a_sui_rooms=s.t_sui_rooms-b_sui  
            pickle.dump(s,f2)
    except EOFError:
        f1.close()
        f2.close()
    os.remove("trip_details.dat")
    os.rename("newfile.dat","trip_details.dat")

def update_b_no(b_std,b_clb,b_sui,user):
    f1=open("passenger.dat","rb")
    f2=open("newfile.dat","wb")
    s=passengers()
    try:
        while True:
            s= pickle.load(f1)
            if s.username==user:
                s.b_no=s.b_no+list([[b_std,b_clb,b_sui]])

            pickle.dump(s,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove("passenger.dat")
    os.rename("newfile.dat","passenger.dat")

def update_t_bill(t_bill,t_reff,user):
    f1=open("passenger.dat","rb")
    f2=open("newfile.dat","wb")
    s=passengers()
    try:
        while True:
            s= pickle.load(f1)
            if s.username==user:
                s.t_bill=s.t_bill+list([t_bill])
                s.t_ref=s.t_ref+list([t_reff])
                s.money=s.money-t_bill
            pickle.dump(s,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove("passenger.dat")
    os.rename("newfile.dat","passenger.dat")

def update_pass_t_id(user):
    global id
    f1=open("passenger.dat","rb")
    f2=open("newfile.dat","wb")
    s=passengers()

    try:
        while True:
            s= pickle.load(f1)
            if s.username==user:
                s.pass_t_id=s.pass_t_id+list([id])
            pickle.dump(s,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove("passenger.dat")
    os.rename("newfile.dat","passenger.dat")
    
def find_ship_facilities():
    global id
    pos=0
    while pos==0:
        f=open("trip_details.dat","rb")
        print '------------------------Facilities------------------------'
        try:
            i=1
            while True:
                s= pickle.load(f)
                print str(i)+')'+s.facilities[0]+','+s.facilities[1]
                i=i+1
                
        except EOFError:
            f.close()
        n=i
        c=input('Enter Your Choice (Number)- ')
        os.system('cls')
        if c in range(1,n):
            f=open("trip_details.dat","rb")
            print
            i=1
            while i<c:
                s=pickle.load(f)
                i=i+1
            s=pickle.load(f)
            print    
            print 'Your Ship Is '+s.ship_name
            id=s.trip_id
            s.display()
            f.close()
            pos=1
        else:
            print 'Invalid Entry'
            pos=0


def find_ship_date():
    global id
    pos=0
    while pos==0:
        f=open("trip_details.dat","rb")
        print '---------------------------Dates---------------------------'
        try:
            i=1
            while True:
                s= pickle.load(f)
                print str(i)+')'+s.date
                i=i+1
                
        except EOFError:
            f.close()
        n=i
        c=input('Enter Your Choice (Number)- ')
        os.system('cls')
        if c in range(1,n):
            f=open("trip_details.dat","rb")
            print
            i=1
            while i<c:
                s=pickle.load(f)
                i=i+1
            s=pickle.load(f)
            print    
            print 'Your Ship Is '+s.ship_name
            id=s.trip_id
            s.display()
            f.close()
            pos=1

        else:
            print 'Invalid Entry'
            pos=0

def find_ship_len():
    global id
    pos=0
    while pos==0:
        f=open("trip_details.dat","rb")
        print '---------------------------Length Of Cruise---------------------------'
        try:
            i=1
            while True:
                s= pickle.load(f)
                print str(i)+')'+str(s.len_cruise)+' Days'
                i=i+1
                
        except EOFError:
            f.close()
        n=i
        c=input('Enter Your Choice (Number)- ')
        os.system('cls')
        if c in range(1,n):
            f=open("trip_details.dat","rb")
            print
            i=1
            while i<c:
                s=pickle.load(f)
                i=i+1
            s=pickle.load(f)
            print    
            print 'Your Ship Is '+s.ship_name
            id=s.trip_id
            s.display()
            f.close()
            pos=1

        else:
            print 'Invalid Entry'
            pos=0
def find_ship_destination():
    global id
    pos=0
    while pos==0:
        f=open("trip_details.dat","rb")
        print '---------------------------Destination---------------------------'
        try:
            i=1
            while True:
                s= pickle.load(f)
                print str(i)+')'+s.to_l
                i=i+1
                
        except EOFError:
            f.close()
        n=i
        c=input('Enter Your Choice (Number)- ')
        os.system('cls')
        if c in range(1,n):
            f=open("trip_details.dat","rb")
            print
            i=1
            while i<c:
                s=pickle.load(f)
                i=i+1
            s=pickle.load(f)
            print    
            print 'Your Ship Is '+s.ship_name
            id=s.trip_id
            s.display()
            f.close()
            pos=1

        else:
            print 'Invalid Entry'
            pos=0
            
def find_ship(user):
    global m
    m=1
    while m==1:
        print '--------------------------------Find Your Ship--------------------------------'
        print '1)Destination\n2)Facilities\n3)Dates\n4)Length Of Cruise'
        print
        ch=input('Enter Your Choice (Number)- ')
        os.system('cls')
        m=0
        if ch==1:
            find_ship_destination()
        elif ch==2:
            find_ship_facilities()
        elif ch==3:
            find_ship_date()
        elif ch==4:
            find_ship_len()
        else:
            print 'Invalid Entry'
            m=1
    

def reset_ship():
    print '---------------------------------Reset Ship---------------------------------'
    print '1)Reset Any One Ship'
    print '2)Reset All Ships'
    print
    ch=input('Enter Your Choice (Number)- ')
    os.system('cls')
    if ch==1:
        display_ship()
        f=open('trip_details.dat','rb')
        c=input('Enter Your Choice (Number)- ')
        os.system('cls')
        i=1
        while i<c:
            s=pickle.load(f)
            i=i+1        
        s=pickle.load(f)
        id=s.trip_id
        f.close()
        f1=open("trip_details.dat","rb")
        f2=open("newfile.dat","wb")
        s=trip_details()
        try:
            while True:
                s= pickle.load(f1)
                if s.trip_id==id:
                    s.a_std_rooms=s.t_std_rooms
                    s.a_clb_rooms=s.t_clb_rooms
                    s.a_sui_rooms=s.t_sui_rooms
                pickle.dump(s,f2)
            
        except EOFError:
            f1.close()
            f2.close()
        os.remove("trip_details.dat")
        os.rename("newfile.dat","trip_details.dat")
        print '\nShip'+str(c)+' Has Been Reseted\n'
    elif ch==2:
        f1=open("trip_details.dat","rb")
        f2=open("newfile.dat","wb")
        s=trip_details()
        try:
            while True:
                s= pickle.load(f1)
                s.a_std_rooms=s.t_std_rooms
                s.a_clb_rooms=s.t_clb_rooms
                s.a_sui_rooms=s.t_sui_rooms
                pickle.dump(s,f2)
            
        except EOFError:
            f1.close()
            f2.close()
        os.remove("trip_details.dat")
        os.rename("newfile.dat","trip_details.dat")
        print '\nAll Ships Have Been Reseted\n'
        
    else:
        print 'Invalid Entry'
        
def cancel_trip(user):
    global id 
    global x
    pos=0
    while pos==0:     
        print '-----------------------------Cancel Trip-----------------------------'
        
        pas_t_id(user)
        if x==0:
            f=open('passenger.dat','rb')
            print '\nNote : Admission Fee Will Not Be Refunded'
            print        
            try:
                while True:
                    s= pickle.load(f)
                    if s.username==user:
                        b_no=list(s.b_no)                    
            except EOFError:
                    f.close()
            n=len(b_no)+1               
            c=input('Enter Your Choice (Number)- ')
            if c in range(1,n):
                pos=1
                os.system('cls')

                f1=open("trip_details.dat","rb")
                f2=open("newfile.dat","wb")
    
                try:
                    while True:
                        s= pickle.load(f1)
                        if s.trip_id==id:
                            s.a_std_rooms=s.a_std_rooms+b_no[c-1][0]
                            s.a_clb_rooms=s.a_clb_rooms+b_no[c-1][1]
                            s.a_sui_rooms=s.a_sui_rooms+b_no[c-1][2]
                        pickle.dump(s,f2)
      
                except EOFError:
                    f1.close()
                    f2.close()
                os.remove("trip_details.dat")
                os.rename("newfile.dat","trip_details.dat")
    
                f1=open("passenger.dat","rb")
                f2=open("newfile.dat","wb")
                s=passengers()

                try:
                    while True:
                        s= pickle.load(f1)
                        if s.username==user:
                            del s.pass_t_id[(c-1)]
                            del s.b_no[c-1]
                            s.money=s.money+s.t_ref[c-1]
                            del s.t_ref[c-1]
                        pickle.dump(s,f2)
            
                except EOFError:
                    f1.close()
                    f2.close()
                os.remove("passenger.dat")
                os.rename("newfile.dat","passenger.dat")
                print '\nYour Trip Has Been Cancelled'
                print '\nYour Money Is Restored\n'
            else:
                print 'Invalid Entry'
                
def update_money(user):

    f1=open("passenger.dat","rb")
    f2=open("newfile.dat","wb")
    s=passengers()

    try:
        while True:
            s= pickle.load(f1)
            if s.username==user:
                status=0
                while status==0:
                    if s.money<3000:
                        print 'Account Balance Is Getting Low'
                        s.money=input('Enter An Amount To Be Stored In The Account [>3000]- ')
                    elif s.money>100000:
                        print 'Amount Is Too Large To Store'
                        s.money=input('Enter An Amount To Be Stored In The Account [>3000]- ')
                    else:
                        status=1

            pickle.dump(s,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove("passenger.dat")
    os.rename("newfile.dat","passenger.dat")

def check_ship(user):
    global id
    f1=open("passenger.dat","rb")
    f2=open("newfile.dat","wb")
    s=passengers()

    try:
        while True:
            s= pickle.load(f1)
            if s.username==user:
                if id in s.pass_t_id:
                    return(1)
                else:
                    return(0)
            pickle.dump(s,f2)
            
    except EOFError:
        f1.close()
        f2.close()
    os.remove("passenger.dat")
    os.rename("newfile.dat","passenger.dat")


def main():
    global m

    t='y'
    while t.lower()=='y':
        
        print '--------------------Welcome To Royal Cruises Enterprises LTD--------------------'
        print '1)Login (Existing Account)'
        print '2)Create New Account'
        print '3)Forgot Password?'
        print '4)Administrative Login'
        print '5)Exit'
        print
        choice=input('Enter Your Choice (Number)- ')
        os.system('cls')
    
        if choice==1:
            account=list(sign_in())
            if account[2]==0:
                stat=0
                user=account[0]
                pas=account[1]
                while stat==0:
                    print '--------------------------------User Account--------------------------------'
                    print '1)Find Ship and Book Room'
                    print '2)View Passenger Bookings'
                    print '3)Cancel Passenger Bookings'
                    print '4)View Passenger Details'
                    print '5)Edit Passenger Details'
                    print '6)Change Password'
                    print '7)Change Security Question'
                    print '8)Logout and Return To Main Menu'
                    stat=1                
                    print
                    ch=input('Enter Your Choice (Number)- ')
                    os.system('cls')
                    if ch==1:
                        find_ship(user)
                        chk=check_ship(user)
                        if chk==1:
                            print '\nThis Ship Is Already Booked\n'
                            stat=0
                        
                        else:
                            if m==0:                    
                                book_room(user)
                                stat=0
                    elif ch==2:
                        print '-----------------------------------------------------------------------------------'            
                        pas_t_id(user)
                        stat=0
                    elif ch==3:
                        cancel_trip(user)
                        stat=0
                    elif ch==4:
                        disp_pass(user)
                        stat=0
                    elif ch==5:
                        edit_pas(user)
                        stat=0
                    elif ch==6:
                        change_password(user,pas)
                        sta=1
                    elif ch==7:
                        f1=open("passenger.dat","rb")
                        f2=open("newfile.dat","wb")
                        s=passengers()
                        secure=list(security())
                        try:
                            while True:
                                s= pickle.load(f1)
                                if s.username==user:
                                    s.security_ques=secure[0]
                                    s.security_pas=secure[1]
                                pickle.dump(s,f2)
            
                        except EOFError:
                            f1.close()
                            f2.close()
                        os.remove("passenger.dat")
                        os.rename("newfile.dat","passenger.dat")
                        stat=0

                    elif ch==8:
                        sta=1
                    else:
                        print 'Invalid Entry'
                        stat=0
                    update_money(user)

            
        elif choice==2:

            account=sign_up()
            user=account[0]
            pas=account[1]
            os.system('cls')
            add_member(user,pas)
           
        elif choice==3:
            forgot_password()
            
        elif choice==4:
            print '-----------------------------Admin Login-----------------------------'
            status=0
            x=0
            while status==0:
                user=raw_input('Enter Admin Username- ')
                if user=='royalcruise':
                    status=1
                    stat=0                    
                    while stat==0:
                        pas=getpass.getpass('Enter Admin Password:')
                        if pas=='royal123':
                            os.system('cls')
                            print '\nWelcome Administrator\n'
                            stat=1
                        else:
                            os.system('cls')
                            print '\nIncorrect Password'
                            print'--------------------Choose The Following--------------------'
                            print '1)Retry Password'
                            print '2)Exit And Return To Main Menu'
                            print
                            c=input('Enter Your Choice (Number)- ')
                            if c==1:
                                stat=0
                            elif c==2:
                                stat=1
                                status=0
                                x=1                           
                            else:
                                print 'Invalid Entry'

                else:
                    status=0
                    os.system('cls')
                    print '\nIncorrect Username'
                    print'--------------------Choose The Following--------------------'
                    print '1)Retry Username'
                    print '2)Exit To Main Menu'
                    print
                    c=input('Enter Your Choice (Number)- ')
            
                    if c==1:
                        pass
                    elif c==2:
                        break
                    else:
                        print 'Invalid Entry'
                if x==1:
                    break

            if status==1:
                statu=1
                while statu==1:
                    print '-----------------------Administrative Features-----------------------'
                    print '1)Display Ship\n2)Create Ship\n3)Edit Ship\n4)Delete Ship\n5)Reset Ship Rooms\n6)Display User Accounts\n7)Delete User Account\n8)Logout And Return To Main Menu'
                    print
                    c=input('Enter Your Choice (Number)- ')
                    os.system('cls')
                    if c==1:
                        print '--------------------------------------------------------------------------'
                        display_ship()
                    elif c==2:
                        add_ship()
                    elif c==3:
                        edit_ship()
                    elif c==4:
                        del_ship()
                    elif c==5:
                        reset_ship()
                    elif c==6:
                        disp_pas()
                    elif c==7:
                        del_pass()
                    elif c==8:
                        statu=0
                    else:
                        print 'Invalid Entry'
                        statu=1
            
        elif choice==5:
            exit()
    if sta==1:
         t='y'
main()
