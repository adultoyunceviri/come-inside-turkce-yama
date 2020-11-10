#Ну и зачем ты тут?
init  python:
    # автоматическое объявление изображений
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']

    if persistent.patch_enabled:
        config.automatic_images_strip = ['patch','gui','images']
    else:
        config.automatic_images_strip = ['gui','images']






define lora = DynamicCharacter("mom_name", color="#ffffff", who_suffix = ':')
define lin = DynamicCharacter("sister_name", color="#ffffff", who_suffix = ':')
define grand = DynamicCharacter("gmom_name", color="#ffffff", who_suffix = ':')

define mod = Character("OscarSix", color="#0f0", who_suffix = ':')
define gg = Character(_("[namegg]"), color="#ffffff", who_suffix = ':')
define kev = Character("Кевин", color="#ffffff", who_suffix = ':')
define sos = Character("Соседка", color="#ffffff", who_suffix = ':')
define un = Character("???", color="#ffffff", who_suffix = ':')
define k = Character("Келли", color="#ffffff", who_suffix = ':')
define j = Character("Джен", color="#ffffff", who_suffix = ':')
define ki = Character("Киара", color="#ffffff", who_suffix = ':')
define b = Character("Босс", color="#ffffff", who_suffix = ':')
define st = Character("Стейси", color="#ffffff", who_suffix = ':')
define sa = Character("Салли", color="#ffffff", who_suffix = ':')
define a = Character("Азну", color="#ffffff", who_suffix = ':')
define sh = Character("Шейла", color="#ffffff", who_suffix = ':')

define audio.moto = "sounds/cimoto.ogg"
define audio.relax = "music/r-relax.mp3"
define audio.lora = "music/As_We_Go.mp3"
define audio.youth = "music/midsummer-sky.mp3"
define audio.sex = "music/acid-trumpet.mp3"
define audio.night = "music/covert-affair.mp3"

define audio.knock = "sounds/knock.ogg"
define audio.photo = "sounds/ci2photo.ogg"
define audio.sms = "sounds/sms_l.ogg"
define audio.vibr = "sounds/civibrate.ogg"
define audio.cldoor = "sounds/cldoor.ogg"
define audio.indaclub = "music/indaclub.ogg"
define audio.shower = "sounds/shower.ogg"
define audio.shop = "sounds/shop.ogg"
define audio.watertap = "sounds/ciwatertap.ogg"
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

init:
    default sketchbookScenes = False
    default callQuiet = False
    default modSlavePaitingBoth = False
    define persistent.rp = False
    default naz = 0 #вырубает назад, дочитываем смс
    default new_flag = 0 #Новоесообщение
    default contact_flag = 0 #номер абонента
    default mute = False #Вибро или Звук
    default show_gal = 0 #Какую картинку в галерее показывать
    default phone_back = 0 # Какой фон
    default cont = False #Зашли из контактов? Для перемотки
    default sms_pics = False # Показывали картинку в СМС?
    default mob_sc = True # Еще не дошли до днева?
    default show_w = 0 #Окно с текстом
    default otv = 0 #ответысмс
    default ebpic = False #первая пикчаШейла
    default smsl_bg = 0 #Фон СМСЛ
    default smsl_txt = 0 #Текст СМСЛ
    default smsl_txt_2 = 0 #Текст СМСЛ
    default smsr_bg = 0 #Фон СМСР
    default smsr_txt = 0 #Текст СМСР

    default sms_sister = []
    default sms_kelly = []
    default sms_jhon = []
    default sms_kevin = []
    default s_kevin = 0
    default sms_cougar = []
    default sms_ella = []
    default p_kelly = 0
    default s_kelly = 0 #ответы 1 смс
    default s_kelly_2 = 0 #ответы 2
    default kelly_name = 0 #знаем ли имя
    default kelly_in = True #утром один или с келли?
    default sc9_nogi_f = False #ноги проходим первый раз?
    default sc10_mom = 0
    default sc10_sis = 0
    default sc10_st = 0 #stacey
    default sc10_st_whom = 0 #stacey kev or gg

    #Отношения
    default dif_s = 0 #разница_сестра
    default dif_l = 0 #разница_lora
    default dif_kelly = 0 #разница_kelly
    default dif_sh = 0 #разница_sheila
    default dif_ki = 0 #разница_kiara
    default dif_j = 0 #разница_jen
    default dif_kev = 0 #разница_kevin
    default dif_b = 0 #разница_boss
    default dif_az = 0 #разница_aznu
    #старое значнеие отношений
    default p_sister_old = 0 #очки отношений Старые
    default p_lora_old = 0 #лора очки отношений
    default p_kelly_old = 0
    default p_sheila_old = 0
    default p_kiara_old = 0
    default p_jen_old = 0
    default p_kevin_old = 0
    default p_boss_old = 0
    default p_aznu_old = 0
    #Какое имя?
    default name_s = False #разница_сестра
    default name_l = False #разница_lora
    default name_kelly = False #разница_kelly
    default name_sh = False #разница_sheila
    default name_ki = False #разница_kiara
    default name_j = False #разница_jen
    default name_kev = False #разница_kevin
    default name_b = False #разница_boss
    default name_az = False #разница_aznu

    default p_sister = 0 #очки отношений

    default m_sister = 0 #ответы 1 смс
    default s_sister = 0 #ответы 2 переживания
    default slave_sister = 0 #Делаем рабыней?
    default love_sister = 0 #Любовь сестра
    default dengi_sister = 0 #спрашивали про деньги? сестра
    default gsc7_menu_p = 0
    default sher_sister = 0 #спрашивали про сестру? сестра
    default rest_sister = 0 #ресторан сестра
    default pool_sister_2 = False #2ариант
    default pool_sister_3 = False #3ариант
    default pool_sister_4 = False #4ариант
    default pravda_sister = 0 #Знает ли правду
    default lozh_sister = 0 #Знает ли ложь
    default slave_k = 0
    default slave_j = 0 #jen
    default slave_ki = 0

    default slave_s = 0 #sally
    default slave_sh = 0 #sheila
    default slave_m = 0 #mary
    default slave_t = 0 #taylor
    default slave_lora = 0
    default p_lora = 0 #лора очки отношений

    default p_kevin = 0
    default p_ylora = 0
    default p_jen = 0
    default j_opazd = 0 # опаздываем к боссу?
    default j_project = 0 # инвестировали?
    default j_deep = 0 # видели?
    default p_kiara = 0
    default p_aznu = 0
    default p_sheila = 0
    default sh_rude = 0
    default sh_love = 0
    default sh_orgasm = 0 #вирт

    default p_boss = 0
    default ntr = 0 # -10 = чужих, - 50 = всех 0 = пофиг 10 = обожаю
    default ntr_1  = 0
    default sex = 0
    default k_sex = 0 #kelly
    default lin_sex = 0 #lindsey
    default ki_sex = 0 #kiara
    default j_sex = 0 #jen
    default lora_sex = 0 #lora
    default s_sex = 0 #sally
    default st_sex = 0 #stacey
    default sh_sex  = 0 #sheila
    default m_sex  = 0 #mary
    default t_sex  = 0 #taylor
    default a_sex  = 0 #aznu

    default tits = 0
    default k_tits = 0 #kelly
    default lin_tits = 0 #lindsey
    default ki_tits = 0 #kiara
    default j_tits = 0 #jen
    default lora_tits = 0 #lora
    default s_tits = 0 #sally
    default st_tits = 0 #stacey
    default sh_tits  = 0 #sheila
    default m_tits  = 0 #mary
    default t_tits  = 0 #taylor
    default a_tits  = 0 #aznu

    default mouth = 0

    default k_mouth = 0 #kelly
    default lin_mouth = 0 #lindsey
    default ki_mouth = 0 #kiara
    default j_mouth = 0 #jen
    default lora_mouth = 0 #lora
    default s_mouth = 0 #sally
    default st_mouth = 0 #stacey
    default sh_mouth = 0 #sheila
    default m_mouth = 0 #mary
    default t_mouth = 0 #taylor
    default a_mouth  = 0 #aznu

    default feet = 0
    default k_feet = 0 #kelly
    default lin_feet = 0 #lindsey
    default ki_feet = 0 #kiara
    default j_feet = 0 #jen
    default lora_feet = 0 #lora
    default s_feet = 0 #sally
    default st_feet = 0 #stacey
    default sh_feet = 0 #sheila
    default m_feet = 0 #mary
    default t_feet = 0 #taylor
    default a_feet  = 0 #aznu

    default anal = 0
    default k_anal = 0 #kelly
    default lin_anal = 0 #lindsey
    default ki_anal = 0 #kiara
    default j_anal = 0 #jen
    default lora_anal = 0 #lora
    default s_anal = 0 #sally
    default st_anal = 0 #stacey
    default sh_anal = 0 #sheila
    default m_anal = 0 #mary
    default t_anal = 0 #taylor
    default a_anal  = 0 #aznu

    #EPI
    default game_1_1 = False #В игры играли?
    default game_1_2 = False
    default game_1_3 = False
    default game_1_4 = False
    default game_2_1 = False
    default game_2_2 = False
    default game_2_3 = False
    default game_2_4 = False

    default helpd = False

    default glavn = False
    default g2_1 = False #Игра 2_1 вин\луз
    default in_game = False #Если в игре
    default dpage_0 = False #страницы открывали?
    default dpage_1 = False
    default dpage_2 = False
    default dpage_3 = False
    default dpage_4 = False
    default dpage_center = False
    default dpage_last = False
    default dpage_end = False

    default lora_page_1_scene = 0
    default lora_page_2_scene = 0
    default dafter_1 = False #первая сцена пройдена?
    default dafter_2 = False
    default dafter_3 = False
    default dafter_4 = False
    default dafter_5 = False
    default dafter_6 = False
    default dafter_7 = False
    default dafter_8 = False
    default dgame_2 = False #Блочим воспоминания
    default dgame_3 = False
    default dgame_4 = False
    default dgame_5 = False
    default dgame_6 = False
    default dgame_7 = False
    default dgame_8 = False

    default d_amount_1 = 0 #Сколько раз были в воспоминаниях?
    default d_amount_2 = 0
    default d_amount_3 = 0
    default d_amount_4 = 0
    default d_amount_5 = 0
    default d_amount_6 = 0
    default d_amount_7 = 0
    default d_amount_8 = 0

    #EP II
    default lora_page_3_scene = 0
    default lora_page_4_scene = 0
    default lora_page_5_scene = 0
    default lora_page_6_scene = 0
    default game_3_1 = False #В игры играли?
    default game_3_2 = False
    default game_3_3 = False
    default game_3_4 = False
    default game_4_1 = False
    default game_4_2 = False
    default game_4_3 = False
    default game_4_4 = False

    default dgame_9 = False #Блочим воспоминания
    default dgame_10 = False
    default dgame_11 = False
    default dgame_12 = False
    default dgame_13 = False
    default dgame_14 = False
    default dgame_15 = False
    default dgame_16 = False
    default d_amount_9 = 0 #Сколько раз были в воспоминаниях?
    default d_amount_10 = 0
    default d_amount_11 = 0
    default d_amount_12 = 0
    default d_amount_13 = 0
    default d_amount_14 = 0
    default d_amount_15 = 0
    default d_amount_16 = 0
    #Имена
    default mom_name = "Лора"
    default sister_name = "Сестра"
    default grand_name = "Бабушка"

