label w0_d1_DoorDash:
    mc "I passed like 15 Chipotles on the way here, I bet I can order a burrito for dinner..."
    # Edit transitions below when we have clock - Lazzy
    scene hotel_room_night with shorter_fade
    "{i}*30 minutes later*{/i}"
    mc "This driver sucks! I ordered this 30 minutes ago, and he still hasn’t picked it up!!!"
    scene hotel_room_night with shorter_fade
    "{i}*20 minutes later*{/i}"
    mc "Uuuugggghhhhh. I’m so hungry. Can this loser hurry up? It isn’t that hard to deliver food."
    scene hotel_room_night with shorter_fade
    "{i}*20 more minutes later, there is a knock at the door*{/i}"
    u "\"Are you [mc]? I’ve got your food.\""
    mc "{i}*Annoyed*{/i} \"What took you so long?\""

    u "{i}*Sigh*{/i} \"Orientation is tomorrow, so everyone is ordering food right now.\""

    menu w0_d1_DoorDashTip:
        mc "\"Whatever, at least you finally got here.\""

        "Tip the driver":
            $ pe_rep = reputation(pe_rep, affection_change)
            $ byte = bytecoin(byte, -35)
            u "\"Your total is 30 Bytecoin.\""
            mc "{i}*Hands over 35 Bytecoin*{/i}"
            mc "\"Keep the change, I guess, have a good one.\""
            u "\"Thank you.\""
            mc "\"No problem.\""
            mc "{i}*Closes the door*{/i}"
            
        "Don't tip the driver":
            $ pe_rep = reputation(pe_rep, -affection_change)
            $ byte = bytecoin(byte, -30)
            u "\"Your total is 30 Bytecoin.\""
            mc "{i}*Hands over 30 Bytecoin with no tip*{/i}"  
            u "\"What?! No tip? In this economy! Are you kidding me?!\""
            u "{i}*in a serious tone*{/i} \"You have no idea how much trouble I went through to get you your stupid Chipotle...\""
            mc "\"You took eight years to get me my food, which is already cold.\""
            mc "\"Get lost, you’re lucky I’m even paying for this food at all.\""
            mc "{i}*Slams the door*{/i}"
            
    mc "{i}*Looks inside the chipotle bag*{/i}"
    mc "{i}*Shocked and angry*{/i} WHERE ARE MY CHIPS AND QUESO????"

jump w0_d1_End