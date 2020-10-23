import turtle as trtl

# The base + fill color of the Island

trtl.pensize(3)
trtl.penup()
trtl.setposition(-100,0)
trtl.pendown()
trtl.color("dim grey")
trtl.begin_fill()
trtl.forward(200)
trtl.left(120)

# The right face of the Island base 
trtl.forward(20)
trtl.right(45)
trtl.forward(30)
trtl.left(105)
trtl.forward(215)
trtl.left(120)

#The left face of the Island base
trtl.forward(30)
trtl.right(22.5)
trtl.forward(20)
trtl.color("saddle brown")
trtl.end_fill()

wn = trtl.Screen()
wn.mainloop()
