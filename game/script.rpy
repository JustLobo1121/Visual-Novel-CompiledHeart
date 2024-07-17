# uso de flags
define prologo = True 
    # reutilizacion de 2 escenarios
define state = 0 # reutilizacion de escenarios
    # state 0 uso neutro
    # state 1/2 rutas practica
    # state 3/4 rutas teoria
define Seleccion = 0 
    # 1 colocar ing inf
    # 2 no colocarlo
define switch = 0
define seguir = True 
    # true te quedas
    # false te vas
define rutaBuena = False
    # mas historia
define rutaMala = False 
    # menos historia
# definicion de imagenes
image bg bus inside = "bus inside.png"
image bg house = "house.png"
image bg carnival base = "carnival.png"
image bg classroom prog = "classroom prog.png"
image bg entrance uni pt1 = "entrance uni pt1.png" # posible uso
image bg entrance uni pt2 = "entrance uni pt2.png"
image bg mainbuilding entrance = "images/mainbuilding entrace.png" # posible uso
image bg mainbuilding stairs pt1= "mainbuilding stairs pt1.png"
image bg mainbuilding stairs night pt2= "mainbuilding stairs pt2 night.png" # cambiar imagen
image bg mainbuilding hallway= "mainbuilding hallway.png"
image bg library uni general = "library uni general.png"
image bg library uni couch = "library uni couch.png" # posible uso
image bg library uni base = "library uni pt0.png"
image bg library uni pt1 = "library uni pt1.png"
image bg library uni pt2 = "library uni pt2.png" # posible uso
image bg office uni pt1 = "office uni pt1.png"
# definiciones de audio
define audio.ColorYourNight = "./audio/Color Your Night.mp3" # casa del prota
define audio.RoadNoise = './audio/road-noise-1.mp3' # efecto de sonido
define audio.FairNoise = './audio/street-fair-background-noise-149086.mp3' # efecto de sonido
define audio.Alone = "./audio/Alone.mp3" # momento con Cristi
define audio.IReallyWantYou = "./audio/I Really Want to Stay at Your House  Cyberpunk 2077 OST.mp3" #final de Cristi y quedarte
define audio.LastGoodbye = "./audio/Last Goodbye.mp3" # Final?
define audio.Lilium = "./audio/lilium.mp3" # final malo e irte
define audio.Majula = "./audio/Majula dark souls 2.mp3" # tema edificio Principal y derivados
define audio.NextToYou = "./audio/NEXT TO YOU.mp3" # final salvacion
define audio.OceanOfMemories = "./audio/Ocean of Memories.mp3" #noche
define audio.OnceUponAtime = "./audio/Once Upon a Time.mp3" # ingreso Nombre
define audio.RightBehindYou = "./audio/Right Behind You.mp3" #momento de tension
define audio.SunsetBridge = "./audio/Sunset Bridge.mp3" #zona biblioteca y derivados
define audio.WithASmile = "./audio/With a Smile.mp3" # tema oficina jefe de carrera
define audio.IntroEffect = "./audio/Undertale Sound Effect Intro.mp3" # efecto de sonido
define audio.Autonomy = "./audio/Autonomy.mp3" # sala de programacion

# personajes 
define pov = ("[povname]") # prota
define narrador = ("Dario") # narrador
define Cristi = ("Cristina") # interes amorozo
define e = ("guia del stand") # 1 solo uso
define ProfCris = ("Profe Cristian") # profes importantes
define ProfKermin = ("Profe Kermit") # profes importantes
# imagenes de uso
image kermit happy = "kermit01.png"
image kermit angry = "kermit02.png"
transform AumentoTamIz:
    zoom 2.0
    xalign 0.0
    yalign 1.0
transform oscurecer:
    alpha 0.8

# prologo   
label start:
    stop music
    scene black
    $ povname = renpy.input("Cual es mi nombre?", length=32)
    $ povname = povname.strip()
    jump feriaUni
    return
