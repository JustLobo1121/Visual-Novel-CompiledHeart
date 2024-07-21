label prolog:
    
    stop music
    $ povname = renpy.input("Cual es mi nombre?", length=32)
    $ povname = povname.strip()
    
    scene bg feria at backgroundZoom(1.05,1.25)
    play music audio.FairNoise fadein 0.5
    pov """
    La feria de la universidad estaba bastante movida, con estudiantes de muchas partes llegando y recorriendo los puestos. Sonreí, 
    
    en mis manos se encontraba:
    """
    menu menuCarr:
        "que carreras tengo en mente"
        "agregar":
            $ carrera = renpy.input("Carrera: ",length=32)
            $ carreras.append(carrera)
            jump menuCarr
        "lista":
            if carreras:
                $ lista = list(dict.fromkeys(carreras))
                if len(carreras) > 1:
                    $ for item in lista: listaConcat = ", ".join(lista[:-1]) + (" y " + lista[-1] if len(lista) > 1 else lista[-1] if lista else "")
                else:
                    $ listaConcat = carreras[0]
                "mi lista es: [listaConcat]"
            else:
                "no tienes unas opciones en mente"
                $ listaConcat = carreras
            jump menuCarr
        "termine":
            if carreras:   
                $ lista = list(dict.fromkeys(carreras)) 
                $ for item in lista: listaConcat = ", ".join(lista[:-1]) + (" y " + lista[-1] if len(lista) > 1 else lista[-1] if lista else "")
                pov "mis opciones son: [listaConcat], esas son."
            else:
                pov "no tengo opciones pensadas."
    if carreras:
        pov "[listaConcat[0]] mi primera opción de carrera, y seguramente mi futura profesión."
    else:
        "lo mejor seria ir pensando en algo"
    
    """ 
    Mis ojos miraron alrededor del lugar con pereza, más que nada debido a la exigencia de mi profesor de elegir al menos una carrera más por si acaso.

    Antes de darme cuenta algo llamó mi atención, y mis pies pararon en seco, al ver un gran puesto en la sección de ingeniería. 
    \'Ingeniería... Dinero...\'

    Estaba lleno de gente que se veía de lejos mal vestida, siendo cada uno extravagante aunque vestían la ropa de la universidad.

    Los múltiples computadores con videojuegos llamaron mi atención, y solo eso me llevó a acercarme, lejos de los ayudantes, y tomar un folleto a escondidas.
    
    \"Es un puntaje razonable: 10%% lenguaje... 30%% matemáticas... Ranking 40%%... El resto 10%%...\"\n

    La carrera era ingeniería civil en informática, eran once semestres, que incluían muchas ciencias y matemáticas.

    Era interesante, pero no era mi interés general, sin embargo, antes de dejar el folleto, 
    mi mano se detuvo al recordar unas palabras que habían quedado grabadas en mi mente.

    '¿En serio crees que lograrás entrar a una universidad? Si llegas a repetir, no te voy a apoyar, ¿Crees que tu padre quiere que lo hagas...'
    """
    if carreras:
        "De pronto, la cara de dudas del profesor al hablarle de [carreras[0]] me dominó."
    else:
        "De pronto, la cara de dudas del profesor al hablarle de no tenia opcines pensadas me dominó."
    e "Hola, ¿Hay alguna duda que tengas?"
    "La voz de uno de los chicos interrumpió mis pensamientos, me había quedado quieto de nuevo."
    pov "Yo..."
    e "¿Te interesa? Mira, la carrera consiste en..."
    """El chico me dio una basta resolución de la carrera, enfocándose en todo lo que había que saber, sin embargo, mi mente no logró retener nada."""
    stop music fadeout 0.5
    scene black with dissolve
    scene bg bus at backgroundZoom(1.05,1.05)
    play music audio.RoadNoise fadein 0.5
    """
    Al final, solo acabe asintiendo a todo, sin entender realmente, y seguí funcionando mecánicamente hasta el bus de regreso.
    
    Al estar en el bus salí de mi trance a mitad de viaje, y en mis manos habían múltiples folletos de mi carrera soñada,
    junto a un solo folleto celeste.
    
    Consideré dejarlo en el puesto, sin embargo, mi profesor lo decía siempre, ante todo, lo ideal siempre era tener un plan b.
    """
    stop audio fadeout 0.5
    play music audio.ColorYourNight fadeout 0.5 volume 0.25 loop
    scene bg house at backgroundZoom(1.5,1.5)
    $ opInfo = False
    pov """
    Lo logré...
        
    Todo el miedo y frustración de los últimos meses se evaporaron apenas fijé la mirada en el puntaje de la Prueba de Selección   Universitaria.
        
    Tardé unos días en reaccionar, e ir directamente a la página de universidades a postularme en 10 universidades cerca de mi casa.
        
    Sentí tanta felicidad, sin embargo, antes de enviar la postulación, 
    entre todos los folletos en el escritorio, apareció un repentino color celeste.
    
    En mi mente, recordé vagamente la razón por la que estaba ahí, y me pregunte si debía verlo mejor.
    """
    menu informarse:
        "quieres informarte sobre la carrera de ingeniería civil informática?"
        "si":
            $ renpy.run(OpenURL("https://admision.ulagos.cl/index.php/admision/carreras/ingcivil-informatica"))
            # llevar a la pag uni ing informatica
            pov "La carrera trataba de diseñar, desarrollar y gestionar sistemas a través de programación y logaritmos."
            pov "Se necesitaba un fuerte manejo de matemáticas y lógica"
            $ opcionInfo = True
            menu opcionCarrera:
                "quieres colocar la ing. civil en informatica entre tus opciones?"
                "si":
                    if opcionInfo:
                        pov "puede que sea buena idea"
                    else:
                        pov "No creo que quedé si lo dejo hasta el final. Apreté el botón de enviar con una clara satisfacción, "
                        pov "de ver mi carrera cómo primera opción, ignorando ingeniería civil informática."
                "no":
                    $ Opcion1 = 2
                    jump finales
        "no":
            "probablemente sea mala opcion"
            $ opcionInfo = False
    play music audio.TitleEffect noloop
    show text "5 meses despues" with Pause(3)
    $ Opcion1 = 0
    
    stop music
    play music audio.nothingCanBeExplained fadein 0.5 volume 0.25
    scene bg classroom prog at backgroundZoom(1.0,1.5)
    show s_kermit at zoomAndAlign(1.75,0.0)   
    show s_prota at center
    "Sentí mis dientes apretarse, al ver en la terminal todos los errores que indicaba el compilador, en pleno control de 
    programación."
    kermit "Ya es hora, es todo por hoy, pueden retirarse..." 
    kermit "Prepárense para la parcial del jueves."
    "Está vez, fueron mis propios puños los que se apretaron, al escuchar una voz suave hablar con sarcasmo, mientras mi mente 
    buscaba todo tipo de razones para no romper mi propia computadora, que seguía produciendo palabras repetidas."
    show s_dario at zoomAndAlign(1.5,1.0)
    narrador "La sala estaba casi vacía, aparte de [povname], el profesor Kermin y un par de chicos, uno dormido, todos los 
    demás se habían ido."
    hide s_dario with dissolve
    """ Inserte mi nombre a regañadientes en el archivo en C.
    Era entendible, considerando mi propio estado, verías a una persona ojerosa y somnolienta, que llevaba en una incómoda silla 
    con mala postura, mirando una borrosa pantalla que se hacía más borrosa a cada momento.
    El estado mental fue ausente, se había ausentado desde que a los 30 minutos de clase, estaba seguro que habían pasado 3 
    horas, y era un error.
    Ignorando el dolor de hombros, forcé mis manos a apagar y guardar mi computador, y mis pies a levantarse.
    """
    hide s_kermit with dissolve
    show s_kermit serius at zoomAndAlign(1.75,0.5)
    pov "Sentí la mirada del profesor sobre mí, por lo que hice una pequeña pausa, antes de comenzar a caminar"
    # pasillos
    stop music
    play music audio.OnceUponAtime
    scene bg mainbuilding hallway at backgroundZoom(1.25,1.5)
    "Los pasillos del lugar estaban silenciosos, vacíos, ya que era tarde."
    # entrada
    scene bg entrance at backgroundZoom(1.12,1.5)
    "Al salir a la entrada principal, un gran frío golpeó mi cuerpo."
    pov "Maldición..."
    """Había sido un día bastante agotador, y aún faltaba para llegar a casa, sin embargo, mis pies se detuvieron al mirar de reojo la biblioteca.

    Seguía abierta a pesar de la hora, y en mi mente se reflejó el libro de matemáticas que el profesor nos había recomendado.

    Ignorando el agotamiento, fui a la biblioteca
    """
    # parte final
    scene bg library general pt1 at backgroundZoom(1.13,1.5)
    """huyendo de el gran frío del exterior, siendo recibido por una cálida temperatura ambiente apenas cruce la puerta, y viendo vacío, un lugar que comúnmente tenía un montón de gente estudiando.
        
    Abrí la puerta con cuidado, con intención de salir rápido, y apenas levanté la vista al mostrador, mi cuerpo se detuvo por instinto.
        
    Un breve vistazo bastó para detener mi atención en una sola persona.
    """
    show s_dario at zoomAndAlign(1.5,0.0)
    show s_cristina at zoomAndAlign(2.0,1.0)
    narrador """Una joven se encontraba detrás del mostrador, siendo la única persona en el lugar vacío.
    
    La joven de lentes, extrañamente familiar, sonreía con gracia viendo una lista, con un cabello ondulado mal amarrado, y una camisa ajustada que moldeaba un gran busto.
        
    Antes de que [povname] se de cuenta, una sonrisa pura y par de ojos brillantes se concentraron en el.
    """

    pov "Mi cuerpo se adormeció, ignorando el agotamiento de programación, mientras el sentimiento ausente de mi mente se evaporó, y todo comenzaba a sentirse mágico."

    pov "Recién al final de ese día, me di cuenta que subía al mismo bus que yo."

    jump casa