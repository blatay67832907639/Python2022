from adventurelib import *

space = Room("""
    you are drifting in space. It feels very cold.
    A slate-blue spaceship sits completely silent to your left,
    its airlock open and waiting.
    """)


spaceship = Room("""
    The bridge if the spaceship is shiny and white, with thousands 
    of small, red, blinking lights.
    """)


current_room = space

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
    global current_room
    #check if action can be done
    if current_room is not space:
        say("there is no airlock here")
        return

else:
    current_room = spaceship
    print("""you heave yourself into the spaceship and slam
    you hand on the button to close the door.
    """)


    

 

@when("brush teeth")
@when("brush")
@when("clean teeth")
def brush_teeth():
  print("you brushed your teeth")
@when("comb hair")
@when("comb")
def comb_hair():
  say("""
    you brush your long flowing locks with the gold hairbrush that you have selected from the 
    in the red basket.
    """) 








def main():
  start()

if __name__ == '__main__':
  main()