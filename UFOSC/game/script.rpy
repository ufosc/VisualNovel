# Transitions
define longer_fade = Fade(0.5, 1.0, 0.5)
define shorter_fade = Fade(0.5, 0.5, 0.5)

# Characters
define r = Character("Rust", color="#FFA500")
define p = Character("Python")
define c = Character("C++")
define j = Character("Java", color="#964000")
define u = Character("???")

#Rust
image rust_normal = "rustv2Normal.png"
image rust_angry = "rustv1Angry.png"

# Backgrounds
image w0_d1_hotel = "backgrounds/w0_d1_hotel.webp"
image w0_d1_vending = "backgrounds/w0_d1_vending.webp"

# Screens
image mine_sweeper = "images/mine_sweeper.png"

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
