# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('Agni', color="#ffae00")

# declare inventory as a default variable, which will be used to store the items that the player picks up during the game.
default inventory = []
label start: # The game starts here.
    "Darkness...It's all you ever see, a world painted in eternal darkness. A world where light is crucial to your survival."
    "Your name is Agni, and you're a waxborne, a candle-based creature."
    "Your mission is to light the world torch to bring light back to your kingdom."
    "But to do that, you'll need to escape this dungeon."

    scene cellclosed
    "You wake up in a dimly lit cell, the air thick with the scent of damp stone and old wood."

# The first part of the game takes place in the cell, where the player can explore and find items to help them escape. The player can choose to look at different parts of the cell, and if they find the stick, they can use it to break the lock on the cell doors and escape into the hallway.
label cell:
    a "I need to find a way out of here. There has to be something I can use."
    show screen inventory_display_toggle # Show the inventory display toggle screen, which will be used to show the inventory item description screen when the player clicks on the "Inventory" button.

    scene cellclosed
    menu Cellchoices:
        a "Where to look?"
        "Left": # First choice
            if "Stick" in inventory: # If the player has already picked up the stick, they will see the empty cell left image and a message saying they've already picked up the stick. Otherwise, they will see the cell left image and have the option to look at the stick or leave.
                scene cellleftempty
                "You see a wall of concrete."
                "You've already picked up the stick."
                scene cellclosed
                jump Cellchoices
            else: # If the player hasn't picked up the stick, they will see the cell left image and have the option to look at the stick or leave.
                scene cellleft
                "You see a wall of concrete."
                menu cellleftchoices:
                    "Look at the stick.": # If the player chooses to look at the stick, they will pick it up and add it to their inventory. They will also see a message describing the stick and how it could be useful.
                        if "Stick" in inventory: # If the player has already picked up the stick, they will see the empty cell left image and a message saying they've already picked up the stick. Otherwise, they will pick up the stick and add it to their inventory.
                            show cellleftempty
                            "You've already picked up the stick."
                            jump Cellchoices
                        else: # If the player hasn't picked up the stick, they will pick it up and add it to their inventory.
                            show cellleftempty
                            "You pick up the stick and examine it. It's a sturdy piece of wood, about two feet long."
                            "It could be useful..."
                            $ inventory.append("Stick")
                            scene cellclosed
                            jump Cellchoices
                    "leave":
                        scene cellclosed
                        jump Cellchoices            
        "Cell Doors": # Second choice
            "You see a set of heavy iron doors, locked with a brittle lock."
            menu celldoorschoices:
                "examine the lock.":
                    if "Stick" in inventory: # If the player has the stick, they will be able to use it to break the lock and escape. Otherwise, they will just examine the lock and find that it's old and rusty.
                        "You take a closer look at the lock. It's old and rusty."
                        "You whack the lock with the stick, trying to break it open."
                        "After a few hits, the lock gives way with a loud snap."
                        scene cellopen # Show the open cell doors image.
                        "The doors swing open, revealing a dimly lit corridor beyond."
                        jump hallway
                    else: # If the player doesn't have the stick, they will just examine the lock and find that it's old and rusty.
                        "You take a closer look at the lock. It's old and rusty."
                        jump cell
                "Leave it alone.": 
                    scene cellclosed
                    jump Cellchoices
        "Right": # Third choice
            scene cellright
            "You see a wall of concrete and cracks."
            menu cellrightchoices:
                "stare at the wall.":
                    "You stare at the wall, noticing the cracks and the rough texture."
                    jump cellrightchoices
                "lick the wall.": # Hilarious choice
                    "You lick the wall, tasting the dampness and the minerals in the stone."
                    "Why did you do that...?"
                    a "Why did I do that...?"
                    jump cellrightchoices
                "leave": # If the player chooses to leave, they will go back to the main cell choices menu.
                    scene cellclosed
                    jump Cellchoices
    hide screen inventory_display_toggle

label hallway: # ending
    scene hallway
    "You step into the hallway, the air growing colder and the darkness seeming to close in around you."
    "The corridor stretches out before you, with doors on either side and a faint light at the end."
    scene castlegrounds

    "You find your way to the castle grounds, a once prosperous area not broken and empty."

    jump castlegrounds

