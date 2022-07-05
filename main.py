import vision
import msg

animal=vision.scan()
print(animal)
msg.snd(animal)
