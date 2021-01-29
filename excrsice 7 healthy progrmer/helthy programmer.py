#=======================HEALTHY PROGRAMMER===========================
# 9 am to 5 pm
# water=water.mp3 (3.5 liters)  drank very 40 min
# eyes=eyes.mp3 (evry 30 min) eydone
# physical activity=physical.mp3 (every 45 min) exdone


from datetime import datetime
from pygame import mixer
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
         a=input()
         if a == stopper:
             mixer.music.stop()
             break
def log_now(msg):
    with open("mylogs.txt","a") as f :
        f.write(f"{msg}{datetime.now()}\n")
if __name__ == '__main__':
    # musiconloop("paani.mp3.mp3" ,"done")
    init_water=time()
    init_eyes=time()
    init_excercise=time()
    watersecs=2400
    eyesec=1800
    excsecs =2700
    while True:
        if time()- init_water>watersecs:
            print("Water drinking time...... enter 'drank' to stop the alarm......\n")
            musiconloop('paani.mp3.mp3','drank')
            init_water=time()
            log_now("drank water at\t")
        if time() - init_eyes > eyesec:
            print("eye excrcise time...... enter 'done' to stop the alarm......\n")
            musiconloop('paani.mp3.mp3', 'done')
            init_eyes = time()
            log_now("eyes relaxed at\t")
        if time() - init_excercise > excsecs:
            print("excercising time...... enter 'doneex' to stop the alarm......\n")
            musiconloop('paani.mp3.mp3', 'doneex')
            init_excercise = time()
            log_now("done excercise at\t")






