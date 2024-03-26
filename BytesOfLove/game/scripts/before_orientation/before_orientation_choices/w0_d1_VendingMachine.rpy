label w0_d1_VendingMachine:
    mc "I think I will go downstairs to the vending machine, I could really go for a Snickers bar and a bag of Doritos right now."
    mc "And, I will save some money. You never know when you will need it."
    mc "I am pretty hungry though, maybe I should eat some more to fuel my body and mind."

    scene w0_d1_vending

    "*[mc] walks downstairs to find a vending machine*"

    show rust_normal at right with fade

    r "Hey there! I’m Rust! Do you go to UB?"

    menu w0_d1_Rust:
        "Mean response":
            $ r_rep = reputation(r_rep, -2)
            mc "Yeah, I do, my name is [mc]."
            r "Cool, you seem chill, what's your major?"
            mc "Wouldn't you like to know…"
            
            hide rust_normal 
            show rust_angry at right

            r "Damn, I was just wondering."
            r "I am in computer engineering, in case you wanted to know my major."
            mc "Oh thanks, I didn't."
            r "Jeez… you don’t have to be mean about it, man."
            mc "Whatever."
            hide rust_angry with dissolve
            "*Rust leaves*"

        "Nice response":
            $ r_rep = reputation(r_rep, 2)
            mc "Yeah I do, my name is [mc], nice to meet you! What major are you?"
            r "*Smiles* I am in computer engineering, what about you?"
            mc "Oh, I’m in computer science!"
            mc "We both need to take programming 1, right?"
            mc "Are you going to be doing it this semester?"
            r "Yes, that's what I am planning on doing."
            r "I have some programming experience from highschool, but I am excited to start learning more."
            r "We can totally work on projects and study together! It will be really cool."
            mc "Absolutely! We will probably be spending a lot of time together."
            r "Yeah, I am excited to become better friends with you."
            r "Well anyway, I have to get back to my room so I can get a good night's sleep."
            r "You should probably do the same."
            r "It was nice to meet you, see you in class!"
            hide rust_normal with dissolve
            "*Rust leaves"

    "*[mc] stands at the vending machine, thinking about what he wants*"
    mc "Hmm they don't have Doritos, I guess I am only getting a Snickers bar tonight."
    "*Gets his snickers bar and heads back up to his room*"

jump w0_d1_End
