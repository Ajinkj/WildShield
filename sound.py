import  vlc
import time



p = vlc.MediaPlayer("dog.mp3")
p.play()
time.sleep(60)
p.stop()