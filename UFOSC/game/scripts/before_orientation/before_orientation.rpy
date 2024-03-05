label w0_d1:
    image w0_d1_hotel = "backgrounds/w0_d1_hotel.webp"
    scene w0_d1_hotel
    "[mc]" "Man, I can't believe it, I'm really starting my first day at University of Byteborough!"
    "[mc]" "I can't wait for everything I'm going to experience, all the parties, friends, clubs, and ladies! (...if i can even talk to them), my real college life starts tomorrow!!"
    "[mc]" "I'm tired from the drive here, 4 hours was brutal."
    "[mc]" "I'm glad I didn't have to fly here though, I definitely don't have the money for that."
    "[mc]" "I am super grateful my parents gave me this car to take to college, I would be lost without it. They also gave me $50 to get through the weekend."
    "[mc]" "*Stomach rumbles* “Oh man I'm hungry, I guess being on the road all day will do that to you."

    menu w0_d1_BeforeFood:
        "[mc]" "What should I get to eat?"

        "Vending Machine":
            "[mc]" "I think I will go downstairs to the vending machine, I could really go for a Snickers bar and a bag of Doritos right now"
            "[mc]" "And, I will save some money, you never know when you will need it."

            menu w0_d1_VendingMachineMenu:
                "[mc]" "But, I am pretty hungry maybe I should eat some more to fuel my body and mind"

                "Vending Machine":
                    jump w0_d1_VendingMachineAgain

                "Room Service":
                    jump w0_d1_RoomService

                "Doordash":
                    jump w0_d1_DoorDash

        "Room Service":
            jump w0_d1_RoomService

        "Doordash":
            jump w0_d1_DoorDash
  
    label w0_d1_End:
        scene w0_d1_hotel with fade
        "[mc]" "Man that hit the spot. What am I going to do with the rest of my night?"
        "[mc]" "I know I will play some valorant, I have been grinding to go from silver to gold."
        scene w0_d1_hotel with fade
        "*Time passes it is now 11:30*"
        "[mc]" "Now I am Silver III! I just have to win a few more games to push to gold!"

        menu w0_d1_Valorant:
            "[mc]" "Do I play one more ranked game on Valorant so I can get gold rank? Or do I head to bed early so I'm not late in the morning? I have to make big decisions tomorrow when"

            "Gaming grind": 
                "[mc]" "Wow, that was miserable. I went back and forth for 4 hours, and sacrificed my pride and rank."
                "[mc]" "Now It's 3:30, I have deranked to Silver I, and I am so tired. I am literally never going to play this game ever again…"                
                "[mc]" "*Walks over to bed and falls asleep immediately*"

            "Sleeping early":
                "[mc]" "*Shift, turn, shift,..,roll* Jeez, I can't seem to get comfy enough to get some sleep."
                "[mc]" "Maybe I'll watch some YouTube until I feel tired…"

jump w1_d1
