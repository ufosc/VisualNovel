label w0_d2_StatueDB:
    $ c_rep = reputation(c_rep, -2)
    $ p_rep = reputation(p_rep, -2)
    $ js_rep = reputation(js_rep, -2)
    mc "*Distracted* Wait, guys. Look at that girl over there."
    mc "She is actually so hot, should I go talk to her?"
    p "What are you even talking about, [mc]?"
    js "Yeah, what is wrong with you?"
    js "Were you even listening to the conversation we were having?"
    mc "What? Of course I was!"

    menu w0_d2_GuessingConvo:
        c "Okay, then what were we talking about?"

        "The Political and Economic State of The World":
            jump w0_d2_StatueDBContinue

        "One Piece":
            jump w0_d2_StatueDBContinue

        "The Seahawks should have ran the ball":
            jump w0_d2_StatueDBContinue

label w0_d2_StatueDBContinue:
    c "See? That wasn’t even close to what we were talking about."
    js "I bet you didn’t know what we were talking about because you were too busy staring at that girl!"
    js "You are so into her!"
    mc "Woah, woah, woah, you are getting mad at me?"
    mc "Look at her, she’s a 10!"
    mc "When do you get to see girls THAT cute?"

    menu w0_d2_CuteGroup:
        p "What? We aren’t cute enough?"

        "Say they're cute":
            mc "Well I am not going to sit here and say that you guys aren’t cute…"
            mc "I hope that is a good enough excuse to not be listening to the conversation."

        "Say they're not cute":
            $ c_rep = reputation(c_rep, -2)
            $ p_rep = reputation(p_rep, -2)
            $ js_rep = reputation(js_rep, -2)
            mc "No way! I don’t think that! That’s crazy! I mean-"
            mc "This feels like a trap!"
            mc "I was just looking at that girl, it wasn’t related to you three."
            p "Okay, I get it…"
            mc "No, I meant-"
    
    c "Well I don’t care who you think is or isn’t cute!"
    c "That is no reason to be ignoring us."
    js "Yeah, sorry our conversation isn’t interesting enough for you."
    mc "No, that’s not what I was saying-"
    bsl "Hey you guys are being really loud."
    bsl "Could you try to keep it down?"
    mc "*Sad* Sorry…"

    jump w0_d2_AfterStatue