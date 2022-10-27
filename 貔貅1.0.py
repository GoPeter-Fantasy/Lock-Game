print('你将经受三只貔貅的验证，只有经受住了每只貔貅的审查，你才能取出貔貅守护之物！')


# coding:utf-8 

from PIL import ImageDraw,ImageFont,Image
import face_recognition
import cv2
import numpy as np
import os
print('第一只貔貅正在开启摄像头：')
print('第一只貔貅正在比对')
known_face_encodings = [] 
known_face_names = [] 

flist = os.listdir("我的照片") 
for f in flist:
	(fname, ext) = os.path.splitext(f)
	fpath = os.path.join("我的照片", f)
	if os.path.isfile(fpath):
		image = face_recognition.load_image_file(fpath)
		known_face_encodings.append(face_recognition.face_encodings(image)[0])
		known_face_names.append(fname)


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

def write_chinese(img, font_type, font_size,color, position, content):
	
	img_PIL = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
	font = ImageFont.truetype(font_type, font_size)
	draw = ImageDraw.Draw(img_PIL)
	draw.text(position, content, font=font, fill=color)
	
	img_OpenCV = cv2.cvtColor(np.asarray(img_PIL), cv2.COLOR_RGB2BGR)
	return img_OpenCV


video_capture = cv2.VideoCapture(0)
name='不认识'	
while name=='不认识':
	ret, frame = video_capture.read() 
	

	small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
	
	rgb_small_frame = small_frame[:, :, ::-1]

	
	if process_this_frame:
		
		face_locations = face_recognition.face_locations(rgb_small_frame)
		face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

		face_names = []
		for face_encoding in face_encodings:
			
			matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
			name = "不认识"
			face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
			best_match_index = np.argmin(face_distances)
			if matches[best_match_index]:
				name = known_face_names[best_match_index]

			face_names.append(name)

	process_this_frame = not process_this_frame

	img = frame
	
	for (top, right, bottom, left), name in zip(face_locations, face_names):
		
		top *= 4
		right *= 4
		bottom *= 4
		left *= 4

		
		cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
		
		cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
		img = write_chinese(frame,"simhei.ttf",20,(255, 255, 255), (left + 6, bottom-20-10), name)
		cv2.imshow('Video', img)

	cv2.imshow('Video', img)



video_capture.release()
cv2.destroyAllWindows()
print('比对成功，第一只貔貅放行！')
guess_password=-999
real_password=123456
count=0

for count in range(3):
    guess_password = int(input("在第二只貔貅这里报上密码:"))
    if guess_password == real_password:
        print("密码正确！第二只貔貅放行！")
        break
    else:
        if count == 2:
            print("次数用尽，第二只貔貅不允许你通过!")
            exit()
        print("密码错误,请重新输入！还剩",2-count,"次机会")


import tkinter
rt = tkinter.Tk()
rt.title('我是第三只貔貅！')
rt.geometry('300x300+200+100')
lb = tkinter.Label(rt, text='绘制圆', width=30, height=2)
lb.place(x=50, y=10)
global s1
global s2
global c1
c1 = 0
 
def xsq(a, b, c):
    global s1
    s1 = a
    global s2
    s2 = b
    global c1
    c1 = c1 + c
    if c1 == 35:
        rt.destroy()
 
def cov1():
    s1 = 35
    s2 = 35
    c = 1
    xsq(s1, s2, c)
 
def cov2():
    s3 = 150
    s4 = 35
    ln2 = cv.create_line(s1, s2, s3, s4, fill='blue', arrowshape=(20, 20, 10), width=5)
    c = 2
    xsq(s3, s4, c)
 
def cov3():
    s3 = 260
    s4 = 35
    ln3 = cv.create_line(s1, s2, s3, s4, fill='blue', arrowshape=(20, 20, 10), width=5)
    c = 3
    xsq(s3, s4, c)
 
def cov4():
    s3 = 35
    s4 = 135
    ln4 = cv.create_line(s1, s2, s3, s4, fill='blue', arrowshape=(20, 20, 10), width=5)
    c = 4
    xsq(s3, s4, c)
 
def cov5():
    s3 = 150
    s4 = 135
    ln5 = cv.create_line(s1, s2, s3, s4, fill='blue', arrowshape=(20, 20, 10), width=5)
    c = 5
    xsq(s3, s4, c)
 
def cov6():
    s3 = 260
    s4 = 135
    ln6 = cv.create_line(s1, s2, s3, s4, fill='blue', arrowshape=(20, 20, 10), width=5)
    c = 6
    xsq(s3, s4, c)
 
def cov7():
    s3 = 35
    s4 = 235
    ln7 = cv.create_line(s1, s2, s3, s4, fill='blue', arrowshape=(20, 20, 10), width=5)
    c = 7
    xsq(s3, s4, c)
 
def cov8():
    s3 = 150
    s4 = 235
    ln8 = cv.create_line(s1, s2, s3, s4, fill='blue', arrowshape=(20, 20, 10), width=5)
    c = 8
    xsq(s3, s4, c)
 
def cov9():
    s3 = 260
    s4 = 235
    ln9 = cv.create_line(s1, s2, s3, s4, fill='blue', arrowshape=(20, 20, 10), width=5)
    c = 9
    xsq(s3, s4, c)
 
