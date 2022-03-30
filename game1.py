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
hallway.south = mess_hall


#define Item 
Item.description = "" #this adds a blank description to each item
room.items = bag()
mess_hall.items.add(red_keycard)
red_keycard.description = "it,s a red keycard. it probly opens a door or a locker"

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."


cargo.items.add(knife)


@when ("go DIRECTRION")
def travel(direction):
    global current_room 
    if direction in current_room.exits():
         current_room = current_room.exit(direction)
         print(f"you go {direction}.")
         print(current_room)


@when("look")
def look():
    print(current_room)
    print(f"There are exits to the {current_room.exits()}.")
    if len(current_room.items) > 0: 
       print("you also see:")
       for item in current_room.items;
           print(item)

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup (item):
    if item in current_room.items:
        t = current_room.items.take(item)
        inventory.add(t)
        print(f"you pick up the {item}")
      else:
        print(f"you dont see a {item}")
        

@when("look at ITEM")
def look_at(item):
    if item in inventory:
        t = inventory.find(item)
        print(t.description)
    else:
         print(f"you aren't carrying an {item}")

if current_room == bridge and escape_pod_open == false and direction == "south"
  print("the door is locked. you need a keycard to swipe")
  return




@when("inventory")
@when("show inventory")
@when("whats in my pocket")
def player_inventory():
    print("you are carrying")
    for item in inventory:
        print(item)



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