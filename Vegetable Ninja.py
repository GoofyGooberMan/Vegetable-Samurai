from cmu_graphics import *
Start = Label(0,-100,-100)
app.stepsPerSecond=50
app.steps=0
app.stepHeight = 250

#BackGround
GroupBackground=Group(
    Rect(0,0,400,400,fill=rgb(139, 69, 19)),
    Rect(0,0,15,400,fill=rgb(109, 50, 19)),
    Rect(25,0,25,400,fill=rgb(109, 50, 19)),
    Rect(60,0,25,400,fill=rgb(109, 50, 19)),
    Rect(95,0,25,400,fill=rgb(109, 50, 19)),
    Rect(130,0,25,400,fill=rgb(109, 50, 19)),
    Rect(165,0,25,400,fill=rgb(109, 50, 19)),
    Rect(200,0,25,400,fill=rgb(109, 50, 19)),
    Rect(235,0,25,400,fill=rgb(109, 50, 19)),
    Rect(270,0,25,400,fill=rgb(109, 50, 19)),
    Rect(305,0,25,400,fill=rgb(109, 50, 19)),
    Rect(340,0,25,400,fill=rgb(109, 50, 19)),
    Rect(375,0,25,400,fill=rgb(109, 50, 19)))
#Title
TitleandLogo=Group(
    Label('Vegetable Samurai!',200,100,size=43, font='arial',bold=True,fill=gradient('Red','Orange',"Yellow","Green","Blue",'hotPink',start='left')),
    Label('Press Space To Start',200,300,size=25, font='arial',bold=True,fill=gradient('Red','Orange',"Yellow","Green","Blue",'hotPink',start='left')),
    Star(90,192,30.5,9,fill='green',border='black'),
    Polygon(98,165,72,222,259,207,98,165,fill='orangeRed',border='black'),
    #katana
    Polygon(313,289,329,278,321,220,305,239, fill='Red',border='black'),
    Oval(311,228,40,20,fill='orange',border='black'),
    Polygon(317,224,291,116,280,131,303,231,320,228,fill='grey',border='black'),
    Polygon(311,230,285,125,280,131,303,231,fill='silver',border='black'),
    Star(313,244,5,4,fill='orange'),
    Star(315,254,5,4,fill='orange'),
    Star(317,264,5,4,fill='orange'),
    Star(319,274,5,4,fill='orange'),
    Line(93,218,115,170),
    Line(122,218,132,173),
    Line(149,215,162,184),
    Line(180,213,179,186),
    Line(210,209,212,195),
    Line(180,213,179,186),
    Line(210,209,212,195),
    Line(98,165,72,222),
    Line(72,222,100,219)
    
    )
TitleandLogo.visible=True
#MouseKatana
MouseBlade=Polygon(273,273,248,227,254,209,283,273,fill='white',border='black')
MouseHandle=Polygon(292,312,274,279,283,270,300,302,border='black')
MouseHilt=Oval(277,273,25,15,fill=rgb(184, 134, 11),border='black')
MouseKatana=Group(
    MouseHandle,
    MouseHilt,
    MouseBlade,
    Star(282,282,5,4,fill='white'),
    Star(287,290,5,4,fill='white'),
    Star(292,298,5,4,fill='white'))

MouseKatana.visible=False

    

