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

    show bg lecturehall with fade

    # TODO: Add audio of class room noises
    
    "Professor" "Today, we are presenting the project every group has been working on for the past month."

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

    show bg lecturehall

    "[mc]" "Alright, time to edit this code."
    
    "[mc]" "All I have to do is create these mines."

    # TODO: Add details about the minesweeper project

    show mine_sweeper

    menu:
        "Which line should I change?"

        "Line 1.":
            "You choose line 1"
        "Line 2":
            "You choose line 2"
    
    hide screen code_editor

    show bg lecturehall with fade

    "[p]" "... And when you start the game, you want to unconver all the squares."

    "[p]" "Like this ..."

    "[p]" "Uhhhh, not like that."

    "[p]" "Let me try that again."

    "[p]" "No, No, no don't do that"

    "Python looks concered"

    # Show concern from python

    "[p]" "Sorry guys, I don't know why this is happening..."

    # Show cpp

    "[c]" "Ugh. Let me do it."

    "C++ takes the computer and clicks again."

    "The program throws the same issue."

    "C++ tries again."

    "[c]" "This can't be happening!"

    "[c]" "Is every square a bomb!?"

    "C++ and Python stare at you, sending a shiver down your spine."

    # Show Java concerned
    "[j]" "I think [mc] wrote the code to display the bombs..."

    "[j]" "But I'm sure he did a great job!"

    # Switch back to cpp who is mad. Add tense music 

    "[c]" "[mc], I though you said you spent all night debugging this code?"

    "[c]" "You said it was working!!!"

    "[mc] is really worried now"

    # Switch back to cpp. She is mad.

    "[c]" "I knew I shouldn't have let you come over last night!"

    "[c]"  "You worthless, good for nothing, mac-using, assembly coding by preference, internshipless, no comment making, no whitespace-using loser!!"

    "Python looks disappointed."

    "[p]" "[mc], you went to her house last night?"

    "[p]" "Right after you left my house??"

    "[p]" "That is not cool!"

    "[p]" "I can't believe you would do this!"

    "Java steps in to defend you."

    "[j]" "I'm sure [mc] didn't mean any harm!"

    # Camera switches to C++

    "[p]" "Yea!"

    "[p]"  "Like what were you guys even doing there??"

    "You open your mouth hesitantly."

    "[mc]" "Uhhhh... paired programming?"

    # Fades to black and intro ends and title "Bytes of Love" shows

    "[mc]" "Welp, I definitely messed up the project for the group, I wonder if I should call someone to apologize."

    menu:

        "Java":
            jump java

        # Add more menu options


label java:

    "You decide to call Java."

    "[mc]" "Hey Java."

    "[mc]" "I'm sorry about yesterday, I-"

    "[j]" "It's okay my little meatball, I understand."

    "[j]" "It actually kind of reminded me of my kid!"



    






screen code_editor:
    add "images/mine_sweeper.png" xpos 500 ypos 500