label feriaUni:
    stop music
    play music FairNoise volume 0.15 loop
    scene bg carnival base with dissolve:
        xzoom 1.5
    $ carreras = []
    $ lista = ""
    $ listaConcat = ""
    pov "La feria de la universidad estaba bastante movida, con estudiantes de muchas partes llegando y recorriendo los puestos. "
    pov "Sonreí, en mis manos se encontraba:"
    menu listaDeCarreras:
        "seleccione si desea tener alguna carrera o no"
        "agregar":
            $ carrera = renpy.input("Carrera: ",length=32)
            $ carreras.append(carrera)
            jump listaDeCarreras
        "lista":
            if carreras:
                $ lista = list(dict.fromkeys(carreras))
                if len(carreras) > 1:
                    $ for item in lista: listaConcat = ", ".join(lista[:-1]) + (" y " + lista[-1] if len(lista) > 1 else lista[-1] if lista else "")
                else:
                    $ listaConcat = carreras[0]
                "mi lista es: [listaConcat]"
            else:
                $ listaConcat = carreras
                "no tienes unas opciones en mente"
                $ listaConcat = carreras
            jump listaDeCarreras
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
        pov "lo mejor seria ir pensando en algo"
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
        """De pronto, la cara de dudas del profesor al hablarle de [carreras[0]] me dominó."""
    else:
        pov "De pronto, la cara de dudas del profesor al hablarle de no tenia opcines pensadas me dominó."
    e "Hola, ¿Hay alguna duda que tengas?"
    """La voz de uno de los chicos interrumpió mis pensamientos, me había quedado quieto de nuevo."""
    pov "Yo..."
    e "¿Te interesa? Mira, la carrera consiste en..."
    """El chico me dio una basta resolución de la carrera, enfocándose en todo lo que había que saber, sin embargo, mi mente no logró retener nada."""

    jump bus
label bus:
    stop music fadeout 0.25
    play music RoadNoise volume 0.25 loop
    scene bg bus inside with dissolve:
        xzoom 1.1
        yzoom 1.1
    pov """
    Al final, solo acabe asintiendo a todo, sin entender realmente, y seguí funcionando mecánicamente hasta el bus de regreso.
    
    Al estar en el bus salí de mi trance a mitad de viaje, y en mis manos habían múltiples folletos de mi carrera soñada,
    junto a un solo folleto celeste.
    
    Consideré dejarlo en el puesto, sin embargo, mi profesor lo decía siempre, ante todo, lo ideal siempre era tener un plan b.
    """
    jump casa
    return
# zona de calma
label casa:
    stop music fadeout 0.5
    play music ColorYourNight fadein 0.25 volume 0.25 loop
    scene bg house with dissolve:
        xzoom 1.5
        yzoom 1.5
    # parte prologo
    if prologo:
        $ opcionInfo = False
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
            "no":
                "probablemente sea mala opcion"
                $ opcionInfo = False
        menu opcionCarrera:
            "quieres colocar la ing. civil en informatica entre tus opciones?"
            "si":
                if opcionInfo:
                    pov "puede que sea buena idea"
                else:
                    pov "No creo que quedé si lo dejo hasta el final. Apreté el botón de enviar con una clara satisfacción, "
                    pov "de ver mi carrera cómo primera opción, ignorando ingeniería civil informática."
                $ Seleccion = 1
                
            "no":
                $ Seleccion = 2
        jump transiciones
    elif state == 0: # parte historia
        narrador "La parcial de programación llegó en un reglón, siendo un evento bastante importante. Era la oportunidad perfecta, para saber que [povname] está por hacer la decisión era correcta."
        menu Teoria_o_Practica:
            "¿Teoría o práctica?"
            "Practica":
                $ state = 1
                $ rutaBuena = True
            "Teoria":
                $ state = 3
                $ rutaMala = True
                """Comencé a dar la teoría en la prueba de programación, al final, decidí ignorar una clara sensación de confusión."""
        jump transiciones
# universidad:
# partes del edificio principal
# tema "once unpon a time"
label entrada_fuera:
    scene bg entrance uni pt2 with dissolve:
        xzoom 1.5
        yzoom 1.5
    if state == 0:
        """Al salir a la entrada principal, un gran frío golpeó mi cuerpo."""
        pov "Maldición..."
        """Había sido un día bastante agotador, y aún faltaba para llegar a casa, sin embargo, mis pies se detuvieron al mirar de reojo la biblioteca."""
        """Seguía abierta a pesar de la hora, y en mi mente se reflejó el libro de matemáticas que el profesor nos había recomendado Ignorando el agotamiento, fui a la biblioteca"""
        jump biblioteca
