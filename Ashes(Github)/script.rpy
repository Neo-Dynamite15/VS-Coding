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
    "You step into the hallway, the air growing colder and the darkness seeming to close in around you."
    "The corridor stretches out before you, with doors on either side and a faint light at the end."
    "Your journey has just begun..."

    return
