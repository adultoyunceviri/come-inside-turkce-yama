################################################################################
## Initialization
################################################################################

init offset = -1

#ну и хули тебе тут надо
################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who" xalign .5

        text what id "what"


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/npanel/backdialog4.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/npanel/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width
transform phone_pickup:
    yalign 1.0 xalign 0.5
    yoffset 900
    easein 0.3 yoffset 100

##END
screen end_ci():
    modal True
    zorder 300
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("end_ci"), Show("end_ci_1")
    imagemap:
        #ground "gui/end_sc/ep2endsc_lindsey_2_cr.png"
        #hover "gui/end_sc/ep2endsc_hover.png"

        if slave_sister >= 2 and p_lora <= 5 and st_sex_1 == 0: #BDSMLin
            ground "gui/end_sc/ep2endsc_lindsey_2_cr.png"
            hover "gui/end_sc/ep2endsc_lindsey_2_cr_hover.png"
        elif p_lora >= 12 and p_kelly < 7 and p_aznu < 17: #Lora
            ground "gui/end_sc/ep2endsc_lora_cr.png"
            hover "gui/end_sc/ep2endsc_lora_cr_hover.png"
        elif slave_sister == 0 and p_lora <= 5 and st_sex_1 == 0 and kelly_in_2 <= 1: #LoveLin
            ground "gui/end_sc/ep2endsc_lindsey_cr.png"
            hover "gui/end_sc/ep2endsc_lindsey_cr_hover.png"
        elif p_aznu >= 17 and p_lora <= 5 and p_kelly < 7: #AznuMax
            ground "gui/end_sc/ep2endsc_aznu_cr.png"
            hover "gui/end_sc/ep2endsc_aznu_cr_hover.png"
        elif p_kelly >= 7 and st_sex_1 == 1 and kelly_in_2 == 2: #Kelly
            ground "gui/end_sc/ep2endsc_kelly_cr.png"
            hover "gui/end_sc/ep2endsc_kelly_cr_hover.png"
        else:
            ground "gui/end_sc/ep2endsc_lora_cr.png"
            hover "gui/end_sc/ep2endsc_lora_cr_hover.png"
        hotspot (0, 844, 1919, 235) action OpenURL ("https://www.patreon.com/ttll") #Патреон
        hotspot (1729, 51, 153, 147) action OpenURL ("https://www.instagram.com/come_inside_game/")  #инста
        hotspot (1721, 224, 162, 144) action OpenURL ("https://discord.gg/aTfjjs7")  #дискорд
screen end_ci_1():
    modal True
    zorder 300
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("end_ci_1"), MainMenu(confirm=False)
    if slave_sister >= 2 and p_lora <= 5 and st_sex_1 == 0:
        add "gui/end_sc/ep2endsc_lindsey_2.png"
    elif p_lora >= 12 and p_kelly < 7 and p_aznu < 17: #Lora
        add "gui/end_sc/ep2endsc_lora.png"
    elif slave_sister == 0 and p_lora <= 5 and st_sex_1 == 0 and kelly_in_2 <= 1: #LoveLin
        add "gui/end_sc/ep2endsc_lindsey.png"
    elif p_aznu >= 17 and p_lora <= 5 and p_kelly < 7: #AznuMax
        add "gui/end_sc/ep2endsc_aznu.png"
    elif p_kelly >= 7 and st_sex_1 == 1 and kelly_in_2 == 2: #Kelly
        add "gui/end_sc/ep2endsc_kelly.png"
    else:
        add "gui/end_sc/ep2endsc_lora.png"
##Сплэш

screen vosem():

    modal True

    zorder 500

    imagemap:
        ground "gui/main/18.png"
        hover "gui/main/analytics-hover.png"
        hotspot (689, 861, 186, 188) action Quit(confirm=False) #нет
        hotspot (1043, 866, 184, 187) action  SetField(persistent, "splashsc", True), Hide('vosem'), With(Dissolve(0.2)) #да

#Анскип
screen unskip(t, condition):
    timer t action Hide("unskip")
    if not condition:
        key "dismiss" action [[]]
##МобилкаДневКарта
screen mob_b():
    key "alt_K_F4" action Quit(confirm=False)
    imagemap:
        ground "gui/npanel/mob-1.png"

        hover "gui/npanel/mob-h-1.png"

        if naz > 0:
            hotspot (1737, 996, 81, 72) action If(renpy.get_screen("sms_screen"), NullAction(), [Show('phone'), Show("clock"), Show("phone_back"), With(Dissolve(0.2))])  #тел
        else:
            hotspot (1737, 996, 81, 72) action If(renpy.get_screen("sms_screen"), true=[Hide('sms_screen'),Hide('clock'), With(Dissolve(0.2)), SetVariable("contact_flag", 0 ),SetVariable("cont", False),SetVariable ("sms_pics", False)], false=[Show('phone'), Show("clock"), Show("phone_back"), With(Dissolve(0.2))])  #тел

        if new_flag > 0:
            imagebutton xalign 0.936 yalign 0.937:
                idle ("gui/phone/new-mes-1.png")

screen mob():
    key "alt_K_F4" action Quit(confirm=False)
    imagemap:
        ground "gui/npanel/mob-2.png"

        hover "gui/npanel/mob-h-2.png"
        if naz > 0:
            hotspot (1737, 996, 81, 72) action If(renpy.get_screen("sms_screen"), NullAction(), [Show('phone'), Show("clock"), Show("phone_back"), With(Dissolve(0.2))])  #тел
        else:
            hotspot (1737, 996, 81, 72) action If(renpy.get_screen("sms_screen"), true=[Hide('sms_screen'),Hide('clock'), With(Dissolve(0.2)), SetVariable("contact_flag", 0 ),SetVariable("cont", False),SetVariable ("sms_pics", False)], false=[Show('phone'), Show("clock"), Show("phone_back"), With(Dissolve(0.2))])  #тел

        hotspot (1737, 920, 81, 72) action If(renpy.get_screen("scr_dnev"), true=[Hide("scr_dnev"), Show("dnev_close")],false=[Show('dnev_open')])  #днев
        if new_flag > 0:
            imagebutton xalign 0.936 yalign 0.937:
                idle ("gui/phone/new-mes-1.png")
screen mob_new_1():
    key "alt_K_F4" action Quit(confirm=False)
    imagemap:
        ground "gui/npanel/mob-2.png"

        hover "gui/npanel/mob-h-2.png"
        hotspot (1737, 996, 81, 72) action NullAction()
        hotspot (1737, 920, 81, 72) action NullAction()
        if new_flag > 0:
            imagebutton xalign 0.936 yalign 0.937:
                idle ("gui/phone/new-mes-1.png")
screen mob_new():
    key "alt_K_F4" action Quit(confirm=False)
    imagemap:
        ground "gui/npanel/mob-3.png"

        hover "gui/npanel/mob-h-2.png"
        hotspot (1737, 996, 81, 72) action NullAction()
        hotspot (1737, 920, 81, 72) action NullAction()
        if new_flag > 0:
            imagebutton xalign 0.936 yalign 0.937:
                idle ("gui/phone/new-mes-1.png")

screen new_sketch():
    on "show" action Hide ("mob"), With(Dissolve(0.2)), Show ("mob_new"), With(Dissolve(0.2))
    timer t*40 repeat False action Hide("mob_new"), With(Dissolve(0.2)),Show ("mob_new_1"), With(Dissolve(0.2))
    timer t*80 repeat False action Hide("mob_new_1"), With(Dissolve(0.2)),Show ("mob_new"), With(Dissolve(0.2))
    timer t*120 repeat False action Hide("mob_new"), With(Dissolve(0.2)), Show ("mob"), With(Dissolve(0.2)),Hide("new_sketch")
## Мобилка ####

init python:
    from datetime import datetime, date, time



screen phone():
    key "K_ESCAPE" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_3" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_2" action Hide("phone"), Hide ("phone_back"), Hide("clock"), With(Dissolve(0.2))
    key "h" action Hide("phone"), Hide ("phone_back"), Hide("clock"), With(Dissolve(0.2))
    modal True
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("phone"), Hide ("phone_back"), Hide("clock"), With(Dissolve(0.2))
    zorder 200
    imagemap:
        ground "gui/phone/phone-2-ground.png"
        if mute == False:
            idle "gui/phone/phone-idle-4.png"
            hover "gui/phone/phone-2-hover-4.png"
            alpha False
        else:
            idle "gui/phone/phone-idle-4-1.png"
            hover "gui/phone/phone-2-hover-4-1.png"
            alpha False

        hotspot (920, 821, 78, 65) action Hide("phone"), Hide ("phone_back"), Hide("clock"), With(Dissolve(0.2)) #Домой
        hotspot (789, 823, 66, 63) action Hide("phone"), Hide ("phone_back"), Hide("clock"), With(Dissolve(0.2))#назад
        hotspot (761, 704, 131, 114) action Show('calls'), Hide ('phone'), Hide('phone_back')#Звонок
        hotspot (895, 705, 118, 115) action Show('contacts'), Hide ('phone'), Hide('phone_back')#СМС
        hotspot (1023, 704, 137, 114) action Show('phone_gallery'), Hide ('phone'), Hide('phone_back') #Галерея
        hotspot (1023, 455, 109, 135) action OpenURL ("https://www.instagram.com/come_inside_game/") #Инста
        hotspot (897, 455, 123, 140) action OpenURL ("https://www.patreon.com/ttll") #Патреон
        hotspot (797, 597, 84, 85) action If(mute == False, true=[SetVariable("mute", True),Play("mute_1", "sounds/civibrate.ogg")],false=[SetVariable("mute", False),Play("mute_1", "sounds/sms_l.ogg")]) #Звук

        hotspot (1030, 593, 96, 90) action Show('phone_settings'), Hide ('phone'), Hide('phone_back') #Настройки
        hotspot (1034, 347, 94, 82) action Call("acc_d") #Камера
    if new_flag > 0:
            imagebutton xalign 0.51 yalign 0.702:
                idle ("gui/phone/new-mes-1.png")