init -3 python:
    persistent.patch_installed = False
init -1 python:
    if persistent.patch_installed and not persistent.patch_first_time:
        persistent.patch_enabled = False
        persistent.patch_first_time = True
    elif not persistent.patch_installed:
        persistent.patch_first_time = False
        persistent.patch_enabled = False

label main_menu:
    call screen main_menu
label start:
    hide screen main_menu
    $ sms_sister = []
    $ sms_kelly = []
    $ sms_jhon = []
    $ sms_kevin = []
    $ sms_cougar = []
    $ sms_ella = []
    $ sms_all = []
    $ smsl_bg = 0
    $ smsl_txt = 0
    $ smsr_bg = 0
    $ smsr_txt = 0
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.3)
    play music relax fadein 1.0
    show screen keymap_screen_b


    image black:
        Solid("#000")
    image white:
        Solid("#FFF")

    scene black

    if persistent.patch_enabled:
        $ mom_name = "Мама"
        $ sister_name = "Сестра"
        $ grand_name ="Бабушка"
    else:
        $ mom_name = "Лора"
        $ sister_name = "Линдси"
        $ grand_name = "Нэнси"



    scene black

    # Джон
    $ new_flag = 3 # новое смс, от Джон
    $ contact_flag = 3 #куда отправлять смс - Джон
    un "{i}Боже, голова болит даже во сне...{#l=Надеюсь вам понравился новый дом!}{i}"
    un "{i}Хотя сегодня, впервые за долгое время, я спал как убитый. И видел сны. Сны с ней...{#l=Вы мой лучший клиент за последние несколько лет.}{i}"
    un "{i}Пора вставать. Новый день, новый дом, новый город, хоть я в нем уже был...Надо бы зайти в аптеку.{#l=И, конечно, я работаю над вашей просьбой о вложении денег. Как только подходящий проект будет найден, я вам напишу.}{i}"
    $ sms_jhon = sms_all
    $ sms_all = []
    scene EP1 asp-1
    with eye_open
    un "{i}Это еще кто?{i}"
    scene EP1 acl-2

    stop music fadeout 1.0
    $ renpy.music.set_volume(0.7)
    play music indaclub fadein 1.0
    image flash:
        "#000"
        alpha 0.5
        linear .45 alpha 1.0
        linear .45 alpha 0.0
        repeat

    show flash

    pause

    scene EP1 acl-1
    show flash
    pause


    hide flash

    scene EP1 asp-2
    with vpunch
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.3)
    play music relax fadein 1.0
    un "{i}Ай! Кажется я был вчера в клубе...{/i}"
    un "{i}Видимо, голова болит из-за этого.{/i}"
    if persistent.patch_enabled:
        un "{i}Тетя Джил не особо жаловала такие места. {/i}"
    else:
        un "{i}Джил не особо жаловала такие места.{/i}"
    un "{i}Надо попытаться вспомнить, что вчера было. После того как рабочие сложили последние коробки, я сразу отправился на набережную. Пил виски, рисовал, предавался воспоминаниям.{/i}"
    $ config.overlay_functions.append(reput_kelly) #следим за репутацией Kelly
    $ config.overlay_functions.append(reput) #следим за репутацией Sister
    $ config.overlay_functions.append(reput_l) #следим за репутацией Lora
    $ config.overlay_functions.append(reput_sh) #следим за репутацией Sheila
    $ config.overlay_functions.append(reput_ki) #следим за репутацией Kiara
    $ config.overlay_functions.append(reput_j) #следим за репутацией Kelly
    $ config.overlay_functions.append(reput_kev) #следим за репутацией Kelly
    $ config.overlay_functions.append(reput_b) #следим за репутацией Kelly
    $ config.overlay_functions.append(reput_az) #следим за репутацией Kelly
    show screen mob_b
    # Систер
    $ new_flag = 1 # новое смс, от линдси
    $ contact_flag = 1 #куда отправлять смс - линдси
    $ naz = 1 #вырубаем назад - линдси
    if mute == False:
        play sound sms
    else:
        play sound vibr
    if persistent.patch_enabled:
        un "{i}Там было все как и тогда. Тепло, немноголюдно и открывался прекрасный вид. Одна лишь разница - теперь я там был один.{/i} {#l=Братишка, привет!}"
    else:
        un "{i}Там было все как и тогда. Тепло, немноголюдно и открывался прекрасный вид. Одна лишь разница - теперь я там был один.{/i} {#l=Привет!}"

    if sms_pics == True: #если открыл руками
        $ sms_all = sms_sister


    show screen sms_screen
    $ new_flag = 0
    $ sms_pics = False #Убираем отключение промотки, если открыл руками
     #отключаем окно
    $ contact_flag = 1 # если заходил в другие контакты
    $ renpy.start_predict_screen("rep_up_sm","rep_up_b","rep_d_sm","rep_d_b")
    un "{i}О чем она говорит?{/i} {#l=Я так рада, что ты вчера согласился меня приютить!}"
    $ show_w = 1
    "{#l=Эти чертовы подруги, одно название, как только у тебя проблемы, сразу пропадают.<<emoji u1F62B>><<emoji u1F621>>}"
    "{#l=Впрочем, все даже удачно сложилось, заодно посмотрю твой новый дом, да и тебя я уже сто лет не видела.}"
    if persistent.patch_enabled:
        "{#l=Я почти на месте! Надеюсь ты ждешь меня, братишка. Вчера ты вел себя странно, когда мы говорили.<<emoji u1F92A>><<emoji u1F92A>><<emoji u1F92A>>}"
    else:
        "{#l=Я почти на месте! Надеюсь ты ждешь меня. Вчера ты вел себя странно, когда мы говорили.<<emoji u1F92A>><<emoji u1F92A>><<emoji u1F92A>>}"
    "{#c=|pic_1>><<phone pic sis-phone-1>> }"
    $ show_w = 0
    $ otv = 1 #Стиль ответов
    menu:
        un "{i}Кажется вчера она мне звонила... Или я ей? В любом случае, я ничего не помню.{/i}"
        "Ээээ...":
            $ show_w = 1
            $ p_sister -= 1
            "{#r=Ээээ....}"

            $ m_sister += 1
            call lin_msg_1 from _call_lin_msg_1
        "Что!?":
            $ show_w = 1
            "{#r=Согласился приютить?}"
            call lin_msg_2 from _call_lin_msg_2
            $ m_sister += 2
        "Жду тебя!":
            $ show_w = 1
            $ p_sister += 1
            $ m_sister += 3
            if persistent.patch_enabled:
                "{#r=А уж как я рад, сестренка! Я очень по тебе скучал, когда был у тети.}"
            else:
                "{#r=А уж как я рад! Я очень по тебе скучал.}"
            call lin_msg_3 from _call_lin_msg_3
        "Игнорировать":
            $ show_w = 1
            $ p_sister -= 1
            $ m_sister += 4
            pass
    $ show_w = 1
    $ sms_pics = False
    "{#l=Буду с минуты на минуту.<<emoji u1F48B>>}"
    $ otv = 0 #Стиль ответов вырубаем
    "{#c=|pic_2>><<phone pic sis-phone-2>> }"
    $ sms_pics = False
    "{#l=Ой, я случайно.}"
    "{#l=А неплохо вышло, оставлю.}"
    $ naz = 0
    $ sms_sister = sms_all
    $ sms_all = []
    $ show_w = 0 #Включаем окно
    un "{i}Вот черт, когда я успел с ней договориться? Зря я вообще ей сказал, что приезжаю.{i}"
    scene EP1 asp-3 with dissolve
    un "Ты еще кто такой?"
    call namemc from _call_namemc

    gg "А ты..."
    un "Без разницы. Дай поспать [gg], голова раскалывается."
    scene EP1 asp-3-1 with dissolve
    gg "А..."
    if persistent.patch_enabled:
        un "Шшш. Кажется я вчера перебрала в клубе, так что хватит ерзать, бери свой телефон и проваливай из моей комнаты, пока сестра не проснулась!"
    else:
        un "Шшш. Кажется я вчера перебрала в клубе, так что хватит ерзать, бери свой телефон и проваливай из моей комнаты, пока соседка не проснулась!"
    gg "Но..."
    hide screen mob_b
    scene EP1 acl-3

    stop music fadeout 1.0
    $ renpy.music.set_volume(0.7)
    play music indaclub fadein 1.0
    image flash:
        "#000"
        alpha 0.5
        linear .45 alpha 1.0
        linear .45 alpha 0.0
        repeat

    show flash

    pause

    scene EP1 acl-4
    show flash

    pause
    hide flash
    scene EP1 asp-4 with dissolve
    with vpunch
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.3)
    play music relax fadein 1.0
    show screen mob_b
    gg "{i}Ох...{i}"
    scene EP1 asp-6 with dissolve
    gg "{i}Кажется мне не рады в собственном доме. Снова. А я вроде как раз хотел решить эту проблему.{i}"
    gg "{i}Думаю, можно оставить ее тут, поспит, пока я приму душ.{i}"
    scene EP1 asp-5 with dissolve
    if persistent.patch_enabled:
        gg "{i}Тем более, что сестра должна скоро приехать. Будет странно, если я буду выгонять голую девушку, во время нашей первой встречи, спустя столько лет.{i}"
    else:
        gg "{i}Тем более, что Линдси должна скоро приехать. Будет странно, если я буду выгонять голую девушку, во время нашей первой встречи, спустя столько лет.{i}"
    scene EP1 asp-7 with dissolve
    gg "{i}Хорошо, что все коробки рабочие разложили по комнатам, а то бы в холле творился бардак.{i}"

    scene EP1 asp-8 with dissolve
    gg "{i}А она вроде миленькая, пусть даже и немного груба. Хотя кто из нас с утра в хорошем настроении.{i}"
    hide screen mob_b
    scene EP1 acl-5

    stop music fadeout 1.0
    $ renpy.music.set_volume(0.7)
    play music indaclub fadein 1.0
    image flash:
        "#000"
        alpha 0.5
        linear .45 alpha 1.0
        linear .45 alpha 0.0
        repeat

    show flash

    pause

    scene EP1 acl-6
    show flash

    pause
    hide flash
    scene EP1 asp-7 with dissolve
    with vpunch
    stop music fadeout 1.0
    $ renpy.music.set_volume(0.3)
    play music relax fadein 1.0
    show screen mob_b
    gg "{i}Ох... В аптеку, не забыть зайти в аптеку...{i}"
    scene EP1 asp-5 with dissolve
    play sound cldoor
    gg "{i}Что это? Дверь? Я забыл закрыть дверь?{i}"
    scene EP1 bsc2-1 with dissolve

    if persistent.patch_enabled:
        gg "{i}Надеюсь, это сестра.{i}"
    else:
        gg "{i}Надеюсь, это Линдси.{i}"
    scene EP1 bsc2-2 with dissolve
    gg "{i}Как же давно мы с ней не виделись...{i}"
    scene EP1 bsc2-3 with dissolve

    $ new_flag = 1 # новое смс, от линдси
    $ contact_flag = 1 #куда отправлять смс - линдси
    if mute == False:
        play sound sms
    else:
        play sound vibr
    $ sms_all = sms_sister
    gg "{#l=Я жду тебя в холле, ты где?} {i}Черт, все-таки не закрыл.{i}"


    gg "{i}Господи, как она выросла. И эта прическа... Последний раз, когда я ее видел, у нее были прямые волосы.{i}"
    scene EP1 bsc2-3-1 with dissolve
    gg "{i}Зато не изменилась ее большая, тяжелая грудь и привычка не носить лифчики.{i}"
    if persistent.patch_enabled:
        gg "{i}Они часто ругались с бабушкой из-за этого.{i}"
    else:
        gg "{i}Они часто ругались с Нэнси из-за этого.{i}"
    scene EP1 bsc2-3-2 with dissolve
    gg "{i}Да и платья тогда она не носила.{i}"
    scene EP1 bsc2-3 with dissolve
    if persistent.patch_enabled:
        gg "Привет, сестренка!"
    else:
        gg "Привет!"

    scene EP1 bsc2-4 with dissolve
    scene EP1 bsc2-5 with dissolve

    if persistent.patch_enabled:
        lin "Братец! Ты так спешил меня встретить, что забыл надеть штаны?"
    else:
        lin "А вот и ты! Ты так спешил меня встретить, что забыл надеть штаны?"
    scene EP1 bsc2-5-1 with dissolve
    gg "{i}Черт.{i}"
    scene EP1 bsc2-5 with dissolve
    lin "А я уже написала тебе смс. Я стучала, но никто не ответил, подергала ручку - а дверь открыта. Не стоять же мне на улице, с этой дурацкой сумкой."

    if m_sister == 1:
        lin "Так ты забыл о нашем разговоре?"
        scene EP1 bsc2-5-1 with dissolve
        call lin_sc2_1 from _call_lin_sc2_1
    elif m_sister == 2:
        lin "Так ты не помнишь, как вчера меня утешал?"
        scene EP1 bsc2-5-1 with dissolve
        call lin_sc2_1 from _call_lin_sc2_1_1
    elif m_sister == 3:
        lin "Это так классно, что ты предложил мне пожить у тебя!"
        scene EP1 bsc2-5-1 with dissolve
        call lin_sc2_3 from _call_lin_sc2_3
    elif m_sister == 4:
        lin "Почему ты не ответил на мои сообщения?"
        scene EP1 bsc2-5-1 with dissolve
        call lin_sc2_4 from _call_lin_sc2_4

    scene EP1 bsc2-8 with dissolve
    lin "Ты переехал только вчера?"
    gg "Да, вчера днем. "
    scene EP1 bsc2-9 with dissolve
    gg "Но я провел тут не больше времени, чем ты, не считая сна, конечно. "
    scene EP1 bsc2-10 with dissolve
    gg "Как только занесли все вещи, я ушел гулять на набережную."
    scene EP1 bsc2-11 with dissolve
    lin "Тут и бассейн есть!"
    scene EP1 bsc2-11-0 with dissolve
    lin "Наконец-то смогу загорать без всех этих сальных взглядов."
    scene EP1 bsc2-11-1 with dissolve
    gg "Вот держи, две ложки сахара, да?"
    scene EP1 bsc2-11-2 with dissolve
    if persistent.patch_enabled:
        lin "Боже, ты помнишь?"
        lin "Бабушка всегда делала мне либо с одной, либо с тремя, как назло."
    else:
        lin "Боже, ты помнишь?"
        lin "Нэнси всегда делала мне либо с одной, либо с тремя, как назло."
    gg "{i}Может она просто хотела заставить тебя делать кофе самой?{i}"
    scene EP1 bsc2-12 with dissolve
    lin "Так что, твои картины начали продаваться?"
    scene EP1 bsc2-12-0 with dissolve
    gg "{i}Ну вот, началось. Из-за таких вопросов я и не хотел встречаться со старыми знакомыми.{i}"
    gg "Да... Картины... Знаешь, у меня купили парочку за баснословные суммы."
    scene EP1 bsc2-12-1 with dissolve
    lin "Судя по этому дому, суммы реально были большими. Три этажа, бассейн, отличный район."
    scene EP1 bsc2-12 with dissolve
    if persistent.patch_enabled:
        lin "Я так за тебя рада! Ты показал, что в нашей семье, не только бабушка может зарабатывать деньги."
    else:
        lin "Я так за тебя рада! Ты показал, что не только Нэнси может зарабатывать деньги."
    scene EP1 bsc2-12-0 with dissolve
    call lin_sc2_5 from _call_lin_sc2_5
    gg "Так значит, твою проблему зовут Зак?"
    scene EP1 bsc2-12 with dissolve
    lin "Да..."
    lin "Мы сильно поругались вчера, и я не могла больше с ним находиться в одном доме."
    gg "Может сядем за стол и расскажешь?"
    scene EP1 bsc2-13 with dissolve
    lin "Конечно! Слушай, у тебя красивая столовая, много света."
    scene EP1 bsc2-17 with dissolve
    if persistent.patch_enabled:
        gg "{i}О, сколько раз я видел, как она выпрашивала деньги у бабушки с точно таким же лицом.{i}"
        gg "{i}Можешь не стараться сестренка, я же уже тебя пригласил.... Хоть и не помню этого.{i}"
        $ renpy.choice_for_skipping()
        mod "For Aşk Rotası: Turn your phone on silent and don't check it. \nFor Enslave Route: Turn off silent and check it constantly."
    else:
        gg "{i}О, сколько раз я видел, как она выпрашивала деньги у Нэнси с точно таким же лицом.{i}"
        gg "{i}Можешь не стараться, я же уже тебя пригласил.... Хоть и не помню этого.{i}"
        $ renpy.choice_for_skipping()
        mod "For Aşk Rotası: Turn your phone on silent and don't check it. \nFor Enslave Route: Turn off silent and check it constantly."
    # Келли СМС
    $ new_flag = 0 # обнуляем, если не прочитали от линдси
    $ new_flag = 2 # новое смс
    $ contact_flag = 2 #куда отправлять смс - келли
    $ naz = 0
    if mute == False:
        play sound sms
    else:
        play sound vibr
    scene EP1 bsc2-14-1 with dissolve
    $ sms_all = []
    lin "{#l=Эй, как там тебя, [gg]} Зак в последнее время очень изменился."
    if contact_flag == 0:
        $ sms_all = sms_kelly
    $ contact_flag = 2
    scene EP1 bsc2-14 with dissolve
    if mute == False:
        play sound sms
    else:
        play sound vibr

    $ new_flag = 2

    lin "{#l=Это же твой номер!?} Он стал холодным, грубым."
    if contact_flag == 0:
        $ sms_all = sms_kelly
    $ contact_flag = 2
    scene EP1 bsc2-17 with dissolve
    if mute == False:
        play sound sms
    else:
        play sound vibr
    $ contact_flag = 2

    lin "{#l=Ты ведь знаешь, что мы ночевали НЕ В МОЕЙ КОМНАТЕ?} Мы стали меньше разговаривать."
    if contact_flag == 0:
        $ sms_all = sms_kelly
    $ contact_flag = 2
    scene EP1 bsc2-15 with dissolve
    if mute == False:
        play sound sms
    else:
        play sound vibr


    lin "{#l=Аууууу!} Постепенно, мы стали друг другу чужими, ты понимаешь?"
    if contact_flag == 0:
        $ sms_all = sms_kelly
    $ contact_flag = 2
    if new_flag == 0:
        scene EP1 bsc2-16 with dissolve
        lin "Почему ты все время отвлекаешься на телефон? Тебе совсем не интересно, что я рассказываю?"
        $ p_sister -= 1
        menu:
            gg "{i}Черт, я расстроил ее, а все из-за этой неуемной девки.{i}"
            "Прости, это из галереи.":
                $ p_sister += 1 #Отношения
                gg "Мне пишут из галереи, по поводу продажи картины, прости, это важно."

                $ s_sister += 1 #галерея
                call lin_sc2_6_1 from _call_lin_sc2_6_1
            "Совсем не интересно.":
                $ p_sister -= 3
                gg "Честно - не особо. Какие-то сопли про бывшего, насколько я понял?"
                $ s_sister += 4

                call lin_sc2_6 from _call_lin_sc2_6

    if new_flag == 2 and mute == False:
        scene EP1 bsc2-16 with dissolve
        lin "[gg], я слышу, тебе кто то пишет, спасибо, что не стал отвлекаться. Но ты ответь, а то это пиликанье немного мешает сосредоточиться."
        $ p_sister += 3
        $ s_sister += 2 #не отвлекся
        gg "Извини, спасибо, я быстро."
        scene EP1 bsc2-18 with dissolve
        call lin_sc2_otvet from _call_lin_sc2_otvet
    if new_flag == 2 and mute == True:
        scene EP1 bsc2-17 with dissolve
        menu:
            gg "Мне тут пишут..."
            "...из галереи.":
                $ p_sister += 3 #Отношения
                gg "Мне пишут, наверное из галереи, по поводу продажи картины, прости, это важно, я отвечу."

                $ s_sister += 1 #галерея
                call lin_sc2_6_1 from _call_lin_sc2_6_1_1
            "...тебя не касается кто.":
                $ p_sister -= 3
                gg "Мне тут пишут, возможно расскажут что-то интереснее твоих розовых соплей."
                $ s_sister += 4

                call lin_sc2_6 from _call_lin_sc2_6_2
    $ naz = 0
    scene EP1 bsc2-18 with dissolve
    gg "{i}Эта девушка из клуба какая-то странная. Но что-то в ней есть. {i}"
    if persistent.patch_enabled:
        gg "{i}А сестренка умеет  давить на жалость, когда ей нужно.{i}"
    else:
        gg "{i}А Линдси умеет  давить на жалость, когда ей нужно.{i}"
    gg "{i}Взгляд потупила, глазки в пол, вся такая беспомощная, ведомая, пассивная...{i}"
    scene EP1 bsc2-18-1 with dissolve
    gg "{i}Послушная девочка, с грудью пятого размера, это ли не мечта?{i}"
    scene EP1 bsc2-19 with dissolve
    gg "{i}А вот и наша паникерша. Не боится идти домой к первому встречному, но боится выйти из его дома.{i}"

    scene EP1 bsc2-18 with dissolve
    if persistent.patch_enabled:
        gg "{i}Хотя, судя по ее первой реакции на меня, ее сестра постоянно ловит кого-то у них в комнате.{i}"
    else:
        gg "{i}Хотя, судя по ее первой реакции на меня, ее соседка постоянно ловит кого-то у них в комнате.{i}"
    scene EP1 bsc2-14 with dissolve
    if s_sister == 1:
        gg "Вопрос с галереей улажен, вернемся к твоему рассказу."
    elif s_sister == 2:
        gg "Прости, больше нас никто не прервет."
    elif s_sister == 4:
        gg "Я закончил, можешь продолжать, если хочешь."
    else:
        gg "Прости, больше нас никто не прервет."
     # Келли СМС
    $ new_flag = 0 # обнуляем, если не прочитали от линдси
    $ new_flag = 2 # новое смс от Келли
    $ contact_flag = 2 #куда отправлять смс - келли
    $ sms_all = sms_kelly
    if mute == False:
        play sound sms
    else:
        play sound vibr

    gg "{#l=Эй, а мы соседи, ты  знал?} Так на..."

    if mute == False:
        scene EP1 bsc2-15 with dissolve
        $ p_sister -= 1
        lin "Опять кто-то пишет... "
        gg "{i}Черт.{i}"
    else:
        scene EP1 bsc2-14 with dissolve
        gg "{i}Что там она опять пишет?.{i}"
    if s_sister == 1:#Галерея
        call lin_sc2_gal from _call_lin_sc2_gal

    elif s_sister == 2: #Не отвлексяМилый
        call lin_sc2_sw from _call_lin_sc2_sw

    elif s_sister == 4: #Грубый
        call lin_sc2_rude_1 from _call_lin_sc2_rude_1

    scene EP1 bsc2-21 with dissolve
    if slave_sister == 1:
        if persistent.patch_enabled:
            gg "{i}Так непривычно говорить ей, что делать...{i}"
            gg "{i}В детстве она мало обращала на меня внимания, будучи занята своими парнями, подругами...{i}"
            gg "{i}А теперь я приютил у себя ту, на чей силуэт я в детстве дрочил. Ее дверь была напротив моей, и иногда, вечером, она ее не закрывала.{i}"
            scene EP1 bsc2-22 with dissolve
            gg "{i}Мягкий желтый свет обрисовывал каждый ее изгиб, когда она переодевалась, перед тем как лечь спать.{i}"
            gg "{i}И этот силуэт голой сестры на стене моей детской был первой порнушкой, которую я посмотрел.{i}"
            gg "{i}Но потом мы с мамой уехали.{i}"
        else:
            gg "{i}Так непривычно говорить ей, что делать...{i}"
            gg "{i}Раньше она мало обращала на меня внимания, будучи занята своими парнями, подругами...{i}"
            gg "{i}А теперь я приютил у себя ту, на чей силуэт я  дрочил. Ее дверь была напротив моей, и иногда, вечером, она ее не закрывала.{i}"
            scene EP1 bsc2-22 with dissolve
            gg "{i}Мягкий желтый свет обрисовывал каждый ее изгиб, когда она переодевалась, перед тем как лечь спать.{i}"
            gg "{i}И этот силуэт голой девушки на стене моей комнаты был первой порнушкой, которую я посмотрел.{i}"
            gg "{i}Но потом мы с Лорой уехали...{i}"
    else:
        if persistent.patch_enabled:
            gg "{i}Наверное, даже удачно вышло, что вчера я был пьян и согласился ее приютить.{i}"
            gg "{i}Иначе бы я нашел сотни причин, почему я не хочу ее видеть. 'Не хочу вспоминать о прошлом'{i}"
            gg "{i}Но я уже вернулся в этот город, и пора бы смириться, что прошлое меня притягивает и манит.{i}"
            scene EP1 bsc2-22 with dissolve
            gg "{i}Сестра, как минимум, будет услаждать мой взор, а также ее можно будет использовать как модель для моих будущих картин.{i}"
            gg "{i}Ведь моя обычная 'модель', думаю, уже всем приелась. Хватит рисовать только ее.{i}"
        else:
            gg "{i}Наверное, даже удачно вышло, что вчера я был пьян и согласился ее приютить.{i}"
            gg "{i}Иначе бы я нашел сотни причин, почему я не хочу ее видеть. 'Не хочу вспоминать о прошлом'{i}"
            gg "{i}Но я уже вернулся в этот город, и пора бы смириться, что прошлое меня притягивает и манит.{i}"
            scene EP1 bsc2-22 with dissolve
            gg "{i}Линдси, как минимум, будет услаждать мой взор, а также ее можно будет использовать как модель для моих будущих картин.{i}"
            gg "{i}Ведь моя обычная 'модель', думаю, уже всем приелась. Хватит рисовать только ее.{i}"
    $ new_flag = 0 # обнуляем, если не прочитали
    $ new_flag = 4 # новое смс от Кевина
    $ contact_flag = 4 #куда отправлять смс - кевин
    $ sms_all = sms_kevin

    if mute == False:
        play sound sms
    else:
        play sound vibr
    $ naz = 4 #Вырубаем назад
    gg "{#l=Хэээй, ты заселился?} {i}Что-то я отвлекся, пора в душ.{i}"


    $ new_flag = 0

    $ contact_flag = 4
    $ sms_all = sms_kevin
    $ show_w = 1
    show screen sms_screen
    $ sms_pics = False #Убираем отключение промотки, если открыл руками
    if persistent.patch_enabled:
        "{#r=Заселился, посидел на набережной со скетчбуком, сходил в клуб, проснулся рядом с незнакомкой, заселил к себе сестру.}"
    else:
        "{#r=Заселился, посидел на набережной со скетчбуком, сходил в клуб, проснулся рядом с незнакомкой, заселил к себе Линдси.}"
    "{#r=Жизнь бьет ключом.}"
    "{#l=Ну блиин, чувааак <<emoji f>>}"
    "{#l=Мог бы и позвать своего лучшего друга на новоселье!}"
    "{#l=Я не просыпался с незнакомкой... НИКОГДА.}"
    "{#r=Прости, сначала хотел побыть один, а потом все заверте...}"
    "{#l=Ну ладно, за незнакомку респект <<emoji l>>}"
    "{#r=<<emoji r>>}"
    if persistent.patch_enabled:
        "{#l=А что за сестра, я ее знаю? Ты что-то рассказывал тогда, младшая, старшая, но я уже все забыл.}"
        "{#r=Старшая... Рассталась с парнем, наша бабушка не дает денег, а тут очень удобно подвернулся я.}"
    else:
        "{#l=А что за Линдси, я ее знаю? Ты что-то рассказывал тогда, о своих знакомствах, но я уже все забыл.}"
        "{#r=Знакомая... Рассталась с парнем, а тут очень удобно подвернулся я.}"
    "{#l=Понятно. Слушай, я зайду к тебе чуть позже?}"
    "{#r=Через час удобно?}"
    if persistent.patch_enabled:
        "{#l=Ээээ... Блин, мать меня убьет, если я прогуляю школу. Если только ненадолго.}"
    else:
        "{#l=Ээээ... Блин, я сейчас занят. Если только ненадолго.}"

    "{#r=Ок.}"
    $ sms_kevin = sms_all
    $ sms_all = []
    $ show_w = 0
    $naz = 0 #Врубаем назад
    gg "{i}Первый человек за день, с кем я действительно хотел бы встретиться.{i}"
    gg "{i}Может быть потому, что он напоминает мне о... ней?{i}"
    scene black with dissolve
    play sound shower
    hide screen mob_b
    gg "{i}Как приятно просто смыть с себя всю накопившуюся усталость.{i}"

    # СЦЕНА ТРИ
    scene EP1 csc3-0 with dissolve
    show screen mob_b
    stop sound
    gg "{i}Осталось найти кроссовки и совместить утреннюю пробежку с походом в аптеку.{i}"
    scene EP1 csc3-0-1 with dissolve
    gg "{i}Все вещи раскиданы по коробкам.{i}"
    scene EP1 csc3-1 with dissolve
    gg "{i}Надо найти, куда рабочие сложили коробки с обувью.{i}"
    scene EP1 csc3-1-1 with dissolve
    gg "{i}Черт, здесь только одежда. Мог бы заметить и издали.{i}"
    scene EP1 asp-5 with dissolve
    if persistent.patch_enabled:
        gg "{i}Наверное положили в комнату сестры.{i}"
    else:
        gg "{i}Наверное положили в комнату моей гостьи.{i}"
    scene EP1 csc3-2 with dissolve
    gg "{i}Интересно, сколько она у меня собралась жить?{i}"
    scene EP1 csc3-4 with dissolve
    if slave_sister == 1:
        if persistent.patch_enabled:
            gg "{i}А у сестренки классная задница!{i}"
        else:
            gg "{i}А у нее классная задница!{i}"
        gg "{i}Она говорила, что будет переодеваться, надо было зайти пораньше, чтобы увидеть стриптиз.{i}"
        scene EP1 csc3-5 with dissolve
        gg "{i}Теперь главное, чтобы она меня не заме...{i}"
        scene EP1 csc3-6 with dissolve
        lin "Что?"
        scene EP1 csc3-7 with dissolve
        lin "[gg], какого черта?"
        scene EP1 csc3-9 with dissolve
        lin "Немедленно убирайся отсюда!"
        scene EP1 csc3-11 with dissolve
        gg "{i}Какое у нее прекрасное тело...{i}"
        lin "Ты слышишь?"
        scene EP1 csc3-12 with dissolve
        gg "{i}Гладкая кожа, большая и упругая грудь, красивый животик...{i}"
        lin "Эй, куда ты смотришь?!"
        scene EP1 csc3-9 with dissolve
        lin "Уходи!"
        gg "Если не хочешь,чтобы я неожиданно врывался - закрывай дверь."
        scene EP1 csc3-8 with dissolve
        if persistent.patch_enabled:
            gg "Это МОЙ дом, сестренка, и я могу заходить куда угодно и когда угодно."
            gg "Не нравится, звони бабушке, она с удовольствием посмеется над твоими проблемами."
        else:
            gg "Это МОЙ дом, и я могу заходить куда угодно и когда угодно."
            gg "Не нравится, звони Нэнси, она с удовольствием посмеется над твоими проблемами."
        $ p_sister -= 3
        lin "Но..."
        gg "Я все сказал."
        scene EP1 csc3-13 with dissolve
        play sound cldoor

    else:
        gg "{i}Черт, я забыл, что она переодевается. Нужно было постучать...{i}"
        scene EP1 csc3-5 with dissolve
        gg "{i}Нужно тихо уйти, пока она меня не заметила. {i}"
        if persistent.patch_enabled:
            gg "{i}Я же не хочу портить свои отношения с сестрой... Она мне нравится с детства, но пусть все развивается медленно, спокойно и само собой. {i}"
        else:
            gg "{i}Я же не хочу портить свои отношения с ней... Она мне нравится, но пусть все развивается медленно, спокойно и само собой. {i}"
        gg "{i}Я просто буду рядом и помогу ей разобраться с ее проблемами. {i}"
        if persistent.patch_enabled:
            gg "{i}И она перестанет видеть во мне лишь младшего брата, и поймет, что я уже мужчина.{i}"
    scene EP1 csc3-13 with dissolve
    gg "{i}Черт, а кроссовки? {i}"
    scene EP1 dsc4-1 with dissolve
    play sound cldoor
    gg "{i}Может доехать на мотоцикле?{i}"
    scene EP1 dsc4-2 with dissolve
    gg "{i}Вчера я ходил пешком, но может сегодня стоит прокатиться?{i}"
    gg "{i}Ты тут не заскучал?{i}"
    gg "{i}Эта дурацкая привычка говорить с мотоциклом осталась с детства, когда такая же модель, была моей любимой игрушкой.{i}"
    gg "{i}Хотя, кажется алкоголь еще не выветрился. Или вчера был не только алкоголь? Ничего не помню.{i}"
    scene EP1 dsc4-4 with dissolve
    gg "{i}Вот черт, она же писала что-то, насчет того, что мы с ней соседи.{i}"
    scene EP1 dsc4-4-1 with dissolve
    gg "{i}А с кем она идет?{i}"
    scene EP1 dsc4-5 with dissolve
    if persistent.patch_enabled:
        gg "{i}Сестра, которая выгоняет ее бойфрендов?{i}"
    else:
        gg "{i}Соседка, которая выгоняет ее бойфрендов?{i}"

    scene EP1 dsc4-6 with dissolve
    gg "{i}А фиолетовая откровенно одевается, не только когда ходит по клубам. Черт, неудобно называть ее просто 'фиолетовая', как же там ее звали...{i}"
    scene EP1 dsc4-7 with dissolve
    un "Эй, о чем задумался? Думал я тебя не замечу?"
    gg "Н-нет..."
    scene EP1 dsc4-8 with dissolve
    un "А чего не здороваешься?"
    scene EP1 dsc4-9 with dissolve
    gg "Мы уже виделись с утра, если ты не забыла."
    scene EP1 dsc4-11 with dissolve
    un "Забудешь тут, просыпаешься не у себя дома, никого нет, какие то коробки стоят, как в каком-то подвале."
    scene EP1 dsc4-10 with dissolve
    if s_kelly == 1:
        un "Что делать, куда идти, где тебя носит..."
        gg "Да, и ты приняла гениальное решение выйти голой. Как бы решить все вопросы одним махом."
        scene EP1 dsc4-15 with dissolve
        gg "Семь бед - один ответ, раздевайся и грози, что будешь щеголять голой, по смс."
        scene EP1 dsc4-14 with dissolve
        un "Ну давай, давай, поиздевайся над бедной девушкой. Вообще не смешно."
    elif s_kelly == 2:
        gg "Да да, в подвале у маньяка, я помню."
        scene EP1 dsc4-15 with dissolve
        gg "Ведь все маньяки оставляют своих жертв дрыхнуть у себя в спальне."
        scene EP1 dsc4-14 with dissolve
        un "Ну давай, давай, поиздевайся над бедной девушкой. Вообще не смешно."
    scene EP1 dsc4-13 with dissolve
    gg "Ну прости, прости. Так значит мы с тобой соседи?"
    scene EP1 dsc4-14 with dissolve
    if persistent.patch_enabled:
        un "Прикинь! Я думала, буду объяснять матери, где меня носило всю ночь, но успела добежать до того, как она заметила мое отсутствие. Я даже успела увидеть одну ее утреннюю 'процедуру'..."
    else:
        un "Прикинь! Я думала, буду объяснять хозяйке дома, где меня носило всю ночь, но успела добежать до того, как она заметила мое отсутствие. Я даже успела увидеть одну ее утреннюю 'процедуру'..."


    scene EP1 dsc4-16 with dissolve
    un "Келли! Мы опоздаем!"
    gg "{i}Так вот, значит, как ее зовут!{i} "
    scene EP1 dsc4-17 with dissolve
    un "Не опоздаем, дай поговорить спокойно!"
    scene EP1 dsc4-15 with dissolve
    k "Даже не думай, что я не заметила облегчение на твоем лице, когда она назвала мое имя, [gg]"
    scene EP1 dsc4-14 with dissolve
    k "А ну покажи, как я записана у тебя в телефоне!"
    menu:
        gg "{i}Не думаю, что это хорошая идея...{i}"
        "Показать":
            $ s_kelly_2 += 1
            scene EP1 dsc4-18 with dissolve
            gg "Вот, держи"

            call kel_sc_4_1 from _call_kel_sc_4_1
        "Забыл телефон дома":
            $ s_kelly_2 += 2
            scene EP1 dsc4-14 with dissolve
            gg "Я только в аптеку вышел, даже не взял телефон."

            call kel_sc_4_2 from _call_kel_sc_4_2
    scene EP1 dsc4-2 with dissolve
    gg "Не ну ты видел? Пиздец."
    if s_kelly_2 == 2:
        $ new_flag = 0 # обнуляем, если не прочитали
        $ contact_flag = 4 #куда отправлять смс - кевин
        $ sms_all = sms_kevin
        $ naz = 4
        show screen sms_screen
        $ show_w = 1
        "{#r=Ебать ты не вовремя написал.}"
        "{#l=???}"
        "{#r=Да проехали...}"
        $ show_w = 0
        $ sms_kevin = sms_all
        $ sms_all = []
        $naz = 0 #Врубаем назад
    gg "{i}Неловко вышло... Но зато теперь я хотя бы знаю как ее зовут - Келли.{i}"
    gg "{i}Келли и Салли... Мама у них, наверное, Молли, младшая сестра Полли, в деревне овечка Долли, собака у них колли и все они те еще тролли...{i}"
    gg "{i}Боже, что за чушь я несу? Это все от нервов, эта девчонка просто выводит меня из себя.{i}"
