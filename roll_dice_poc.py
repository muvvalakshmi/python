
import random
lst=[1,2,3,4,5,6]
lst1=[]
count=0         
def dice(lst):
    print(format(lst[1],'>25'))
    print(format('+-----------+','>30'))
    print(format('/|','>18'),format('/|','>11'))
    print(format('/ |','>18'),format(lst[2],'>3'),format('/ |','>7'))
    print(format('+--+--------+','>27'),' +',lst[0])
    print(format(lst[5],'>13'),format('|  /','>3'),format('|  /','>11'))
    print(format('| /','>17'),format(lst[4],'>4'),format('| /','>6'))
    print(format('|/','>16'),format('|/','>11'))
    print(format('+-----------+','>27'),format(lst[3],'>20'),sep='\n')

#random.shuffle(lst)
dice(lst)
print("Enter the Direction you want")
print("R -> to roll right side\nL -> to roll left side\nU -> to roll upside\nD -5> to roll Downside\nQ -> to Quit")

def roll_right(right): #This function rotates the cube towards right
    temp=lst[4]        #intially front value stored into temporary variable, so front facing value will be empty,
    lst[4]=lst[5]      #now front value changed by left value 
    lst[5]=lst[2]      #left value changed by back value
    lst[2]=lst[0]      #back value shifted to right
    lst[0]=temp        #front value shifted to right    
    r=right.copy()
    lst1.append(['Right ',r])
    dice(right)
    return right

#     print(right)
# Right_rotation = roll_right(lst)
#print("Right rotated",Right_rotation)

def roll_left(left):
    temp=lst[5]
    lst[5]=lst[4]       
    lst[4]=lst[0]      
    lst[0]=lst[2]      
    lst[2]=temp
    l=left.copy()
    lst1.append(['Left ',l])
    dice(left)

    return left
# Left_rotation = roll_left(lst)
# print("Left rotated",Left_rotation)


def roll_up(up):
    temp=lst[4]        # front stored in temp, so front facing is empty now,
    lst[4]=lst[3]      # bottom to front, bottom is empty
    lst[3]=lst[2]      # back to bottom, back is empty
    lst[2]=lst[1]      # top to back, now top is empty
    lst[1]=temp        # front is now changed to top face 
    u=up.copy()
    lst1.append(['Up ',u])
    dice(up)

    return up
# Up_rotation = roll_up(lst)
# print("Up rotated",Up_rotation)


def roll_down(down):
    temp=lst[3]        # ====> bottom stored in temp, so bottom face is empty now,
    lst[3]=lst[4]      #------>bottom to front, front is empty
    lst[4]=lst[1]      #------>top to front, top is empty
    lst[1]=lst[2]      #------>back to top, now back is empty
    lst[2]=temp        #------>back is now changed to top face 
    d=down.copy()
    lst1.append(['Down ',d])
    dice(down)

    return down
# Down_rotation = roll_down(lst)
# print("Down rotated",Down_rotation)



while True:
    option = (input("Enter the direction to rotate:").strip()[0]).upper()
    if option == 'R':
        count+=1
        print("Right rotation",roll_right(lst))
    elif option == 'L':
        count+=1
        print("Left rotation",roll_left(lst))
    elif option == 'U':
        count+=1
        print("Up rotation",roll_up(lst))
    elif option == 'D':
        count+=1
        print("Down rotation",roll_down(lst))
    elif option == 'Q':
        print(count,"Rotations done!")
        print(lst1)
    
        for i,j in lst1:
            print(i)
            dice(j)
        break

       
    else:
        print("Invalid Move")
