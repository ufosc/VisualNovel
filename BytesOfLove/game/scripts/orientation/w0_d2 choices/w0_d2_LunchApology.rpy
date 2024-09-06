label w0_d2_LunchApology:
    p "\"Hey JavaScript!\""
    p "\"Is it okay if we join you?\""
    js "\"Yeah, sure!\""
    #hide python_happy
    #show python_pocket
    #show cpp_normal at right with dissolve
    mc "\"Lunch was good, I am glad that we got to eat some good food.\""

    menu w0_d2_LunchApologyC:
        mc "\"Hey guys, about what happened on the campus tour...\""

        "Apologize and smooth things over":
            $ c_rep = reputation(c_rep, 2)
            $ p_rep = reputation(p_rep, 2)
            $ js_rep = reputation(js_rep, 2)
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
        js "\"I totally agree, [mc]!\""
        js "\"I think we can be good friends as well.\""
        p "\"Yeah, and it’s so good that we are all computer science majors.\""
        p "\"Hopefully we will have a lot of classes together.\""
        jump w0_d2_AfterLunch
