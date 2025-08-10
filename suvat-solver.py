import math

print('enter values (leave blank if unknown):')

s = input('displacment(s):')
u = input('initial velocity(u):')
v = input('final velocity(v):')
a = input('acceleration(a):')
t = input('time(t):')

s = float(s) if s else None 
u = float(u) if u else None 
v = float(v) if v else None 
a = float(a) if a else None 
t = float(t) if t else None 

# v = u + at  
if v is None and u is not None and a is not None and t is not None:
    v = u + ( a * t )

# s = ut + 1/2at^2  
if s is None and u is not None and t is not None and a is not None:
    s = (u * t) + (0.5 * a * (t**2))

# v² = u^2 + 2as    
if v is None and u is not None and a is not None and s is not None:
    v = math.sqrt ((u ** 2) + 2 * (a * s))

# t = (v - u) / a   
if t is None and v is not None and u is not None and a is not None:
    t = (v - u) / a

# a =  (v - u) / t
if a is None and v is not None and u is not None and t is not None:
    a = (v -u) / t

# s - ((u + v) / 2) t
if s is None and v is not None and u is not None and t is not None:
    s = ((u + v) / 2 ) * t

# a = (v^2 - u^2) / 2s
if a is None and v is not None and u is not None and s is not None:
    a = ((v ** 2) - (u ** 2)) / (2 * s)

#  u = v - at
if u is None and v is not None and a is not None and t is not None:
    u = v - a * t

print("Displacement (s):", s)
print("Initial velocity (u):", u)
print("Final velocity (v):", v)
print("Acceleration (a):", a)
print("Time (t):", t)