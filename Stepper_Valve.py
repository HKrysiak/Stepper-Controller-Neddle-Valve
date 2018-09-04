res='y'
while res!='n' or res!='N':
    import time
    import piplates.MOTORplate as MOTOR

    direction = raw_input("Enter roation direction ccw or cw: ")
    MOTOR.stepperCONFIG(0,'a',direction,'F', 2000, 2)
    steps = input("Enter number of steps: ")

    MOTOR.stepperMOVE(0,'a',steps)

    flag = 1
    while(flag):
        time.sleep(0.1)
        stat = MOTOR.getINTflag0(0)
        if (stat & 0x20):
            flag = 0
    print "Move Complete!"
    time.sleep(1)
    MOTOR.stepperSTOP(0,'a')
    MOTOR.stepperOFF(0,'a')
    

        
    
   
    