label entrada:
    scene bg entrance uni pt2 with dissolve:
        xzoom 1.5
        yzoom 1.5
    if state == 2:
        narrador "El mundo se veía más claro, cuando la figura de ella esperando en la puerta, apareció en la visión de [povname]."

        """Apenas notó que estaba ahí, no dije lo que le quería decir en realidad, sino lo que yo necesitaba."""
        pov "Lo decidí."
        jump oficina_de_cristian
label pasillo:
    stop music fadeout 0.25
    scene bg mainbuilding hallway with dissolve:
        xzoom 1.5
        yzoom 1.5
    play music OnceUponAtime volume 0.25 loop
    if state == 0:
        """Los pasillos del lugar estaban silenciosos, vacíos, ya que era tarde."""
        jump entrada_fuera

label escaleras:
    scene bg mainbuilding stairs pt1 with dissolve:
            xzoom 1.5
            yzoom 1.5
    if state == 1 or state == 2 or state == 3:
        stop music fadeout 0.5
        play music OnceUponAtime fadein 0.25 volume 0.25
        if state == 1:
            """
            Apenas salí de clase, me escabullí a la biblioteca.
            Fui con paso alegre, pasando por el familiar espacio de logias llenas de estudiantes, fui directo al mostrador.
            """
            # cambiar salto
            jump biblioteca_mostrador
        elif state == 2:
            narrador "[povname] comenzo a caminar hasta programacion, dónde el profesor lo esperaba con una sonrisa sádica."
            """Kermin, este profe"""
            jump sala_programacion
        elif state == 3:
            """Extrañado, comencé a caminar hasta programación, dónde el profesor me esperaba con una sonrisa sádica"""
            jump sala_programacion
    elif state == 4:
        """
        No quería ver a mis amigos en éste momento, sintiendo un sentimiento desgarrador de fracaso.
        En realidad, a pesar de mis dudas, rendirse siempre se sentía mal después de todo.

        Sin embargo, no probaba que las palabras de esa persona fueran ciertas.
        """
        jump finales
label escaleras_noche: 
    stop music
    scene bg mainbuilding stairs night pt2 with dissolve
    play music OnceUponAtime volume 0.25 loop
    if state == 2:
        """
        Había sido bastante satisfactorio a comparación de los anteriores, en los que acababa siempre sintiendo una gran frustración.
        
        Independiente de mi nota, mi realización había sido completa, por lo que estaba bien.
        """
        jump entrada
# salas/oficina
label sala_programacion:
    scene bg classroom prog with dissolve:
        xzoom 1.5
    stop music fadeout 0.25
    play music Autonomy fadein 0.25 volume 0.25
    if state == 0:
        """
        Sentí mis dientes apretarse, al ver en la terminal todos los errores que indicaba el compilador, en pleno control de programación.
        """
        show kermit happy at AumentoTamIz with dissolve
        ProfKermin "Ya es hora, es todo por hoy, pueden retirarse..."
        ProfKermin "Prepárense para la parcial del jueves."
        show kermit happy at oscurecer with dissolve
        """
        Está vez, fueron mis propios puños los que se apretaron, al escuchar una voz suave hablar con sarcasmo, 
        mientras mi mente buscaba todo tipo de razones para no romper mi propia computadora, que seguía produciendo palabras repetidas
        """

        narrador "La sala estaba casi vacía, aparte de [povname], el profesor Kermin y un par de chicos, uno dormido, todos los demás compañeros se habían ido."

        """
        Inserte mi nombre a regañadientes en el archivo en C.
        Era entendible, considerando mi propio estado, verías a una persona ojerosa y somnolienta, que llevaba en una incómoda silla con mala postura,

        mirando una borrosa pantalla que se hacía más borrosa a cada momento.

        El estado mental fue ausente, se había ausentado desde que a los 30 minutos de clase, estaba seguro que habían pasado 3 horas, y era un error.

        Ignorando el dolor de hombros, forcé mis manos a apagar y guardar mi computador, y mis pies a levantarse.

        Sentí la mirada del profesor sobre mí, por lo que hice una pequeña pausa, antes de comenzar a caminar
        """
        jump pasillo
    elif state == 1:
        """
        Comencé a dar la práctica en la prueba de programación, y con cada código, mi mente comenzó a maquetar todo en mi cabeza más fácil.
        Al final, dejé muchas alarmas, con una extraña sensación de satisfacción.
        """
        jump escaleras
    elif state == 2:
        """
        Al cerrar la puerta fui directo a una computadora, y comencé a esperar el enunciado del código.
        Esto lo iba a decidir.

        No sabía si era nerviosismo, o el hecho de basar una decisión tan importante en un solo parcial, sin embargo, todo se sentía surrealista.

        Por un momento recordé, los momentos en la carrera, los frustrantes primeros rojos de mi vida, las amistades que hice, los momentos divertidos y estresantes, el cansancio y constante presión.

        "Había sido una mezcla de experiencias, que habían mejorado a la persona del primer día, tal vez a golpes, pero era algo.
        """
        ProfKermin "Los códigos están en la plataforma."
        # minijuego
        jump minijuego
    elif state == 3:
        """
        Una decisión bastante importante iría después de esté parcial.
        Sentí que mi éxito en está carrera se iba a definir en éste momento, lo que hizo que la presión que me daba esa persona, siguiera allí aún cuando no estaba.
        """
        ProfKermin "El problema está subido a la plataforma."
        """
        No pude deshacer el nudo en mi garganta, sintiendo que faltaba algo importante.
        Apenas leí el problema, me di cuenta que no podía hacerlo.
        """
        scene black with dissolve
        jump minijuego
