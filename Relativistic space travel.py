def Space_travel(D, B):
    if B > 1 or B < 0:
        print('Invalid input')
    else:
        c = 3e8  
        year = 3600*24*365
        #Earth's Perspective 
        v = B*c
        t = D/v
        T = t/year
        print("From Earth's perspective it takes {} years to travel".format(round(T)))
        #Spaceship's perspective
        gamma = 1/((1-B**2)**0.5)
        t = gamma*(t-((v*D)/c**2))
        Ts = t/year
        print("From the spaceship's perspective it takes {} years to travel".format(round(Ts)))
    
Space_travel(3e18, 6)