#Сцена ПЯТЬ
    scene EP1 esc5-1 with dissolve
    gg "{i}Как быстро они от меня убежали, а ведь улица прямая, чуть ли не до горизонта.{i}"
    scene EP1 esc5-2 with dissolve
    $ new_flag = 0 # обнуляем, если не прочитали
    $ new_flag = 2 # новое смс от Кевина
    $ contact_flag = 2 #куда отправлять смс - кевин
    $ sms_all = sms_kelly

    if mute == False:
        play sound sms
    else:
        play sound vibr
    gg "{i}О, мои соседи справа. Точнее соседка. {i} {#l=Козлина.}"

    scene EP1 esc5-3 with dissolve
    gg "{i}Точнее соседки. {i}"
    scene EP1 esc5-4 with dissolve:

        subpixel True
        yalign 1.0
        pause 1.0
        linear 5.0 yalign 0.0

    gg "{i}Какая сочная девушка. Люблю шоколад.{i}"




    scene EP1 esc5-5 with dissolve
    gg "{i}Я ее явно заинтересовал. Хотя это неудивительно, Джон сказал, что мой дом не покупали несколько лет. Естественно ей интересно, кто его приобрел.{i}"
    scene EP1 esc5-6 with dissolve
    gg "{i}Молоко и шоколад. Интересное сочетание. {i}"
    scene EP1 esc5-7 with dissolve
    gg "{i}А у моих соседок неплохие изгибы. {i}"
    scene EP1 esc5-7-1 with dissolve


    gg "{i}Черт. Надеюсь она не видела, как я пялюсь. {i}"
    menu:
        gg "{i}Пора познакомиться с соседками.{i}"
        "Say hello {color=#0f0}{b}[Şantaj Rotası]{/b}{/color}":
            $ p_jen -= 1
            gg "Привет, я ваш новый сосед!"
            call sc5_jen from _call_sc5_jen
        "Pass {color=#0f0}{b}[Aşk Rotası]{/b}{/color}":
            pass
    scene EP1 esc5-8 with dissolve
    if p_jen == -1:
        gg "Ненавижу, когда игнорят."
    else:
        gg "{i}Пусть сами приходят знакомиться.{i}"
    un "Ты так сексуальна в этом платье..."
    un "Киара, ну не на улице же."
    menu:
        gg "{i}Интересно, что они там делают.{i}"
        "Turn around {color=#0f0}{b}[Şantaj]{/b}{/color}":
            call sc5_jen_1 from _call_sc5_jen_1
        "Keep going {color=#0f0}{b}[Aşk]{/b}{/color}":
            pass
    scene EP1 esc5-8 with dissolve
    gg "{i}Быстро до аптеки и обратно, скоро должен прийти Кевин.{i}"
    scene black with dissolve
    play sound shop
    gg "{i}Не люблю эту магазинную толкучку...{i}"
    gg "{i}Надо не забыть переименовать контакт Келли.{i}"
    $ kelly_name = 1

