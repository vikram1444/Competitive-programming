def find_rectangular_overlap(rect1, rect2):
    flag = False
    
    if(rect1['left_x']<rect2['left_x']):
        if(rect1['left_x']+rect1['width']<=rect2['left_x']):
            flag=True
        else:
            x=rect2['left_x']
            width=min(rect1['left_x']+rect1['width']-rect2['left_x'],rect2['width'])
    else:
        if(rect2['left_x']+rect2['width']<=rect1['left_x']):
            flag=True
        else:
            x=rect1['left_x']
            width=min(rect2['left_x']+rect2['width']-rect1['left_x'],rect1['width'])
    if(rect1['bottom_y']<rect2['bottom_y']):
        if(rect1['bottom_y']+rect1['height']<=rect2['bottom_y']):
            flag=True
        else:
            y=rect2['bottom_y']
            height=min(rect1['bottom_y']+rect1['height']-rect2['bottom_y'],rect2['height'])
    else:
        if(rect2['bottom_y']+rect2['height']<=rect1['bottom_y']):
            flag=True
        else:
            y=rect1['bottom_y']
            height=min(rect2['bottom_y']+rect2['height']-rect1['bottom_y'],rect1['height'])
    if(flag==True):
        print'None'
    else:
         print x,y,width,height
rect1=eval(raw_input('r1:'))
rect2=eval(raw_input('r2:'))
find_rectangular_overlap(rect1,rect2)
