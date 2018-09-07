import time
import piplates.MOTORplate as MOTOR

res='y'
while res!='n' or res!='N':
    
    direction = raw_input("Enter roation direction ccw or cw: ") #Set stepper rotation direction
    MOTOR.stepperCONFIG(0,'a',direction,'F', 2000, 2) #Set up stepper motor
    steps = input("Enter number of steps: ") 

    MOTOR.stepperMOVE(0,'a',steps) #tell stepper motor to move user input number of steps

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
    

        
    
   
    

