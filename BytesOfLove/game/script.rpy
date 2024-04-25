# Transitions
define longer_fade = Fade(0.5, 1.0, 0.5)
define shorter_fade = Fade(0.5, 0.5, 0.5)

# Transformations
transform speaking:
    zoom 1.0 # The character is in their normal state when speaking

transform not_speaking:
    zoom 0.95 # Slightly smaller
    xalign 0.5
    yalign 0.5
 
    #EX: show python_normal at speaking

# Music

# Characters
define r = Character("Rust", color="#B27300")
define p = Character("Python", color="#7DC23B")
define c = Character("C++", color="00599C")
define j = Character("Java", color="#964000")
define js = Character("JavaScript", color="#FFD700")
define u = Character("???", color="5c5f5d")

#CHANGE PERL COLOR
define pe = Character("Perl", color="5c5f5d")
define bsl = Character("Breakout Session Leader", color="5c5f5d")

#Rust
image rust_normal = "Rust/Rust_Base_1.png"
image rust_talk = "Rust/Rust_Base_2.png"
image rust_angry = "Rust/Rust_Angry.png"
image rust_confused = "Rust/Rust_ConfusedGlare.png"
default r_rep = 50

#Java
image java_normal = "Java/Java_Base_1.png"
image java_happy = "Java/Java_Base_2.png"
image java_uh = "Java/Java_MouthOpen.png"
image java_wink = "Java/Java_Wink.png"
default j_rep = 50

#CPP
image cpp_normal = "C++/C++_Base_1.png"
image cpp_happy = "C++/C++_Base_2.png"
image cpp_talk = "C++/C++_Talking.png"

default c_rep = 50

#Python
image python_normal = "Python/Python_Base_1.png"
image python_happy = "Python/Python_Base_2.png"
image python_pocket = "Python/Python_HandsPocket_1.png"
image python_pocket_happy = "Python/Python_HandsPocket_2.png"


image python_nojacket_normal = "Python/Python_Base_1.5.png"
image python_nojacket_happy = "Python/Python_Base_2.5.png"

image python_angry_talk = "Python/Python_HandsPocket_Angry.png"
image python_angry = "Python/Python_HandsPocket_Angry2.png"

default p_rep = 50

#Javascript
image js_normal = "JavaScript/JavaScript_Base_1.png"
image js_smirk = "JavaScript/JavaScript_Smirk.png"
image js_talk = "JavaScript/JavaScript_Talking.png"

default js_rep = 50

#Perl
default pe_rep = 50

# Backgrounds
image w0_d1_hotel = "backgrounds/w0_d1_hotel.webp"
image w0_d1_vending = "backgrounds/w0_d1_vending.webp"
image w0_d2_sunnyhotel = "backgrounds/w1_d1_sunnyhotel.webp"
image w0_d2_lecturehall = "backgrounds/w1_d1_lecturehall.webp"

image test = "backgrounds/IMG_3556.jpg"
image test2 = "backgrounds/IMG_3563.jpg"
image test3 = "backgrounds/IMG_3595.jpg"

image w0_d2_insidecar = "backgrounds/w1_d1_insidecar.webp"
image w0_d2_urgentcar = "backgrounds/w1_d1_urgentcar.webp"

image w0_d2_breakout = "backgrounds/w1_d1_breakoutroom.webp"

image w0_d2_cafeteria = "backgrounds/w1_d1_cafeteria.webp"

image w0_d2_statue = "backgrounds/statuev1.webp"

# Screens
image mine_sweeper = "images/mine_sweeper.png"
image black = "backgrounds/black-background.png"

# Bytecoin
default byte = 50

init python:
    def reputation(rep, effect):
        min = 0
        max = 100
        rep = rep + effect

        if rep > max:
            rep = max

        elif rep < min:
            rep = min

        return rep

    def bytecoin(bytecoin, effect):
        min = 0
        bytecoin = bytecoin + effect

        if bytecoin < min:
            bytecoin = min

        return bytecoin


# The game starts here.

label start:
    stop music fadeout 4
    # PROLOUGUE
    "Welcome to Bytes of Love! A visual novel currently being developed by the University of Florida's Open Source Club!"
    "This is an educational dating simulator where you build relationships with other programming languages that are represented as anime-style characters."
    "Throughout the game, these characters will immerse you into computer science and the college experience."
    "The choices you make will affect your standing with other characters and influence the events you experience."
    default check = True
    while check:
        $ mc = renpy.input("Your name: ", length=12).strip()
        if mc.isalpha() and " " not in mc:
            $ mc = mc.capitalize()
            $ check = False
        elif not mc:
            "Please enter a name"
        else:
            "Please enter a single word name using only alphabetic characters."

    "Your name is [mc]."

    #jump w1_d1_LunchApology
    
    jump w0_d1