#Настройки
screen phone_settings:
    key "K_ESCAPE" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_3" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_2" action Hide ('phone_settings'), With(Dissolve(0.2)),Hide ('clock'), With(Dissolve(0.2))
    key "h" action Hide ('phone_settings'), With(Dissolve(0.2)),Hide ('clock'), With(Dissolve(0.2))
    layer "screens"
    zorder 200
    modal True
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide ('phone_settings'), With(Dissolve(0.2)),Hide ('clock'), With(Dissolve(0.2))

    imagemap:
        ground "gui/phone/phone-settings-1.png"
        hover "gui/phone/phone-settings-hover.png"
        selected_idle 'gui/phone/phone-settings-hover.png'
        #Левое
        #Фон
        hotspot (782, 164, 54, 55) action StylePreference("bgl", "Default") #Стандарт
        hotspot (881, 163, 58, 56) action StylePreference("bgl", "Blue") #Синий
        hotspot (983, 163, 56, 57) action StylePreference("bgl", "Yellow") #Желтый
        hotspot (1083, 161, 57, 59) action StylePreference("bgl", "Black") #Черный
        #Текст
        hotspot (781, 287, 58, 60) action StylePreference("text", "White") #Белый
        hotspot (880, 287, 58, 59) action StylePreference("text", "Blue") #Синий
        hotspot (985, 287, 55, 60) action StylePreference("text", "Yellow") #Желтый
        hotspot (1080, 286, 60, 63) action StylePreference("text", "Black") #Черный
        #Правое
        #Фон
        hotspot (782, 418, 57, 54)  action StylePreference("bgr", "Default") #Стандарт
        hotspot (879, 417, 60, 54) action StylePreference("bgr", "Blue") #Синий
        hotspot (983, 416, 55, 58) action StylePreference("bgr", "Yellow") #Желтый
        hotspot (1081, 415, 59, 57) action StylePreference("bgr", "Black") #Черный
        #Текст
        hotspot (783, 540, 55, 56) action StylePreference("textr", "White") #Белый
        hotspot (878, 541, 62, 55) action StylePreference("textr", "Blue") #Синий
        hotspot (983, 539, 58, 60) action StylePreference("textr", "Yellow") #Желтый
        hotspot (1081, 536, 59, 65) action StylePreference("textr", "Black") #Черный


        hotspot (862, 823, 199, 65) action Show('phone'),Show("clock"), Show("phone_back"), Hide ('phone_settings') #Домой
        hotspot (789, 823, 66, 63) action Show('phone'),Show("clock"), Show("phone_back"), Hide ('phone_settings') #назад
#Галерея
screen phone_gallery:
    key "K_ESCAPE" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_3" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_2" action Hide ('phone_gallery'), With(Dissolve(0.2)),Hide ('clock'), With(Dissolve(0.2))
    key "h" action Hide ('phone_gallery'), With(Dissolve(0.2)),Hide ('clock'), With(Dissolve(0.2))
    layer "screens"
    zorder 200
    modal True
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide ('phone_gallery'), With(Dissolve(0.2)),Hide ('clock'), With(Dissolve(0.2))

    imagemap:
        ground "gui/phone/phone-gallery.png"
        hover "gui/phone/phone-sms-hover.png"
        hotspot (862, 823, 199, 65) action Show('phone'),Show("clock"), Show("phone_back"), Hide ('phone_gallery') #Домой
        hotspot (789, 823, 66, 63) action Show('phone'),Show("clock"), Show("phone_back"), Hide ('phone_gallery') #назад




    python:
        yadj.value = yadjValue
    vbox:
        align(.5005, 0.3)
        frame:
            style "g_frame"
            vbox:
                # контейнер для пузырьков с сообщениями
                frame:

                    xmargin 0 ymargin 0
                    xpadding 0 ypadding 0
                    background None
                    vpgrid:


                        yfill False
                        mousewheel True
                        draggable True
                        side_xfill True

                        cols 2
                        spacing 0
                        xfill True

                        imagebutton: #5
                            idle ("gui/phone/gal-1.png")
                            hover ("gui/phone/gal-1-hover.png")
                            action Show("gallery_i"),SetVariable ("show_gal", 1)

                        imagebutton: #5
                            idle ("gui/phone/gal-2.png")
                            hover ("gui/phone/gal-2-hover.png")
                            action Show("gallery_i"),SetVariable ("show_gal", 2)
                        if p_sheila > 0:
                            imagebutton: #5
                                idle ("gui/phone/gal-3.png")
                                hover ("gui/phone/gal-3-hover.png")
                                action Show("gallery_i"),SetVariable ("show_gal", 3)


screen gallery_i(): #Картинки в галерее
    key "K_ESCAPE" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_3" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])

    on "show" action If(mob_sc == True, true=[Hide("mob_b")],false=[Hide("mob")]),Hide("clock")

    modal True
    zorder 300
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("gallery_i"),Show("clock"), SetVariable ("show_gal", 0), If(mob_sc == True, true=[Show("mob_b")],false=[Show("mob")])
    if show_gal == 1:
        add "images/gallery/gallery_1.webp"
        imagebutton xalign 0.95 yalign 0.95:
                idle ("gui/phone/set.png")
                hover ("gui/phone/set-hover.png")
                action SetVariable ("phone_back", 0),Hide("gallery_i"),Hide("phone_gallery"),Show('phone'), Show("phone_back"),If(mob_sc == True, true=[Show("mob_b")],false=[Show("mob")]),Show('clock')
    elif show_gal == 2:
        add "images/gallery/gallery_2.webp"
        imagebutton xalign 0.95 yalign 0.95:
                idle ("gui/phone/set.png")
                hover ("gui/phone/set-hover.png")
                action SetVariable ("phone_back", 1),Hide("gallery_i"),Hide("phone_gallery"),Show('phone'), Show("phone_back"),If(mob_sc == True, true=[Show("mob_b")],false=[Show("mob")]),Show('clock')
    elif show_gal == 3:
        add "images/EP1/ksc12-4-0.webp"
        imagebutton xalign 0.95 yalign 0.95:
                idle ("gui/phone/set.png")
                hover ("gui/phone/set-hover.png")
                action SetVariable ("phone_back", 2),Hide("gallery_i"),Hide("phone_gallery"),Show('phone'), Show("phone_back"),If(mob_sc == True, true=[Show("mob_b")],false=[Show("mob")]),Show('clock')

 ## Мобилка фон ####
screen phone_back():
        modal True
        zorder 100
        if phone_back == 0:
            imagemap:
                ground "gui/phone/phone-back.png"
                alpha False
        elif phone_back == 1:
            imagemap:
                ground "gui/phone/phone-back-3.png"
                alpha False
        elif phone_back == 2:
            imagemap:
                ground "gui/phone/phone-back-5.png"
                alpha False
screen calls():
    key "K_ESCAPE" action If(renpy.get_screen("navigation"), Hide("navigation"), [FileTakeScreenshot(), Show("navigation")])
    key "mouseup_3" action If(renpy.get_screen("navigation"), Hide("navigation"), [FileTakeScreenshot(), Show("navigation")])
    key "mouseup_2" action  Hide("calls"), Hide("clock"), With(Dissolve(0.2))
    key "h" action  Hide("calls"), Hide("clock"), With(Dissolve(0.2))
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("calls"), Hide("clock"), With(Dissolve(0.2))
    modal True
    zorder 100

    imagemap:
        if persistent.patch_enabled:
            ground "gui/phone/phone-call.png"
        else:
            ground "gui/phone/phone-call-1.png"

        hover "gui/phone/phone-call-hover.png"



        hotspot (862, 823, 199, 65) action Show('phone'),Show("clock"), Show("phone_back"), Hide ('calls') #Домой
        hotspot (789, 823, 66, 63) action Show('phone'),Show("clock"), Show("phone_back"), Hide ('calls') #назад

