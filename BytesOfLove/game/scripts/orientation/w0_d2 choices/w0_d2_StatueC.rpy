label w0_d2_StatueC:
    $ c_rep = reputation(c_rep, 2)
    $ p_rep = reputation(p_rep, -2)
    $ js_rep = reputation(js_rep, -2)
    mc "Yep, I totally knew that. It’s pretty insensitive of Python to support someone like that."
    p "I seriously didn’t know, jeez..."
    p "You guys don’t need to be mean about it."
    c "At least someone knows what they’re talking about, thanks, [mc]."
    js "There is no way you knew that!"
    js "And even if you did, C++ is being so mean, there’s no need to be nasty!"
    js "I bet you’re just agreeing with her because you think she’s cute!"
    js "God, men are so shallow!"
    mc "*Flustered* No, not at all! I seriously mean what I said."
    
    # Short choice decided other file was not neccessary - Lazzy
    menu w0_d2_CuteC:
        c "Hm, so you don’t think I’m cute?"

        "Admit C++ is cute":
            $ c_rep = reputation(c_rep, 2)
            mc "*Flustered*"
            mc "Well... that’s not what I was saying."
            mc "I do think you’re kinda cute..."
            c "*Blushes*"
            js "Ugh I knew it!"
            #this \/ line is good but awarge
            js "Stop being such a simp!" 
            js "So typical of boys to only care about looks."
            js "C++, don’t think you’re right just because this guy agrees with you!"
            c "And what would you know about being right?"
            c "You’re just jealous he didn’t take your side!"
            js "I wouldn’t want someone so superficial to agree with me anyway!"
            mc "Woah, I’m not superficial, I just think-"
            c "[mc], be quiet. This isn’t even about you!"

        "Call out C++":
            $ c_rep = reputation(c_rep, -2)
            mc "Don’t go fishing for a compliment just because I agreed with you..."
            mc "I agree that Python shouldn’t go around calling statues cool without knowing what they represent."
            mc "That's it."
            c "So you think I’m ugly!?"
            mc "I-"
            js "Why are you begging for his attention C++?"
            js "This isn’t about you, it’s about the statue."
            js "Or did you forget what you were mad about already?"
            c "Okay sugar queen, no one asked you for your input."
            c "You’re just mad because he didn’t take your side."
            js "At least he doesn’t think I’m ugly..."
            c "Excuse me!?"
            mc "I never said-"
    
    jump w0_d2_StatueSexist