#TitleAnimation
TitleAnimation=Group(
    Label('Vegetable Samurai!',200,100,size=43, font='arial',bold=True,fill=gradient('Red','Orange',"Yellow","Green","Blue",'hotPink',start='left')),
    Star(90,192,30.5,9,fill='green',border='black'),
    Polygon(98,165,72,222,149,215,162,185,fill='orangeRed',border='black'),
    Polygon(192,182,179,215,299,207,fill='orangeRed', border='black'),
    Oval(150,199,31,37,fill='orangeRed',border='black'),
    Polygon(192,147,166,196,155,270,184,196,fill="white",opacity=100),
    Line(93,218,115,170),
    Line(122,218,132,176),
    Line(200,213,198,184),
    Line(240,209,244,193),
    Line(98,165,72,222),
    Line(72,222,100,219),
    Line(200,213,179,215),
    Line(192,182,179,215),
    #Katana
    Polygon(313-260,289+70,329-260,278+70,321-260,220+70,305-260,239+70, fill='Red',border='black'),
    Oval(311-260,228+70,40,20,fill='orange',border='black'),
    Polygon(317-260,224+70,291-260,116+70,280-260,131+70,303-260,231+70,320-260,228+70,fill='grey',border='black'),
    Polygon(311-260,230+70,285-260,125+70,280-260,131+70,303-260,231+70,fill='silver',border='black'),
    Star(313-260,244+70,5,4,fill='orange'),
    Star(315-260,254+70,5,4,fill='orange'),
    Star(317-260,264+70,5,4,fill='orange',),
    Star(319-260,274+70,5,4,fill='orange',)
    )
#vegetables
#Tomato/GameOver (Its a Fruit not a vegetable)
Tomato=Group(Star(52,63,30,6,fill='green',border='black'),
    Circle(53,81,30,border='black',fill=gradient('red','crimson')),
    Line(39,67,64,93),
    Line(39,93,64,67))
#Pickle +10 points
Pickle=Group(
    Oval(172,79,90,40,border='black',fill=gradient('oliveDrab','olive')),
    Circle(143,71,2),
    Circle(155,83,2),
    Circle(191,79,2),
    Circle(170,72,2),
    Circle(195,69,2))
#Brocoli
Brocoli=Group(
    Rect(290,58,20,50,border='black',fill=gradient('white','green',start='bottom')),
    Circle(274,53,15,border='black',fill='green'),
    Circle(288,55,10,border='black',fill='green'),
    Circle(301,43,15,border='black',fill='green'),
    Circle(315,54,15,border='black',fill='green'),
    Circle(326,45,15,border='black',fill='green'),
    Circle(279,33,12,fill='green',border='black'))
#Cauliflower
Cauliflower=Group(
    Rect(290,58+90,20,50,border='black',fill='lightGoldenrodYellow'),
    Circle(274,53+90,15,border='black',fill='lightGoldenrodYellow'),
    Circle(288,55+90,10,border='black',fill='lightGoldenrodYellow'),
    Circle(301,43+90,15,border='black',fill='lightGoldenrodYellow'),
    Circle(315,54+90,15,border='black',fill='lightGoldenrodYellow'),
    Circle(326,45+90,15,border='black',fill='lightGoldenrodYellow'),
    Circle(279,33+90,12,fill='lightGoldenrodYellow',border='black'))
#Olive
Olive=Group(
    Oval(169,149,40,30,fill='oliveDrab',border='black'),
    Circle(182,147,5,fill='red',border='black'))
#Cabbage
Cabbage=Group(
    Circle(50,160,30,border='black',fill='limeGreen'),
    Oval(25,160,30,60,border='black',fill='darkgreen'),
    Oval(75,160,30,60,border='black',fill='darkgreen'),
    Oval(50,180,60,30,border='black',fill='darkgreen'),
    Line(39,133,44,165),
    Line(47,131,50,165),
    Line(55,131,55,165))
Cabbage.visible=False
Olive.visible=False
Cauliflower.visible=False
Brocoli.visible=False
Pickle.visible=False
Tomato.visible=False
#Counter
FakeCounter=Label(150,0,0,visible=False)
Timer=Label(150,62,45,size=16,font='arial',bold=True,fill=gradient('Red','Orange',"Yellow","Green","Blue",'hotPink',start='left'))
score=Label(0,62,60,size=16,font='arial',bold=True,fill=gradient('Red','Orange',"Yellow","Green","Blue",'hotPink',start='left'))
Lives=Label(3,339,43,size=16,font='arial',bold=True,fill='red')   
Timer.visible=False
score.visible=False
TitleAnimation.visible=False
if Timer.value==0:
    gameover()
if Lives.value==0:
    gameover()
#Functions

