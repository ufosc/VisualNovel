label w0_d2_StatueSexist:
    p "\"Everyone just shut up!\""
    p "\"It’s not that important and you’re talking over the tour guide!\""
    p "\"[mc] was just having an opinion about the statue.\""
    
    menu w0_d2_StatueSexistC:
        p "\"He didn’t say that anybody was hot or ugly, so let’s all just relax.\""

        "Say something sexist":
            $ p_rep = reputation(p_rep, -4)
            $ js_rep = reputation(js_rep, -4)
            $ c_rep = reputation(c_rep, -4)
            mc "\"Look sweetheart, I don’t need your help here.\""
            p "\"I'M SORRY WHAT!?\""
            js "\"There is no way you just said that.\""
            c "\"Please shut up.\""
        
        "Say something normal":
            mc "\"Thank you, Python.\""
            mc "\"I wasn’t trying to step on any toes.\""

    bsl "\"Uh... I am not a tour guide, I am just the leader of our breakout session.\""
    bsl "\"Which you guys have really been interrupting.\""
    bsl "\"Could you try to keep it down?\""
    mc "{i}Disappointed{/i} \"Sorry...\""

    jump w0_d2_AfterStatue
