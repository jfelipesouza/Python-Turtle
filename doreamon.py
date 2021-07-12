from turtle import *

setup(420,420)
speed(10)
bgcolor('gray')
shape('triangle')
colormode(255)
title('Desenhando o Doraemon')


def drawRound(a,b=True):
    pendown()
    if b ==True:
        begin_fill()
    setheading(180)
    circle(a,360)
    if b == True:
        end_fill()

def drawRect(tamanho,largura,b=True):
    setheading(0)
    pendown()
    if b == True:
        begin_fill()
    forward(tamanho)
    right(90)
    forward(largura)
    right(90)
    forward(tamanho)
    right(90)
    forward(largura)
    if b == True:
        end_fill()

def header():
    # cabeça do carinha

    color('blue','blue')
    penup()
    goto(0,100)
    drawRound(75,True)
    color('#fff',"#fff")
    penup()
    goto(0,72)
    drawRound(60,True)

def eyes():
    
    #esquerdo
    
    color('black','white')
    penup()
    goto(-20,80)
    drawRound(17,True)
    
    #direito
    
    color('black','white')
    penup()
    goto(19,80)
    drawRound(17,True)
    #esquerdo
    color('black','black')
    penup()
    goto(-18,70)
    drawRound(6,True)
    color('white','white')
    penup()
    goto(-18,66)
    drawRound(2)
    #direito
    color('black','black')
    penup()
    goto(17,70)
    drawRound(6,True)
    color('white','white')
    penup()
    goto(17,66)
    drawRound(2)

def nose():
    #nariz do carinha

    color('red','red')
    penup()
    goto(0,40)
    drawRound(7)

def mouth():
    #boca
    color('black','black')
    penup()
    goto(-30,-20)
    pendown()
    setheading(-27)
    circle(70,55)
    #bigodinho do meio
    penup()
    goto(0,26)
    pendown()
    goto(0,-25)

def bigodinho():
    color('#000',"#000")
    
    penup()
    goto(-10,5)
    pendown()
    goto(-40,5)
    
    penup()
    goto(10,5)
    pendown()
    goto(40,5)
    
    penup()
    goto(-10,15)
    pendown()
    goto(-40,20)

    penup()
    goto(10,15)
    pendown()
    goto(40,20)

    penup()
    goto(-10,-5)
    pendown()
    goto(-40,-10)

    penup()
    goto(10,-5)
    pendown()
    goto(40,-10)


header()
eyes()
nose()
mouth()
bigodinho()

hideturtle()

done()