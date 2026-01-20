screen staffroll():
    zorder 99
    add "gui/staffroll.png" at credit_scroll


transform credit_scroll:
    ypos 600 alpha 1.0
    linear 20.25 yoffset -3000
    easein 5 yoffset -3600
    pause 10
    easein 5 alpha 0

label start_credits:
    show screen staffroll() nopredict
    return