cv = tkinter.Canvas(rt, bg='#cccccc', width=500, height=500)
button1 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov1)
button1.place(x=25, y=25)
button2 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov2)
button2.place(x=140, y=25)
button3 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov3)
button3.place(x=255, y=25)
button4 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov4)
button4.place(x=25, y=125)
button5 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov5)
button5.place(x=140, y=125)
button6 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov6)
button6.place(x=255, y=125)
button7 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov7)
button7.place(x=25, y=225)
button8 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov8)
button8.place(x=140, y=225)
button9 = tkinter.Button(rt, text='', bg='red', width=2, height=1, command=cov9)
button9.place(x=255, y=225)
ov1 = cv.create_oval((10, 10, 60, 60), fill='red', width=5, outline='yellow', dash=(5, 2))
ov2 = cv.create_oval((125, 10, 175, 60), fill='red', width=5, outline='yellow', dash=(5, 2))
ov3 = cv.create_oval((240, 10, 290, 60), fill='red', width=5, outline='yellow', dash=(5, 2))
ov4 = cv.create_oval((125, 110, 175, 160), fill='red', width=5, outline='yellow', dash=(5, 2))
ov5 = cv.create_oval((10, 110, 60, 160), fill='red', width=5, outline='yellow', dash=(5, 2))
ov6 = cv.create_oval((240, 110, 290, 160), fill='red', width=5, outline='yellow', dash=(5, 2))
ov7 = cv.create_oval((125, 210, 175, 260), fill='red', width=5, outline='yellow', dash=(5, 2))
ov8 = cv.create_oval((10, 210, 60, 260), fill='red', width=5, outline='yellow', dash=(5, 2))
ov9 = cv.create_oval((240, 210, 290, 260), fill='red', width=5, outline='yellow', dash=(5, 2))
def ass3():
    rt.destroy()
cv.place(x=0, y=0)
rt.mainloop()

print('你已通过三只貔貅的检验，确定为守护之物的主人！')

import math, random,time
import threading
import tkinter as tk
import re

Fireworks=[]
maxFireworks=8
height,width=600,600

class firework(object):
    def __init__(self,color,speed,width,height):
       
        self.radius=random.randint(2,4)  
        self.color=color   
        self.speed=speed  
        self.status=0   
        self.nParticle=random.randint(20,30) 
        self.center=[random.randint(0,width-1),random.randint(0,height-1)]   
        self.oneParticle=[]    
        self.rotTheta=random.uniform(0,2*math.pi) 

        

        self.ellipsePara=[random.randint(30,40),random.randint(20,30)]   
        theta=2*math.pi/self.nParticle
        for i in range(self.nParticle):
            t=random.uniform(-1.0/16,1.0/16)  
            x,y=self.ellipsePara[0]*math.cos(theta*i+t), self.ellipsePara[1]*math.sin(theta*i+t)    
            xx,yy=x*math.cos(self.rotTheta)-y*math.sin(self.rotTheta),  y*math.cos(self.rotTheta)+x*math.sin(self.rotTheta)     
            self.oneParticle.append([xx,yy])
        
        self.curParticle=self.oneParticle[0:]    
        self.thread=threading.Thread(target=self.extend)  
        

    def extend(self):         
        for i in range(100):
            self.status+=1    
            self.curParticle=[[one[0]*self.status/100, one[1]*self.status/100] for one in self.oneParticle]   
            time.sleep(self.speed/50)
    
    def explode(self):
        self.thread.setDaemon(True)   
        self.thread.start()          
            

    def __repr__(self):
        return ('color:{color}\n'  
                'speed:{speed}\n'
                'number of particle: {np}\n'
                'center:[{cx} , {cy}]\n'
                'ellipse:a={ea} , b={eb}\n'
                'particle:\n{p}\n'
                ).format(color=self.color,speed=self.speed,np=self.nParticle,cx=self.center[0],cy=self.center[1],p=str(self.oneParticle),ea=self.ellipsePara[0],eb=self.ellipsePara[1])


def colorChange(fire):
    rgb=re.findall(r'(.{2})',fire.color[1:])
    cs=fire.status
    
    f=lambda x,c: hex(int(int(x,16)*(100-c)/30))[2:]   
    if cs>70:
        ccr,ccg,ccb=f(rgb[0],cs),f(rgb[1],cs),f(rgb[2],cs)
    else:
        ccr,ccg,ccb=rgb[0],rgb[1],rgb[2]
        
    return '#{0:0>2}{1:0>2}{2:0>2}'.format(ccr,ccg,ccb)



def appendFirework(n=1):   
    if n>maxFireworks or len(Fireworks)>maxFireworks:
        pass
    elif n==1:
        cl='#{0:0>6}'.format(hex(int(random.randint(0,16777215)))[2:])   
        a=firework(cl,random.uniform(1.5,3.5),width,height)
        Fireworks.append( {'particle':a,'points':[]} )  
        a.explode()
    else:
        appendFirework()
        appendFirework(n-1)


def show(c):
    for p in Fireworks:               
        for pp in p['points']:
            c.delete(pp)
    
    for p in Fireworks:               
        oneP=p['particle']
        if oneP.status==100:        
            Fireworks.remove(p)     
            appendFirework()          
            continue
        else:
            li=[[int(cp[0]*2)+oneP.center[0],int(cp[1]*2)+oneP.center[1]] for cp in oneP.curParticle]      
            color=colorChange(oneP)  
            for pp in li:
                p['points'].append(c.create_oval(pp[0]-oneP.radius,  pp[1]-oneP.radius,  pp[0]+oneP.radius,  pp[1]+oneP.radius,  fill=color))  

    root.after(50, show,c)  

if __name__=='__main__':
    appendFirework(maxFireworks)
    
    root = tk.Tk()
    root.title('貔貅守护之物')
    cv = tk.Canvas(root, height=height, width=width)
    cv.create_rectangle(0, 0, width, height, fill="black")

    cv.pack()

    root.after(50, show,cv)
    root.mainloop()


