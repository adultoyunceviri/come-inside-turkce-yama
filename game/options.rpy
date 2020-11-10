## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.
define analytics.tracking_id = "UA-141770414-1"
define config.name = _("Come Inside - Episode II")

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True
define config.default_fullscreen = True
define config.default_music_volume = 0.7
define config.default_sfx_volume = 0.7
define config.default_language = "english"
## The version of the game.

define config.version = "0.2.1"



## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
""")


## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "CI_0.2.1"
define config.layers = ['master', 'transient', 'screens', 'over_screens', 'overlay']


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/As_We_Go.mp3"


## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 0

default preferences.gl_framerate = 60
## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "CI-1548506988"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "renpy-icon.png"
define config.windows_icon = "renpy-icon.png"



## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')

## Set this to a string containing your Apple Developer ID Application to enable
## codesigning on the Mac. Be sure to change it to your own Apple-issued ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"

init python:
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['game_menu'].remove('K_MENU')
    #репутация
    def reput_kelly(): #Репутация
     #Kelly
        global p_kelly
        global p_kelly_old
        global dif_kelly
        dif_kelly = p_kelly - p_kelly_old
        if dif_kelly == 0:
            return
        if dif_kelly == 1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kelly")
                renpy.show_screen("rep_up_sm") #+1
        if dif_kelly == 3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kelly")
                renpy.show_screen("rep_up_b") #+3
        if dif_kelly == -1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kelly")
                renpy.show_screen("rep_d_sm")
        if dif_kelly == -3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kelly")
                renpy.show_screen("rep_d_b")
        p_kelly_old = p_kelly
        return
    def reput(): #Репутация
        #Sister
        global p_sister
        global p_sister_old
        global dif_s
        dif_s = p_sister - p_sister_old
        if dif_s == 0:

            return
        if dif_s == 1 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sister")
                renpy.show_screen("rep_up_sm") #+1
        if dif_s == 1 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Lindsey")
                renpy.show_screen("rep_up_sm") #+1
        if dif_s == 3 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sister")
                renpy.show_screen("rep_up_b") #+3
        if dif_s == 3 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Lindsey")
                renpy.show_screen("rep_up_b") #+3
        if dif_s == -1 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sister")
                renpy.show_screen("rep_d_sm") #-1
        if dif_s == -1 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Lindsey")
                renpy.show_screen("rep_d_sm") #-1
        if dif_s == -3 and persistent.patch_enabled == True and persistent.rp == True:
           if not renpy.in_rollback():
                renpy.notify("Sister")
                renpy.show_screen("rep_d_b") #-3
        if dif_s == -3 and persistent.patch_enabled == False and persistent.rp == True:
           if not renpy.in_rollback():
                renpy.notify("Lindsey")
                renpy.show_screen("rep_d_b") #-3
        p_sister_old = p_sister
        return
    def reput_sher(): #Репутация
        #Sheril
        global p_sher
        global p_sher_old
        global dif_sher
        dif_sher = p_sher - p_sher_old
        if dif_sher == 0:

            return
        if dif_sher == 1 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Little sis")
                renpy.show_screen("rep_up_sm") #+1
        if dif_sher == 1 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sheryl")
                renpy.show_screen("rep_up_sm") #+1
        if dif_sher == 3 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Little sis")
                renpy.show_screen("rep_up_b") #+3
        if dif_sher == 3 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sheryl")
                renpy.show_screen("rep_up_b") #+3
        if dif_sher == -1 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Little sis")
                renpy.show_screen("rep_d_sm") #-1
        if dif_sher == -1 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sheryl")
                renpy.show_screen("rep_d_sm") #-1
        if dif_sher == -3 and persistent.patch_enabled == True and persistent.rp == True:
           if not renpy.in_rollback():
                renpy.notify("Little sis")
                renpy.show_screen("rep_d_b") #-3
        if dif_sher == -3 and persistent.patch_enabled == False and persistent.rp == True:
           if not renpy.in_rollback():
                renpy.notify("Sheryl")
                renpy.show_screen("rep_d_b") #-3
        p_sher_old = p_sher
        return
    def reput_l(): #Репутация
        #Lora
        global p_lora
        global p_lora_old
        global dif_l
        dif_l = p_lora - p_lora_old
        if dif_l == 0:
            return
        if dif_l == 1 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Mom")
                renpy.show_screen("rep_up_sm")
        if dif_l == 1 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Lora")
                renpy.show_screen("rep_up_sm")
        if dif_l == 3 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Mom")
                renpy.show_screen("rep_up_b")
        if dif_l == 3 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Lora")
                renpy.show_screen("rep_up_b")
        if dif_l == -1 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Mom")
                renpy.show_screen("rep_d_sm")
        if dif_l == -1 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Lora")
                renpy.show_screen("rep_d_sm")
        if dif_l == -3 and persistent.patch_enabled == True and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Mom")
                renpy.show_screen("rep_d_b")
        if dif_l == -3 and persistent.patch_enabled == False and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Lora")
                renpy.show_screen("rep_d_b")
        p_lora_old = p_lora
        return
    def reput_sh(): #Репутация
        #Sheila
        global p_sheila
        global p_sheila_old
        global dif_sh
        dif_sh = p_sheila - p_sheila_old
        if dif_sh == 0:
            return
        if dif_sh == 1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sheila")
                renpy.show_screen("rep_up_sm")
        if dif_sh == 3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sheila")
                renpy.show_screen("rep_up_b")
        if dif_sh == -1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sheila")
                renpy.show_screen("rep_d_sm")
        if dif_sh == -3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Sheila")
                renpy.show_screen("rep_d_b")
        p_sheila_old = p_sheila
        return
    def reput_ki(): #Репутация
        #Kiara
        global p_kiara
        global p_kiara_old
        global dif_ki
        dif_ki = p_kiara - p_kiara_old
        if dif_ki == 0:
            return
        if dif_ki == 1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kiara")
                renpy.show_screen("rep_up_sm")
        if dif_ki == 3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kiara")
                renpy.show_screen("rep_up_b")
        if dif_ki == -1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kiara")
                renpy.show_screen("rep_d_sm")
        if dif_ki == -3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kiara")
                renpy.show_screen("rep_d_b")
        p_kiara_old = p_kiara
        return
    def reput_j(): #Репутация
        #Jen
        global p_jen
        global p_jen_old
        global dif_j
        dif_j = p_jen - p_jen_old
        if dif_j == 0:
            return
        if dif_j == 1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Jen")
                renpy.show_screen("rep_up_sm")
        if dif_j == 3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Jen")
                renpy.show_screen("rep_up_b")
        if dif_j == -1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Jen")
                renpy.show_screen("rep_d_sm")
        if dif_j == -3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Jen")
                renpy.show_screen("rep_d_b")
        p_jen_old = p_jen
        return
    def reput_kev(): #Репутация
        #Kevin
        global p_kevin
        global p_kevin_old
        global dif_kev
        dif_kev = p_kevin - p_kevin_old
        if dif_kev == 0:
            return
        if dif_kev == 1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kevin")
                renpy.show_screen("rep_up_sm")
        if dif_kev == 3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kevin")
                renpy.show_screen("rep_up_b")
        if dif_kev == -1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kevin")
                renpy.show_screen("rep_d_sm")
        if dif_kev == -3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Kevin")
                renpy.show_screen("rep_d_b")
        p_kevin_old = p_kevin
        return
    def reput_b(): #Репутация
        #Boss
        global p_boss
        global p_boss_old
        global dif_b
        dif_b = p_boss - p_boss_old
        if dif_b == 0:
            return
        if dif_b == 1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Boss")
                renpy.show_screen("rep_up_sm")
        if dif_b == 3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Boss")
                renpy.show_screen("rep_up_b")
        if dif_b == -1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Boss")
                renpy.show_screen("rep_d_sm")
        if dif_b == -3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Boss")
                renpy.show_screen("rep_d_b")
        p_boss_old = p_boss
        return
    def reput_az(): #Репутация
        #Aznu
        global p_aznu
        global p_aznu_old
        global dif_az
        dif_az = p_aznu - p_aznu_old
        if dif_az == 0:
            return
        if dif_az == 1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Aznu")
                renpy.show_screen("rep_up_sm")
        if dif_az == 3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Aznu")
                renpy.show_screen("rep_up_b")
        if dif_az == -1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Aznu")
                renpy.show_screen("rep_d_sm")
        if dif_az == -3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Aznu")
                renpy.show_screen("rep_d_b")
        p_aznu_old = p_aznu
        return
    def reput_tay(): #Репутация
        #Taylor
        global p_tay
        global p_tay_old
        global dif_tay
        dif_tay = p_tay - p_tay_old
        if dif_tay == 0:
            return
        if dif_tay == 1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Taylor")
                renpy.show_screen("rep_up_sm")
        if dif_tay == 3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Taylor")
                renpy.show_screen("rep_up_b")
        if dif_tay == -1 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Taylor")
                renpy.show_screen("rep_d_sm")
        if dif_tay == -3 and persistent.rp == True:
            if not renpy.in_rollback():
                renpy.notify("Taylor")
                renpy.show_screen("rep_d_b")
        p_tay_old = p_tay
        return
    def bla_bla(): #следим отображать ли главную
        if glavn == True:
            renpy.show_screen("scr_dnev") #Если возврат, а не закрытие отдаем экран главной

    def label_callback(label, abnormal): #аналитика

        # Filter out labels that are part of Ren'Py and not the game.
        filename = renpy.get_filename_line()[0]
        if filename.startswith("renpy/common/"):
            return

        analytics.event("Label", label)

    config.label_callback = label_callback


image helpdi = "gui/dnev/helpd.webp"
image dnev = "gui/dnev/notepad-open-25.webp"
image do = Movie(play="gui/dnev/no.webm", mask="gui/dnev/mask.webm")
image dnevnik = Ani("gui/dnev/notepad-open-", 25, 0.01, loop = False, reverse = False, ext="webp")
#Стрелка +1
image rep_up_small = Ani("gui/rep/upsmall/Rep_small_up-", 114, 0.02, loop = False, reverse = False, ext="png")
#Стрелка +3
image rep_up_big = Ani("gui/rep/upbig/Rep_big_up-", 114, 0.02, loop = False, reverse = False, ext="png")
#Стрелка -1
image rep_d_small = Ani("gui/rep/dsmall/Rep_small_down-", 114, 0.02, loop = False, reverse = False, ext="png")
#Стрелка -3
image rep_d_big = Ani("gui/rep/dbig/Rep_big_down-", 114, 0.02, loop = False, reverse = False, ext="png")
image dnevnik-close: #Я не ебу почему реверс не работает
        "gui/dnev/notepad-open-25.webp"
        0.01
        "gui/dnev/notepad-open-24.webp"
        0.01
        "gui/dnev/notepad-open-23.webp"
        0.01
        "gui/dnev/notepad-open-22.webp"
        0.01
        "gui/dnev/notepad-open-21.webp"
        0.01
        "gui/dnev/notepad-open-20.webp"
        0.01
        "gui/dnev/notepad-open-19.webp"
        0.01
        "gui/dnev/notepad-open-18.webp"
        0.01
        "gui/dnev/notepad-open-17.webp"
        0.01
        "gui/dnev/notepad-open-16.webp"
        0.01
        "gui/dnev/notepad-open-15.webp"
        0.01
        "gui/dnev/notepad-open-14.webp"
        0.01
        "gui/dnev/notepad-open-13.webp"
        0.01
        "gui/dnev/notepad-open-12.webp"
        0.01
        "gui/dnev/notepad-open-11.webp"
        0.01
        "gui/dnev/notepad-open-10.webp"
        0.001
        "gui/dnev/notepad-open-9.webp"
        0.001
        "gui/dnev/notepad-open-8.webp"
        0.001
        "gui/dnev/notepad-open-7.webp"
        0.001
        "gui/dnev/notepad-open-6.webp"
        0.001
        "gui/dnev/notepad-open-5.webp"
        0.001
        "gui/dnev/notepad-open-4.webp"
        0.001
        "gui/dnev/notepad-open-3.webp"
        0.001
        "gui/dnev/notepad-open-2.webp"
        0.001
        "gui/dnev/notepad-open-1.webp"
        0.001

init python:
    # перелистывание
    # сначала новые страницы, затем старые
    # если страницу не указывать, то будет пустая
    def pflip(new1="pageleft", new2="pageright", old1="pageleft", old2="pageright", delay=.5):
        renpy.hide("pleft")
        renpy.hide("pright")
        renpy.show(old1, [lf()], tag="pleft")
        renpy.show(new2, [rg()], tag="pright")
        renpy.show(old2, [r2c(delay*.5)], tag="plist")
        renpy.pause(delay*.5)
        renpy.show(new1, [c2l(delay*.5)], tag="plist")
        renpy.pause(delay*.5)
        renpy.show(new1, [lf()], tag="pleft")
        renpy.show(new2, [rg()], tag="pright")
        renpy.hide("plist")
    def lflip(new1="pageleft", new2="pageright", old1="pageleft", old2="pageright", delay=.5): #Вправо
        renpy.hide("pright")
        renpy.hide("pleft")

        renpy.show(new1, [lf()], tag="pleft")
        renpy.show(old2, [rg()], tag="pright")

        renpy.show(old1, [l2c(delay*.5)], tag="plist")
        renpy.pause(delay*.5)
        renpy.show(new2, [c2r(delay*.5)], tag="plist")
        renpy.pause(delay*.5)

        renpy.show(new1, [lf()], tag="pleft")
        renpy.show(new2, [rg()], tag="pright")

        renpy.hide("plist")


init:
    # положение левой страницы
    transform lf():
        xpos .5005 xanchor 1.0 ypos  0
    # положение правой страницы
    transform rg():
        xpos .5 xanchor 0.0 ypos  0
    # right to center (листание справа к центру)
    transform r2c(delay=.25):
        xpos .5 xanchor 0.0 xzoom 1.0 ypos 0
        easeout delay xzoom 0.001
    # center to left (листание от центра влево)
    transform c2l(delay=.25):
        xpos .5005 xanchor 1.0 xzoom 0.001 ypos 0
        easein delay xzoom 1.0
    # left to center слева к центру
    transform l2c(delay=.25):
        xpos .5005 xanchor 1.0  xzoom 1.0 ypos 0
        easeout delay xzoom 0.001
    #center to right от центра вправо
    transform c2r(delay=.25):
        xpos .5 xanchor 0.0 xzoom 0.001 ypos 0
        easeout delay xzoom 1.0
init python:
    # стек для хранения состояния экранов до вызова call
    screens = []
    # действие по кнопке ESC
    gamemenu = config.game_menu_action
    # добавить очередной список экранов
    def s_push(item):
        global screens
        screens.append(item)
    # извлечь последний список экранов
    def s_pop():
        global screens
        if len(screens) > 0:
            return screens.pop()
        return []
    # стартовое количество денег для тестирования
    money = 10
    # флаг вызова локации в новом контексте
    is_call = False
    # из экрана нельзя выполнить обычный call label
    # создадим его аналог
    class MyCall(Action):
        def __init__(self, label, *args, **kwargs):
            self.label = label
            self.args = args
            self.kwargs = kwargs
        def __call__(self):
            global screens, is_call
            # отключаем ESC
            config.game_menu_action = NullAction()
            # запоминаем экраны
            s_push(renpy.current_screen().screen_name)
            # включаем флаг вызова нового контекста (чтобы спрятать кнопку)
            is_call = True
            # вызываем локацию в новом контексте
            renpy.call_in_new_context(self.label, *self.args, **self.kwargs)
    # функция для восстановления экранов в новом контексте
    def show_screens():
        for i in screens[-1:]:
            renpy.show_screen(i)
    # функция для возвращениея из локации в новом контексте
    def myreturn():
        global is_call
        # спрятать экраны
        for i in s_pop():
            renpy.hide_screen(i)
        # снять флаг новой локации, чтобы кнопка ее вызова снова появилась
        is_call = len(screens) > 0
        if not is_call:
            config.game_menu_action = gamemenu
        # сохранение данных игры
        renpy.retain_after_load()
        Return()()
    # чтобы можно было привязать к копке, например
    MyReturn = renpy.curry(myreturn)

init python:
    def eyewarp(x):
        return x**1.33
    eye_open = ImageDissolve("gui/eye.png", .5, ramplen=128, reverse=False, time_warp=eyewarp)
    eye_shut = ImageDissolve("gui/eye.png", .5, ramplen=128, reverse=True, time_warp=eyewarp)

    if not persistent.splashsc:
        persistent.splashsc = False

init python:


    # поиск тегов с настройками кнопки
    import re
    def get_tags(text, prefix='#'):
        # выуживаем все теги ремарок
        return re.findall('{' + prefix + '([^}]+)}', text)

    # поиск в строке тега (и его значения) по имени
    def get_tag(text, tag, default=None):
        val = default
        tags = get_tags(text)
        for i in tags:
            parts = i.split('=')
            if len(parts) > 0:
                if parts[0].strip() == tag.strip():
                    if len(parts) > 1:
                        val = parts[1]
        return val

    # найти в ремарках значение тега 'image'
    def get_image(text):
        # по-умолчанию картинки нет
        return get_tag(text, 'image')

    # найти в ремарках значение тега 'align'
    def get_align(text):
        # по-умолчанию выравнивание текста берем стандартное
        return float(get_tag(text, 'align', str(gui.choice_button_text_xalign)))

    build.directory_name = "ComeInside-0.2.1"
    build.archive("Patch", "all")
    build.classify('game/patch/**.**', 'Patch')

init 111 python:
    #СМС Настройки
#Текст
#Слева
    renpy.register_style_preference(
        "text", "White", style.sms_l_text, "color", "#fff")
    renpy.register_style_preference(
        "text", "Blue", style.sms_l_text, "color", "#003399")
    renpy.register_style_preference(
        "text", "Yellow", style.sms_l_text, "color", "#ffff01")
    renpy.register_style_preference(
        "text", "Black", style.sms_l_text, "color", "#000")
#Справа
    renpy.register_style_preference(
        "textr", "White", style.sms_r_text, "color", "#fff")
    renpy.register_style_preference(
        "textr", "Blue", style.sms_r_text, "color", "#003399")
    renpy.register_style_preference(
        "textr", "Yellow", style.sms_r_text, "color", "#ffff01")
    renpy.register_style_preference(
        "textr", "Black", style.sms_r_text, "color", "#000")
#Фон
    renpy.register_style_preference(
        "bgl", "Default", style.sms_l, "background", Frame("gui/phone/smsleft.png", 16, 16))
    renpy.register_style_preference(
        "bgl", "Blue", style.sms_l, "background", Frame("gui/phone/smsleft-b.png", 16, 16))
    renpy.register_style_preference(
        "bgl", "Yellow", style.sms_l, "background", Frame("gui/phone/smsleft-y.png", 16, 16))
    renpy.register_style_preference(
        "bgl", "Black", style.sms_l, "background", Frame("gui/phone/smsleft-bl.png", 16, 16))
#Фон
    renpy.register_style_preference(
        "bgr", "Default", style.sms_r, "background", Frame("gui/phone/smsright.png", 16, 16))
    renpy.register_style_preference(
        "bgr", "Blue", style.sms_r, "background", Frame("gui/phone/smsleft-b.png", 16, 16))
    renpy.register_style_preference(
        "bgr", "Yellow", style.sms_r, "background", Frame("gui/phone/smsleft-y.png", 16, 16))
    renpy.register_style_preference(
        "bgr", "Black", style.sms_r, "background", Frame("gui/phone/smsleft-bl.png", 16, 16))