label oficina_de_cristian:
    stop music
    scene black with dissolve
    play music IntroEffect volume 0.5
    show text "Epilogo" with Pause(1.5)
    scene black with dissolve
    play music WithASmile fadein 1.0 volume 0.25 loop
    narrador "Ante el final de la clase de introducción a la ingeniería, [povname] siguió al profesor al aula, debido a la conversación a inicio del semestre debido a éste tema."
    scene bg office uni pt1 with dissolve:
        xzoom 1.5
    ProfCris "Dime, a qué conclusión llegaste."
    narrador "Una suave sonrisa se posó en el jefe de carrera."
    play music RightBehindYou volume 0.05
    menu Quedate_o_fuera:
        "Yo..."
        "Voy a quedarme":
            stop music fadeout 1.5
            if rutaBuena:
                play music IReallyWantYou volume 0.25 fadein 1.5 loop
            else:
                play music OceanOfMemories volume 0.25 fadein 0.5 loop
            $ seguir = True
            ProfCris "¿Qué te convenció?"

            pov "En realidad, disfruté bastante de programación esté semestre, creo que me gusta resolver problemas usando la lógica."

            ProfCris "Tú concéntrate en pasar, siempre puedes venir a verme y tomarte un té."

            pov "Gracias"

            """Sentí una sonrisa en mi cara, y un peso menos en el pecho, en realidad, todo se sentía más bien que hacía unos días.
            En realidad acabé descubriendo mi pasión."""
            if rutaBuena:
                narrador "Con ese alivio en el pecho, [povname] se dirigío a la biblioteca con pasos animados, dónde Cristina lo esperaba con una sonrisa."
                jump biblioteca
            else:
                jump finales
        "Voy a irme":
            stop music fadeout 1.0
            play music Lilium volume 0.25 loop
            $ seguir = False
            $ state = 4
            ProfCris "¿Al final fue eso?"
            pov "No creo que está ingeniería sea algo para mí."
            ProfCris "Entiendo, fue un placer tenerte aquí."
            pov"Gracias."
            narrador "[povname] se dirigía al frente con pasos decaídos, pero seguros."
            
            jump escaleras
