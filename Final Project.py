#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Separately send mail using their mail


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 


#The mail addresses and  password
sender_address ='noerardixxx@gmail.com'                  
sender_pass ='xxxxx'                                       

# list of reciver email_id to the mail 
li = ['salamahxxx@gmail.com','saintekxxxx@gmail.com','indonesia@gmail.com']                                                         
#[item for item in input("Enter Receiver Mail Address :- ").split()] this is used to take user input of receiver mail id


# getting length of list 
length = len(li) 
  
# Iterating the index 
# same as 'for i in range(len(list))' 

# Here we iterate the loop and send msg one by one to the reciver
for i in range(length): 
   
   X = li[i]
   reciver_mail = X
   
   print(reciver_mail)
   
   message = MIMEMultipart()
   message['From'] = sender_address
   message['To'] =  reciver_mail                            #  Pass Reciver Mail Address
   message['Subject'] =  'Final Project Indonesia.ai'       #The subject line
    

   mail_content = '''Sorry ganggu guys, ini lagi coba-coba kirim multiple email pakai pyhton. Buat final project indonesia.ai'''

   
   #The body and the attachments for the mail
   message.attach(MIMEText(mail_content, 'plain'))

   s = smtplib.SMTP('smtp.gmail.com', 587) 
   s.starttls() 
   s.login(sender_address, sender_pass) 
   text = message.as_string()
   s.sendmail(sender_address, reciver_mail, text) 
   s.quit() 

   print('Mail Sent')


# In[ ]:




