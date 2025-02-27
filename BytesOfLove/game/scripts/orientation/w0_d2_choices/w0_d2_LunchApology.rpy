label w0_d2_LunchApology:
    hide python_pocket
    show python_pocket_happy at left
    p "\"Hey JavaScript!\""
    p "\"Is it okay if we join you?\""
    hide python_pocket_happy
    show python_pocket at left
    hide js_normal
    show js_talk
    js "\"Yeah, sure!\""
    hide js_talk
    show js_normal
    mc "\"Lunch was good, I am glad that we got to eat some good food.\""

    menu w0_d2_LunchApologyC:
        mc "\"Hey guys, about what happened on the campus tour...\""

        "Apologize and smooth things over":
            $ c_rep = reputation(c_rep, affection_change)
            $ p_rep = reputation(p_rep, affection_change)
            $ js_rep = reputation(js_rep, affection_change)
            mc "\"I just want to apologize one more time for what happened.\""
            mc "\"I think that we could all be good friends.\""
            mc "\"And I am excited to get to know you guys better in the future.\""

            jump w0_d2_LunchFlirtDecision

        "Don't apologize":
            mc "\"...\""
            mc "\"Huh, I totally forgot what I was about to say.\""
            jump w0_d2_AfterLunch

menu w0_d2_LunchFlirtDecision:
    "Flirt":
        jump w0_d2_LunchFlirt
        
    "Don't Flirt":
        hide js_normal
        show js_talk
        js "\"I totally agree, [mc]!\""
        js "\"I think we can be good friends as well.\""
        hide js_talk
        show js_normal
        hide python_pocket
        show python_pocket_happy at left
        p "\"Yeah, and it’s so good that we are all computer science majors.\""
        p "\"Hopefully we will have a lot of classes together.\""
        hide python_pocket_happy
        show python_pocket at left
        jump w0_d2_AfterLunch
