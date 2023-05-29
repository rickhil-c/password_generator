import math

def Area_Triangle():
        base_1 = float(input('Enter base'))
        height = float(input('Enter height'))
        area_triangle = round(((base_1 * height) / 2),3)
        print(f'''Area = 1/2({base_1}) * {height}
= {(base_1 * height)}/{2}
= {area_triangle}''')

def Area_Quad():
     base_1 = float(input('Enter base'))
     base_2 = float(input('Enter base 2 (length of the top side)'))
     height = float(input('Enter height'))
     area_quad = round(((base_1 + base_2 * height) / 2), 3)
     print(f'''Area = 1/2({base_1} + {base_2}) * {height}
= {base_1 + base_2} * {height}
= {(base_1 + base_2 * height)}/{2}
= {area_quad}''')

def Area_Circle():
    radius = float(input("Enter radius or 0 if it isn't provided"))
    if radius != 0:
        area_circle_r = round(((math.pi) * (radius ** 2)), 3)
        print(f'''Area = {math.pi} * {radius}^2
= {math.pi} * {radius ** 2}
= {area_circle_r}''')

    else:
        diameter = float(input("Enter diameter or 0 if it isn't provided"))
        if diameter != 0:
            area_circle_d = round(((math.pi) * ((diameter / 2) ** 2)), 3)
            print(f'''Area = {math.pi} * {diameter}^2
= {math.pi} * {(diameter / 2) ** 2}
= {area_circle_d}''')

        else:
            circumference = float(input('Enter circumference'))
            area_circle_c = round(((math.pi) * ((circumference / math.pi / 2) ** 2)), 3)
            print(f'''Area = {math.pi} * {circumference}^2
= {math.pi} * {(circumference / math.pi / 2) ** 2}
= {area_circle_c}''')


