label w0_d2_StatueDB:
    $ c_rep = reputation(c_rep, -2)
    $ p_rep = reputation(p_rep, -2)
    $ js_rep = reputation(js_rep, -2)
    hide python_pocket_happy
    show python_pocket at left
    hide cpp_talk
    show cpp_normal
    hide js_talk
    show js_normal at right
    mc "{i}Distracted{/i} \"Wait, guys. Look at that girl over there.\""
    mc "\"She is actually so hot, should I go talk to her?\""
    hide python_pocket_happy
    show python_angry_talk at left
    p "\"What are you even talking about, [mc]?\""
    hide python_angry_talk
    show python_angry at left
    hide js_normal
    show js_talk at right
    js "\"Yeah, what is wrong with you?\""
    js "\"Were you even listening to the conversation we were having?\""
    hide js_talk
    show js_normal at right
    mc "\"What? Of course I was!\""
    hide cpp_normal
    show cpp_talk

    menu w0_d2_GuessingConvo:
        c "\"Okay, then what were we talking about?\""

        "\"The political and economic state of the world\"":
            jump w0_d2_StatueDBContinue

        "\"Breaking Bad\"":
            jump w0_d2_StatueDBContinue

        "\"The Seahawks should have ran the ball\"":
            jump w0_d2_StatueDBContinue

label w0_d2_StatueDBContinue:
    c "\"See? That wasn’t even close to what we were talking about.\""
    hide cpp_talk
    show cpp_normal
    hide js_normal
    show js_talk at right
    js "\"I bet you didn’t know what we were talking about because you were too busy staring at that girl!\""
    js "\"You are sooo into her!\""
    hide js_talk
    show js_normal at right
    mc "\"Woah, woah, woah. You’re getting mad at me?\""
    mc "\"Look at her, she’s a 10!\""
    mc "\"When do you get to see girls THAT cute?\""
    hide python_angry
    show python_angry_talk at left

    menu w0_d2_CuteGroup:
        p "\"What? Aren’t we cute enough?\""

        "Admit the girls are cute":
            hide python_angry_talk
            show python_angry at left
            mc "\"Well I am not going to sit here and say that you guys aren’t cute...\""
        
        "Deny that they're cute":
            $ c_rep = reputation(c_rep, -2)
            $ p_rep = reputation(p_rep, -2)
            $ js_rep = reputation(js_rep, -2)
            hide python_angry_talk
            show python_angry at left
            mc "\"No way! I don’t think that! That’s crazy! I mean-\""
            mc "\"This feels like a trap!\""
            mc "\"I was just looking at that girl, it wasn’t related to you three.\""
            hide python_angry
            show python_angry_talk at left
            p "\"Okay, I see how it is...\""
            hide python_angry_talk
            show python_angry at left
            mc "\"No, I meant-\""
    
    hide cpp_normal
    show cpp_angry_talk
    c "\"Well I don’t care who you think is or isn’t cute!\""
    c "\"That’s no reason to be ignoring us.\""
    hide cpp_angry_talk
    show cpp_normal
    hide js_normal
    show js_talk at right
    js "\"Yeah, sorry our conversation isn’t interesting enough for you.\""
    hide js_talk
    show js_normal at right
    mc "\"No, that’s not what I was saying-\""
    show bsl_talk
    bsl "\"Hey you guys are being really loud.\""
    bsl "\"Could you try to keep it down?\""
    hide bsl_talk
    show bsl_normal
    mc "\"Sorry...\""

    jump w0_d2_AfterStatue