def gameover():
        Rect(80, 80, 240, 150, fill='Orange')
        Label('Game Over!', 200, 120, size=30)
        Label('Score: ' + str(score.value) + ' Points', 200, 200, size=20)
        app.stop()
        
def onMousePress(mouseX,mouseY):
    if(Pickle.contains(mouseX,mouseY)==True):
        if Pickle.visible==True:
            Pickle.visible=False
            score.value+=10
    if(Brocoli.contains(mouseX,mouseY)==True):
        if Brocoli.visible==True:
            Brocoli.visible=False
            score.value+=15
    if(Cauliflower.contains(mouseX,mouseY)==True):
        if Cauliflower.visible==True:
            Cauliflower.visible=False
            score.value+=15
    if(Olive.contains(mouseX,mouseY)==True):
        if Olive.visible==True:
            Olive.visible=False
            score.value+=150
    if(Cabbage.contains(mouseX,mouseY)==True):
        if Cabbage.visible==True:
            Cabbage.visible=False
            score.value+=10
    if(Tomato.contains(mouseX,mouseY)==True):
        if Tomato.visible==True:
            Tomato.visible=False
            Lives.value-=1
def onKeyPress(key):
    if key == 'space' and Start.value==0:
        TitleandLogo.visible=False
        TitleAnimation.visible=True
        Start.value = 1
       
def onKeyRelease(key):
     TitleAnimation.visible=False
     if Start.value==1:
        Cabbage.visible=True
        Olive.visible=True
        Cauliflower.visible=True
        Brocoli.visible=True
        Pickle.visible=True
        Tomato.visible=True
        Timer.visible=True
        score.visible=True
        MouseKatana.visible=True
       
        
    
def onStep():
    FakeCounter.value -= 1/60
    Timer.value = int(FakeCounter.value)
    if Timer.value==0:
        gameover()
    if Lives.value==0:
        gameover()
    if Tomato.centerY>410:
        makeTomato()
    if Pickle.centerY>410:
        makePickle()
    if Brocoli.centerY>410:
        makeBrocoli()
    if Olive.centerY>410:
        makeOlive()
    if Cauliflower.centerY>410:
        makeCauliflower()
    if Cabbage.centerY>410:
        makeCabbage()
    
    #Vegetables Fall
    if Tomato.centerY<450:
        Tomato.centerY+=1
    if Pickle.centerY<450:
        Pickle.centerY+=2
    if Brocoli.centerY<450:
        Brocoli.centerY+=3
    if Cauliflower.centerY<450:
        Cauliflower.centerY+=3
    if Olive.centerY<450:
        Olive.centerY+=5
    if Cabbage.centerY<450:
        Cabbage.centerY+=2
def onMouseMove(x,y):
    MouseKatana.centerX=x
    MouseKatana.centerY=y
    if score.value<=50:
        MouseHandle.fill='blue'
def makeTomato():
    if Start.value==1:
        Tomato.add
        Tomato.visible=True
        Tomato.centerX = randrange(0, 360)
        Tomato.centerY = (-1)
def makePickle():
    if Start.value==1:
        Pickle.add
        Pickle.visible=True
        Pickle.centerX = randrange(0, 360)
        Pickle.centerY = (-1)
def makeBrocoli():
    if Start.value==1:
        Brocoli.add
        Brocoli.visible=True
        Brocoli.centerX = randrange(0, 360)
        Brocoli.centerY = (-1)
def makeCauliflower():
    if Start.value==1:
        Cauliflower.add
        Cauliflower.visible=True
        Cauliflower.centerX = randrange(0, 360)
        Cauliflower.centerY = (-1)
def makeOlive():
    if Start.value==1:
        Olive.add
        Olive.visible=True
        Olive.centerX = randrange(0, 360)
        Olive.centerY = (-1)
def makeCabbage():
    if Start.value==1:
        Cabbage.add
        Cabbage.visible=True
        Cabbage.centerX = randrange(0, 360)
        Cabbage.centerY = (-1)

cmu_graphics.run()