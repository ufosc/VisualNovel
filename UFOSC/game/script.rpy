#Characters
define python = Character("Python")

#Backgrounds

#Audio


# The game starts here.

label start:

    $ player_name = renpy.input("Your name: ").strip()

    "Your name is [player_name]."

    return