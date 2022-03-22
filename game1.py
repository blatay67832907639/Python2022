from adventurelib import *

space = Room("""
    you are drifting in space. It feels very cold.
    A slate-blue spaceship sits completely silent to your left,
    its airlock open and waiting.
    """)


cargo = room("""
    the place were the cargo is stored
    """)



docking = room("""
   a room were other space crafts join and depart
   """)


airlock = room("""
    the door witch you enter to leave and enter space through ship
    """)


hallway = room("""
   the hall way leeding to all the rooms
    """)

bridge = Room("""
    The bridge if the spaceship is shiny and white, with thousands 
    of small, red, blinking lights.
    """)


quarters = room("""
        were the cabin/crew mates sleep   
        """)          




mess_hall = room("""
     a place in the ship where the astranauts eat and drink
        """)



escape_pods = room("""
    these pods are used for emergency only 
    """)




cockpit = room("""
   the room you control the hole space craft in and all the things on the ship
   """)

spaceship.east = hallway
spaceship.south = quarters
hallway.east == bridge 
hallway.north = cargo

@when ("go DIRECTRION")
def travel(direction):
    pass

#variables
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