## Мобилка Контакты ####
screen contacts():
    key "K_ESCAPE" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_3" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_2" action  Hide("contacts"), Hide("clock"),SetVariable("contact_flag", 0),SetVariable("cont", False), With(Dissolve(0.2))
    key "h" action  Hide("contacts"), Hide("clock"),SetVariable("contact_flag", 0),SetVariable("cont", False), With(Dissolve(0.2))
    on "show" action SetVariable("cont", True), If(contact_flag == 1, true=[SetVariable("sms_sister", sms_all),SetVariable("sms_all", [])]),If(contact_flag == 2, true=[SetVariable("sms_kelly", sms_all),SetVariable("sms_all", [])]),If(contact_flag == 3, true=[SetVariable("sms_jhon", sms_all),SetVariable("sms_all", [])]),If(contact_flag == 4, true=[SetVariable("sms_kevin", sms_all),SetVariable("sms_all", [])]),If(contact_flag == 5, true=[SetVariable("sms_cougar", sms_all),SetVariable("sms_all", [])]),If(contact_flag == 6, true=[SetVariable("sms_ella", sms_all),SetVariable("sms_all", [])])
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("contacts"), Hide("clock"),SetVariable("contact_flag", 0),SetVariable("cont", False), With(Dissolve(0.2))
    modal True
    zorder 100

    imagemap:
        if persistent.patch_enabled:
            if kelly_name == 0:
                ground "gui/phone/phone-cont.png"
                hover "gui/phone/phone-cont-hover.png"
            elif kelly_name == 1:
                ground "gui/phone/phone-cont-k.png"
                hover "gui/phone/phone-cont-k-hover.png"
            elif kelly_name == 2:
                ground "gui/phone/phone-cont-l.png"
                hover "gui/phone/phone-cont-l-hover.png"
        else:
            if kelly_name == 0:
                ground "gui/phone/phone-cont-1.png"
                hover "gui/phone/phone-cont-1-hover.png"
            elif kelly_name == 1:
                ground "gui/phone/phone-cont-k-1.png"
                hover "gui/phone/phone-cont-k-1-hover.png"
            elif kelly_name == 2:
                ground "gui/phone/phone-cont-l-1.png"
                hover "gui/phone/phone-cont-l-1-hover.png"

        hotspot (760, 110, 400, 89) action If(sms_sister != [], true=[If(new_flag == 1, true=[SetVariable("new_flag", 0)]), SetVariable("sms_all", []), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 1)],false=[If(new_flag == 1, true=[SetVariable("new_flag", 0),]), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 1)]) #Линдси
        hotspot (760, 198, 400, 89) action If(sms_kelly != [], true=[If(new_flag == 2, true=[SetVariable("new_flag", 0)]), SetVariable("sms_all", []), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 2)],false=[If(new_flag == 2, true=[SetVariable("new_flag", 0),]), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 2)]) #Kelly
        hotspot (760, 286, 400, 89) action If(sms_jhon != [], true=[If(new_flag == 3, true=[SetVariable("new_flag", 0)]), SetVariable("sms_all", []), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 3)],false=[If(new_flag == 3, true=[SetVariable("new_flag", 0),]), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 3)]) #Jhon
        hotspot (760, 372, 400, 89) action If(sms_kevin != [], true=[If(new_flag == 4, true=[SetVariable("new_flag", 0)]), SetVariable("sms_all", []), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 4)],false=[If(new_flag == 4, true=[SetVariable("new_flag", 0),]), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 4)]) #Kevin
        hotspot (760, 460, 400, 89) action If(sms_cougar != [], true=[If(new_flag == 5, true=[SetVariable("new_flag", 0)]), SetVariable("sms_all", []), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 5)],false=[If(new_flag == 5, true=[SetVariable("new_flag", 0),]), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 5)]) #Cougar
        hotspot (760, 546, 400, 89) action  If(sms_ella != [], true=[If(new_flag == 6, true=[SetVariable("new_flag", 0)]), SetVariable("sms_all", []), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 6)],false=[If(new_flag == 6, true=[SetVariable("new_flag", 0),]), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 6)]) #Элла
        hotspot (760, 634, 400, 89) action  If(sms_lora != [], true=[If(new_flag == 7, true=[SetVariable("new_flag", 0)]), SetVariable("sms_all", []), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 7)],false=[If(new_flag == 7, true=[SetVariable("new_flag", 0),]), Show('sms_screen'), Hide('contacts'), SetVariable("contact_flag", 7)]) #Элла

        hotspot (862, 823, 199, 65) action Show('phone'),Show("clock"), Show("phone_back"), Hide ('contacts'), SetVariable("contact_flag", 0), SetVariable("cont", False) #Домой
        hotspot (789, 823, 66, 63) action Show('phone'),Show("clock"), Show("phone_back"), Hide ('contacts'), SetVariable("contact_flag", 0), SetVariable("cont", False)#назад
        if new_flag == 1:
            imagebutton xalign 0.59 yalign 0.135:
                idle ("gui/phone/new-mes.png")
        elif new_flag == 2:
            imagebutton xalign 0.59 yalign 0.215:
                idle ("gui/phone/new-mes.png")
        elif new_flag == 3:
            imagebutton xalign 0.59 yalign 0.295:
                idle ("gui/phone/new-mes.png")
        elif new_flag == 4:
            imagebutton xalign 0.59 yalign 0.375:
                idle ("gui/phone/new-mes.png")
        elif new_flag == 5:
            imagebutton xalign 0.59 yalign 0.455:
                idle ("gui/phone/new-mes.png")
        elif new_flag == 6:
            imagebutton xalign 0.59 yalign 0.535:
                idle ("gui/phone/new-mes.png")

## БредоЭкраны ####

## Мобилка Часы ####
screen clock():

    layer "over_screens"

    $ time_now = datetime.now().strftime('%H:%M')
    if renpy.get_screen ("phone"):
        text "{size=152}{font=gui/fonts/ROBOTO-THIN.ttf}[time_now]{/font}{/size}" xpos 0.41 ypos 0.04

        text "{size=16}{font=gui/fonts/OPENSANS-LIGHT.ttf}[time_now]{/font}{/size}" xpos 0.41 ypos 0.02
    else:
        text "{size=16}{font=gui/fonts/OPENSANS-LIGHT.ttf}[time_now]{/font}{/size}" xpos 0.41 ypos 0.02

## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice
##КвикМеню
screen keymap_screen:

    key "K_ESCAPE" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "mouseup_3" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "K_MENU" action Show('save')
    key "alt_K_F4" action Quit(confirm=False)

screen keymap_screen_b:

    key "K_ESCAPE" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
    key "K_MENU" action Show('save')
    key "alt_K_F4" action Quit(confirm=False)
    key "mouseup_3" action If(renpy.get_screen("save"), Hide("save"), [FileTakeScreenshot(), Show("save")])
screen navigation():
    layer "over_screens"
    modal True
    zorder 200
    style_prefix "navigation"
    key "K_ESCAPE" action Hide('navigation')
    key "mouseup_3" action Hide('navigation')
    imagemap:
        ground "gui/game/game-menu.webp"
        idle "gui/game/game-menu.webp"
        hover "gui/game/game-menu-hover.webp"
        hotspot (1750, 938, 159, 137) action [Hide("save"),Show("navigation"), Return()]
        hotspot (16, 914, 154, 156) action Hide("navigation"), MainMenu()
        hotspot (195, 933, 328, 108) action Show("save")
        hotspot (597, 934, 326, 108) action Show("load")
        hotspot (997, 934, 327, 109) action Show("preferences")
        hotspot (1397, 933, 328, 108) action Quit()

##ЭкранДнева

# ДНЕВ
init:

    $ t = 0.01
    $ t_1 = 0.00000001
    image dnevnik = Ani("gui/dnev/notepad-open-", 25, t, loop = False, ext="webp")


# экран днева с пожеланиями
screen p_dnev():
    if persistent.patch_enabled:
        add "gui/dnev/clean_dnev.png"
    else:
        add "gui/dnev/clean_dnev_1.png"
# экран днева с кнопками
screen scr_dnev():
    modal True
    zorder 100

    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action SetVariable("glavn", False), Hide("scr_dnev"), Show("dnev_close")
    key "mouseup_2" action SetVariable("glavn", False), Hide("scr_dnev"), Show("dnev_close") #колесико клик Закрываем
    key "mouseup_3" action SetVariable("glavn", False), Hide("scr_dnev"), Show("dnev_close") #райтклик
    key "mouseup_5" action SetVariable("glavn", False), Hide("scr_dnev"),With(Pause(1.0)), MyCall("cflip_page_lora_1") #скроллвниз
    key "K_RIGHT" action SetVariable("glavn", False), Hide("scr_dnev"),With(Pause(1.0)), MyCall("cflip_page_lora_1") #Стрелка Вправо
    key "K_LEFT" action SetVariable("glavn", False), Hide("scr_dnev"), Show("dnev_close") #Стрелка влево
    key "mousedown_4" action SetVariable("glavn", False), Hide("scr_dnev"), Show("dnev_close") #скроллназад
    key "K_ESCAPE" action Show('navigation')
    if helpd: #если в первый раз, показываем хелп
        add "helpdi"
    else:
        add "dnev"
    if not is_call:
        imagebutton xalign 0.345 yalign 0.037:
        #эта картинка используется когда кнопка не в фокусе
            idle ("gui/dnev/dnev-open-lora.webp")
        #эта картинка используется когда кнопка в фокусе
            hover ("gui/dnev/dnev-open-lora-hover.webp")
        #это действие произойдет если на кнопку навести курсор

        #это действие произойдет если на кнопку навести курсор, а потом убрать

        #и собственно действие которое будет происходить при нажатии
            action  SetVariable("glavn", False), Hide("scr_dnev"),With(Pause(1.0)), MyCall("cflip_page_lora_1")
        # кнопка, которая выполняет аналог call label

