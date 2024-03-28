label w0_d1:
    scene w0_d1_hotel

    mc "Man, I can't believe it, tomorrow is the first day of orientation at the University of Byteborough."
    mc "I can't wait for everything I'm going to experience, all the parties, friends, clubs, and ladies!"
    mc "If I can even talk to them..."
    mc "I’m tired from the drive here, 4 hours was brutal."
    mc "But at least I didn’t have to fly, I definitely don’t have the money for that."
    mc "I am super grateful my parents gave me a new car for college though."
    mc "I don’t know what I’d do without it..."
    mc "They also gave me 50 Bytecoin to get through the weekend."
    mc "{i}*Stomach rumbles*{/i}"
    mc "Oh man, I’m hungry. I guess being on the road all day will do that to you."

    menu w0_d1_BeforeFood:
        mc "What should I get to eat?"

        "Vending Machine":
            jump w0_d1_VendingMachine

        "Room Service":
            jump w0_d1_RoomService

        "Doordash":
            jump w0_d1_DoorDash
  
    label w0_d1_End:
        scene w0_d1_hotel with longer_fade
        mc "Man that hit the spot."
        mc "What am I going to do with the rest of my night?"
        mc "I know I’ll play some Valorant. I’ve been grinding so I can go from silver to gold."
        #Add clock below when it is made - Lazzy
        scene w0_d1_hotel with shorter_fade
        "{i}*Time passes it's now 11:30PM*{/i}"
        mc "Now I’m Silver 3! I just have to win a few more games to push to gold!"
        mc "Do I play one more ranked game so I can get gold, or do I head to bed early so I'm not late in the morning?"

        menu w0_d1_Valorant:
            mc "I have a big day tomorrow."

            "Gaming grind": 
                scene w0_d1_hotel with shorter_fade
                mc "{i}*4 hours later*{/i}"
                mc "Wow, that was miserable. I went back and forth for 4 hours, and sacrificed my pride and rank."
                mc "Now it’s 3:30 AM, I deranked to Silver I, and I am so tired."                
                mc "I am literally never going to play this game ever again…"
                "{i}*You walk over to your bed and fall asleep immediately*{/i}"

            "Sleeping early":
                mc "{i}*Shift, turn, shift, roll*{/i}"
                mc "Jeez, I can't seem to get comfy enough to fall asleep."
                mc "Maybe I'll watch some YouTube until I feel tired…"
                # Cant add this until we decide background artstyle - Lazzy

jump w0_d2
