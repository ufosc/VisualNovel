# Characters
define p = Character("Python")
define c = Character("C++")
define j = Character("Java")

# Backgrounds
image bg lecturehall = "backgrounds/bg lecturehall.jpg"
image bg black = "backgrounds/bg black.jpg"

# Screens
image mine_sweeper = "images/mine_sweeper.png"

#Audio

# The game starts here.

label start:
    # PROLOUGUE

    $ mc = renpy.input("Your name: ").strip()

    "Your name is [mc]."

    # FOR DEBUGGIN SCENES
    jump mine_sweeper

    show bg lecturehall with fade

    # TODO: Add audio of class room noises
    
    "Professor" "Today is the day we are presenting the project every group has been working on for the past month."

    "Professor" "First we have [mc]'s group."

    "Professor" "Come up to the front to present."

    # Switch to cpp have her fade in or something

    # TODO: Replace character with cpp
    show sylvie blue normal

    c "Hey [mc], you finished the project right?"
    
    c "This is like 25 percent of our grade!"

    "[mc]" "Yeah for sure"

    "[mc]" "*yawns*"

    "[mc]" "I even spent two hours debugging the whole thing."

    "[mc]" "You don't have to worry about anything."

    hide sylvie

    # Show disgusted look from python

    show bg black with fade

    "You recall the events last night..."


label mine_sweeper:
    show bg lecturehall

    "[mc]" "Alright, time to edit this code."
    
    "[mc]" "All I have to do is create these mines."

    show screen code_editor

    menu:
        "Which line should I change?"

        "Line 1.":
            "You choose line 1"
        "Line 2":
            "You choose line 2"




screen code_editor:
    add "images/mine_sweeper.png" xpos 500 ypos 500
