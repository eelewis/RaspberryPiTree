

###############  IMPORT LIBRARIES  ##############################
import subprocess
import time
import os
import tkinter as tk
from tkinter import *
import tkinter.font as font




###############  GLOBAL DATA  ##################################

gui = tk.Tk()
nowPlaying = False
#process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/shortHouse.mp3'])
pgid = ''
font = font.Font(family="Helvetica", size=18, weight='bold')

###############  GUI COMPONENTS  ################################

def songOne():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Ave.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
     
        
def songTwo():
    global nowPlaying
    global process
    global pgid

    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Manger.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songThree():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Carol.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songFour():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Halls.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songFive():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Gentlemen.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songSix():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Wenceslas.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songSeven():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Herald.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songEight():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Happy.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songNine():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Jingle.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songTen():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/vulf.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songEleven():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Emmanuel.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songTwelve():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/HolyNight.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songThirteen():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Tannenbaum.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songFourteen():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/SilentNight.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songFifteen():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Noel.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songSixteen():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Holly.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songSeventeen():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/TwelveDays.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songEighteen():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Housetop.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songNineteen():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/Kings.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)
        
        
def songTwenty():
    global nowPlaying
    global process
    global pgid
    
    if process.poll() == None:
        print('A song is currently playing')
        
    else:
        process = subprocess.Popen(['sudo', 'python', '/home/pi/lightshowpi/py/synchronized_lights.py', '--file=/home/pi/lightshowpi/music/WishJoy.mp3'], preexec_fn = os.setpgrp)
        print('Process spawned with PID: %s' % process.pid)
        pgid = os.getpgid(process.pid)




def stopMusic():
    global nowPlaying
    global process
    if process.poll() == None:
        subprocess.check_call(['sudo', 'kill', str(pgid)])



            
            ########  INTERFACE  ##############
        
gui.geometry("800x300") ## size of interface
gui.title("Ivy Tech Computer Club")



 
    ## main content
mainContent = tk.Frame(gui);

song1 = tk.Button(mainContent, text="Ave Maria", height = 2, width = 16, font='font', command = songOne)
song2 = tk.Button(mainContent, text="Away in a Manger", height = 2, width = 16, font='font', wraplength = 100, command = songTwo)
song3 = tk.Button(mainContent, text="Carol of the Bells", height = 2, width = 16, font='font', command = songThree)
song4 = tk.Button(mainContent, text="Deck the Halls", height = 2, width = 16, font='font', command = songFour)
song5 = tk.Button(mainContent, text="God Rest ye Merry Gentlemen", height = 2, width = 16, font='font', wraplength = 120, command = songFive)
song6 = tk.Button(mainContent, text="Good King Wenceslas", height = 2, width = 16, font='font', wraplength = 100, command = songSix)
song7 = tk.Button(mainContent, text="Hark the Herald Angels Sing", height = 2, width = 16, font='font', wraplength = 120, command = songSeven)
song8 = tk.Button(mainContent, text="Have a Happy Christmas", height = 2, width = 16, font='font', wraplength = 120, command = songEight)
song9 = tk.Button(mainContent, text="Jingle Bells", height = 2, width = 16, font='font', command = songNine)
song10 = tk.Button(mainContent, text="Christmas in L.A.", height = 2, width = 16, font='font', wraplength = 100, command = songTen)
song11 = tk.Button(mainContent, text="Oh Come, Oh Come, Emmanuel", height = 2, width = 16, font='font', wraplength = 140, command = songEleven)
song12 = tk.Button(mainContent, text="Oh Holy Night", height = 2, width = 16, font='font', command = songTwelve)
song13 = tk.Button(mainContent, text="O Tannenbaum", height = 2, width = 16, font='font', command = songThirteen)
song14 = tk.Button(mainContent, text="Silent Night", height = 2, width = 16, font='font', command = songFourteen)
song15 = tk.Button(mainContent, text="The First Noel", height = 2, width = 16, font='font', command = songFifteen)
song16 = tk.Button(mainContent, text="The Holly and the Ivy", height = 2, width = 16, font='font', wraplength = 100, command = songSixteen)
song17 = tk.Button(mainContent, text="Twelve Days of Christmas", height = 2, width = 16, font='font', wraplength = 100, command = songSeventeen)
song18 = tk.Button(mainContent, text="Up on the Housetop", height = 2, width = 16, font='font', wraplength = 100, command = songEighteen)
song19 = tk.Button(mainContent, text="We Three Kings", height = 2, width = 16, font='font', command = songNineteen)
song20 = tk.Button(mainContent, text="Wish you... / Joy to the World", height = 2, width = 16, font='font', wraplength = 120, command = songTwenty)


stop = tk.Button(mainContent, text="Stop Music", height = 2, width = 12, font='font', command = stopMusic)

## when you size these the units are em: width and height of the letter m in that font

##load buttons in
mainContent.pack()

song1.grid(row=0, column=0, padx=3, pady=3) ## adjust padding to put space between butons, row and column to layout buttons
song2.grid(row=0, column=1, padx=3, pady=3)
song3.grid(row=0, column=2, padx=3, pady=3)
song4.grid(row=0, column=3, padx=3, pady=3)
song5.grid(row=0, column=4, padx=3, pady=3)
song6.grid(row=1, column=0, padx=3, pady=3)
song7.grid(row=1, column=1, padx=3, pady=3)
song8.grid(row=1, column=2, padx=3, pady=3)
song9.grid(row=1, column=3, padx=3, pady=3)
song10.grid(row=1, column=4, padx=3, pady=3)
song11.grid(row=2, column=0, padx=3, pady=3)
song12.grid(row=2, column=1, padx=3, pady=3)
song13.grid(row=2, column=2, padx=3, pady=3)
song14.grid(row=2, column=3, padx=3, pady=3)
song15.grid(row=2, column=4, padx=3, pady=3)
song16.grid(row=3, column=0, padx=3, pady=3)
song17.grid(row=3, column=1, padx=3, pady=3)
song18.grid(row=3, column=2, padx=3, pady=3)
song19.grid(row=3, column=3, padx=3, pady=3)
song20.grid(row=3, column=4, padx=3, pady=3)

stop.grid(row=4, column=2, padx=3, pady=3) 

#######################  RUN  #####################################
gui.mainloop()
























######################## EXTRA SCROLL SPACE  #####################
############################# END OF FILE  #######################
