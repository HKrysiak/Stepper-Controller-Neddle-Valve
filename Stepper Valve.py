>>> import time
>>> import piplates.MOTORplate as MOTOR
MOTOR.stepperCONFIG(0,'a','cw','F', 2000, 2)
MOTOR.stepperMOVE(0,'a',200)
flag = 1
while(flag):
    time.sleep(0.1)
    stat = MOTOR.getINTflag0(0)
    if (stat & 0x20):
        flag = 0
print "Move Complete!"
