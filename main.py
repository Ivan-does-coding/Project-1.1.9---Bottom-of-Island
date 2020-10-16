import turtle as trtl

# The base + fill color of the Island

trtl.pensize(7)
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

#The top part outline of the Island 

# The left face of the island
trtl.color("dim grey")
trtl.penup()
trtl.setposition(-117.5,47.5)
trtl.penup()
trtl.left(162.5)
trtl.pendown()
trtl.forward(40)

#The underpart of the cliff
for i in range (2):
  trtl.left(25)
  trtl.forward(30)

# The left overhang part of the cliff
for i in range (5):
  trtl.right(25)
  trtl.forward(10)

trtl.color("sienna")
trtl.right(25)
trtl.forward(10)


# The top of the cliff
trtl.forward(100)
trtl.left(10)
trtl.forward(70)
trtl.left(15)
trtl.forward(30)


# The right cliff of the outline
for i in range (4):
  trtl.right(25)
  trtl.forward(5)

trtl.color("dim grey")

# The right face of the island
trtl.left(25)
trtl.forward(30)
trtl.right(35)
trtl.forward(35)

wn = trtl.Screen()
wn.mainloop()
