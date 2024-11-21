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
define p = Character("???", color="#7DC23B")
define c = Character("???", color="00599C")
define j = Character("Java", color="#964000")
define js = Character("???", color="#FFD700")
define u = Character("???", color="#5c5f5d")
define a = Character("Advisor", color="#f4f880")

#CHANGE PERL COLOR
define pe = Character("Perl", color="5c5f5d")
define bsl = Character("Breakout Session Leader", color="5c5f5d")

#Rust
image rust_normal = "Rust/Rust_Base_1.png"
image rust_talk = "Rust/Rust_Base_2.png"
image rust_angry = "Rust/Rust_Angry.png"
image rust_confused = "Rust/Rust_ConfusedGlare.png"

image rust_wave = "Rust/Rust_Wave.png"
image rust_wave_talking = "Rust/Rust_Wave_1.png"
default r_rep = 50

#Java
image java_normal = "Java/Java_Base_1.png"
image java_happy = "Java/Java_Base_2.png"
image java_uh = "Java/Java_MouthOpen.png"
image java_wink = "Java/Java_Wink.png"
image java_angry = "Java/Java_Angry.png"

image java_glasses_normal = "Java/Java_Base_Glasses.png"
image java_glasses_happy = "Java/Java_Base_Glasses_2.png"
image java_glasses_angry = "Java/Java_Angry_Glasses.png"
image java_glasses_uh = "Java/Java_Glasses_MouthOpen.png"
default j_rep = 50

#CPP
image cpp_normal = "C++/C++_Base_1.png"
image cpp_happy = "C++/C++_Base_2.png"
image cpp_talk = "C++/C++_Talking.png"

image cpp_angry = "C++/C++_Angry.png"
image cpp_angry_talk = "C++/C++_AngryTalking.png"

image cpp_handhip_talk = "C++/C++_Base_HandHip.png"
image cpp_handhip_normal = "C++/C++_Base_HandHip_1.png"
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
image js_blush = "JavaScript/JavaScript_BlushSmile.png"
image js_angry = "JavaScript/JavaScript_Angry.png"

default js_rep = 50

#Perl
default pe_rep = 50


#background characters with no impact
#this needs to be changed to the final character image for the advisor
image advisor = "SideCharacters/advisor_tempImage.png"


# Backgrounds
'''
the following structure will be used for each of the images that need a different day image
all that will need to be added to each of the files is what the global energy variable is set to

while true:
    if energy == 4: 
        image image_name = "map_images/image_morning"



    elif energy == 3:
        image image_name = "map_images/image_afternoon"


    elif energy == 2:
        image image_name = "map_images/image_evening"
    
    
    elif energy == 1:    
        image image_name = "map_images/image_night"
return

'''
image instruction_screen = "backgrounds/instruction_screen.png"
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

image w0_d3_buffet = "backgrounds/hotelBuffet.jpg"


#new backgrounds 
image breakout_room = "backgrounds/breakout-room.PNG"
image campus_pathway = "backgrounds/campus_pathway.PNG"
image dining_hall = "backgrounds/dining-hall.PNG"
image driving_car = "backgrounds/driving-car.png"
image empty_lecture_hall = "backgrounds/empty-lecture-hall.png"
image full_lecture_hall = "backgrounds/full-lecture-hall.png"
image hotel_buffet = "backgrounds/hotel-buffet.png"
image hotel_room_day = "backgrounds/hotel-room-day.png"
image hotel_room_night = "backgrounds/hotel-room-night.png"
image office = "backgrounds/office.PNG"
image parking_lot = "backgrounds/parking-lot.png"
image starting_car = "backgrounds/starting-car.png"
image statue_garden = "backgrounds/statue-garden.PNG"
image vending_machine = "backgrounds/vending-machine.PNG"








image w0_d3_Advisor = "backgrounds/ciseDungeon.png"

image w0_d3_parkingLot = "backgrounds/IMG_3556.jpg"


# Day/Night Cycle
default energy = 0
transform morning_tint:
    matrixcolor TintMatrix("#FFFFFF") # no tint
transform afternoon_tint:
    matrixcolor TintMatrix("#FFD700") # afternoon tint
transform sunset_tint:
    matrixcolor TintMatrix("#FF4500") # sunset tint
transform night_tint:
    matrixcolor TintMatrix("#2C3E50") # night tint

# Code below can be placed at the beginning of scenes to implement tint
# $ energy = "Insert #"
# if energy == 0:
#     show  "Insert Backgound Image" at morning_tint
# if energy == 1:
#     show  "Insert Backgound Image" at afternoon_tint
# if energy == 2:
#     show  "Insert Backgound Image" at sunset_tint
# if energy == 3:
#     show  "Insert Backgound Image" at night_tint
    

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
    scene campus_pathway with shorter_fade
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

