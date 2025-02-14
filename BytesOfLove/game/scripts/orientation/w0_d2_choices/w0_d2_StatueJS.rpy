label w0_d2_StatueJS:
    $ p_rep = reputation(p_rep, 2)
    $ js_rep = reputation(js_rep, 2)
    $ c_rep = reputation(c_rep, -2)
    hide js_talk
    show js_normal at right
    hide python_pocket_happy
    show python_pocket at left
    mc "\"I agree with JavaScript and Python, you need to take a chill pill C++.\""
    mc "\"He does look cool, I didn’t realize that was ‘Firewall’ Jackson either.\""
    hide js_normal
    show js_normal at right
    hide cpp_talk
    show cpp_angry_talk
    c "\"Ugh whatever.\""
    c "\"You guys need to be more knowledgeable, though, it’s embarrassing.\""
    hide cpp_angry_talk
    show cpp_angry
    hide js_normal
    show js_talk at right
    js "\"That is ridiculous, why do you even know that?\""
    hide js_talk
    show js_normal at right
    hide cpp_angry
    show cpp_angry_talk
    c "\"Who doesn’t know that?\""
    c "\"Have you ever taken a history class?\""
    hide cpp_angry_talk
    show cpp_angry
    hide js_normal
    show js_talk at right
    js "\"Yes I have!\""
    js "\"You are being so mean right now, C++, there’s no need to be nasty!\""
    js "\"I bet you’re just mad because [mc] doesn’t agree with you.\""
    hide js_talk
    show js_normal at right
    hide cpp_angry
    show cpp_handhip_talk
    c "\"Well [mc] is only agreeing with you because he thinks you’re cute.\""
    hide cpp_handhip_talk
    show cpp_handhip_normal
    mc "{i}Flustered{/i} \"Whoa whoa whoa, I never said that.\""
    hide js_normal
    show js_smirk at right

    menu w0_d2_CuteJS:
        js "\"Hm, so do you think I’m cute?\""

        "Admit JavaScript is cute":
            $ js_rep = reputation(js_rep, 2)
            mc "{i}Flustered{/i}"
            mc "\"Well... that’s not exactly what I was saying...\""
            mc "\"But, I do think you’re kind of cute.\""
            hide js_smirk
            show js_blush at right
            js "{i}Blushes{/i} \"Well that makes sense…\""
            hide cpp_handhip_normal
            show cpp_handhip_talk
            c "\"Ugh I knew it!\""
            c "\"So typical of boys to only care about looks.\""
            c "\"JavaScript, don’t think you’re right just because this guy agrees with you!\""
            hide cpp_handhip_talk
            show cpp_handhip_normal
            hide js_blush
            show js_talk at right
            js "\"And what would you know about being right?\""
            js "\"You’re just mad because he didn’t take your side!\""
            hide js_talk
            show js_smirk at right
            hide cpp_handhip_normal
            show cpp_handhip_talk
            c "\"I wouldn’t want someone so superficial to agree with me anyway!\""
            hide cpp_handhip_talk
            show cpp_handhip_normal
            mc "\"Woah, I’m not superficial, I just think--\""

        "Call out JavaScript":
            $ js_rep = reputation(js_rep, -2)
            mc "\"Alright, don’t go fishing for a compliment just because I agreed with you...\""
            mc "\"I agree that Python shouldn’t go around calling statues cool without knowing what they represent.\""
            mc "\"That's it.\""
            hide js_smirk
            show js_talk at right
            js "\"So you think I'm ugly!?\""
            hide js_talk
            show js_angry at right
            mc "\"I-\""
            hide cpp_handhip_normal
            show cpp_talk
            c "\"Why are you begging for his attention, JavaScript?\""
            c "\"This isn’t about you, it’s about the statue.\""
            c "\"Or did you forget what you were so mad about already?\""
            hide cpp_talk
            show cpp_handhip_normal
            hide js_angry
            show js_talk at right
            js "\"Listen, know it all, no one asked you for your input in the first place.\""
            js "\"You’re just mad because he didn’t take your side.\""
            hide js_talk
            show js_angry at right
            hide cpp_handhip_normal
            show cpp_handhip_talk
            c "\"At least he doesn’t think I’m ugly...\""
            hide cpp_handhip_talk
            show cpp_handhip_normal
            hide js_angry
            show js_talk at right
            js "\"Excuse me!?\""
            hide js_talk
            show js_normal at right
            mc "\"I never said-\""
    
    jump w0_d2_StatueSexist