label castlegrounds:
    show screen inventory_display_toggle # Show the inventory display toggle screen, which will be used to show the inventory item description screen when the player clicks on the "Inventory" button.
    
    scene castlegrounds
    menu castlegroundchoices:
        a "Now what...?"
        "Left": # First choice
            jump entrance
        "Fountain": # Second choice
            scene fountain 
            "You head to the middle and see the fountain, a once shining piece is now a shell broken and filled with stillwater..."
            scene castlegrounds
            jump castlegroundchoices
        "Forward": # Third choice
            if "Gold Key" in inventory: # If the player has already picked up the gold key, they will see the empty library image and a message saying they've already picked up the gold key. Otherwise, they will see the library image and have the option to look at the gold key or leave.
                "No need to go there again..."
                scene castlegrounds
                jump castlegroundchoices
            else: # If the player hasn't picked up the gold key, they will see the quarters
                jump castlequarters
        "Right": # Fourth choice
            scene castlegateempty
            "You head to the right and see the entrance to the throne room."
            menu castlegatechoices:
                "Peek through the doors.":
                    scene castlegateempty
                    "You peek through the doors and see a grand throne room, with a throne at the far end and a large chandelier hanging from the ceiling."
                    "The room is empty, and for some reason..."
                    "The world torch is... gone...?"
                    a "Wait... Where's the world torch...?"
                    a "I thought it was supposed to be here...?"
                    a "I thought..."
                    a "..."
                    jump castlegrounds
                "Leave it alone.":
                    scene castlegrounds
                    jump castlegrounds

    hide screen inventory_display_toggle 

label castlequarters:
    show screen inventory_display_toggle # Show the inventory display toggle screen, which will be used to show the inventory item description screen when the player clicks on the "Inventory" button.

    scene quarters
    "You head forward and see the castle quarters, a once lively area now broken and empty."
    menu castlequarterschoices:
        a "Now what...?"
        "Right": # First choice
            if "Corpse" in inventory:
                "No need to go there again..."
                scene quarters
                jump castlequarterschoices
            else:
                scene blackscreen with fade
                "As you head to the right, you enter a room."
                "You find the corpse of a nighthound..."
                "What killed it...?"
                "You shake your head and decide to take the corpse with you, just in case it could be useful..."
                $ inventory.append("Corpse")
                scene quarters with fade
                jump castlequarterschoices
        "Forward": # Second choice
            if "Corpse" in inventory:
                scene blackscreen with fade
                "You see a pedestal holding up a key with the floor having weird lines..."
                "You toss the carcass of the night hound into the floor and set off the trap"
                "The corpse is stabbed by the spikes making it a platform to reach the key."
                $ inventory.append("Gold Key")
                scene castlegrounds
                jump castlegrounds
            else:
                scene quarters
                "You see a pedestal holding up a key with the floor having weird lines..."
                scene blackscreen with fade
                "You step on the floor and set off the trap"
                scene death
                "Spikes shoot out of the floor, impaling you and killing you instantly."
                "You died."
                return



    hide screen inventory_display_toggle


label entrance:
    show screen inventory_display_toggle # Show the inventory display toggle screen, which will be used to show the inventory item description screen when the player clicks on the "Inventory" button.

    scene castlegate
    "You find yourself at the castle gate, it's locked."
    a "..."

    menu entrancechoices:
        "Try to open the gate.": # First choice
            if "Gold Key" in inventory: # If the player has the gold key, they will be able to use it to open the gate and escape. Otherwise, they will just try to open the gate and find that it's locked.
                "You take out the gold key and try it on the gate."
                scene castlegateempty
                "The key fits perfectly, and with a satisfying click, the gate swings open."
                scene blackscreen with fade
                "You step through the gate, leaving the castle grounds behind you."
                "As you walk away, you can't help but feel a sense of relief and freedom."
                "However... your journey has just begun..."
                return
            else: 
                "You try to open the gate, but it's locked tight."
                a "It's locked... I need to find a key or something to open it..."
                jump entrancechoices
        "Leave it alone.":
            scene castlegrounds
            jump castlegroundchoices

    hide screen inventory_display_toggle

    return
