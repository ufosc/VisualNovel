#Characters
define python = Character("Python")

#Backgrounds
image bg lecturehall = "backgrounds/bg lecturehall.jpg"

#Audio


# The game starts here.

label start:

    show bg lecturehall

    $ player_name = renpy.input("Your name: ").strip()

    "Your name is [player_name]."

    jump test_menu

    return

label test_menu:

    show bg lecturehall

    "Hi [player_name]"

screen hello_world():
    tag example
    zorder 1
    modal false

    text "Hello World"