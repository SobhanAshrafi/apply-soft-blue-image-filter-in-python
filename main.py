from turtle import color
from PIL import Image
import sys

# function to apply blue filter
def set_Blue_filter(i,j):   
    
    for x in range(i):
        for y in range(0,j):
            color = a.getpixel((x,y)) 
            if color[2] <= 235:
                color = color[:2] + (color[2]+20,)
                a.putpixel( (x , y) , color )
        

    






try:
    Im_Path = sys.argv[1]

except :
    Im_Path = "image_path.jpg"



a= Image.open(Im_Path)

(i,j) = a.width , a.height


set_Blue_filter(i,j)


a.show()



#creat new image path name
tmp = - ( 1 + Im_Path[::-1].find('.') )
New_Im_Path = Im_Path[0:l] + "_processed0" + Im_Path[l:]

#Saving Edited Image
a.save()
