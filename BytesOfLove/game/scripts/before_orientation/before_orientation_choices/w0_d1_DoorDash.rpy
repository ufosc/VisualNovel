label w0_d1_DoorDash:
    mc "I passed Chipotle like fifteen times on the way here, I bet I can order some for delivery…"
    scene w0_d1_hotel with shorter_fade
    "*15 minutes later*"
    mc "This driver sucks! I ordered this 30 minutes ago and he still hasn’t picked it up!!!"
    scene w0_d1_hotel with shorter_fade
    "*20 minutes later*"
    mc "Uuuugggghhhhh. I’m so hungry. Can this loser hurry up? It isn’t that hard to deliver food."
    scene w0_d1_hotel with shorter_fade
    "*20 more minutes later, there is a knock at the door*"
    u "Here you go."
    mc "*Annoyed* What took you so long."
    u "*Sigh* Orientation is tomorrow, everyone is ordering food."

    menu w0_d1_DoorDashTip:
        mc "Whatever, at least you finally got here."

        "Tip driver":
            $ pe_rep = reputation(pe_rep, 2)
            $ byte = bytecoin(byte, -35)
            u "Your total is 30 Bytecoin."
            mc "*Hands over 35 Bytecoin*"
            mc "Keep the change, I guess, have a good one."
            u "Mhm."
            u "*Leaves*"
            mc "*Shouts* You're welcome!"
            mc "*To themselves* Some people are just awful…"
            mc "*Closes the door*"
            
        "Don't tip driver":
            $ pe_rep = reputation(pe_rep, -2)
            $ byte = bytecoin(byte, -30)
            u "Your total is 30 Bytecoin."
            mc "*Hands over 30 Bytecoin with no tip*"  
            u "What?! No tip? In this economy! Are you kidding me?!"
            u "*in a serious tone* You have no idea how much trouble I went through to get you your stupid Chipotle…"
            mc "You took eight years to get me my food, which is already cold."
            mc "Get lost, you are lucky I am even paying for this food at all."
            mc "*Slams the door*"
            
    mc "*Looks inside the chipotle bag*"
    mc "*Shocked and angry* WHERE ARE MY CHIPS AND QUESO????"

jump w0_d1_End