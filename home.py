from tkinter import*
import time
import os ,random,sys
import re

#below is the function to change from and forget previous frame to new frame
def buttonClick():
	f1.pack_forget()
	f2.pack()

root=Tk()
root.title("Image Identification Captcha V.1 ")
root.wm_iconbitmap('icc.ico') #Test case icon
root.geometry("1920x766+0+0")

#frame1
f1=Frame(root,height='766',width='1920',bg='#FF6F00',cursor='arrow')
f1.propagate(0)
f1.pack()

#Canvas 1 for writing text associaated with frame1
canvas1=Canvas(f1,bg='grey',height=100,width=900,cursor='arrow')
canvas1.pack()
c1=canvas1.create_text(500,50,text="Image Identification Captcha V.1",font=('Times',40,'italic underline'))

# i have used label below inside which time is being shown
timeon=time.asctime(time.localtime(time.time()))
label1=Label(f1,text=timeon,bg='#EEEEEE',fg='red',font=('Arial',18,'bold'),bd=6,relief=RAISED)
label1.pack(side=TOP)
#++++++++++++++++++++++++++++++++++++++++background image
bgimg=PhotoImage(file='backg.gif',width=1800)
Piclabel=Label(f1,image=bgimg)
Piclabel.pack()
#Piclabel.place(x=)

#Start button is defined below
b=Button(f1,text='Start Image Identification Captcha',width='70',relief=RAISED,bd=7,height='2',command=buttonClick)
b.place(x=510,y=450)
#Exit Button is defined below
exit=Button(f1,text='Exit',width='10',height='2',relief=RAISED,bd=7,command=quit)
exit.place(x=700,y=505)
#+++++++++++++++++++++++++++++++++++++++++++++++++++Next Frame++++++++++++++++++++++++++++++++++++++++++++++++++++++
f2=Frame(root,height='766',width='1920',bg='#EEEEEE',cursor='arrow')
f2.propagate(0)
f2.pack()
#Menu bar is defined here
menubar=Menu(root)
root.config(menu=menubar)
filemenu=Menu(root,tearoff=0)
filemenu.add_command(label='About Us')

#separating File and Exit into two submenu
menubar.add_cascade(label='File',menu=filemenu)
exitmenu=Menu(root,tearoff=0)
exitmenu.add_command(label='Exit',command=root.destroy)
menubar.add_cascade(label='Exit',menu=exitmenu)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++
#Defining inside frame which is being used for placing of checkbox 
insideFrame=Frame(f2,height=604,width=614)
insideFrame.pack()
insideFrame.place(x=400,y=70)

#defining verifyframe inside which two button reset and verify is placed
verifyFrame=Frame(f2,height=42,width=614,bg='#888888')
verifyFrame.pack()
verifyFrame.place(x=400,y=680)
#defining DescLabel for displaying the task that user has to perform 
DescLabel=Label(f2,height=2,width=60,text='',bd=7,bg='#90CAF9',font=('Arial',12,'bold'))
DescLabel.pack()
DescLabel.place(x=400,y=18)

