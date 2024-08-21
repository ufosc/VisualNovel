label w0_d3_MeetingRust:

    if r_rep == 50:
        r "\"Hey there! My name is Rust.\""
        show rust_normal at right with dissolve 


        menu w0_d3_FirstTimeRust:
            r "\"You look about my age, do you go to UB?\""
            
            "Be mean":
                $ r_rep = reputation(r_rep, -2)
                mc "\"Yeah, I do, my name is [mc].\""
                r "\"Cool, you seem chill. What’s your major?\""
                mc "\"Wouldn’t you like to know...\""
                
                hide rust_normal 

                show rust_angry at right

                r "\"Damn, I was just wondering.\""
                r "\"I’m in Computer Engineering, in case you wanted to know mine.\""
                mc "\"Oh thanks, I didn’t want to know.\""
                r "\"Jeez, you don’t have to be mean about it, man.\""
                mc "\"Whatever.\""
                hide rust_angry with dissolve
                "{i}Rust leaves{/i}"

            "Be nice":
                $ r_rep = reputation(r_rep, 2)
                mc "\"Yeah I do! My name is [mc], nice to meet you!\""
                mc "\"What major are you?\""
                r "{i}*Smiles*{/i} \"I’m in computer engineering, what about you?\""
                mc "\"Oh cool, I’m in computer science!\""
                mc "\"We both need to take Programming 1 as freshmen, right?\""
                mc "\"Are you going to be doing it this semester?\""
                r "\"Yeah, that’s what I am planning on doing.\""
                r "\"I have some programming experience from highschool, but I’m excited to start learning more here.\""
                r "\"We could totally work on projects and study together!\""
                mc "\"Absolutely! That would be really cool!\""
                mc "\"We’ll probably be spending a lot of time together then.\""
                r "\"For sure, I’m excited to become better friends with you.\""
                r "\"Well anyway, I have to get going.\""
                r "\"Gotta do a few more things before I leave for orientation.\""
                r "\"It was nice seeing you again, hope to see you around soon!\""
                hide rust_normal with dissolve
                "{i}Rust leaves{/i}"

    elif r_rep < 50:
        mc "Hey there, your name is..."
        window hide
        show rust_normal at right with dissolve 
        
        menu w0_d3_RustName:
            "Robust":
                window show
                $ r_rep = reputation(r_rep, -2)
                mc "Your name is Robust, right?"
                hide rust_normal
                show rust_angry at right
                r "Oh, it’s you."
                r "Of course you don’t remember."
                r "My name is Rust."
                r "Now what do you want?"
            
            "Robin":
                window show
                $ r_rep = reputation(r_rep, -2)
                mc "Your name is Robin, right?"
                hide rust_normal
                show rust_angry at right
                r "Oh, it’s you."
                r "Of course you don’t remember."
                r "My name is Rust."
                r "Now what do you want?"
            
            "Rust":
                window show
                mc "Your name is Rust, right?"
                hide rust_normal
                show rust_angry at right
                r "Oh, it’s you."
                r "Yeah, that's my name."
                r "What do you want?"

            "Resch":
                window show
                $ r_rep = reputation(r_rep, -2)
                mc "Your name is Resch, right?"
                hide rust_normal
                show rust_angry at right
                r "Oh, it’s you."
                r "Of course you don’t remember."
                r "My name is Rust."
                r "Now what do you want?"

    else:
        r "Now what do you want?"