screen page_end():
    if dpage_end == False:
        timer t*0.01 repeat False action Call("dpage_end_f")
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("page_end"),With(Pause(1.0)), Call("cflip_page_end_z")
    key "K_LEFT" action Hide("page_end"),With(Pause(1.0)), Call("cflip_page_end_b") #СтрелкаНазад
    key "mousedown_4" action Hide("page_end"),With(Pause(1.0)), Call("cflip_page_end_b") #КолесикоНазад
    key "mouseup_2" action Hide("page_end"),With(Pause(1.0)), Call("cflip_page_end_g") #колесико клик главная
    key "mouseup_3" action  Hide("page_end"),With(Pause(1.0)), Call("cflip_page_end_z") #райтклик закрыть
    key "K_ESCAPE" action Show('navigation')
    add "gui/dnev/page_END.png"

screen page_lora_3():
    if dpage_3 == False:
        timer t*0.01 repeat False action Call("dpage_3_f")
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("page_lora_3"),With(Pause(1.0)), Call("cflip_page_lora_3_z")
    $ renpy.start_predict_screen("page_lora_4")
    key "K_LEFT" action Hide("page_lora_3"),With(Pause(1.0)), Call("cflip_page_lora_3_b") #СтрелкаНазад
    key "mousedown_4" action Hide("page_lora_3"),With(Pause(1.0)), Call("cflip_page_lora_3_b") #КолесикоНазад
    key "mouseup_2" action Hide("page_lora_3"),With(Pause(1.0)), Call("cflip_page_lora_3_g") #колесико клик главная
    key "mouseup_3" action  Hide("page_lora_3"),With(Pause(1.0)), Call("cflip_page_lora_3_z") #райтклик закрыть
    key "K_ESCAPE" action Show('navigation')
    key "mouseup_5" action  Hide("page_lora_3"),With(Pause(1.0)), Call("cflip_page_lora_4") #КолесиковнизЛора3
    key "K_RIGHT" action  Hide("page_lora_3"),With(Pause(1.0)), Call("cflip_page_lora_4") #КолесиковнизЛора3
    if lora_page_3_scene == 4: #Если пройдена  Сцена 12
        add "gui/dnev/page_lora_3.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris9-sc-done.png")
            hover ("gui/dnev/ris9-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_9_taylor")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris10-sc-done.png")
            hover ("gui/dnev/ris10-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_10_sport")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris11-sc-done.png")
            hover ("gui/dnev/ris11-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_11_spit")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris12-sc-done.png")
            hover ("gui/dnev/ris12-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_12_pereodev")

    elif lora_page_3_scene == 3: #Если пройдена Сцена 11
        add "gui/dnev/page_lora_3.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris9-sc-done.png")
            hover ("gui/dnev/ris9-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_9_taylor")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris10-sc-done.png")
            hover ("gui/dnev/ris10-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_10_sport")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris11-sc-done.png")
            hover ("gui/dnev/ris11-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_11_spit")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris12.png")
            hover ("gui/dnev/ris12-hover.png")
            action If(dgame_12 == True, true=[Hide("page_lora_3"), Call("lora_12_pereodev")],false=[Call("remember_12")])

    elif lora_page_3_scene == 2: #Если пройдена сцена 10
        add "gui/dnev/page_lora_3.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris9-sc-done.png")
            hover ("gui/dnev/ris9-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_9_taylor")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris10-sc-done.png")
            hover ("gui/dnev/ris10-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)), Call("lora_10_sport")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris11.png")
            hover ("gui/dnev/ris11-hover.png")
            action If(dgame_11 == True, true=[Hide("page_lora_3"), Call("lora_11_spit")],false=[Call("remember_11")])
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris12.png")
            hover ("gui/dnev/ris12-hover.png")
            action Call("remember_12")

    elif lora_page_3_scene == 1: #Если пройдена Сцена 9
        add "gui/dnev/page_lora_3.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris9-sc-done.png")
            hover ("gui/dnev/ris9-sc-hover-done.png")
            action Hide("page_lora_3"), With(Dissolve(1.0)),Call("lora_9_taylor")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris10.png")
            hover ("gui/dnev/ris10-hover.png")
            action If(dgame_10 == True, true=[Hide("page_lora_3"), Call("lora_10_sport")],false=[Call("remember_10")])
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris11.png")
            hover ("gui/dnev/ris11-hover.png")
            action Call("remember_11")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris12.png")
            hover ("gui/dnev/ris12-hover.png")
            action Call("remember_12")

    elif lora_page_2_scene == 4: #Если пройдена сцена в ванной
        add "gui/dnev/page_lora_3.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris9.png")
            hover ("gui/dnev/ris9-hover.png")
            action If(dgame_9 == True, true=[Hide("page_lora_3"), Call("lora_9_taylor")],false=[Call("remember_9")])
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris10.png")
            hover ("gui/dnev/ris10-hover.png")
            action Call("remember_10")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris11.png")
            hover ("gui/dnev/ris11-hover.png")
            action Call("remember_11")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris12.png")
            hover ("gui/dnev/ris12-hover.png")
            action Call("remember_12")
    else:
        add "gui/dnev/page_lora_3.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris9.png")
            hover ("gui/dnev/ris9-hover.png")
            action Call("remember_9")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris10.png")
            hover ("gui/dnev/ris10-hover.png")
            action Call("remember_10")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris11.png")
            hover ("gui/dnev/ris11-hover.png")
            action Call("remember_11")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris12.png")
            hover ("gui/dnev/ris12-hover.png")
            action Call("remember_12")

screen page_lora_4():
    if dpage_4 == False:
        timer t*0.01 repeat False action Call("dpage_4_f")
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("page_lora_4"),With(Pause(1.0)), Call("cflip_page_lora_4_z")
    $ renpy.start_predict_screen("page_center")
    key "K_LEFT" action Hide("page_lora_4"),With(Pause(1.0)), Call("cflip_page_lora_4_b") #КолесикоНазад
    key "mousedown_4" action Hide("page_lora_4"),With(Pause(1.0)), Call("cflip_page_lora_4_b") #КолесикоНазад
    key "mouseup_2" action Hide("page_lora_4"),With(Pause(1.0)), Call("cflip_page_lora_4_g") #колесико клик главная
    key "mouseup_3" action  Hide("page_lora_4"),With(Pause(1.0)), Call("cflip_page_lora_4_z") #райтклик закрыть
    key "K_ESCAPE" action Show('navigation')
    add "gui/dnev/page_lora_4.png"
    key "mouseup_5" action  Hide("page_lora_4"),With(Pause(1.0)), Call("cflip_page_center") #КолесиковнизЛора4
    key "K_RIGHT" action  Hide("page_lora_4"),With(Pause(1.0)), Call("cflip_page_center") #КолесиковнизЛора4
screen page_center():
    if dpage_center == False:
        timer t*0.01 repeat False action Call("dpage_center_f")
    $ renpy.start_predict_screen("page_last")
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("page_center"),With(Pause(1.0)), Call("cflip_page_center_z")
    key "K_LEFT" action Hide("page_center"),With(Pause(1.0)), Call("cflip_page_center_b") #СтрелкаНазад
    key "mousedown_4" action Hide("page_center"),With(Pause(1.0)), Call("cflip_page_center_b") #КолесикоНазад
    key "mouseup_2" action Hide("page_center"),With(Pause(1.0)), Call("cflip_page_center_g") #колесико клик главная
    key "mouseup_3" action  Hide("page_center"),With(Pause(1.0)), Call("cflip_page_center_z") #райтклик закрыть
    key "K_ESCAPE" action Show('navigation')
    key "mouseup_5" action  Hide("page_center"),With(Pause(1.0)), Call("cflip_page_last") #КолесиковнизЛора4
    key "K_RIGHT" action  Hide("page_center"),With(Pause(1.0)), Call("cflip_page_last") #СтрелкаЛора4
    add "gui/dnev/page_center.png"
screen page_last():
    if dpage_last == False:
        timer t*0.01 repeat False action Call("dpage_last_f")
    $ renpy.start_predict_screen("page_end")
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("page_last"),With(Pause(1.0)), Call("cflip_page_last_z")
    key "K_LEFT" action Hide("page_last"),With(Pause(1.0)), Call("cflip_page_last_b") #СтрелкаНазад
    key "mousedown_4" action Hide("page_last"),With(Pause(1.0)), Call("cflip_page_last_b") #КолесикоНазад
    key "mouseup_2" action Hide("page_last"),With(Pause(1.0)), Call("cflip_page_last_g") #колесико клик главная
    key "mouseup_3" action  Hide("page_last"),With(Pause(1.0)), Call("cflip_page_last_z") #райтклик закрыть
    key "K_ESCAPE" action Show('navigation')
    key "mouseup_5" action  Hide("page_last"),With(Pause(1.0)), Call("cflip_page_end") #КолесиковнизЛора4
    key "K_RIGHT" action  Hide("page_last"),With(Pause(1.0)), Call("cflip_page_end") #СтрелкаЛора4
    add "gui/dnev/page_last.png"

