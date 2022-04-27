GlowScript 3.0 VPython
from vpython import *

# background :
scene2 = canvas(background=color.black)

# variables:

μ = 2.5             # mass ratio
L = 45              # total length of string
r = 10              # initial length of pendulum
d = 20              # distance b/w pulleys
R = L - d - r       # initial length of Counter-weight
θ = radians(90)     # starting angle from vertical

g = 9.8
v = 0               # rate of change of 'r' wrt time
ω = 0               # angular velocity
a = 0               # rate of change of 'v' wrt time
α = 0               # angular acceleration
t = 0 
dt = 0.0001
T = 100

# system objects:

# colors
pulleys_color = vec(0.5,0.2,0)
thread_color = vec(0.7,0.7,0.7)

#text 
s = 'μ : ' + μ + '\nθ : '+ degrees(θ)
text(text=s, color=color.white, pos = vec(-20,10,0), height = 2, width = 2)

thread1 = cylinder(pos=vector(0,0,0), axis=vec( r*sin(θ), -r*cos(θ),0), radius=0.2, color= thread_color )
pendulum = sphere(pos = thread1.axis, radius = 1, color = color.orange, make_trail = True, trail_color = color.red)

thread2 = cylinder(pos=vector(-d,0,0), axis=vector(0,R,0), radius=0.2, color= thread_color )
block = sphere(pos = thread2.axis, radius = 2, color = color.green )

thread3 = cylinder(pos=thread1.pos, axis=thread2.pos, radius=0.2, color= thread_color )

# pulleys:
pulley = shapes.circle(radius=1)
extrusion( path = [ vec(0,0,0.3) , vec(0,0,-0.3)], shape = pulley , color= pulleys_color )
axle1 = cylinder(pos = vec(0,0,0.3), axis = vec(cos(θ),sin(θ),0), radius = 0.1)

extrusion( path = [ vec(-d,0,0.3) , vec(-d,0,-0.3)], shape = pulley , color= pulleys_color )
axle2 = cylinder(pos = vec(-d,0,0.3), axis = vec(cos(θ),sin(θ),0), radius = 0.1)

while t < T:
 rate(10/dt)
 
 # animating:
 X = pendulum.pos = thread1.axis = vec( r*sin(θ), -r*cos(θ),0)
 thread2.axis = vec( 0,-R,0)
 block.pos = vec(-d,-R,0)
 axle1.axis = vec(cos(θ),sin(θ),0)
 axle2.axis = vec(cos(θ),sin(θ),0)
 
 # updating:
 l = mag(X)                               # length of pendulum
 a = ( l*(ω*ω) + g*(cos(θ)-μ ) )/( 1+μ )
 α = -( 2*(v*ω) + g*sin(θ) )/ l
 v += a*dt
 ω += α*dt
 θ += ω*dt 
 r += v*dt
 R = L - d -  r
 t += dt

print("terminated")