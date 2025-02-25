label w0_d2_StatueC:
    $ c_rep = reputation(c_rep, affection_change)
    $ p_rep = reputation(p_rep, -affection_change)
    $ js_rep = reputation(js_rep, -affection_change)
    hide python_pocket_happy
    show python_angry at left
    hide cpp_talk
    show cpp_normal
    show js_normal at right
    mc "\"Yep, I totally knew that. It’s pretty insensitive of Python to support someone like that.\""
    hide python_angry
    show python_angry_talk at left
    p "\"I seriously didn’t know, jeez...\""
    p "\"You guys don’t need to be mean about it.\""
    hide python_angry_talk
    show python_angry at left
    hide cpp_normal
    show cpp_handhip_talk
    c "\"At least someone knows what they’re talking about, thanks, [mc].\""
    hide cpp_handhip_talk
    show cpp_normal
    hide js_normal
    show js_talk at right
    js "\"There is no way you knew that!\""
    js "\"And even if you did, C++ is being so mean, there’s no need to be nasty!\""
    js "\"I bet you’re just agreeing with her because you think she’s cute!\""
    js "\"God, men are so shallow!\""
    hide js_talk
    show js_normal at right
    mc "{i}Flustered{/i} \"No, not at all! I seriously mean what I said.\""
    hide cpp_normal
    show cpp_talk
    
    # Short choice decided other file was not neccessary - Lazzy
    menu w0_d2_CuteC:
        c "\"Hm, so you don’t think I’m cute?\""

        "Admit C++ is cute":
            $ c_rep = reputation(c_rep, affection_change)
            hide cpp_talk
            show cpp_normal
            mc "{i}Flustered{/i}"
            mc "\"Well... that’s not what I was saying.\""
            mc "\"I do think you’re kinda cute...\""
            hide cpp_normal
            show cpp_happy
            c "{i}Blushes{/i}"
            hide js_normal
            show js_talk at right
            js "\"Ugh I knew it!\""
            #this \/ line is good but awarge
            js "\"Stop being such a simp!\"" 
            js "\"So typical of boys to only care about looks.\""
            js "\"C++, don’t think you’re right just because this guy agrees with you!\""
            hide js_talk
            show js_angry at right
            hide cpp_happy
            show cpp_angry_talk
            c "\"And what would you know about being right?\""
            c "\"You’re just jealous he didn’t take your side!\""
            hide cpp_angry_talk
            show cpp_angry
            hide js_angry
            show js_talk at right
            js "\"I wouldn’t want someone so superficial to agree with me anyway!\""
            hide js_talk
            show js_angry at right
            mc "\"Woah, I’m not superficial, I just think-\""
            hide cpp_angry
            show cpp_angry_talk
            c "\"[mc], be quiet. This isn’t even about you!\""
            hide cpp_angry_talk
            show cpp_angry

        "Call out C++":
            $ c_rep = reputation(c_rep, -affection_change)
            hide cpp_talk
            show cpp_normal
            mc "\"Don’t go fishing for a compliment just because I agreed with you...\""
            mc "\"I agree that Python shouldn’t go around calling statues cool without knowing what they represent.\""
            mc "\"That's it.\""
            hide cpp_talk
            show cpp_angry_talk
            c "\"So you think I’m ugly!?\""
            hide cpp_angry_talk
            show cpp_angry
            mc "\"I-\""
            hide js_angry
            show js_talk at right
            js "\"Why are you begging for his attention C++?\""
            js "\"This isn’t about you, it’s about the statue.\""
            js "\"Or did you forget what you were mad about already?\""
            hide js_talk
            show js_normal
            hide cpp_angry
            show cpp_angry_talk
            c "\"Okay sugar queen, no one asked you for your input.\""
            c "\"You’re just mad because he didn’t take your side.\""
            hide cpp_angry_talk
            show cpp_angry
            hide js_normal
            show js_talk at right
            js "\"At least he doesn’t think I’m ugly...\""
            hide js_talk
            show js_normal at right
            hide cpp_angry
            show cpp_angry_talk
            c "\"Excuse me!?\""
            hide cpp_angry_talk
            show cpp_angry
            mc "\"I never said-\""
    
    jump w0_d2_StatueSexist