while True:


 formula = str(input("What do you want to calculate?"))

 if str(formula) == "area".lower():
     shape = input(f'What shape are you interested in finding the {str(formula)} of?')

     if str(shape) == 'quad':
            Area_Quad()

     elif str(shape) == 'triangle':
           Area_Triangle()

     elif str(shape) == 'circle':
           Area_Circle()

     else: break


 elif formula == "volume".lower():

     Shape = input(f'What shape are you interested in finding the {str(formula)} of?')
     Height = float(input("Enter Height"))
     if str(Shape) == "prism":
         base_shape = str(input("What is its base?(quad,triangle,circle)"))

         if str(base_shape) == 'quad':
             base_1 = float(input('Enter base'))
             base_2 = float(input('Enter base 2 (length of the top side)'))
             height = float(input('Enter height'))
             area_quad = round(((base_1 + base_2 * height) / 2), 3)
             print(f'''Area = 1/2({base_1} + {base_2}) * {height}
     = {base_1 + base_2} * {height}
     = {(base_1 + base_2 * height)}/{2}
     = {area_quad}''')
             print("Therefore,")
             print(f"""Volume = ({area_quad} * {Height})/3 
       = {area_quad * Height}/3
       = {(area_quad * Height) / 3}""")

         elif str(base_shape) == 'triangle':
             base_1 = float(input('Enter base'))
             height = float(input('Enter height'))
             area_triangle = round(((base_1 * height) / 2), 3)
             print(f'''Area = 1/2({base_1}) * {height}
     = {(base_1 * height)}/{2}
     = {area_triangle}''')
             print("Therefore,")
             print(f"""Volume = ({area_triangle} * {Height})/3 
       = {area_triangle * Height}/3
       = {(area_triangle * Height) / 3}""")


         elif str(base_shape) == 'circle':
             radius = float(input("Enter radius or 0 if it isn't provided"))
             if radius != 0:
                 area_circle_r = round(((math.pi) * (radius ** 2)), 3)
                 print(f'''Area = {math.pi} * {radius}^2
     = {math.pi} * {radius ** 2}
     = {area_circle_r}''')
                 print("Therefore,")
                 print(f"""Volume = ({area_circle_r} * {Height})/3 
       = {area_circle_r * Height}/3
       = {(area_circle_r * Height) / 3}""")
             else:
                 diameter = float(input("Enter diameter or 0 if it isn't provided"))
                 if diameter != 0:
                     area_circle_d = round(((math.pi) * ((diameter / 2) ** 2)), 3)
                     print(f'''Area = {math.pi} * {diameter}^2
     = {math.pi} * {(diameter / 2) ** 2}
     = {area_circle_d}''')
                     print("Therefore,")
                     print(f"""Volume = ({area_circle_d} * {Height})/3 
       = {area_circle_d * Height}/3
       = {(area_circle_d * Height) / 3}""")
                 else:
                     circumference = float(input('Enter circumference'))
                     area_circle_c = round(((math.pi) * ((circumference / math.pi / 2) ** 2)), 3)
                     print(f'''Area = {math.pi} * {circumference}^2
     = {math.pi} * {(circumference / math.pi / 2) ** 2}
     = {area_circle_c}''')
                     print("Therefore,")
                     print(f"""Volume = ({area_circle_c} * {Height})/3 
       = {area_circle_c * Height}/3
       = {(area_circle_c * Height) / 3}""")



     elif str(Shape) == "pyramid":
             base_shape = str(input("What is its base?(quad,triangle,circle)"))

             if str(base_shape) == 'quad':
                 base_1 = float(input('Enter base'))
                 base_2 = float(input('Enter base 2 (length of the top side)'))
                 height = float(input('Enter height'))
                 area_quad = round(((base_1 + base_2 * height) / 2), 3)
                 print(f'''Area = 1/2({base_1} + {base_2}) * {height}
     = {base_1 + base_2} * {height}
     = {(base_1 + base_2 * height)}/{2}
     = {area_quad}''')
                 print("Therefore,")
                 print(f"""Volume = ({area_quad} * {Height})/3 
      = {area_quad * Height}/3
      = {(area_quad * Height) / 3}""")


             elif str(base_shape) == 'triangle':
                 base_1 = float(input('Enter base'))
                 height = float(input('Enter height'))
                 area_triangle = round(((base_1 * height) / 2), 3)
                 print(f'''Area = 1/2({base_1}) * {height}
     = {(base_1 * height)}/{2}
     = {area_triangle}''')
                 print("Therefore,")
                 print(f"""Volume = ({area_triangle} * {Height})/3 
       = {area_triangle * Height}/3
       = {(area_triangle * Height) / 3}""")


             elif str(base_shape) == 'circle':
                 radius = float(input("Enter radius or 0 if it isn't provided"))
                 if radius != 0:
                     area_circle_r = round(((math.pi) * (radius ** 2)), 3)
                     print(f'''Area = {math.pi} * {radius}^2
     = {math.pi} * {radius ** 2}
     = {area_circle_r}''')
                     print("Therefore,")
                     print(f"""Volume = ({area_circle_r} * {Height})/3 
       = {area_circle_r * Height}/3
       = {(area_circle_r * Height) / 3}""")
                 else:
                     diameter = float(input("Enter diameter or 0 if it isn't provided"))
                     if diameter != 0:
                         area_circle_d = round(((math.pi) * ((diameter / 2) ** 2)), 3)
                         print(f'''Area = {math.pi} * {diameter}^2
     = {math.pi} * {(diameter / 2) ** 2}
     = {area_circle_d}''')
                         print("Therefore,")
                         print(f"""Volume = ({area_circle_d} * {Height})/3 
       = {area_circle_d * Height}/3
       = {(area_circle_d * Height) / 3}""")
                     else:
                         circumference = float(input('Enter circumference'))
                         area_circle_c = round(((math.pi) * ((circumference / math.pi / 2) ** 2)), 3)
                         print(f'''Area = {math.pi} * {circumference}^2
     = {math.pi} * {(circumference / math.pi / 2) ** 2}
     = {area_circle_c}''')
                         print("Therefore,")
                         print(f"""Volume = ({area_circle_c} * {Height})/3 
       = {area_circle_c * Height}/3
       = {(area_circle_c * Height) / 3}""")


     else:
         print("Volume inapplicable.")
         continue

 else: continue