# label del minijuego
label minijuego:
    # despues del mini juego
    if state == 2:
        """
        Un repentino nerviosismo vino encima de mí, era un sentimiento bastante familiar que sucedía cada vez que tenía una mala calificación.

        Al abrir el problema, sentí mis manos temblar, un sentimiento de presión que hizo que quisiera ir a hablar en éste momento con el jefe de carrera.
        """
        narrador "Sin embargo, unas simples de palabras lo detuvieron."
        Cristi "Si quieres, lo podrías hablar conmigo."
        """
        Eso hizo que comenzará a bosquejar el problema en mi mente."
        En realidad, fue un último parcial bastante sencillo, al que me quedé hasta el final, a pesar de que todos mis compañeros abandonaron.

        Mi mente maquetó el código casi enseguida y mis dedos se movieron por instinto.

        A pesar de todo, era verdad que independiente de mi decisión, mis múltiples caídas y la presión de esa persona, jamás lo iba a sentir está experiencia cómo un fracaso.

        Al final del parcial, salí de aquella sala con la espalda bastante más ligera que de costumbre.
        """
        jump escaleras_noche
    elif state == 3:
        """
        Sentí cómo todas las pequeñas frustraciones e ideas dominaron mi mente, la cuál, estaba tratando desesperadamente de ignorarlas y hacer el problema.

        Sin embargo, no podía.
        
        Era realmente triste que hiciera lo que hiciera, sin importar cuánto me esforzará en realidad, siguiera fracasando.
        
        Lo poco que sentía haber logrado aparte, era fácilmente mermado por un par de palabras de desaprobación.
        
        La presión de la universidad no ayudaba a lidiar con eso, y por eso había acabado así.
        
        Quería lidiar con todo solo, y no quería que todos creyeran que al final no servía.
        
        Desde el principio, solo todo fue simplemente una demostración inmadura para llevarle la contraria a esa persona.
        Y acabé fracasando.
        """
        scene bg classroom prog with dissolve:
            xzoom 1.5
        """
        Al final, acabé saliendo hasta el final de clases, sin poder haber hecho nada.
        Me fui a mi casa sin verla
        """
        jump oficina_de_cristian
# partes de la biblioteca
# tema "sunset bridge"
label biblioteca:
    scene bg library uni general with dissolve:
        xzoom 1.5
        yzoom 2.5
    if state == 0:
        stop music fadeout 0.25
        play music SunsetBridge volume 0.25 loop
        """
        huyendo de el gran frío del exterior, siendo recibido por una cálida temperatura ambiente apenas cruce la puerta, y viendo vacío, un lugar que comúnmente tenía un montón de gente estudiando.

        Abrí la puerta con cuidado, con intención de salir rápido, y apenas levanté la vista al mostrador, mi cuerpo se detuvo por  instinto.

        Un breve vistazo bastó para detener mi atención en una sola persona.
        """

        narrador "esa persona es Cristina, Una joven se encontraba detrás del mostrador, siendo la única persona en el lugar vacío."
        narrador "La joven de lentes, extrañamente familiar, sonreía con gracia viendo una lista, con un cabello ondulado mal amarrado,"
        narrador "y una camisa ajustada que moldeaba un gran busto."
        narrador "antes de que [povname] se de cuenta, una sonrisa pura y par de ojos brillantes se concentraron en su persona."

        """
        Mi cuerpo se adormeció, ignorando el agotamiento de programación, mientras el sentimiento ausente de mi mente se evaporó, y todo comenzaba a sentirse mágico.
        
        Recién al final de ese día, me di cuenta que subía al mismo bus que yo.
        """
        jump transiciones
    elif state == 2:
        # momento Cristi
        pov "Lo hice."
        Cristi "Lo hiciste."
        pov "¿Fue lo correcto?"
        pov "Dependerá de ti…"
        """
        Un pequeño gesto de tristeza se hizo presente en su cara, una conversación pendiente que debíamos tener en un futuro.
        
        Sin embargo, era algo que podría esperar ahora.
        
        Inmediatamente la vi sonreír, sabiendo que iba a comenzar otra de nuestras largas charlas que seguían hasta nuestro camino a casa.
        """
        jump finales
