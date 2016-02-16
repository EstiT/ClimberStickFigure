#Collier, R. "Lectures Notes for COMP1405B – Introduction to Computer Science I" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).

#Stephenson, B. "Tutorial 1: Drawing with the SimpleGraphics Library" [PDF document].
#Retrieved from cuLearn: https://www.carleton.ca/culearn/ (Fall 2015).


#get x  and y co-ordinates
x=float(input("I'm going to draw you a picture, please type a number 1-250 to decide how far to the right it should be: "))
y=float(input("Now please type a number 1-100 to decide how far down it should be: "))


from SimpleGraphics import *

background("white")#set background colour
setFill("medium violet red") #Hold colour
blob(520+x,340+y,380+x,350+y,300+x,200+y,390+x,180+y,400+x,280+y,510+x,240+y) #Draw hold
setFont("Bold","50")#text format
text(250+x,35+y,"Clip Art Climbs High!")#title text
setOutline("black")

setFill("light blue")#set colour of right foot hold
blob(400+x, 440+y, 420+x, 420+y, 450+x, 450+y, 500+x, 480+y, 440+x, 490+y, 360+x, 450+y) #right foot Hold
setFill("pink")#set colour of left foot hold
blob(100+x, 490+y, 150+x, 400+y, 160+x, 380+y, 180+x, 400+y, 199+x, 390+y,200+x,460+y) #left foot Hold
setFill("dark orchid")#set colour of right hand hold
blob(250+x, 55+y, 240+x,85+y,210+x,95+y,260+x,100+y,270+x,95+y) #right hand Hold
setFill("brown2")#set colour of left hand hold
blob(130+x,140+y,160+x,120+y,180+x,160+y,160+x,180+y,150+x,200+y) #left hand Hold
setFill("light slate blue");blob(30+x,240+y,110+x,220+y,130+x,280+y,110+x,280+y,10+x,240+y) #Hold
setFill("lawn green");blob(300+x,400+y,360+x,380+y,230+x,380+y,240+x,410+y,340+x,440+y) #Hold

setFill("black")#set colour of climber
ellipse(190+x,110+y,60,60) #head
ellipse(200+x,175+y,100,100) #chest
polygon(199.5+x,226+y,230+x,350+y,330+x,325+y,297+x,210+y)#body
curve(203+x, 225+y, 200+x, 230+y, 100+x, 220+y, 115+x, 130+y, 160+x, 150+y) #left arm
curve(203+x, 226+y, 200+x, 231+y, 100+x, 221+y, 115+x, 131+y, 160+x, 151+y) #left arm2
ellipse(150+x,140+y,20 ,20) #left Hand
curve(295+x, 206+y, 365+x, 100+y, 250+x, 70+y, 250+x, 60+y) #rightarm
curve(295+x, 207+y, 365+x, 101+y, 250+x, 71+y, 250+x, 61+y) #rightarm2
ellipse(240+x,60+y,20,20)#right hand
curve(225+x,330+y,140+x,260+y,180+x,450+y)#left leg
curve(225+x,331+y,140+x,261+y,180+x,451+y)#left leg2
line(180+x,450+y,150+x,430+y)#left foot
line(180+x,451+y,150+x,431+y)#left foot2
curve(325+x,315+y,410+x,340+y,400+x,460+y)#right leg
curve(325+x,316+y,410+x,341+y,400+x,461+y)#right leg
line(400+x,460+y,430+x,438+y)#right foot
line(400+x,461+y,430+x,439+y)#right foot2
setOutline("white");curve(197+x,160+y,207+x,165+y,218+x,155+y)#smile1
curve(196+x,159+y,207+x,165+y,218+x,154+y);curve(195+x,158+y,207+x,165+y,218+x,153+y);curve(194+x,157+y,207+x,165+y,218+x,152+y)#smile2,3,4
setFill("white");ellipse(200+x,130+y,10,10)#eye
setFill("Black");setOutline("black");ellipse(180+x,120+y,10,10)#another eye
polygon(185+x,142+y,183+x,147+y,191+x,149+y,192+x,144+y)#nose
setWidth(5);setOutline("gold");line(252+x,114+y,258+x,102+y)#lines to show stick figure is trying hard
line(258+x,128+y,268+x,122+y)#lines to show stick figure is trying hard
line(261+x,140+y,274+x,142+y)#lines to show stick figure is trying hard


setWidth(1);setOutline("light sea green")#set width of outline and colour of chalk bag
curve(217+x,300+y,210+x,320+y,300+x,320+y,324+x,300+y)#chalk bag strap
curve(217+x,301+y,210+x,321+y,300+x,321+y,324+x,301+y)#chalk bag strap2
curve(217+x,302+y,210+x,322+y,300+x,322+y,324+x,302+y)#chalk bag strap3
setFill("light sea green");setOutline("black");ellipse(270+x,310+y,40,40)#chalkbag
setOutline("light sea green");rect(270+x,320+y,40,10); #chalk bag
setOutline("black");setFill("light sea green");ellipse(270+x,310+y,40,20)#chalk bag




