# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character('Agni', color="#ffae00")

default inventory = []
label start:
    "Darkness...It's all you ever see, a world painted in eternal darkness. A world where light is crucial to your survival."
    "Your name is Agni, and you're a waxborne, a candle-based creature."
    "Your mission is to light the world torch to bring light back to your kingdom."
    "But to do that, you'll need to escape this dungeon."

    scene cellclosed
    "You wake up in a dimly lit cell, the air thick with the scent of damp stone and old wood."

label cell:
    a "I need to find a way out of here. There has to be something I can use."
    show screen inventory_display_toggle

    scene cellclosed
    menu Cellchoices:
        a "Where to look?"
        "Left":
            if "Stick" in inventory:
                scene cellleftempty
                "You see a wall of concrete."
                "You've already picked up the stick."
                scene cellclosed
                jump Cellchoices
            else:
                scene cellleft
                "You see a wall of concrete."
                menu cellleftchoices:

                    "Look at the stick.":
                        if "Stick" in inventory:
                            show cellleftempty
                            "You've already picked up the stick."
                            jump Cellchoices
                        else:
                            show cellleftempty
                            "You pick up the stick and examine it. It's a sturdy piece of wood, about two feet long."
                            "It could be useful..."
                            $ inventory.append("Stick")
                            scene cellclosed
                            jump Cellchoices
                    "leave":
                        scene cellclosed
                        jump Cellchoices            
        "Cell Doors":
            "You see a set of heavy iron doors, locked with a brittle lock."
            menu celldoorschoices:
                "examine the lock.":
                    if "Stick" in inventory:
                        "You take a closer look at the lock. It's old and rusty."
                        "You whack the lock with the stick, trying to break it open."
                        "After a few hits, the lock gives way with a loud snap."
                        scene cellopen
                        "The doors swing open, revealing a dimly lit corridor beyond."
                        jump hallway
                    else:
                        "You take a closer look at the lock. It's old and rusty."
                        jump cell
                "Leave it alone.":
                    scene cellclosed
                    jump Cellchoices
        "Right":
            scene cellright
            "You see a wall of concrete and cracks."
            menu cellrightchoices:
                "stare at the wall.":
                    "You stare at the wall, noticing the cracks and the rough texture."
                    jump cellrightchoices
                "lick the wall.":
                    "You lick the wall, tasting the dampness and the minerals in the stone."
                    "Why did you do that...?"
                    a "Why did I do that...?"
                    jump cellrightchoices
                "leave":
                    scene cellclosed
                    jump Cellchoices
    hide screen inventory_display_toggle

label hallway:
    "You step into the hallway, the air growing colder and the darkness seeming to close in around you."
    "The corridor stretches out before you, with doors on either side and a faint light at the end."
    "Your journey has just begun..."

    return