#LoraPage2
screen page_lora_2():
    if dpage_2 == False:
        timer t*0.01 repeat False action Call("dpage_2_f")
    $ renpy.start_predict_screen("page_lora_3")
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("page_lora_2"),With(Pause(1.0)), Call("cflip_back_page_lora_2_list_g_z")
    key "K_LEFT" action Hide("page_lora_2"),With(Pause(1.0)), Call("cflip_back_page_lora_2_list") #СтрелкаНазад
    key "mousedown_4" action Hide("page_lora_2"),With(Pause(1.0)), Call("cflip_back_page_lora_2_list") #КолесикоНазад
    key "mouseup_2" action Hide("page_lora_2"),With(Pause(1.0)), Call("cflip_back_page_lora_2_list_g") #колесико клик главная
    key "mouseup_3" action  Hide("page_lora_2"),With(Pause(1.0)), Call("cflip_back_page_lora_2_list_g_z") #райтклик закрыть
    key "K_ESCAPE" action Show('navigation')
    key "mouseup_5" action  Hide("page_lora_2"),With(Pause(1.0)), Call("cflip_page_lora_3") #КолесиковнизЛора2
    key "K_RIGHT" action  Hide("page_lora_2"),With(Pause(1.0)), Call("cflip_page_lora_3") #КолесиковнизЛора2
    key "a" action NullAction() #блочим
    key "A" action NullAction()
    key "d" action NullAction()
    key "D" action NullAction()
    key "ф" action NullAction()
    key "Ф" action NullAction()
    key "в" action NullAction()
    key "В" action NullAction()
    if lora_page_2_scene == 4: #Если пройдена  Сцена 2_3
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5-sc-done.png")
            hover ("gui/dnev/ris5-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_zaezd")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6-sc-done.png")
            hover ("gui/dnev/ris6-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_7read")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7-sc-done.png")
            hover ("gui/dnev/ris7-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_8bath")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8-sc-done.png")
            hover ("gui/dnev/ris8-sc-hover-done.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)), Call("lora_cry")
    elif game_2_3 == True: #Если пройдена игра 7
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5-sc-done.png")
            hover ("gui/dnev/ris5-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_zaezd")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6-sc-done.png")
            hover ("gui/dnev/ris6-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_7read")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7-sc.png")
            hover ("gui/dnev/ris7-sc-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_8bath")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8-sc-done.png")
            hover ("gui/dnev/ris8-sc-hover-done.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)), Call("lora_cry")
    elif lora_page_2_scene == 3: #Если пройдена Сцена 2_2
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5-sc-done.png")
            hover ("gui/dnev/ris5-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_zaezd")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6-sc-done.png")
            hover ("gui/dnev/ris6-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_7read")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7.png")
            hover ("gui/dnev/ris7-hover.png")
            action If(dgame_7 == True, true=[MyCall("game_lora_2_3")],false=[Call("remember_7")])
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8-sc-done.png")
            hover ("gui/dnev/ris8-sc-hover-done.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)), Call("lora_cry")
    elif game_2_2 == True: #Если пройдена игра 6
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5-sc-done.png")
            hover ("gui/dnev/ris5-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_zaezd")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6-sc.png")
            hover ("gui/dnev/ris6-sc-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_7read")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7.png")
            hover ("gui/dnev/ris7-hover.png")
            action Call("remember_7")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8-sc-done.png")
            hover ("gui/dnev/ris8-sc-hover-done.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)), Call("lora_cry")
    elif lora_page_2_scene == 2: #Если пройдена сцена 2_4
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5-sc-done.png")
            hover ("gui/dnev/ris5-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_zaezd")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6.png")
            hover ("gui/dnev/ris6-hover.png")
            action If(dgame_6 == True, true=[MyCall("game_lora_2_2")],false=[Call("remember_6")])
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7.png")
            hover ("gui/dnev/ris7-hover.png")
            action Call("remember_7")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8-sc-done.png")
            hover ("gui/dnev/ris8-sc-hover-done.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)), Call("lora_cry")
    elif game_2_4 == True: #Если пройдена игра 2_4
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5-sc-done.png")
            hover ("gui/dnev/ris5-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_zaezd")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6.png")
            hover ("gui/dnev/ris6-hover.png")
            action Call("remember_6")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7.png")
            hover ("gui/dnev/ris7-hover.png")
            action Call("remember_7")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8-sc.png")
            hover ("gui/dnev/ris8-sc-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)), Call("lora_cry")

    elif lora_page_2_scene == 1: #Если пройдена Сцена 5
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5-sc-done.png")
            hover ("gui/dnev/ris5-sc-done-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)),Call("lora_zaezd")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6.png")
            hover ("gui/dnev/ris6-hover.png")
            action Call("remember_6")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7.png")
            hover ("gui/dnev/ris7-hover.png")
            action Call("remember_7")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8.png")
            hover ("gui/dnev/ris8-hover.png")
            action If(dgame_8 == True, true=[MyCall("game_lora_2_4")],false=[Call("remember_8")])
    elif game_2_1 == True: #Если пройдена игра 5
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5-sc.png")
            hover ("gui/dnev/ris5-sc-hover.png")
            action Hide("page_lora_2"), With(Dissolve(1.0)), Call("lora_zaezd")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6.png")
            hover ("gui/dnev/ris6-hover.png")
            action Call("remember_6")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7.png")
            hover ("gui/dnev/ris7-hover.png")
            action Call("remember_7")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8.png")
            hover ("gui/dnev/ris8-hover.png")
            action Call("remember_8")
    elif lora_page_1_scene == 4:
        $ renpy.start_predict_screen("inputcolor","displaysequence","racetheclock")
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5.png")
            hover ("gui/dnev/ris5-hover.png")
            action If(dgame_5 == True, true=[Hide("page_lora_2"), Call("game_lora_2_1")],false=[Call("remember_5")])
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6.png")
            hover ("gui/dnev/ris6-hover.png")
            action Call("remember_6")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7.png")
            hover ("gui/dnev/ris7-hover.png")
            action Call("remember_7")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8.png")
            hover ("gui/dnev/ris8-hover.png")
            action Call("remember_8")
    else:
        add "gui/dnev/page_lora_2.png"
        imagebutton xalign 0.227 yalign 0.107: #5
            idle ("gui/dnev/ris5.png")
            hover ("gui/dnev/ris5-hover.png")
            action Call("remember_5")
        imagebutton xalign 0.7655 yalign 0.107: #6
            idle ("gui/dnev/ris6.png")
            hover ("gui/dnev/ris6-hover.png")
            action Call("remember_6")
        imagebutton xalign 0.227 yalign 0.662: #7
            idle ("gui/dnev/ris7.png")
            hover ("gui/dnev/ris7-hover.png")
            action Call("remember_7")
        imagebutton xalign 0.768 yalign 0.662: #8
            idle ("gui/dnev/ris8.png")
            hover ("gui/dnev/ris8-hover.png")
            action Call("remember_8")

#LoraPage1
screen page_lora_1():
    if dpage_1 == False:
        timer t*0.01 repeat False action Call("dpage_1_f")
    button:
        xysize(1920,1080)  # put here the actual size of your screen
        action Hide("page_lora_1"),With(Pause(1.0)), Call("cflip_back_page_lora_1")
    key "K_LEFT" action Hide("page_lora_1"),With(Pause(1.0)), Call("cflip_back_page_lora_1_list") #КолесикоНазад
    key "mousedown_4" action Hide("page_lora_1"),With(Pause(1.0)), Call("cflip_back_page_lora_1_list") #КолесикоНазад
    key "mouseup_2" action Hide("page_lora_1"),With(Pause(1.0)), Call("cflip_back_page_lora_1_list") #колесико клик главная
    key "mouseup_3" action  Hide("page_lora_1"),With(Pause(1.0)), Call("cflip_back_page_lora_1") #райтклик закрыть
    key "mouseup_5" action  Hide("page_lora_1"),With(Pause(1.0)), Call("cflip_page_lora_2") #КолесиковнизЛора2
    key "K_RIGHT" action  Hide("page_lora_1"),With(Pause(1.0)), Call("cflip_page_lora_2") #КолесиковнизЛора2
    key "K_ESCAPE" action Show('navigation')
    key "a" action NullAction() #блочим
    key "A" action NullAction()
    key "d" action NullAction()
    key "D" action NullAction()
    key "ф" action NullAction()
    key "Ф" action NullAction()
    key "в" action NullAction()
    key "В" action NullAction()
    if lora_page_1_scene == 2 and game_1_3 == True: #Если пройдена сцена 1 и 2 и игра 3
        add "gui/dnev/page_lora_1_sc_done.png"
        imagebutton xalign 0.227 yalign 0.107: #1
            idle ("gui/dnev/ris1-sc-done.png")
            hover ("gui/dnev/ris1-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_kuh")
        imagebutton xalign 0.7655 yalign 0.107: #2
            idle ("gui/dnev/ris2-sc-done.png")
            hover ("gui/dnev/ris2-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_pse")
        imagebutton xalign 0.227 yalign 0.662: #3
            idle ("gui/dnev/ris3-sc.png")
            hover ("gui/dnev/ris3-sc-hover.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_beach")
        imagebutton xalign 0.768 yalign 0.662: #4
            idle ("gui/dnev/ris4.png")
            hover ("gui/dnev/ris4-hover.png")
            action Call("remember_4")
    elif lora_page_1_scene == 1 and game_1_2 == True: #Если пройдена сцена 1 и игра 2
        add "gui/dnev/page_lora_1_sc_done.png"
        imagebutton xalign 0.227 yalign 0.107: #1
            idle ("gui/dnev/ris1-sc-done.png")
            hover ("gui/dnev/ris1-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_kuh")
        imagebutton xalign 0.7655 yalign 0.107: #2
            idle ("gui/dnev/ris2-sc.png")
            hover ("gui/dnev/ris2-sc-hover.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_pse")
        imagebutton xalign 0.227 yalign 0.662: #3
            idle ("gui/dnev/ris3.png")
            hover ("gui/dnev/ris3-hover.png")
            action Call("remember_3")
        imagebutton xalign 0.768 yalign 0.662: #4
            idle ("gui/dnev/ris4.png")
            hover ("gui/dnev/ris4-hover.png")
            action Call("remember_4")

    elif lora_page_1_scene == 1: #Если пройдена сцена 1
        add "gui/dnev/page_lora_1_sc_done.png"
        imagebutton xalign 0.227 yalign 0.107: #1
            idle ("gui/dnev/ris1-sc-done.png")
            hover ("gui/dnev/ris1-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_kuh")
        imagebutton xalign 0.7655 yalign 0.107: #2
            idle ("gui/dnev/ris2.png")
            hover ("gui/dnev/ris2-hover.png")
            action If(dgame_2 == True, true=[MyCall("game_lora_1_2")],false=[Call("remember_2")])
        imagebutton xalign 0.227 yalign 0.662: #3
            idle ("gui/dnev/ris3.png")
            hover ("gui/dnev/ris3-hover.png")
            action Call("remember_3")
        imagebutton xalign 0.768 yalign 0.662: #4
            idle ("gui/dnev/ris4.png")
            hover ("gui/dnev/ris4-hover.png")
            action Call("remember_4")
    elif lora_page_1_scene == 2: #Если пройдена сцена 1 и 2
        add "gui/dnev/page_lora_1_sc_done.png"
        imagebutton xalign 0.227 yalign 0.107: #1
            idle ("gui/dnev/ris1-sc-done.png")
            hover ("gui/dnev/ris1-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_kuh")
        imagebutton xalign 0.7655 yalign 0.107: #2
            idle ("gui/dnev/ris2-sc-done.png")
            hover ("gui/dnev/ris2-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_pse")
        imagebutton xalign 0.227 yalign 0.662: #3
            idle ("gui/dnev/ris3.png")
            hover ("gui/dnev/ris3-hover.png")
            action If(dgame_3 == True, true=[MyCall("game_lora_1_3")],false=[Call("remember_3")])
        imagebutton xalign 0.768 yalign 0.662: #4
            idle ("gui/dnev/ris4.png")
            hover ("gui/dnev/ris4-hover.png")
            action Call("remember_4")
    elif lora_page_1_scene == 3 and game_1_4 == True: #Если пройдена сцена 1 и 2 и 3 и игра 4
        add "gui/dnev/page_lora_1_sc_done.png"
        imagebutton xalign 0.227 yalign 0.107: #1
            idle ("gui/dnev/ris1-sc-done.png")
            hover ("gui/dnev/ris1-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_kuh")
        imagebutton xalign 0.7655 yalign 0.107: #2
            idle ("gui/dnev/ris2-sc-done.png")
            hover ("gui/dnev/ris2-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_pse")
        imagebutton xalign 0.227 yalign 0.662: #3
            idle ("gui/dnev/ris3-sc-done.png")
            hover ("gui/dnev/ris3-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_beach")
        imagebutton xalign 0.768 yalign 0.662: #4
            idle ("gui/dnev/ris4-sc.png")
            hover ("gui/dnev/ris4-sc-hover.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_zh")
    elif lora_page_1_scene == 3: #Если пройдена сцена 1 и 2 и 3
        add "gui/dnev/page_lora_1_sc_done.png"
        imagebutton xalign 0.227 yalign 0.107: #1
            idle ("gui/dnev/ris1-sc-done.png")
            hover ("gui/dnev/ris1-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_kuh")
        imagebutton xalign 0.7655 yalign 0.107: #2
            idle ("gui/dnev/ris2-sc-done.png")
            hover ("gui/dnev/ris2-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_pse")
        imagebutton xalign 0.227 yalign 0.662: #3
            idle ("gui/dnev/ris3-sc-done.png")
            hover ("gui/dnev/ris3-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_beach")
        imagebutton xalign 0.768 yalign 0.662: #4
            idle ("gui/dnev/ris4.png")
            hover ("gui/dnev/ris4-hover.png")
            action If(dgame_4 == True, true=[MyCall("game_lora_1_4")],false=[Call("remember_4")])


    elif lora_page_1_scene == 4: #Если пройдена сцена 1 и 2 и 3 и 4
        add "gui/dnev/page_lora_1_sc_done.png"
        imagebutton xalign 0.227 yalign 0.107: #1
            idle ("gui/dnev/ris1-sc-done.png")
            hover ("gui/dnev/ris1-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_kuh")
        imagebutton xalign 0.7655 yalign 0.107: #2
            idle ("gui/dnev/ris2-sc-done.png")
            hover ("gui/dnev/ris2-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_pse")
        imagebutton xalign 0.227 yalign 0.662: #3
            idle ("gui/dnev/ris3-sc-done.png")
            hover ("gui/dnev/ris3-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_beach")
        imagebutton xalign 0.768 yalign 0.662: #4
            idle ("gui/dnev/ris4-sc-done.png")
            hover ("gui/dnev/ris4-sc-hover-done.png")
            action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_zh")
    else:
        if game_1_1 == False: #Если не играли в игру 1
            if dpage_2 == True:
                timer t*0.01 repeat False action Call("start_1")
            add "gui/dnev/page_lora_1.png"

            imagebutton xalign 0.227 yalign 0.107: #1
        #эта картинка используется когда кнопка не в фокусе
                idle ("gui/dnev/ris1.png")
        #эта картинка используется когда кнопка в фокусе
                hover ("gui/dnev/ris1-hover.png")
        #это действие произойдет если на кнопку навести курсор

        #это действие произойдет если на кнопку навести курсор, а потом убрать

        #и собственно действие которое будет происходить при нажатии
                action MyCall("game_lora_1")
        # кнопка, которая выполняет аналог call label
            imagebutton xalign 0.7655 yalign 0.107: #2
                idle ("gui/dnev/ris2.png")
                hover ("gui/dnev/ris2-hover.png")
                action Call("remember_2")
            imagebutton xalign 0.227 yalign 0.662: #3
                idle ("gui/dnev/ris3.png")
                hover ("gui/dnev/ris3-hover.png")
                action Call("remember_3")
            imagebutton xalign 0.768 yalign 0.662: #4
                idle ("gui/dnev/ris4.png")
                hover ("gui/dnev/ris4-hover.png")
                action Call("remember_4")
        else: #Если играли в игру 1
            timer t*0.01 repeat False action Call("good_end_1")
            add "gui/dnev/page_lora_1_sc_1.png"
            imagebutton xalign 0.227 yalign 0.107: #1
                idle ("gui/dnev/ris1-sc.png")
                hover ("gui/dnev/ris1-sc-hover.png")
                action Hide("page_lora_1"), With(Dissolve(1.0)), Call("lora_kuh")
            imagebutton xalign 0.7655 yalign 0.107: #2
                idle ("gui/dnev/ris2.png")
                hover ("gui/dnev/ris2-hover.png")
                action Call("remember_2")
            imagebutton xalign 0.227 yalign 0.662: #3
                idle ("gui/dnev/ris3.png")
                hover ("gui/dnev/ris3-hover.png")
                action Call("remember_3")
            imagebutton xalign 0.768 yalign 0.662: #4
                idle ("gui/dnev/ris4.png")
                hover ("gui/dnev/ris4-hover.png")
                action Call("remember_4")



#Анимация репутации
screen rep_up_sm(): #+1
    zorder 1

    add "rep_up_small" xalign 1.0 yalign 0.0
    timer 0.02*112 repeat False action Hide("rep_up_sm")
screen rep_up_b(): #+3
    zorder 1
    add "rep_up_big" xalign 1.0 yalign 0.0
    timer 0.02*112 repeat False action Hide("rep_up_b")
screen rep_d_sm(): #-1
    zorder 1
    add "rep_d_small" xalign 1.0 yalign 0.0
    timer 0.02*112 repeat False action Hide("rep_d_sm")
screen rep_d_b(): #-3
    zorder 1
    add "rep_d_big" xalign 1.0 yalign 0.0
    timer 0.02*112 repeat False action Hide("rep_d_b")


    #text "{size=62}{font=gui/fonts/ROBOTO-THIN.ttf}Sally{/font}{/size}"   xalign 0.94 yalign 0.02 #EPII
    #text "{size=62}{font=gui/fonts/ROBOTO-THIN.ttf}Taylor{/font}{/size}"   xalign 0.94 yalign 0.02 #EPII
    #text "{size=62}{font=gui/fonts/ROBOTO-THIN.ttf}Stacey{/font}{/size}"   xalign 0.94 yalign 0.02 #EPII
    #text "{size=62}{font=gui/fonts/ROBOTO-THIN.ttf}Sheryl{/font}{/size}"   xalign 0.94 yalign 0.02 #EPII
    #text "{size=62}{font=gui/fonts/ROBOTO-THIN.ttf}Nancy{/font}{/size}"   xalign 0.94 yalign 0.02 #EPII

#Анимация открытия дневника

screen dnev_open():
    modal True
    add "dnevnik"
    if main_menu:
        timer t_1 repeat False action Hide("dnev_open")
    else:
        timer t*25 repeat False action Hide("dnev_open"), Show("scr_dnev")
#Анимация закрытия дневника
screen dnev_close():
    modal True
    add "dnevnik-close"
    timer t*40 repeat False action Hide("dnev_close")




##МейнМеню

screen main_menu():
    style_prefix "main_menu"
    if persistent.splashsc == False:
        on "show" action Show('vosem')
    imagemap:
        ground 'gui/main/main_menu.webp'
        hover 'gui/main/main_menu-hover.webp'
        hotspot (120, 934, 330, 109) action Start()
        hotspot (573, 934, 327, 109) action Show('load')
        hotspot (1021, 934, 329, 109) action Show('preferences')
        hotspot (1472, 934, 328, 109) action Quit(confirm=True)
    imagebutton:
        align(0.98, 0.04)
        auto "/gallery/images/gallery_%s.webp"
        action [ui.callsinnewcontext("galleryNameChange"), ShowMenu("galleryMenu")]

## ДАНЕТ
screen confirm(message, yes_action, no_action):
    key "mouseup_3" action no_action
    layer "over_screens"
    modal True

    zorder 400


    if message == layout.ARE_YOU_SURE:
        imagemap:
            ground 'gui/main/main_menu-sure1.webp'
            hover 'gui/main/main_menu-sure-hover1.webp'
            hotspot (1004, 342, 88, 89) action yes_action
            hotspot (824, 343, 94, 87) action no_action
    elif message == layout.DELETE_SAVE:
        imagemap:
            ground 'gui/main/aus-del.webp'
            hover 'gui/main/main_menu-sure-hover1.webp'
            hotspot (1004, 342, 88, 89) action yes_action
            hotspot (824, 343, 94, 87) action no_action
    elif message == layout.OVERWRITE_SAVE:
        imagemap:
            ground 'gui/main/aus-del.webp'
            hover 'gui/main/main_menu-sure-hover1.webp'
            hotspot (1004, 342, 88, 89) action yes_action
            hotspot (824, 343, 94, 87) action no_action
    elif message == layout.LOADING:
        imagemap:
            ground 'gui/main/aus-del.webp'
            hover 'gui/main/main_menu-sure-hover1.webp'
            hotspot (1004, 342, 88, 89) action yes_action
            hotspot (824, 343, 94, 87) action no_action
    elif message == layout.QUIT:
        imagemap:
            ground 'gui/main/main_menu-sure1.webp'
            hover 'gui/main/main_menu-sure-hover1.webp'
            hotspot (1004, 342, 88, 89) action yes_action
            hotspot (824, 343, 94, 87) action no_action
    elif message == layout.MAIN_MENU:
        imagemap:
            ground 'gui/game/rusgm.webp'
            hover 'gui/main/main_menu-sure-hover1.webp'
            hotspot (1004, 342, 88, 89) action yes_action
            hotspot (824, 343, 94, 87) action Hide("confirm"), Show("navigation")





    ## Right-click and escape answer "no".
    key "game_menu" action no_action
## Настройки #######################################################
screen preferences():
    layer "over_screens"
    key "K_ESCAPE" action If(renpy.get_screen("preferences"), Hide("preferences"), Show("navigation"))
    key "mouseup_3" action If(renpy.get_screen("preferences"), Hide("preferences"), Show("navigation"))
    modal True

    zorder 300
    if main_menu:
        imagemap:
            ground 'gui/main/settings-main-n.webp'
            idle 'gui/main/settings-main-n.webp'
            hover 'gui/main/settings-hover-main-n.webp'
            selected_idle 'gui/settings-active-2-n.webp'
            selected_hover 'gui/settings-active-1-n.webp'
            alpha False
            hotspot (972, 103, 104, 65) action Preference('display', 'window')  #окно
            hotspot (1141, 104, 104, 64) action Preference('display', 'fullscreen') #фулл
            bar pos (974, 224) value Preference("music volume") style "pref_slider" #музыка
            bar pos (974, 306) value Preference("sound volume") style "pref_slider" #Звук
            hotspot (972, 361, 191, 26) action Preference("skip", "toggle")  #Unseen text
            hotspot (971, 401, 208, 30) action Preference("after choices", "toggle") #After
            hotspot (972, 441, 235, 33) action InvertSelected(Preference("transitions", "toggle")) #Transitions
            hotspot (966, 484, 113, 47) action ToggleField(persistent, 'rp', True, False) #RP
            #bar pos (974, 493) value Preference("text speed") style "pref_slider" #Скорость текста




            hotspot (120, 934, 330, 109) action Start()
            hotspot (573, 934, 327, 109) action Hide("preferences"), Show('load')
            hotspot (1021, 934, 329, 109) action Hide("preferences"), Show("main_menu")
            hotspot (1472, 934, 328, 109) action Hide("preferences"), Quit(confirm=True)
    else:
        imagemap:
            ground 'gui/game/settings-game-n.webp'
            idle 'gui/game/settings-game-n.webp'
            hover 'gui/game/settings-hover-game-n.webp'
            selected_idle 'gui/settings-active-2-n.webp'
            selected_hover 'gui/settings-active-1-n.webp'
            alpha False
            hotspot (972, 103, 104, 65) action Preference('display', 'window')  #окно
            hotspot (1141, 104, 104, 64) action Preference('display', 'fullscreen') #фулл
            bar pos (974, 224) value Preference("music volume") style "pref_slider" #музыка
            bar pos (974, 306) value Preference("sound volume") style "pref_slider" #Звук
            hotspot (972, 361, 191, 26) action Preference("skip", "toggle")  #Unseen text
            hotspot (971, 401, 208, 30) action Preference("after choices", "toggle") #After
            hotspot (972, 441, 235, 33) action InvertSelected(Preference("transitions", "toggle")) #Transitions
            hotspot (966, 484, 113, 47) action ToggleField(persistent, 'rp', True, False) #RP
            #bar pos (974, 493) value Preference("text speed") style "pref_slider" #Скорость текста



            hotspot (1782, 942, 90, 90) action Hide("preferences"),Hide("navigation")
            hotspot (47, 943, 91, 89) action Hide("preferences"), MainMenu()
            hotspot (195, 933, 328, 108) action Hide("preferences"), Show("save")

            hotspot (597, 934, 326, 108) action Hide("preferences"), Show("load")
            hotspot (997, 934, 327, 109) action Hide("preferences"), Show("navigation")
            hotspot (1397, 933, 328, 108) action Hide("preferences"), Show("navigation"), Quit()
init -2 python:
    style.pref_slider.left_bar = "gui/bar/full.png"
    style.pref_slider.right_bar = "gui/bar/empty.png"

    style.pref_slider.xmaximum = 270
    style.pref_slider.ymaximum = 28

    style.pref_slider.thumb = "gui/bar/thumb.png"
    style.pref_slider.thumb_offset = 14
    style.pref_slider.thumb_shadow = None
## Загрузка###############################################
screen load():
    layer "over_screens"
    modal True
    zorder 300
    key "K_ESCAPE" action If(renpy.get_screen("load"), Hide("load"), Hide("navigation"))
    key "mouseup_3" action If(renpy.get_screen("load"), Hide("load"), Hide("navigation"))
    if main_menu:
        imagemap:
            ground 'gui/main/load.webp'
            idle 'gui/main/load.webp'
            hover 'gui/main/load-main_menu-hover.webp'
            selected_idle 'gui/main/load-main_menu-hover-1.webp'
            selected_hover 'gui/main/load-main_menu-hover.webp'
            hotspot (493, 661, 69, 68) clicked FilePage(1)
            hotspot (616, 658, 67, 71) clicked FilePage(2)
            hotspot (740, 661, 65, 66) clicked FilePage(3)
            hotspot (863, 660, 65, 69) clicked FilePage(4)
            hotspot (985, 661, 67, 67) clicked FilePage(5)
            hotspot (1108, 659, 67, 70) clicked FilePage(6)
            hotspot (1231, 659, 66, 70) clicked FilePage(7)
            hotspot (1355, 661, 66, 69) clicked FilePage(8)
            hotspot (332, 650, 87, 90) clicked FilePagePrevious()
            hotspot (1495, 650, 90, 89) clicked FilePageNext()

            hotspot (331, 84, 394, 227) clicked FileLoad(1):
                use load_save_slot(number=1)
            hotspot (762, 84, 394, 227) clicked FileLoad(2):
                use load_save_slot(number=2)
            hotspot (1192, 84, 394, 227) clicked FileLoad(3):
                use load_save_slot(number=3)
            hotspot (331, 367, 394, 225) clicked FileLoad(4):
                use load_save_slot(number=4)
            hotspot (762, 367, 394, 225) clicked FileLoad(5):
                use load_save_slot(number=5)
            hotspot (1192, 367, 394, 225) clicked FileLoad(6):
                use load_save_slot(number=6)

            hotspot (928, 794, 92, 90) action Hide("load"), Show("main_menu")
            hotspot (120, 934, 330, 109) action Start()
            hotspot (573, 934, 327, 109) action Hide("load"), Show("main_menu")
            hotspot (1021, 934, 329, 109) action Hide("load"), Show("preferences")
            hotspot (1472, 934, 328, 109) action Hide("load"), Quit(confirm=True)
    else:
        imagemap:
            ground 'gui/game/load-game.webp'
            idle 'gui/game/load-game.webp'
            hover 'gui/game/load-game-hover.webp'
            selected_idle 'gui/game/load-game-hover-1.webp'
            selected_hover 'gui/game/load-game-hover.webp'

            hotspot (493, 661, 69, 68) clicked FilePage(1)
            hotspot (616, 658, 67, 71) clicked FilePage(2)
            hotspot (740, 661, 65, 66) clicked FilePage(3)
            hotspot (863, 660, 65, 69) clicked FilePage(4)
            hotspot (985, 661, 67, 67) clicked FilePage(5)
            hotspot (1108, 659, 67, 70) clicked FilePage(6)
            hotspot (1231, 659, 66, 70) clicked FilePage(7)
            hotspot (1355, 661, 66, 69) clicked FilePage(8)
            hotspot (332, 650, 87, 90) clicked FilePagePrevious()
            hotspot (1495, 650, 90, 89) clicked FilePageNext()
## Со        hotspot (712, 980, 178, 100) clicked Hide("save"), Show("load")
## Со        hotspot (1030, 980, 178, 100) clicked Show("delete_save", fr = "save")

            hotspot (331, 84, 394, 227) clicked FileLoad(1):
                use load_save_slot(number=1)
            hotspot (762, 84, 394, 227) clicked FileLoad(2):
                use load_save_slot(number=2)
            hotspot (1192, 84, 394, 227) clicked FileLoad(3):
                use load_save_slot(number=3)
            hotspot (331, 367, 394, 225) clicked FileLoad(4):
                use load_save_slot(number=4)
            hotspot (762, 367, 394, 225) clicked FileLoad(5):
                use load_save_slot(number=5)
            hotspot (1192, 367, 394, 225) clicked FileLoad(6):
                use load_save_slot(number=6)

            hotspot (928, 794, 92, 90) action Hide("load"), Show("navigation")
            hotspot (1782, 942, 90, 90) action Hide("load"),Hide("navigation")
            hotspot (47, 943, 91, 89) action Hide("load"), MainMenu()
            hotspot (195, 933, 328, 108) action Hide("load"), Show("save")
            hotspot (597, 934, 326, 108) action Hide("load"), Show("navigation")
            hotspot (997, 934, 327, 109) action Hide("load"), Show("preferences")
            hotspot (1397, 933, 328, 108) action Hide("load"),Show("navigation"), Quit()
## Сохранение ###############################################
screen save():
    layer "over_screens"
    modal True
    zorder 300
    style_prefix "save"
    key "mouseup_3" action If(renpy.get_screen("save"), Hide("save"), Hide("navigation"))
    key "K_ESCAPE" action If(renpy.get_screen("save"), Hide("save"), Hide("navigation"))
    imagemap:
        ground 'gui/game/save-game.webp'
        idle 'gui/game/save-game.webp'
        hover 'gui/game/save-game-hover.webp'
        selected_idle 'gui/game/save-game-hover-1.webp'
        selected_hover 'gui/game/save-game-hover.webp'

        hotspot (493, 661, 69, 68) clicked FilePage(1)
        hotspot (616, 658, 67, 71) clicked FilePage(2)
        hotspot (740, 661, 65, 66) clicked FilePage(3)
        hotspot (863, 660, 65, 69) clicked FilePage(4)
        hotspot (985, 661, 67, 67) clicked FilePage(5)
        hotspot (1108, 659, 67, 70) clicked FilePage(6)
        hotspot (1231, 659, 66, 70) clicked FilePage(7)
        hotspot (1355, 661, 66, 69) clicked FilePage(8)
        hotspot (332, 650, 87, 90) clicked FilePagePrevious()
        hotspot (1495, 650, 90, 89) clicked FilePageNext()
## Со        hotspot (712, 980, 178, 100) clicked Hide("save"), Show("load")
## Со        hotspot (1030, 980, 178, 100) clicked Show("delete_save", fr = "save")

        hotspot (331, 84, 394, 227) clicked FileSave(1):
            use load_save_slot(number=1)
        hotspot (762, 84, 394, 227) clicked FileSave(2):
            use load_save_slot(number=2)
        hotspot (1192, 84, 394, 227) clicked FileSave(3):
            use load_save_slot(number=3)
        hotspot (331, 367, 394, 225) clicked FileSave(4):
            use load_save_slot(number=4)
        hotspot (762, 367, 394, 225) clicked FileSave(5):
            use load_save_slot(number=5)
        hotspot (1192, 367, 394, 225) clicked FileSave(6):
            use load_save_slot(number=6)

        hotspot (928, 794, 92, 90) action Hide("save"), Show("navigation")
        hotspot (1782, 942, 90, 90) action [Hide("save"),Hide("navigation"), Return()]
        hotspot (47, 943, 91, 89) action Hide("save"), MainMenu()
        hotspot (195, 933, 328, 108) action Hide("save"),Show("navigation")
        hotspot (597, 934, 326, 108) action Hide("save"), Show("load")
        hotspot (997, 934, 327, 109) action Hide("save"), Show("preferences")
        hotspot (1397, 933, 328, 108) action Hide("save"),Show("navigation"), Quit()
    fixed:


        order_reverse True
        frame:
            background None
            xmaximum 1000   #this value is in pixels, you may need to change it to match the size of whatever your dialogue box's actual width is
            ymaximum 400
            xalign 0.37
            yalign 0.81
            xsize 1000
            ysize 50
            input default "" value VariableInputValue("save_name") length 15 allow " 0123456789абвгдежзийклмнопрстуфхцчшщыэюяьёАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЫЬЭЮЯqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"

style input:
    color "#fff"
    size 40

screen load_save_slot:
    $ file_text = FileSaveName(number)





    add FileScreenshot(number) xalign 0.5 yalign 0.5
    if file_text:
        add Solid("#000000", xysize=(385, 37)) alpha 0.8 xoffset -3 yalign 0.985  xalign 0.8
        text file_text size 25 yalign 0.985  xalign 0.05
    text FileSlotName(number, 6) xalign 0.05
    text FileTime(number, format=_("{#file_time} %A, %H:%M"))  xalign 0.2
    if FileLoadable(number):
        imagebutton xalign 0.88 yalign 0.97 idle "gui/del1.png" hover "gui/del-hover1.png" action FileDelete(number)
        key "save_delete" action FileDelete(number)

#Переименовать


##Выбор
screen choice(items):
    if otv == 1:


        style_prefix "choice_2"
        layer "master"
        vpgrid:
            cols 2
            spacing 10
            xalign 0.5
            yalign 0.725

            for i in items:
                textbutton i.caption action i.action text_xalign get_align(i.caption)
                add get_image(i.caption) yalign .5 xpos pad
    else:
        style_prefix "choice"


        hbox:
            for i in items:
                textbutton i.caption action i.action


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True
style choice_2_vbox is hbox
style choice_2_button is button
style choice_2_button_text is button_text

style choice_2_hbox:
    xalign 0.5
    yalign 0.5

    spacing gui.choice_2_spacing

style choice_2_button is default:
    properties gui.button_properties("choice_2_button")
    background Frame("gui/phone/pchoice.png",0,0)
    hover_background  Frame("gui/phone/pchoice-hover.png",0,0)
    spacing gui.choice_2_spacing
style choice_button_2_text is default:
    properties gui.button_text_properties("choice_2_button")
    align (0.5, 0.5)
    spacing gui.choice_2_spacing

style choice_vbox is hbox
style choice_button is button
style choice_button_text is button_text

style choice_hbox:
    xalign 0.5
    yalign 0.817

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")


style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    align (0.5, 0.5)

## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    zorder 100

    if quick_menu:
        textbutton("ADULT OYUN ÇEVİRİ HİLELER"):
            action Show("cheatMenu"), ToggleVariable("quick_menu")
            xalign 1.0
            yalign 1.0

 ##       hbox:
 ##           style_prefix "quick"
##
 ##           xalign 0.5
 ##           yalign 1.0

##            textbutton _("Вернуться") action Rollback()
 ##           textbutton _("История") action ShowMenu('history')
 ##           textbutton _("Пропустить") action Skip() alternate Skip(fast=True, confirm=True)
 ##           textbutton _("Авто") action Preference("auto-forward", "toggle")
 ##           textbutton _("Сохранить") action ShowMenu('save')
 ##           textbutton _("Б.Сохранение") action QuickSave()
 ##           textbutton _("Б.Загрузка") action QuickLoad()
 ##          textbutton _("Параметры") action ShowMenu('preferences')


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"
    if not renpy.in_rollback():
        frame at notify_appear:
            text "[message!tq]"

        timer 1.5 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty


style notify_frame:
    xalign 0.98
    yalign 0.015

    #background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    size 60
    font "gui/fonts/ROBOTO-THIN.ttf"


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    hbox:
        style_prefix "quick"

        xalign 0.5
        yalign 1.0

        textbutton _("Back") action Rollback()
        textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
        textbutton _("Auto") action Preference("auto-forward", "toggle")
        textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 900


screen gui_tooltip:
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

init python:
    renpy.music.register_channel("gs_2_1", "sfx", False)
    renpy.music.register_channel("mute_1", "sfx", False)
