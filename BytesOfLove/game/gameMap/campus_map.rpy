screen campusroadmap:
    frame:
        xalign 0.0
        yalign 0.0
        xsize 1920
        ysize 1000
        background "map_images/campus_roadmap.png"

        imagebutton: # setting the x and y pos of these as well 
            focus_mask True
            xpos 207
            ypos 129
            idle "map_images/lecture_idle.png"
            hover "map_images/lecutre_hover.png"
            action Return()
        
        imagebutton:
            focus_mask True
            xpos 1020
            ypos 215    
            idle "map_images/park_idle.png"
            hover "map_images/park_hover.png"
            action Return()

        imagebutton:
            focus_mask True
            xpos 215
            ypos 397
            idle "map_images/cafe_idle.png"
            hover "map_images/cafe_hover.png"
            action Return()

        imagebutton:
            focus_mask True 
            xpos 1010
            ypos 400
            idle "map_images/gym_idle.png"
            hover "map_images/gym_hover.png"
            action Return()

        imagebutton:
            focus_mask True 
            xpos 320
            ypos 590
            idle "map_images/dorm_idle.png"
            hover "map_images/dorm_hover.png"
            action Return()

        imagebutton:
            focus_mask True 
            xpos 1030
            ypos 603
            idle "map_images/back_idle.png"
            hover "map_images/back_hover.png"
            action Return()

