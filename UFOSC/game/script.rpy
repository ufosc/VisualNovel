# Transitions
define longer_fade = Fade(0.5, 1.0, 0.5)
define shorter_fade = Fade(0.5, 0.5, 0.5)

# Characters
define r = Character("Rust", color="#FFA500")
define p = Character("Python", color="#7DC23B")
define c = Character("C++", color="00599C")
define j = Character("Java", color="#964000")
define js = Character("JavaScript", color="#f7df1e")
define u = Character("???")
define bsl = Character("Breakout Session Leader")

#Rust
image rust_normal = "rustv2Normal.png"
image rust_angry = "rustv1Angry.png"

#Java
image java_temp = "tempJava.png"

#CPP
image cpp_temp = "tempCPP.png"

#Python
image python_temp = "tempPython.png"

#Javascript
image js_temp = "tempJS.png"

# Backgrounds
image w0_d1_hotel = "backgrounds/w0_d1_hotel.webp"
image w0_d1_vending = "backgrounds/w0_d1_vending.webp"
image w1_d1_sunnyhotel = "backgrounds/w1_d1_sunnyhotel.webp"
image w1_d1_lecturehall = "backgrounds/w1_d1_lecturehall.jpg"

image w1_d1_insidecar = "backgrounds/w1_d1_insidecar.webp"
image w1_d1_urgentcar = "backgrounds/w1_d1_urgentcar.webp"

image w1_d1_breakout = "backgrounds/breakoutRoom.webp"

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

    jump w0_d1