#Сцена ШЕСТЬ
    scene EP1 fsc6-1 with dissolve
    stop sound
    play sound cldoor
    gg "Ты уже здесь!? Как ты зашел?"
    scene EP1 fsc6-2 with dissolve
    kev "Дверь была открыта."
    if persistent.patch_enabled:
        gg "{i}Да сколько можно, надо выработать привычку. Раньше дверь всегда запирала тетя Джил.{i}"
    else:
        gg "{i}Да сколько можно, надо выработать привычку. Раньше дверь всегда запирала Джил.{i}"
    scene EP1 fsc6-2-1 with dissolve
    if s_kelly_2 == 2:
        kev "А что там не так было с смс?"
        gg "Моя незнакомка из клуба попросила показать телефон, чтобы посмотреть, как она у меня записана..."
        kev "А как она была записана? Телка11?"
        gg "ФиолетоваяЧикаизКлуба"
        kev "Тоже неплохо..."
        gg"Ну и я ей сказал, что оставил телефон дома, а тут пришло твое сообщение. Ты меня подставил. *смеется*"
        scene EP1 fsc6-3 with dissolve
        kev "Реально? Хах, чувак, тебе не повезло."
    if persistent.patch_enabled:
        kev "Кстати, ты видел, в чем твоя сестра там загорает!?"
    else:
        kev "Кстати, ты видел, в чем твоя гостья там загорает!?"
    gg "Нет, но по твоей реакции, похоже что голая."
    scene EP1 fsc6-2-2 with dissolve
    kev "Почти, чувак! Я от окна минут пять не отлипал."
    scene EP1 fsc6-2-1 with dissolve
    gg "Она может загорать в парандже, и все равно будет выглядеть сексуально."
    scene EP1 fsc6-3 with dissolve
    kev "А ты... Ты ее видел голой?"
    if slave_sister == 1:
        gg "Буквально полчаса назад. Зашел к ней в комнату, пока она переодевалась."
        scene EP1 fsc6-2-1 with dissolve
        kev "Чувааак. И она тебя спалила?"
        gg "А я и не прятался. Она приехала ко мне, живет в моем доме, дверь была не закрыта..."
        $ p_kevin -= 1
        kev "Воу. Жестковато."
        gg "А с ней так и нужно. Я ее хорошо узнал, пока мы жили вместе."
        scene EP1 fsc6-3 with dissolve
        kev "Я бы так не смог, она же...Она... Как произведение искусства. Ее тело совершенно... Ее стать..."
        gg "Словосочетание которое ты ищешь - большие сиськи."
        kev "Хах, ты прав. ГИГАНТСКИЕ СИСЬКИ. Кайф. "
        scene EP1 fsc6-2-2 with dissolve
        kev "Но я бы так не смог. Внаглую заходить, пялиться. Она же ангел... Ею можно только любоваться."
        gg "Вот я и полюбовался."
        kev "Я имел ввиду издалека. Ты же художник, ты должен понимать."
        $ p_kevin -= 1

    else:
        gg "Полностью нет, но сегодня видел спину и часть груди. Зашел к ней в комнату, пока она переодевалась."
        scene EP1 fsc6-2-1 with dissolve
        kev "Чувааак. И она тебя спалила?"
        gg "Нет, я быстро оттуда убрался."
        $ p_kevin += 1
        scene EP1 fsc6-2-2 with dissolve
        kev "Везет тебе. Переехал и сразу в доме ходит такая красотка."
        if persistent.patch_enabled:
            kev "Хотя, с другой стороны, это напрягает. У меня мать постоянно ходит в нижнем белье. Такая возбуждающая. Это давит на мозги. И не только на мозги."
        else:
            kev "Хотя, с другой стороны это напрягает. У меня хозяйка дома постоянно ходит в нижнем белье. Такая возбуждающая. Это давит на мозги. И не только на мозги."
        gg "Что, прямо по дому!?"
        scene EP1 fsc6-3 with dissolve
        kev "Ну не прямо по дому, у себя в комнате..."
        scene EP1 fsc6-2-2 with dissolve
        gg "Дверь не закрывает?"
        scene EP1 fsc6-3 with dissolve
        kev "Да не, закрывает..."
        scene EP1 fsc6-4 with dissolve
        gg "И каким же образом она умудряется тебя возбуждать своим видом?"
        kev "Так я приоткрываю... Дверь то... Смотри!"
        scene EP1 fsc6-4-1 with dissolve
        call screen kev_mom

        if persistent.patch_enabled:
            gg "У тебя очень красивая мама. Жаль, что тем летом ее не было в городе..."
        else:
            gg "У тебя очень красивая хозяйка. Жаль, что тем летом ее не было в городе..."
        scene EP1 fsc6-4 with dissolve
        kev "Ну, тогда нам и так  хватало приключений."

    scene EP1 fsc6-2-2 with dissolve
    kev "Кстати, я так и не понял, откуда у тебя столько бабла."
    kev "Дом этот, мотоцикл у входа... Неужели картины так хорошо продаются?"
    scene EP1 fsc6-2-2 with dissolve
    gg "Нууу... Да. Я нашел классного агента, она продает все что я рисую."
    scene EP1 fsc6-3 with dissolve
    kev "Черт, везет тебе. Познакомь меня с ней."
    scene EP1 fsc6-2-2 with dissolve
    gg "А ты начал рисовать? Не думаю, что она возьмется за твои художества..."
    kev "Нет, что ты, конечно нет. Но она же девушка, этого достаточно, чтобы я захотел познакомиться."
    gg "*смеется* Ааа, ты все об этом. Нет, не думаю, что ты в ее вкусе."
    kev "Да... Я слишком часто в последнее время слышу эту фразу..."
    scene EP1 fsc6-5 with dissolve
    kev "Эх... О, это твой старый скетчбук!?"
    scene EP1 fsc6-6 with dissolve
    kev "Ты им все еще пользуешься?"
    gg "Первый раз открыл его вчера, впервые за последние годы."
    scene EP1 fsc6-7 with dissolve
    kev "Этого рисунка я не помню."
    $ glavn = False
    $ dgame_2 = True
    if persistent.patch_enabled:
        gg "Ну я же писал, что взял скетчбук на набережную, вот, что-то навеяло. Раньше мы часто бывали там с мамой. А теперь там был только я..."
    else:
        gg "Ну я же писал, что взял скетчбук на набережную, вот, что-то навеяло. Раньше мы часто бывали там с Лорой. А теперь там был только я..."
    $ renpy.start_predict_screen("dnev_open","dnev_close","phone_backev","phone") #предварительный подгруз картинок
    $ config.overlay_functions.append(bla_bla) #следим за главной

    #$ config.overlay_functions.append(after_dnev) #следим за рисунками
    #Вводим Днев
    hide screen mob_b
    show screen mob
    $ mob_sc = False
    hide screen keymap_screen_b
    show screen keymap_screen

    $ helpd = True #Если открываем первый раз - хелп
    show screen dnev_open
    gg "И вообще, дай сюда..."
    if lora_page_1_scene == 1:
        scene EP1 fsc6-8 with dissolve
        gg "Ты на что там уставился?"
        scene EP1 fsc6-9 with dissolve
        kev "Да ты залип в свой скетчбук, а мне чего делать?"
        kev "А тут такой прекрасный вид... *Вздыхает*"
    else:
        scene EP1 fsc6-8 with dissolve
        gg "Эй, ты куда?"
        scene EP1 fsc6-9 with dissolve
        kev "Да надоело уже играть..."
        kev "А тут такой прекрасный вид... *Вздыхает*"
    if persistent.patch_enabled:
        gg "Какой интересный у сестренки купальник... Или как там называется такая полоска ткани."
    else:
        gg "Какой интересный у нее купальник... Или как там называется такая полоска ткани."
    kev "Тоже заметил? Очень сексуально..."
    if slave_sister == 1:
        kev "Как можно жестоко обращаться с таким совершенством?"
        kev "Ее нужно носить на руках, холить и лелеять..."
        gg "Это совершенство сядет тебе на шею, при любом удобном случае."
        gg "Она в жизни ни дня не проработала."
        if persistent.patch_enabled:
            gg "И я пытаюсь с ней быть не грубым, а... строгим, что ли... Как наш отец, когда ее содержал. Как наша бабушка, которая ее содержала. Как ее парни..."
        else:
            gg "И я пытаюсь с ней быть не грубым, а... строгим, что ли... Как Нэнси, которая ее содержала. Как ее парни..."
        kev "Да понял я, понял."
        gg "А теперь, судя по всему, ее содержу я. Так пусть она знает свое место в этом доме."
        kev "Все равно мне это не нравится."

    scene EP1 fsc6-10 with dissolve
    kev "Как же тебе всегда везет! Картины эти, незнакомки в кровати, красотки у бассейна..."
    scene EP1 fsc6-11 with dissolve
    kev "И не просто красотки, а с..."
    scene EP1 fsc6-10 with dissolve
    gg "Если описывать это так, то, конечно, звучит заманчиво. А на деле одна головная боль."
    if slave_sister == 0:
        gg "Но, ты тоже, со своими горячими фотографиями, не отстаешь в везении."
        kev "Это не везение, а подготовка, навыки к шпионажу и отличная камера в телефоне!"
    if persistent.patch_enabled:
        kev "Черт, твоя сестра реально заводит. Как же уже надоело дрочить."
    else:
        kev "Черт, Линдси реально заводит. Как же уже надоело дрочить."
    gg "Так заведи себе уже девушку."
    kev "Ага, конечно."
    scene EP1 fsc6-11 with dissolve
    kev "Вот с такими."
    scene EP1 fsc6-10 with dissolve
    kev "И она мне будет дрочить. *смеется*"
    kev "А если серьезно, то с нашей последней встречи, мне уже так не везло. В тебе есть какая-то магия, чувак. Ты бабий магнит."
    gg "Хах, ну если магнит, значит скоро найдем и тебе девушку, раз уж я теперь живу здесь."
    kev "Очень на это надеюсь."
    if lora_page_1_scene == 1:
        kev "Слушай, мне уже пора обратно, я только с одного урока сбежал. Может мама даже не узнает..."
        gg "Ну ладно, а я то как раз хотел пригласить тебя поближе рассмотреть мою сестру. Но раз тебе пора..."
    else:
        kev "Слушай, мне уже пора обратно, я ненадолго отлучился..."
        gg "Ну ладно, а я то как раз хотел пригласить тебя поближе рассмотреть мою гостью. Но раз тебе пора..."

    kev "Черт! Но мне реально пора, в следующий раз. Пусть не снимает купальник! Или лучше снимает..."


   #Сцена Семь

    scene EP1 gsc7-1 with dissolve
    if lora_page_1_scene == 1:
        gg "{i}Сестренка всегда любила понежиться на солнце.{i}"
    else:
        gg "{i}Линдси всегда любила понежиться на солнце.{i}"
    scene EP1 gsc7-2 with dissolve
    gg "{i}И очень часто так и засыпала, из-за того, что ночами сидела с подружками допозна.{i}"
    scene EP1 gsc7-3 with dissolve
    gg "{i}К ее удивлению, она часто просыпалась со сползшей бретелькой купальника и голой грудью.{i}"
    scene EP1 gsc7-4 with dissolve
    if slave_sister == 1:
        gg "Спишь?"
    else:
        if persistent.patch_enabled:
            gg "Эй, сестренка, ты спишь?"
        else:
            gg "Эй, Линдси, ты спишь?"
    scene EP1 gsc7-5 with dissolve
    gg "{i}А у этого купальника даже нет бретелек! Еще удобнее и еще меньше подозрений в мою сторону.{i}"
    scene EP1 gsc7-6 with dissolve
    gg "{i}Одно движение, и ее сочные, большие сиськи станут свободны...{i}"
    scene EP1 gsc7-7 with dissolve
    gg "{i}Черт, я ее все же разбудил.{i}"
    scene EP1 gsc7-7-2 with dissolve
    if persistent.patch_enabled:
        lin "Братец! Ты уже вернулся? Там к тебе кто-то стучался, но мне так лень было вставать и открывать..."
    else:
        lin "Ты уже вернулся? Там к тебе кто-то стучался, но мне так лень было вставать и открывать..."

    scene EP1 gsc7-8 with dissolve
    gg "{i}Ну конечно. Лень лишний раз тащить свои сиськи куда-либо, кроме клуба, магазина или пляжа.{i}"

    scene EP1 gsc7-7 with dissolve
    gg "Это заходил мой старый друг. Ты ему, кстати, очень понравилась."
    scene EP1 gsc7-7-5-1 with dissolve
    lin "Да? А сколько ему лет? Сколько зарабатывает?"
    scene EP1 gsc7-7-5 with dissolve
    if persistent.patch_enabled:
        gg "Он еще учится в школе и не работает. Но, похоже, он влюбился с первого взгляда."
    else:
        gg "Молодой и не работает. Но, похоже, он влюбился с первого взгляда."
    scene EP1 gsc7-7-1 with dissolve
    lin "Ааа... Знаешь, я сейчас еще не готова к новым отношениям... Мне нужно больше времени, чтобы справиться с разрывом... Но, в любом случае, это очень мило."
    scene EP1 gsc7-7-3 with dissolve
    lin "Ох, какая жара... Пойдем, посидим у бассейна, немного охладимся."
    scene EP1 gsc7-9 with dissolve #
    if persistent.patch_enabled:
        gg "{i}В чем-то Кевин был прав. Пусть сестра и напоминает мне о... ней, но видеть ее, тем более в таком виде, довольно приятно.{i}"
    else:
        gg "{i}В чем-то Кевин был прав. Пусть Линдси и напоминает мне о... ней, но видеть ее, тем более в таком виде, довольно приятно.{i}"
    scene EP1 gsc7-9-1 with dissolve
    if persistent.patch_enabled:
        gg "{i}Ее сочное тело привлекало меня и когда я был совсем ребенком. Пусть это были больше шалости, но меня всегда к ней влекло.{i}"
    else:
        gg "{i}Ее сочное тело привлекало меня и раньше. Меня всегда к ней влекло.{i}"
    scene EP1 gsc7-9-2 with dissolve
    gg "{i}А сейчас, когда она стала яркой, взрослой женщиной...{i}"
    scene EP1 gsc7-9-3 with dissolve
    if slave_sister == 1:
        gg "{i}Женщиной, которая находится в полной моей власти. И которая со мной должна стать послушной девочкой.{i}"
    else:
        gg "{i}Женщиной, которой я должен помочь справится с трудностями, ведь теперь за нее в ответе я.{i}"
    scene EP1 gsc7-10 with dissolve #
    call gsc7_menu from _call_gsc7_menu
    lin "Что-то я проголодалась от всех этих разговоров."
    call gsc7_end from _call_gsc7_end
    scene EP1 gsc7-16 with dissolve


    call kel_sc7 from _call_kel_sc7

    $ naz = 0
    $ otv = 0
    $ show_w = 0 #вкл

    hide screen sms_screen
    hide screen clock
    scene EP1 isc9-0 with dissolve
    gg "{i}Интересно, что она имеет ввиду под сюрпризом?{/i}"
    gg "{i}И почему меня все время о них предупреждают? Что раньше, что сейчас...{/i}"
    scene EP1 isc9-0-1 with dissolve
    gg "{i}Мне кажется эта девчонка немного сумасшедшая.{/i}"
    scene EP1 isc9-0-2 with dissolve
    stop music fadeout 4.0
    play music sex fadein 4.0
    k "Сюрприиииз!"
    play sound cldoor

    scene EP1 isc9-0-3 with dissolve
    gg "{i}О господи! Такого я от нее не ожидал. {w} Это же взлом с проникновением.{w} С другой стороны дверь была открыта...{/i}"
    gg "{i}А сам сюрприз, конечно, не особо удивляет, от такой особы.{/i}"
    scene EP1 isc9-0-4 with dissolve
    gg "{i}Какой вид... Не могу поверить, что я мог забыть секс с ней.{/i}"
    scene EP1 isc9-6-2 with dissolve #лицо
    k "Эй, ну ты чего молчишь? Как тебе мой сюрприз?"
    scene EP1 isc9-6-2-1 with dissolve #лицо
    gg "*раздевается* Великолепно, мне кажется такими и должны быть все сюрпризы."
    scene EP1 isc9-0-4 with dissolve
    k "Тогда чего ты ждешь? Пора освежить наши воспоминания о прошлой ночи."

    menu:
        gg "{i}Хорошо, что Линдси ушла в кафе, она могла бы нам помешать.{i}"
        "Ступни":
            $ feet += 1
            $ k_feet+ 1
            call kel_sc9_nogi from _call_kel_sc9_nogi

        "Догги":
            $ p_kelly += 1
            $ sex += 1
            $ k_sex += 1
            call kel_sc9_dog from _call_kel_sc9_dog
    scene EP1 isc10-7 with dissolve
    stop music fadeout 2.0
    play music relax fadein 2.0
    k "Фууух. Это было классно, правда? Правда я не вспомнила, именно так ли было прошлой ночью..."
    scene EP1 isc10-8 with dissolve
    k "Поэтому обязательно нужно повторить!"
    scene EP1 isc10-7 with dissolve
    gg "Мне тоже понравилось... Это... было великолепный сюрприз. Как раз то, чего мне уже давно не хватало."
    gg "Хорошего секса с красивой девушкой."
    scene EP1 isc10-5 with dissolve
    k "Я для тебя просто 'красивая девушка для секса'!?."
    gg "{i}Ну конечно нет, ты любовь всей моей жизни, которую я годами добивался. Господи, девушки...{i}"
    scene EP1 isc10-4 with dissolve
    k "Отвечай!"
    menu:
        gg "{i}Черт, иногда нужно просто держать свои мысли при себе...{i}"
        "Не просто":
            $ p_kelly += 1
            call kel_sc10_love from _call_kel_sc10_love

        "Ты передергиваешь":
            $ p_kelly -= 1
            call kel_sc10_waitamin from _call_kel_sc10_waitamin

    $ new_flag = 3 # новое смс, от Джон
    $ contact_flag = 3 #куда отправлять смс - Джон
    $ naz = 3
    scene EP1 isc10-8 with dissolve
    if mute == False:
        play sound sms
    else:
        play sound vibr
    if sms_pics == True: #если открыл руками
        $ sms_all = sms_jhon
        $ new_flag = 0
        $ sms_pics = False #Убираем отключение промотки, если открыл руками
        $ contact_flag = 3
    $ sms_all = sms_jhon
    k "Что-то я немного устала от этих разговоров. {#l=Удачно сложилось, я нашел подходящий вам вариант.}"
    if mute == False:
        play sound sms
    else:
        play sound vibr
    if sms_pics == True: #если открыл руками
        $ sms_all = sms_jhon
        $ new_flag = 0
        $ sms_pics = False #Убираем отключение промотки, если открыл руками
        $ contact_flag = 3
    gg "Может немного поспим? На самом деле, до твоего сюрприза, я хотел немного вздремнуть.{#l=Завтра утром вас будут ждать на презентации одного проекта.}"
    if sms_pics == True: #если открыл руками
        $ sms_all = sms_jhon
        $ new_flag = 0
        $ sms_pics = False #Убираем отключение промотки, если открыл руками
        $ contact_flag = 3
    if mute == False:
        play sound sms
    else:
        play sound vibr
    k "Дневной сон - лучшее, что придумало человечество после секса! Эй, кто тебе там пишет? {#l=Она будет проходить в том огромном офисном здании, на въезде в город. Скажете секретарше, что вы от меня.}"
    show screen sms_screen
    $ naz = 0
    $ new_flag = 0
    gg "Прости, это мой агент по недвижимости. Я просил его поискать куда можно сейчас вложиться. Не думал, что он так оперативно сработает. {#r=Быстро сработано! Спасибо, я буду.}"
    $ sms_all = []
    gg "Ну вот теперь можно и поспать. "
    k "Кстати, забыла спросить, а ты где-то учишься? И вообще, кем работаешь?"
    gg "И кто-то еще на меня обижался... Разве я не рассказывал тебе в клубе?"
    k "Не помню... Значит нет! *смеется*"
    if persistent.patch_enabled:
        gg "Я пока что бросил школу... Свалившиеся деньги, переезд, сама понимаешь, не до того... Да и, в принципе, пока не планирую туда возвращаться. Зачем?"
        scene EP1 isc10-6 with dissolve
        k "Как я тебе завидую... Я бы тоже бросила школу, но сам понимаешь... Мне не разрешат...Арр."
    else:
        gg "Я пока что бросил учебу... Свалившиеся деньги, переезд, сама понимаешь, не до того... Да и, в принципе, пока не планирую туда возвращаться. Зачем?"
        scene EP1 isc10-6 with dissolve
        k "Как я тебе завидую... Я бы тоже бросила, но сам понимаешь... Мне не разрешат...Арр."

    scene EP1 isc10-2 with dissolve
    k "А что насчет денег?"
    gg "Кхм... Я, эээ.. художник. И мои картины в последнее время очень популярны. Настолько, что я смог позволить себе все это."
    scene EP1 isc10-1 with dissolve
    k "О, так это твои картины в холле? Прикольные..."
    gg "Ммм, нет, они продавались вместе с домом... Мои картины пока еще не привезли, они прибудут позже."
    gg "На втором этаже будет мастерская... Или на третьем, я не помню. Но, в общем, теперь творить я буду здесь."
    scene EP1 isc10 with dissolve
    k "Ой, а меня нарисуешь? Ну пожалуйста, пожалуйста, пожалуйста..."
    scene EP1 isc10-7 with dissolve
    if persistent.patch_enabled:
        k "Сестра сдохнет от зависти, если меня нарисует настоящий художник..."
    else:
        k "Соседка сдохнет от зависти, если меня нарисует настоящий художник..."
    gg "Конечно, если ты готова неподвижно позировать по несколько часов подряд..."
    k "Несколько часов!? Хмм, тогда это будет картина 'Спящая красавица' *смеется*"
    k "Кстати, насчет спящих, давай уже спать."
    gg "С удовольствием."
    scene black
    with eye_shut
    gg "{i}Никогда не мог сразу заснуть.{/i}"
    if persistent.patch_enabled:
        gg "{i}Когда мама уже спала глубоким сном, я все еще ворочался, витая в своих мыслях.{/i}"
        gg "{i}Возможно это из-за моей буйной фантазии. А может из-за упругой маминой задницы, которой она прижималась ко мне ночами.{/i}"
    else:
        gg "{i}Когда Лора уже спала глубоким сном, я все еще ворочался, витая в своих мыслях.{/i}"
        gg "{i}Возможно это из-за моей буйной фантазии. А может из-за упругой задницы, которой она прижималась ко мне ночами.{/i}"

    gg "{i}Зачем я вернулся в этот город? Ведь я мог выбрать любое место на карте, чтобы скрыться.{/i}"
    gg "{i}Но, меня неудержимо тянуло сюда. Место, где есть знакомые мне люди, где меня будет очень легко найти.{/i}"
    gg "{i}Или, я просто хочу быть пойманным?{/i}"
    $ dgame_3 = True
    $ dgame_4 = True
    gg "{i}Но в этом городе я провел лучшие дни в жизни. Скорее всего, я надеялся что история повторится.{/i}"
    show screen new_sketch
    gg "{i}Наверное, я уже готов вспоминать следующие 'счастливые дни'."
    gg "{i}Черт, все равно не спится... Может принять ванну? На втором этаже есть большая, Джон о ней упоминал.{/i}"
    gg "{i}Так, главное нужно тихо выйти, чтобы не разбудить Келли.{/i}"
    show screen mob
    scene jsc11-1 with dissolve
    play sound cldoor
    gg "{i}Воу, кажется сестренка тоже решила поваляться в ванной.{/i}"
    scene jsc11-2 with dissolve
    if slave_sister == 2:
        lin "[gg]! Это снова ты? Сюда дверь не запирается!"
        scene jsc11-3 with dissolve
        gg "Ну, вообще-то, там на двери есть такая пимпочка, и если ее повернуть..."
        lin "Да блин! Мне уже кажется ты специально меня преследуешь!"
        gg "Я тебя не преследую! Просто захотелось расслабиться."
        lin "Ладно, ладно... [gg], ты не мог бы выйти, пожалуйста?"
        lin "Дважды за первый день стоять перед тобой полностью голой несколько... Смущает."
        if persistent.patch_enabled:
            scene jsc11-4 with dissolve
            gg "{i}Скоро это будет последней вещью в этом мире, которая будет тебя смущать, сестренка.{/i}"
        else:
            scene jsc11-4 with dissolve
            gg "{i}Скоро это будет последней вещью в этом мире, которая будет тебя смущать.{/i}"
        scene jsc11-4-1 with dissolve
        gg "{i}Думаю, сейчас стоит ей уступить. Я так сегодня немного перегнул палку.{/i}"
        gg "Конечно, Линдси. Расслабляйся спокойно, тебе нужно отдохнуть."
        lin "Спасибо."
    else:
        lin "[gg]! Тебя стучаться не учили?"
        scene jsc11-3 with dissolve
        gg "Я..."
        lin "Ты еще и оправдываться собрался? Выйди вон!"
        gg "Конечно, прости..."
    scene jsc11-5 with dissolve
    if slave_sister == 2:
        gg "{i}Но, раз я сделал ей поблажку, то теперь можно посмотреть как она принимает ванну.{/i}"
        scene jsc11-6 with dissolve
        gg "{i}Отлично, она увидела, как я выхожу, теперь нужно быстро проскользнуть обратно.{/i}"
        scene jsc11-7 with dissolve
        gg "{i}О, мы любим принимать ванны с пеной, как мило.{/i}"
        scene jsc11-8 with dissolve
        gg "{i}Голая, беззащитная, и такая красивая.{/i}"
        scene jsc11-9 with dissolve
        gg "{i}Скоро мы будем принимать ванны вместе и ты будешь меня мыть своим языком.{/i}"
        scene jsc11-10 with dissolve
        lin "*хихикает*"
        gg "{i}Шаг за шагом, уступка за уступкой и ты станешь во всем послушной мне.{/i}"
        gg "{i}Будешь одеваться, так как я скажу. И раздеваться, по первому моему слову. {/i}"
        scene jsc11-11 with dissolve
        gg "{i}Возможно я куплю тебе ошейник и буду выгуливать. Или куплю клетку, и ты будешь жить там, пока мне не понадобишься.{/i}"
        gg "{i}Ты будешь моей вещью, моей собственностью, беспрекословной исполнительницей всех моих желаний.{/i}"
        gg "{i}Но это будет позже, а пока нужно уходить, пока я не спугнул раньше времени, свою будущую рабыню.{/i}"
        scene jsc11-5 with dissolve
        if persistent.patch_enabled:
            gg "{i}Наверное совсем не того ты ожидала, сестренка, когда просилась ко мне пожить.{/i}"
        else:
            gg "{i}Кажется, я совсем не зря позвал Линдси к себе жить.{/i}"
        gg "{i}Надо возвращаться к Келли и поспать. Главное ее не разбудить.{/i}"
    else:
        gg "{i}Я сегодня целый день пытаюсь ее не обидеть, а она обращается со мной так грубо.{/i}"
        gg "{i}Хочешь, чтобы я вышел вон?{/i}"
        scene jsc11-6 with dissolve
        gg "{i}А я выйду и зайду обратно!{/i}"
        scene jsc11-7 with dissolve
        gg "{i}Вроде не заметила.{/i}"
        scene jsc11-8 with dissolve
        gg "{i}До этого она закрывалась руками, теперь все самое интересное скрыто проклятой пеной...{/i}"
        gg "{i}Хотя нет, не все. Ее прекрасная грудь, не скрыта ничем.{/i}"
        scene jsc11-9 with dissolve
        gg "{i}Что она делает? {/i}"
        scene jsc11-10 with dissolve
        lin "*хихикает*"
        if persistent.patch_enabled:
            gg "{i}О, сестренка любит поиграться с пеной, пока никто не видит.{/i}"
        else:
            gg "{i}О, мы любим поиграться с пеной, пока никто не видит.{/i}"
        gg "{i}Скажу честно, так выглядит гораздо сексуальнее.{/i}"
        scene jsc11-11 with dissolve
        gg "{i}Как хочется раздеться и просто залезть к ней в ванну.{/i}"
        gg "{i}Но, думаю, сейчас она вряд ли оценит такой шаг.{/i}"
        gg "{i}Ладно, не будем искушать судьбу, пора уходить.{/i}"
        scene jsc11-5 with dissolve
        if persistent.patch_enabled:
            gg "{i}Кажется, я совсем не зря позвал сестру к себе жить.{/i}"
        else:
            gg "{i}Кажется, я совсем не зря позвал Линдси к себе жить.{/i}"
        gg "{i}Надо возвращаться к Келли и поспать. Главное ее не разбудить.{/i}"
    scene black with dissolve
    hide screen mob
    gg "{i}Спать....{/i}"
    pause 2.0
    if mute == False:
        play sound sms
        $ new_flag = 5 # новое смс, от Шейлы
        $ contact_flag = 5 #куда отправлять смс -  Шейлы
        $ naz = 5

        gg "{i}Ммм. Кто-то пишет...{/i}"
        menu:
            "{i}Черт, похоже я проспал весь день и вечер... Но все равно чувствую себя разбитым... Да и Келли вроде еще спит, прямо у меня на груди, может ответить завтра? Если я начну дергаться, Келли может проснуться. {/i}{#l=Ты совсем про меня забыл?}"
            "Спать":
                $ p_kelly += 3
                call msc_u from _call_msc_u_2
            "Ответить":
                call ksc12 from _call_ksc12
    else:
        call msc_u from _call_msc_u_3
    call nsc14 from _call_nsc14
    if j_opazd > 0:
        $ dgame_5 = True
        $ dgame_8 = True
    scene dsc4-2 with dissolve
    if j_opazd > 0:
        show screen new_sketch
        gg "{i}Эта поездка немного меня развеяла... Наверное, можно приступать к следующему рисунку.{/i}"
    if j_project == 2: #Если не согласились и не видели минет, то смс
        $ new_flag = 0 # обнуляем, если не прочитали
        $ new_flag = 1 # новое смс от Кевина
        $ contact_flag = 1 #куда отправлять смс - кевин
        $ sms_all = sms_sister
        if mute == False:
            play sound sms
        else:
            play sound vibr
        gg "{i}Ну, не скучай!{/i} {#l=Ты там еще долго? К тебе тут гости.}"
    elif j_project < 2 and j_deep == 0: #Если отказался, но ушел, то смс
        $ new_flag = 0 # обнуляем, если не прочитали
        $ new_flag = 1 # новое смс от Кевина
        $ contact_flag = 1 #куда отправлять смс - кевин
        $ sms_all = sms_sister
        if mute == False:
            play sound sms
        else:
            play sound vibr
        gg "{i}Ну, не скучай тут, скоро еще покатаемся!{/i} {#l=Ты там еще долго? К тебе тут гости.}"
    else:
        gg "{i}Ну, не скучай, скоро еще покатаемся!{/i}"

    scene dsc4-3 with dissolve
    stop music fadeout 3.0
    play music lora fadein 5.0
    gg "{i}Интересно, где сейчас {b}она{/b}...{/i}"
    if lora_page_2_scene == 2:
        gg "{i}Я не провел здесь и двух дней, а уже столько всего о ней вспомнил... А ведь когда-то я зарекался больше никогда о ней не думать...{/i}"
        gg "{i}Чем больше я вспоминаю о ней, тем сильнее это на меня влияет. Тем больше я в ее власти... Пусть она далеко, но так она сможет влиять на мои мысли, действия и поступки...{/i}"
        gg "{i}Если я хочу мыслить трезво, я должен отказаться  от этого... Я должен ей противостоять... Может лучше будет переключитья на Тейлор?{/i}"
    if lora_page_1_scene == 0:
        gg "{i}Даже этот город не смог заставить меня начать вспоминать о ней. {/i}"
        gg "{i}Ведь чем больше я погружаюсь в это, тем сильнее это на меня влияет. Тем больше я в ее власти... Пусть она далеко, но так она сможет влиять на мои мысли, действия и поступки...{/i}"
        gg "{i}Если я хочу мыслить трезво, я никогда не должен восстанавливать мои рисунки о ней. Я должен сопротивляться... Может лучше будет переключиться на Тейлор?{/i}"
    gg "{i}Какая же здесь все-таки классная погода... Ну, пора смотреть, что там за гости.{/i}"
    scene ssc19-1 with dissolve
    gg "Что!? Как!?"
    lora "Ты так и не избавился от своей привычки не запирать дверь?"
    if persistent.patch_enabled:
        lora "Как ты у меня вырос, мой мальчик... Я так по тебе скучала..."
    else:
        lora "Я так по тебе скучала..."
    scene ssc19-2 with dissolve
    if p_lora >= 5:
        if persistent.patch_enabled:
            gg "{i}Мама... Здесь... И она тоже скучала, я знал...{/i}"
        else:
            gg "{i}Мама... Здесь... И она тоже скучала, я знал...{/i}"
        gg "{i}Нет, я должен бороться. Я должен ей сопротивляться, после того, как она со мной поступила!{/i}"
    if p_lora < 5:
        gg "{i}Не думал, что она отважится появится, после того, как она со мной поступила!{/i}"
    scene ssc19-1 with dissolve

    gg "Но почему ты не предупредила... Как ты узнала где я живу?"
    lora "[gg], если хочешь появится неожиданно, не стоит предупреждать противника. Разве ты не помнишь?"
    lora "Пойдем присядем. Кстати, у тебя ужасно неудобные эти... скамейки? Нужно будет купить другие."
    scene ssc19-3 with dissolve
    if persistent.patch_enabled:
        lora "А узнала из соц. сетей твоей глупышки сестры, конечно. Там уже двадцать фоток у твоего бассейна, у местной кафешки, у пары памятников..."
        lora "Понять где ты, было несложно, сынок..."
    else:
        lora "А узнала из соц. сетей Линдси, конечно. Там уже двадцать фоток у твоего бассейна, у местной кафешки, у пары памятников..."
        lora "Понять где ты, было несложно..."
    scene ssc19-4 with dissolve

    gg "{i}Я... Я так долго мечтал, чтобы мы были вместе, но теперь... Я не видел ее столько времени...{/i}"
    gg "{i}Кто она теперь? Чего хочет!? Почему сейчас?{/i}"

    scene black
    with eye_shut
    with vpunch
    if persistent.patch_enabled:
        gg "{i}...почему... почему сейчас...мама...{/i}"
    else:
        gg "{i}...почему... почему сейчас...{/i}"
    lora "[gg], с тобой все в порядке?"

    if persistent.patch_enabled:
        lora "Сынок? Ты меня слышишь? Да что с тобой?"
    else:
        lora "Ты меня слышишь? Да что с тобой?"
    call ep2
    $ show_w = 1 #1 - выкл бокс 0 вкл

    show screen end_ci with dissolve
    gg "gg"
    return




return
