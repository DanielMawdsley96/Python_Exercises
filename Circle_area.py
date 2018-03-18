def point_distance(xc, yc, xp, yp):
    dx = xp -xc
    dy = yp -yc
    r = (dx**2+dy**2)**0.5 
    return r
    
def Circle_Area(xc, yc, xp, yp):
    R = point_distance(xc, yc, xp, yp)
    Area = 3.14*R
    print(round(Area))
    return Area

Circle_Area(7, 4, 5, 8)