#creating a option list which have name of task string and random function will be used later to select one from it
option=['Traffic Light','House','Store','Dog','Car','Bus','Cat']
#defining str1 to avoid runtime conflict
str1=""
#defining boolean variable and integer variable for associating with checkbox
v1,v2,v7,v4,v5,v6,v7,v8,v9=True,True,True,True,True,True,True,True,True
x1,x2,x3,x4,x5,x6,x7,x8,x9=0,0,0,0,0,0,0,0,0
inside=0
#defining Click() function for all major operation
def click():
	#random option will be choose
	randomval=random.choice(option)
	str1="Click on the picture of "+randomval #giving user a task 
	DescLabel['text']=str1 #inserting str1 into text attribute of descLabel
	#below image is being choosen randomnly 
	pic1=random.choice(os.listdir("image/"))
	photo1=PhotoImage(file="image/"+pic1)
	pic2=random.choice(os.listdir("image/"))
	photo2=PhotoImage(file="image/"+pic2)
	pic3=random.choice(os.listdir("image/"))
	photo3=PhotoImage(file="image/"+pic3)
	pic4=random.choice(os.listdir("image/"))
	photo4=PhotoImage(file="image/"+pic4)
	pic5=random.choice(os.listdir("image/"))
	photo5=PhotoImage(file="image/"+pic5)
	pic6=random.choice(os.listdir("image/"))
	photo6=PhotoImage(file="image/"+pic6)
	pic7=random.choice(os.listdir("image/"))
	photo7=PhotoImage(file="image/"+pic7)
	pic8=random.choice(os.listdir("image/"))
	photo8=PhotoImage(file="image/"+pic8)
	pic9=random.choice(os.listdir("image/"))
	photo9=PhotoImage(file="image/"+pic9)

	#below defining storevalue function which extract checkbox status value using get() function and store them in variable x1 to x9 for 9 images
	def storevalue(num):
		print('in')
		global inside
		inside=inside+1
		#definig global variable in order to change value at later stage of execution
		global x1,x2,x3,x4,x5,x6,x7,x8,x9
		global v1,v2,v7,v4,v5,v6,v7,v8,v9
		t1=t2=t7=t4=t5=t6=t7=t8=t9=0

		#using Regex method and compile a regex expression and storing it in variable strc which can be used in re.match() arguments.
		strc=re.compile(r"("+randomval+".....)")

		#for image 1 and checkbutton 1
		if num==1:
			print(num)
			x1=x1+1
			if re.match(strc,pic1) and x1%2!=0: #Regex expression is being match ,that is task given and image value is being match to check result
				v1=True	
				img1['relief']='sunken'
				print(x1)			#if Regex is match and result true is passed
			elif re.match(strc,pic1)!=True and x1%2==0:
				v1=True			#if regex doesnot match then false is return
				img1['relief']='raised'
				print("elif",x1,v1)
				print(x1)
			else:
				v1=False
				img1['relief']='sunken'
				print("else",x1,v1)

		if re.match(strc,pic1) and x1==0:
			v1=False	
			print("1st",x1,v1)		

		#for image 2 and checkbutton 2
		if num==2:
			x2=x2+1
			print(num)
			if re.match(strc,pic2) and x2%2!=0: 
				v2=True	
				img2['relief']='sunken'
				print(x2)			
			elif re.match(strc,pic2)!=True and x2%2==0:
				v2=True		
				img2['relief']='raised'	
				print("elif",v2)
				print(x2)
			else:
				v2=False
				img2['relief']='sunken'
				print("else",v2)
				
		if re.match(strc,pic2) and x2==0:
			v2=False	
			print("2st",v2)	

		#for image 7 and checkbutton 7
		
		if num==3:
			print(num)
			x3=x3+1
			if re.match(strc,pic3) and x3%2!=0: 
				v3=True	
				img3['relief']='sunken'
				print(x3)			
			elif re.match(strc,pic3)!=True and x3%2==0:
				v3=True
				img3['relief']='raised'			
				print("elif",v3)
				print(x3)
			else:
				v3=False
				img3['relief']='sunken'
				print("else",v3)
				
		if re.match(strc,pic3) and x3==0:
			v3=False	
			print("3st",v3)	

		#for image 4 and checkbutton 4
	
		if num==4:
			print(num)
			x4=x4+1
			if re.match(strc,pic4) and x4%2!=0: 
				v4=True	
				img4['relief']='sunken'
				print(x4)			
			elif re.match(strc,pic4)!=True and x4%2==0:
				v4=True	
				img4['relief']='raised'		
				print("elif",v4)
				print(x4)
			else:
				v4=False
				img4['relief']='sunken'
				print("else",v4)
				
		if re.match(strc,pic4) and x4==0:
			v4=False	
			print("4st",v4)	
		#for image 5 and checkbutton 5
		if num==5:
			print(num)
			x5=x5+1
			if re.match(strc,pic5) and x5%2!=0: 
				v5=True	
				img5['relief']='sunken'
				print(x5)			
			elif re.match(strc,pic5)!=True and x5%2==0:
				v5=True	
				img5['relief']='raised'		
				print("elif",v5)
				print(x5)
			else:
				v5=False
				img5['relief']='sunken'
				print("else",v5)
				
		if re.match(strc,pic5) and x5==0:
			v5=False	
			print("5st",v5)	


		#for image 6 and checkbutton 6
		
		if num==6:
			print(num)
			x6=x6+1
			if re.match(strc,pic6) and x6%2!=0: 
				v6=True	
				img6['relief']='sunken'
				print(x6)			
			elif re.match(strc,pic6)!=True and x6%2==0:
				v6=True
				img6['relief']='raised'		
				print("elif",v6)
				print(x6)
			else:
				v6=False
				img6['relief']='sunken'
				print("else",v6)
				
		if re.match(strc,pic6) and x6==0:
			v6=False	
			print("6st",v6)	
		#for image 7 and checkbutton 7
		
		if num==7:
			print(num)
			x7=x7+1
			if re.match(strc,pic7) and x7%2!=0: 
				v7=True	
				img7['relief']='sunken'
				print(x7)			
			elif re.match(strc,pic7)!=True and x7%2==0:
				v7=True
				img7['relief']='raised'			
				print("elif",v7)
				print(x7)
			else:
				v7=False
				img7['relief']='sunken'
				print("else",v7)
				
		if re.match(strc,pic7) and x7==0:
			v7=False	
			print("7st",v7)	


		#for image 8 and checkbutton 8
		
		if num==8:
			print(num)
			x8=x8+1
			if re.match(strc,pic8) and x8%2!=0: 
				v8=True	
				img8['relief']='sunken'
				print(x8)			
			elif re.match(strc,pic8)!=True and x8%2==0:
				v8=True	
				img8['relief']='raised'		
				print("elif",v8)
				print(x8)
			else:
				v8=False
				img8['relief']='sunken'
				print("else",v8)
				
		if re.match(strc,pic8) and x8==0:
			v8=False	
			print("8st",v8)	

		#for image 9 and checkbutton 9
		if num==9:
			print(num)
			x9=x9+1
			if re.match(strc,pic9) and x9%2!=0: 
				v9=True	
				img9['relief']='sunken'
				print(x9)			
			elif re.match(strc,pic9)!=True and x9%2==0:
				v9=True
				img9['relief']='raised'			
				print("elif",v9)
				print(x9)
			else:
				v9=False
				img9['relief']='sunken'
				print("else",v9)
				
		if re.match(strc,pic9) and x9==0:
			v9=False	
			print("9st",v9)	

	#Below veifyfun() is defined to check that given images those are checked are matching with task or not
	def verifyfun():
		#For Debugging 
		print(v1,v2,v7,v4,v5,v6,v7,v8,v9)
		#print(x1,x2,x7,x4,x5,x6,x7,x8,x9)

		#if all the images that are checked and task are matching then success
		if (v1==True and v2==True and v7==True and v4==True and v5==True and v6==True and v7==True and v8==True and v9==True) and (inside!=0):
			doneframe=Frame(root,height=766,width=1920,bg='#FFF9C4')
			doneframe.propagate(0)
			f2.pack_forget()
			doneframe.pack()
			verlabel=Label(doneframe,height=7,width=50,text="Verification Successfull",fg='black',font=('Adobe Fangsong Std R',20,'italic'))
			verlabel.pack()
			verlabel.place(x=400,y=400)

		else:
			print('Error')#if checked images and task doesnot match then not sucess and even in task given and images checked are matched (nextline)
			errorframe=Frame(root,height=766,width=1920,bg='#FFF9C4')#but there are some images which user doesdnot click but are matched with  task then varify is not success
			errorframe.propagate(0)
			f2.pack_forget()
			errorframe.pack()
			errlabel=Label(errorframe,height=7,width=50,text="Verification Unsuccessfull",fg='black',font=('Adobe Fangsong Std R',20,'italic'))
			errlabel.pack()
			errlabel.place(x=400,y=400)	
	#checkbutton are defined below
	img1=Button(insideFrame,image=photo1,height=200,width=200,relief=RAISED,bd=7,fg='red',command=lambda:storevalue(1))
	img1.image=photo1
	img1.pack()
	img1.place(x=0,y=0)

	img2=Button(insideFrame,image=photo2,height=200,width=200,relief=RAISED,bd=7,command=lambda:storevalue(2))
	img2.image=photo2
	img2.pack()
	img2.place(x=200,y=0)

	img3=Button(insideFrame,image=photo3,height=200,width=200,relief=RAISED,bd=7,command=lambda:storevalue(3))
	img3.image=photo3
	img3.pack()
	img3.place(x=400,y=0)

	img4=Button(insideFrame,image=photo4,height=200,width=200,relief=RAISED,bd=7,command=lambda:storevalue(4))
	img4.image=photo4
	img4.pack()
	img4.place(x=0,y=200)

	img5=Button(insideFrame,image=photo5,height=200,width=200,relief=RAISED,bd=7,command=lambda:storevalue(5))
	img5.image=photo5
	img5.pack()
	img5.place(x=200,y=200)

	img6=Button(insideFrame,image=photo6,height=200,width=200,relief=RAISED,bd=7,command=lambda:storevalue(6))
	img6.image=photo6
	img6.pack()
	img6.place(x=400,y=200)

	img7=Button(insideFrame,image=photo7,height=200,width=200,relief=RAISED,bd=4,command=lambda:storevalue(7))
	img7.image=photo7
	img7.pack()
	img7.place(x=0,y=400)

	img8=Button(insideFrame,image=photo8,height=200,width=200,relief=RAISED,bd=7,command=lambda:storevalue(8))
	img8.image=photo8
	img8.pack()
	img8.place(x=200,y=400)

	img9=Button(insideFrame,image=photo9,height=200,width=200,relief=RAISED,bd=7,command=lambda:storevalue(9))
	img9.image=photo9
	img9.pack()
	img9.place(x=400,y=400)

	#verify button is defined below
	verify=Button(verifyFrame,text='Verify',relief=RAISED,bd=7,command=verifyfun)
	verify.pack()
	verify.place(x=550,y=4)
#reset button is defined below
Reset=Button(verifyFrame,text='Reset',relief=RAISED,bd=7,command=click)
Reset.pack()
Reset.place(x=10,y=4)
#calling click() for displaying of images and checkbutton and major operation
click()

root.mainloop()