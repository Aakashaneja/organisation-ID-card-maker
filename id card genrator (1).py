from PIL import  Image, ImageDraw , ImageFont
import random
import os
import datetime
import qrcode


#setting up the directories to store


image = Image.new('RGB',(1000,900),(255,255,255))
draw =ImageDraw.Draw(image)
font = ImageFont.truetype('arial.ttf', size=45)

os.system("title ID CARD generator by Nikita ")
d_date = datetime.datetime.now()
reg_format_date = d_date.strftime("%d-%m-%Y\t\t\t\t\t ID CARD generator\t\t\t\t\t %I:%M:%S %p")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(reg_format_date)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

#starting position of the message
print("\n\n All fields are mandatory")
print("avoid any kind of spelling mistakes")
print("write rverything in uppercase letters")
(x , y)=(50,50)
company =input("\n Enter your company name :")
color ='rgb(0,0,0)'
font =ImageFont.truetype('arial.ttf',size=80)
draw.text((x , y),company ,fill = color,font = font)

#adding an unique id number.we can manually take it from user
(x , y)=(600,50)
id_no = random.randint(1000000,9000000)
id_no = str('ID'+str(id_no))
color = 'rgb(0,0,0)' #black color
font= ImageFont.truetype('arial.ttf',size=60)
draw.text((x , y),id_no ,fill = color,font = font)

(x , y)=(50,160)
name = input("Enter your full name: ")
color = 'rgb(0,0,0)'
font= ImageFont.truetype('arial.ttf',size=45)
draw.text((x , y),name ,fill = color,font = font)

(x , y)=(50,250)
dob = input("enter your date of birth :")
color = 'rgb(0,0,0)'
draw.text((x , y),dob ,fill = color,font = font)

(x , y)=(50,350)
gender = input("enter your Gender :")
color = 'rgb(0,0,0)'
draw.text((x , y) , gender ,fill = color,font = font)
(x , y)=(50,450)

age = input("enter your age:")
color = 'rgb(0,0,0)'
draw.text((x , y),age ,fill = color,font = font)

(x , y)=(50,550)
blood_group = input("enter your blood group:")
color = 'rgb(0,0,0)'
draw.text((x , y),blood_group ,fill = color,font = font)

(x , y)=(50,650)
mobile_number = input("enter your mobile number :")
color = 'rgb(0,0,0)'
draw.text((x , y),mobile_number ,fill = color,font = font)

(x , y)=(50,750)
address = input("enter your address :")
color = 'rgb(0,0,0)'
draw.text((x , y),address ,fill = color,font = font)
#save the edited image

#saving an image
image.save(str(name)+'.bmp')
img = qrcode.make(str(company)+str(id_no))
img.save(str(id_no)+'.bmp')

#opening a saved image
til = Image.open(name+'.bmp')
img = Image.open(str(id_no)+'.bmp')
til.paste(img,(600,350))
til.save(name+'.bmp')
print(('\n\n\n your ID CARD Successfully created in a bmp file '+name+'.bmp' ))
