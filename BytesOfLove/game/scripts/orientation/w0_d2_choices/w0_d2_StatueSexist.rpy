label w0_d2_StatueSexist:
    hide python_angry
    show python_angry_talk at left
    p "\"Everyone just shut up!\""
    p "\"It’s not that important and you’re talking over the tour guide!\""
    p "\"[mc] was just having an opinion about the statue.\""
    hide python_angry_talk
    show python_angry at left

    menu w0_d2_StatueSexistC:
        p "\"He didn’t say that anybody was hot or ugly, so let’s all just relax.\""

        "Say something sexist":
            $ p_rep = reputation(p_rep, -4)
            $ js_rep = reputation(js_rep, -4)
            $ c_rep = reputation(c_rep, -4)
            mc "\"Look sweetheart, I don’t need your help here.\""
            hide python_angry
            show python_angry_talk at left
            p "\"I'M SORRY WHAT!?\""
            hide python_angry_talk
            show python_angry at left
            hide js_angry
            show js_talk at right
            js "\"There is no way you just said that.\""
            hide js_talk
            show js_angry at right
            hide cpp angry
            show cpp_angry_talk
            c "\"Please shut up.\""
            hide cpp_angry_talk
            show cpp_angry
        
        "Say something normal":
            mc "\"Thank you, Python.\""
            mc "\"I wasn’t trying to step on any toes.\""

    
    bsl "\"Uh... I am not a tour guide, I am just the leader of our breakout session.\""
    bsl "\"Which you guys have really been interrupting.\""
    bsl "\"Could you try to keep it down?\""
    mc "\"Sorry...\""

    jump w0_d2_AfterStatue
