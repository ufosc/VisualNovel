label w0_d2_LunchFlirt:
    menu w0_d2_LunchFlirtC:
        "Flirt with Python":
            $ p_rep = reputation(p_rep, -2)
            mc "Especially you Python."
            mc "{i}*Winks*{/i}"
            p "Wow, way to ruin an apology."
            p "I expected nothing less."
            c "Typical man..."
        "Flirt with C++":
            $ c_rep = reputation(c_rep, -2)
            mc "Especially you C++."
            mc "{i}*Winks*{/i}"
            c "Wow, way to ruin an apology."
            c "I expected nothing less."
            js "What a simp..."

        "Flirt with JavaScript":
            $ js_rep = reputation(js_rep, -2)
            mc "Especially you JavaScript."
            mc "{i}*Winks*{/i}"
            js "Wow, way to ruin an apology."
            js "I expected nothing less."
            c "Men..."

        "Everyone":
            $ p_rep = reputation(p_rep, -6)
            $ js_rep = reputation(js_rep, -6)
            $ c_rep = reputation(c_rep, -6)
            mc "Maybe I could get to know all of you really well back at my hotel tonight..."
            c "What the actual fuck is wrong with you."
            c "That is so disgusting."
            p "I can’t believe you, you are despicable."
            js "I think I might actually throw up..."

    mc "Hmm, I thought that would go differently."
    mc "Can’t blame me, shooters gotta shoot..."

    jump w0_d2_AfterLunch