label biblioteca_libros:
    stop music fadeout 0.25
    play music Alone volume 0.25 fadein 1.5 loop
    scene bg library uni pt1 with dissolve:
        xzoom 1.5
        yzoom 1.5
    if state == 1:
        narrador "esta área de libros es usualmente vacía, por lo que fueron para hablar a solas."
        narrador "[povname] no podia evitar hacerse ideas, al verla dudar tanto, sintiendo que la conversación de la tarde igual no iba a ser necesaria," 
        narrador "sin embargo, después de mucho tiempo, [povname] escuchó las palabras que estaba evitando pensar."

        Cristi "… Según vi, estabas investigando un cambio de carrera, ¿… Estás seguro?"

        """
        Parpadeé con torpeza, completamente congelado ante esa afirmación.

        Y pronto, el sentimiento amargo que se había aliviado desde que la conocí, subió por mi garganta, recordando mi conversació más actual con el jefe de carrera.
        """

        Cristi "¿no te gusta...?"

        """
        No era eso.
        Aunque costaba mucho, era una carrera muy entretenida, sin embargo, habían varias cosas que seguían rondando en mi cabeza.
        
        Una presencia que me hizo cuestionar acerca de si todos mis logros eran eso, y no simplemente fracasos que me estaban llevando por un camino amargo.
        
        Aparte, el proceso de adaptación había sido bastante complicado, y quitando pequeños desahogos a lo largo del semestre, sentía que buena parte de la frustración seguía acomulandose ahí.
        
        Una pequeña presión constante, que hizo que el parcial fuera extrañamente importante.
        """
        pov "Yo… Lo iba a considerar en esté parcial."
        Cristi "Mira… No sé tú situación y no hablé mucho contigo… Sin embargo… Por experiencia propia, a veces un cambio así no arregla tus problemas en realidad."

        """
        Una afirmación bastante acertada.
        Al menos en la corta experiencia que estaba teniendo, una carrera universitaria consumía gran parte de mi vida y tiempo.
        Sin embargo, los problemas estaban ahí, aparte de la carrera.

        Nada me aseguraba que al cambiar de carrera, no cambiará nada, y acabará teniendo que de plano salir de la universidad.
        
        Al ver un bosquejo de confusión en mi cara, sentí su mano sobre la mía, y en ese momento me di cuenta que había estado temblando.
        Sentí mucha vergüenza, y trate de separarlas, pero ella las apretó.
        """

        Cristi "Mira… No quisiera presionarte, pero si pasa algo, tienes mucha gente con la que podrías hablar de ello…"

        """
        Un nudo en el pecho se me retorció, en realidad, sabía que nunca tendría esa confianza con nadie, solo me mordí el labio interno
        """

        pov "Yo…"
        Cristi "Si quieres, lo podrías hablar conmigo…"
        """
        Ante esas palabras, la miré, y noté algo, estaba bastante nerviosa.

        En todo el tiempo que mi mente se llenaba de una tormenta de ideas, había pasado por alto el detalle de que cada palabra hacía mí, 
        equivalía al sentimiento de presentar en público.
        
        Aún así, una calidez llegó a mi interior, sabiendo que a pesar de eso, se había preocupado lo suficiente para abordarme aún cuando le costaba.
        
        El sentimiento dulce dominó fácilmente al amargo, seguía allí, sin embargo, no fue tan fuerte como la noche anterior.
        
        Incluso la existencia de esa persona se había aplacado un momento.
        
        En realidad, verla era un alivio que me motivaba a seguir, sin embargo, saber que también estaba ahí para mi, solo hizo que hubiera algo nuevo
        """
        pov "Cuando lo decida, te lo diré a ti"
        """
        Era gratitud
        
        Una familiar sonrisa pura vino a mí, y ante un claro sonrojo en mis mejillas, solo se rio.
        """
        Cristi "Buena suerte… Te veo a las 17:00"
        jump transiciones
