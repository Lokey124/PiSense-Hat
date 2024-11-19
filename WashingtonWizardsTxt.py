from sense_hat import SenseHat

sense = SenseHat()
sense.set_rotation(270)

blue = (0, 0, 255)
red = (51, 0, 0)

message = "Washington Wizards 2025!! "

speed = 0.09

while True:
        sense.show_message(message, speed, text_colour=blue, back_colour=red)
