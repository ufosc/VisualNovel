#Characters
define python = Character("Python")

#Backgrounds
image bg lecturehall = "backgrounds/bg lecturehall.jpg"
image bg black = "backgrounds/bg black.jpg"

#Audio


# The game starts here.

label start:

    show bg black

    $ player_name = renpy.input("Your name: ").strip()

    "Your name is [player_name]."

    jump test_menu

    return

label test_menu:
    show screen hello_world
    "Hi [player_name]"


screen hello_world:

    text "Void PlaceMines(int totalSquares, int minesToPlace)" yalign 0.5 xalign 0.5