# Transitions
define longer_fade = Fade(0.5, 1.0, 0.5)
define shorter_fade = Fade(0.5, 0.5, 0.5)

# Characters
define r = Character("Rust", color="#FFA500")
define p = Character("Python", color="#7DC23B")
define c = Character("C++", color="00599C")
define j = Character("Java", color="#964000")
define js = Character("JavaScript", color="#f7df1e")
define u = Character("???", color="5c5f5d")
define bsl = Character("Breakout Session Leader", color="5c5f5d")

#Rust
image rust_normal = "Rust/Rust_Base_1.png"
image rust_talk = "Rust/Rust_Base_2.png"
image rust_angry = "Rust/Rust_Angry.png"
image rust_confused = "Rust/Rust_ConfusedGlare.png"
default rust_rep = 0

#Java
image java_normal = "Java/Java_Base_1.png"
image java_happy = "Java/Java_Base_2.png"
image java_uh = "Java/Java_MouthOpen.png"
image java_wink = "Java/Java_Wink.png"
default java_rep = 0

#CPP
image cpp_normal = "C++/C++_Base_1.png"
image cpp_happy = "C++/C++_Base_2.png"
image cpp_talk = "C++/C++_Talking.png"

default cpp_rep = 0

#Python
image python_normal = "Python/Python_Base_1.png"
image python_happy = "Python/Python_Base_2.png"
image python_pocket = "Python/Python_HandsPocket_1.png"
image python_pocket_happy = "Python/Python_HandsPocket_2.png"


image python_nojacket_normal = "Python/Python_Base_1.5.png"
image python_nojacket_happy = "Python/Python_Base_2.5.png"



default python_rep = 0

#Javascript
image js_temp = "tempJS.png"
default js_rep = 0

# Backgrounds
image w0_d1_hotel = "backgrounds/w0_d1_hotel.webp"
image w0_d1_vending = "backgrounds/w0_d1_vending.webp"
image w0_d2_sunnyhotel = "backgrounds/w1_d1_sunnyhotel.webp"
image w0_d2_lecturehall = "backgrounds/w1_d1_lecturehall.webp"

image w0_d2_insidecar = "backgrounds/w1_d1_insidecar.webp"
image w0_d2_urgentcar = "backgrounds/w1_d1_urgentcar.webp"

image w0_d2_breakout = "backgrounds/w1_d1_breakoutroom.webp"

image w0_d2_cafeteria = "backgrounds/w1_d1_cafeteria.webp"

image w0_d2_statue = "backgrounds/statuev1.webp"

# Screens
image mine_sweeper = "images/mine_sweeper.png"
image black = "backgrounds/bg black.jpg"

#Audio

# The game starts here.

label start:
    # PROLOUGUE
    "Welcome to Bytes of Love! A visual novel currently being developed by the University of Florida's Open Source Club!"
    "This is an educational dating simulator where you romance programming languages that are represented as anime-style characters while learning about multiple programming languages."
    "If you have any questions or comments about the project, please reach out to anyone in the \"Maintainers\" section of the GitHub!"
    $ mc = renpy.input("Your name: ").strip()

    "Your name is [mc]."

    #jump w1_d1_LunchApology
    
    jump w0_d1