label biblioteca_mostrador:
    stop music fadeout 0.25
    scene bg library uni base with dissolve:
        xzoom 1.5
        yzoom 1.5
    play music SunsetBridge volume 0.25 fadein 1.5 loop
    if state == 3:
        """Fui con paso alegre, directo al mostrador."""
    pov "Hola… Cris, tiempo sin verte."
    Cristi "Hola… Nos vimos ayer, sabes…"
    """
    Ella se encontraba igual o más radiante, me había motivado a darle pequeñas pláticas a lo largo del día.
    
    Casi siempre era una conversación unilateral, con ella no pudiendo contestar más de una cosa, pero sin lugar a dudas fue mi momento más aliviante.

    Aunque en éste momento, sentí que fue todo lo contrario, ya que aunque estuviera hablando con ella normalmente, mi interior se estaba derrumbando por completo.
    Después de una plática pequeña, una parte de mí se animó a pedirle algo importante.
    """
    pov "Bueno… ¿Podrías esperarme después de clase? Tengo algo que decirte…"
    Cristi "Yo… Supongo…"
    pov "Salgo a las 17:00… Es mi último parcial."
    Cristi "El último…"
    stop music fadeout 1.5
    play music RightBehindYou volume 0.05 fadein 0.5
    if state == 1:
        """
        Al ver su cara dudosa, supe que quería decirme algo, así que espere un poco, así que espere un poco.
        En un momento subrealista, la chica callada salió del mostrador,
        
        y me agarró de la muñeca, arrastrandome al área de libros
        """
        jump biblioteca_libros
    if state == 3:
        """
        Al ver su cara dudosa, supe que quería decirme algo, así que espere un poco, sin embargo, no dijo nada, hasta que momentos después sólo negó con la cabeza.

        Una familiar sonrisa pura vino a mí, y ante mi expresión confusa, una mueca de preocupación se posó en su rostro, sin embargo, no tocó el tema más allá.
        """
        Cristi "Buena suerte."
        jump escaleras
# controladores
label transiciones:
    stop music fadeout 0.25
    scene black with dissolve
    if Seleccion == 0: # paso a ruta buena/mala
        $ Seleccion = 10
        play music IntroEffect volume 0.5
        show text "Capítulo único \n 'Programación'" with Pause(3)
        jump casa
    elif Seleccion == 1: 
        $ Seleccion = 0
        $ prologo = False
        play music IntroEffect volume 0.5 noloop
        show text "5 meses despues" with Pause(3)
        jump sala_programacion
    elif Seleccion == 2: #final de salvacion
        jump finales
    if rutaBuena and switch == 0:
        $ switch = 1
        jump sala_programacion
    elif rutaBuena and switch == 1:
        $ state = 2
        jump escaleras
    elif rutaMala and switch == 0:
        $ switch = 1
        """Apenas salí de clase ese día, me escabullí a la biblioteca"""
        jump biblioteca_mostrador
    return
label finales: # completo
    scene black with dissolve
    if Seleccion == 2:
        play music NextToYou volume 0.25 fadein 1.5
        play music IntroEffect volume 0.5
        show text "Final: Te salvaste" with Pause(3)
        play music IntroEffect volume 0.5
        show text "Felicidades?" with Pause(3)
    elif seguir and rutaBuena: # finales originales
        """
        Una paz bastante temporal, sabiendo que era apenas mi primer semestre de ingeniería, sin embargo, 
        me sentía aún más preparado para el segundo de lo que podría esperar.
        """
        play audio IntroEffect volume 0.5
        show text "Final: \n“Bienvenido a la carrera y buena suerte”" with Pause(3)
    elif not seguir and rutaBuena:
        pov """
        Mi futuro dependía de mí, después de todo.
        
        Tal vez jamás iba a ser el futuro que había imaginado, iba a ser un futuro distinto, pero me aseguraría que al fin y al cabo, fuera uno con el que estuviera feliz.
        
        Uno por el que sentía que valía la pena luchar.
        """
        narrador "[povname] habiendo decidido su futuro, decidido aunque algo decaido se fue de la universidad"
        play audio IntroEffect volume 0.5
        show text "Final: \n“Buena suerte en tu futuro”" with Pause(3)
    elif not seguir and rutaMala:# finales originales
        pov """
        Mi futuro dependía de mí, después de todo.

        Tal vez jamás iba a ser el futuro que había imaginado, iba a ser un futuro distinto, pero me aseguraría que al fin y al cabo, fuera uno con el que estuviera feliz.
        
        Uno por el que sentía que valía la pena luchar.
        """
        play audio IntroEffect volume 0.5
        show text "Final: \n“Buena suerte en lo que decidas”" with Pause(3)
    elif seguir and rutaMala: 
        narrador """
        Una paz bastante temporal, [povname] sabiendo que era apenas su primer semestre de ingeniería, sin embargo, se sentía aún más preparado para el segundo de lo que podría esperar.
        
        [povname] seguira su pasion y con determinacion a Cristina.
        """
        play audio IntroEffect volume 0.5
        show text "Final: \n“Bienvenido a la carrera...”" with Pause(3)
    return