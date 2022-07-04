from Tello import Tello
import sys
from datetime import datetime
import time



def ReadCommand(command):
    #for command in commands:
    #print(command)
    
    '''
    if command.find('delay') != -1:
        sec = float(command.partition('delay')[2])
        print ('delay %s' % sec)
        time.sleep(sec)
        pass
    else:
        '''
    tello.send_command(command)
    return

start_time = str(datetime.now())

tello = Tello()

while True:
    try:
        commands = input()
        if commands == "close":
            tello.socket.close()
        if commands:
            ReadCommand(commands)
        log = tello.get_log()
        print(log)
    except KeyboardInterrupt:
        print ('\n Closing socket. . .\n')
        tello.socket.close() 
        break
    
        





