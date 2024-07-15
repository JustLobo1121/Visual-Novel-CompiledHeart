# personajes 
define pov = ("[povname]") # prota
define povInside = ("pensamientos de [povname]")
define narrador = ("Dario") # dice las desc. y esos
define Cristi = ("Cristina") # interes amorozo
define e = ("guia del stand") # 1 solo uso
define ProfCris = ("Profe Cristian") # profes importantes
define ProfKermin = ("Profe Kermin") # profes importantes
# uso de flags
define prologo = True # reutilizacion de 2 escenarios
define state = 0 # reutilizacion de escenarios
# state 0 uso neutro
# state 1/2 rutas practica
# state 3/4 rutas teoria
define switch = 0
# 1 practica
# 2 teoria
define Seleccion = 0 # 2 opciones
define Quedarse = True 
# true te quedas
# false te vas
define rutaBuena = False # mas historia
define rutaMala = False # menos historia
# definicion de imagenes
image bg bus inside = "bus inside.png"
image bg house = "house.png"
image bg carnival base = "carnival.png"
image bg carnival gym = "carnival gym.png"
image bg classroom prog pt0 = "classroom prog pt0.png"
image bg classroom prog pt1 = "classroom prog pt1.png"
image bg classroom prog pt2 = "classroom prog pt2.png"
image bg entrance uni pt1 = "entrance uni pt1.png"
image bg entrance uni pt2 = "entrance uni pt2.png"
image bg mainbuilding entrance = "images/mainbuilding entrace.png"
image bg mainbuilding stairs pt1= "mainbuilding stairs pt1.png"
image bg mainbuilding stairs pt2= "mainbuilding stairs pt2.png"
image bg mainbuilding stairs night pt2= "mainbuilding stairs pt2 night.png"
image bg mainbuilding floor2 night = "mainbuilding floor2 night.png"
image bg mainbuilding hallway= "mainbuilding hallway.png"
image bg mainbuilding hallway night = "mainbuilding hallway night.png"
image bg library uni general = "library uni general.png"
image bg library uni couch = "library uni couch.png"
image bg library uni base = "library uni pt0.png"
image bg library uni pt1 = "library uni pt1.png"
image bg library uni pt2 = "library uni pt2.png"
image bg office uni pt1 = "office uni pt1.png"
image bg office uni pt2 = "office uni pt2.png"
image bg bathroom uni = "bathroom uni.png"
image bg outside uni = "outside uni.png"
# escena de inicio
label start:
    scene black
    $ povname = renpy.input("Cual es mi nombre?", length=32)
    $ povname = povname.strip()
    jump feriaUni
    return
# prologo
label feriaUni:
    scene bg carnival base with dissolve:
        xzoom 1.5
    
    pov "La feria de la universidad estaba bastante movida, "
    pov "con estudiantes de muchas partes llegando y recorriendo los puestos. "
    pov "Sonreí, en mis manos se encontraba:"
    $ carreras = []
    $ lista = ""
    $ listaConcat = ""
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
                pov "mis opciones son: [listaConcat], esas son."
            else:
                pov "no tengo opciones pensadas."
    if carreras:
        pov "[carreras[0]] mi primera opción de carrera, y seguramente mi futura profesión."
    else:
        pov "lo mejor seria ir pensando en algo"
    povInside "Mis ojos miraron alrededor del lugar con pereza, "
    povInside "más que nada debido a la exigencia de mi profesor de elegir al menos una carrera más por si acaso."
    povInside "Antes de darme cuenta algo llamó mi atención, "
    povInside "y mis pies pararon en seco, al ver un gran puesto en la sección de ingeniería. \'Ingeniería... Dinero...\'"
    povInside "Estaba lleno de gente que se veía de lejos mal vestida, siendo cada uno extravagante aunque vestían la ropa de la universidad."
    povInside "Los múltiples computadores con videojuegos llamaron mi atención, y solo eso me llevó a acercarme, lejos de los ayudantes, y tomar un folleto a escondidas."
    povInside " \"Es un puntaje razonable: 10%% lenguaje... 30%% matemáticas... Ranking 40%%... El resto 10%%...\" "
    povInside "La carrera era ingeniería civil en informática, eran once semestres, que incluían muchas ciencias y matemáticas."
    povInside "Era interesante, pero no era mi interés general, sin embargo, antes de dejar el folleto, "
    povInside "mi mano se detuvo al recordar unas palabras que habían quedado grabadas en mi mente."
    "¿En serio crees que lograrás entrar a una universidad? Si llegas a repetir, no te voy a apoyar, ¿Crees que tu padre quiere que lo hagas..."
    if carreras:
        povInside "De pronto, la cara de dudas del profesor al hablarle de [carreras[0]] me dominó."
    else:
        pov "De pronto, la cara de dudas del profesor al hablarle de no tenia opcines pensadas me dominó."
    e "Hola, ¿Hay alguna duda que tengas?"
    povInside "La voz de uno de los chicos interrumpió mis pensamientos, me había quedado quieto de nuevo."
    pov "Yo..."
    e "¿Te interesa? Mira, la carrera consiste en..."
    povInside "El chico me dio una basta resolución de la carrera, enfocándose en todo lo que había que saber, sin embargo, mi mente no logró retener nada."

    jump bus
    return
label bus:
    scene bg bus inside with dissolve:
        xzoom 1.1
        yzoom 1.1
    pov "Al final, solo acabe asintiendo a todo, sin entender realmente, y seguí funcionando mecánicamente hasta el bus de regreso."
    pov "Al estar en el bus salí de mi trance a mitad de viaje, y en mis manos habían múltiples folletos de mi carrera soñada,"
    pov "junto a un solo folleto celeste."
    pov "Consideré dejarlo en el puesto, sin embargo, mi profesor lo decía siempre, ante todo, lo ideal siempre era tener un plan b."
    jump casaDelProta
    return
label casaDelProta:
    scene bg house with dissolve:
        xzoom 1.5
        yzoom 1.5
    if prologo:
        $ opcionInfo = False
        pov "Lo logré..."
        pov "Todo el miedo y frustración de los últimos meses se evaporaron apenas fijé la mirada en el puntaje de la Prueba de Selección   Universitaria."
        pov "Tardé unos días en reaccionar, e ir directamente a la página de universidades a postularme en 10 universidades cerca de mi     casa."
        pov "Sentí tanta felicidad, sin embargo, antes de enviar la postulación, "
        pov "entre todos los folletos en el escritorio, apareció un repentino color celeste."
        pov "En mi mente, recordé vagamente la razón por la que estaba ahí, y me pregunte si debía verlo mejor."

        menu informarse:
            "quieres informarte sobre la carrera de ingeniería civil informática?"
            "si":
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
    elif state == 0:
        narrador "La parcial de programación llegó en un reglón, siendo un evento bastante importante. Era la oportunidad perfecta, para saber que [povname] está por hacer la decisión era correcta."
        menu Teoria_o_Practica:
            "¿Teoría o práctica?"
            "Practica":
                $ state = 1
                $ rutaBuena = True
            "Teoria":
                $ state = 3
                $ rutaMala = True
                povInside "Comencé a dar la teoría en la prueba de programación, al final, decidí ignorar una clara sensación de confusión."
        jump transiciones
    return
label entrada_Uni:
    scene bg entrance uni pt2 with dissolve:
        xzoom 1.5
        yzoom 1.5

    if state == 0:
        povInside "Al salir a la entrada principal, un gran frío golpeó mi cuerpo."
        pov "Maldición..."
        povInside "Había sido un día bastante agotador, y aún faltaba para llegar a casa, sin embargo, mis pies se detuvieron al mirar de reojo la biblioteca."
        povInside"Seguía abierta a pesar de la hora, y en mi mente se reflejó el libro de matemáticas que el profesor nos había recomendado Ignorando el agotamiento, fui a la biblioteca"
        jump bibloteca_general
    elif state == 2:
        narrador "El mundo se veía más claro, cuando la figura de ella esperando en la puerta, apareció en la visión de [povname]."

        povInside "Apenas notó que estaba ahí, no dije lo que le quería decir en realidad, sino lo que yo necesitaba." 
        pov "Lo decidí."
        jump Oficina_Cristian
    return
label pasillo_Uni:
    scene bg mainbuilding hallway with dissolve:
        xzoom 1.5
        yzoom 1.5
    if state == 0:
        povInside "Los pasillos del lugar estaban silenciosos, vacíos, ya que era tarde."
        jump entrada_Uni
    return
label bibloteca_general:
    scene bg library uni general with dissolve:
        xzoom 2
        yzoom 2.5
    if state == 0:
        povInside "huyendo de el gran frío del exterior, siendo recibido por una cálida temperatura ambiente apenas cruce la puerta, y viendo vacío, un lugar que comúnmente tenía un montón de gente estudiando."
        povInside "Abrí la puerta con cuidado, con intención de salir rápido, y apenas levanté la vista al mostrador, mi cuerpo se detuvo por instinto."
        povInside "Un breve vistazo bastó para detener mi atención en una sola persona."

        narrador "esa persona es Cristina, Una joven se encontraba detrás del mostrador, siendo la única persona en el lugar vacío."
        narrador "La joven de lentes, extrañamente familiar, sonreía con gracia viendo una lista, con un cabello ondulado mal amarrado,"
        narrador "y una camisa ajustada que moldeaba un gran busto."
        narrador "antes de que [povname] se de cuenta, una sonrisa pura y par de ojos brillantes se concentraron en su persona."

        povInside "Mi cuerpo se adormeció, ignorando el agotamiento de programación, mientras el sentimiento ausente de mi mente se evaporó, y todo comenzaba a sentirse mágico."
        povInside "Recién al final de ese día, me di cuenta que subía al mismo bus que yo."
        jump transiciones
    elif state == 2:
        pov "Lo hice."
        Cristi "Lo hiciste."
        pov "¿Fue lo correcto?"
        pov "Dependerá de ti…"
        povInside "Un pequeño gesto de tristeza se hizo presente en su cara, una conversación pendiente que debíamos tener en un futuro."
        povInside "Sin embargo, era algo que podría esperar ahora."
        povInside "Inmediatamente la vi sonreír, sabiendo que iba a comenzar otra de nuestras largas charlas que seguían hasta nuestro camino a casa."
        jump finales
    return
label biblioteca_mostrador:
    scene bg library uni base with dissolve:
        xzoom 1.5
        yzoom 1.5
    if state == 3:
        povInside "Fui con paso alegre, directo al mostrador."
    pov "Hola… Cris, tiempo sin verte."
    Cristi "Hola… Nos vimos ayer, sabes…"
    povInside "Ella se encontraba igual o más radiante, me había motivado a darle pequeñas pláticas a lo largo del día."
    povInside "Casi siempre era una conversación unilateral, con ella no pudiendo contestar más de una cosa, pero sin lugar a dudas fue mi momento más aliviante."
    povInside "Aunque en éste momento, sentí que fue todo lo contrario, ya que aunque estuviera hablando con ella normalmente, mi interior se estaba derrumbando por completo."
    povInside "Después de una plática pequeña, una parte de mí se animó a pedirle algo importante."
    pov "Bueno… ¿Podrías esperarme después de clase? Tengo algo que decirte…"
    Cristi "Yo… Supongo…"
    pov "Salgo a las 17:00… Es mi último parcial."
    Cristi "El último…"
    povInside "Al ver su cara dudosa, supe que quería decirme algo, así que espere un poco,"
    if state == 1:
        povInside "Al ver su cara dudosa, supe que quería decirme algo, así que espere un poco, así que espere un poco."
        povInside "En un momento subrealista, la chica callada salió del mostrador,"
        povInside "y me agarró de la muñeca, arrastrandome al área de libros"
        jump biblioteca_zona_libros
    if state == 3:
        povInside "Al ver su cara dudosa, supe que quería decirme algo, así que espere un poco, sin embargo, no dijo nada, hasta que momentos después sólo negó con la cabeza."
        povInside "Una familiar sonrisa pura vino a mí, y ante mi expresión confusa, una mueca de preocupación se posó en su rostro, sin embargo, no tocó el tema más allá."
        Cristi "Buena suerte."
        jump escaleras_dia
    return
label biblioteca_zona_libros:
    scene bg library uni pt1 with dissolve:
        xzoom 1.5
        yzoom 1.5
    if state == 1:
        narrador "esta área de libros es usualmente vacía, por lo que fueron para hablar a solas."
        narrador "[povname] no podia evitar hacerse ideas, al verla dudar tanto, sintiendo que la conversación de la tarde igual no iba a ser necesaria," 
        narrador "sin embargo, después de mucho tiempo, [povname] escuchó las palabras que estaba evitando pensar."

        Cristi "… Según vi, estabas investigando un cambio de carrera, ¿… Estás seguro?"

        povInside "Parpadeé con torpeza, completamente congelado ante esa afirmación."
        povInside "Y pronto, el sentimiento amargo que se había aliviado desde que la conocí, subió por mi garganta, recordando mi conversació más actual con el jefe de carrera."

        Cristi "¿no te gusta...?"

        povInside "No era eso."
        povInside "Aunque costaba mucho, era una carrera muy entretenida, sin embargo, habían varias cosas que seguían rondando en mi cabeza."
        povInside "Una presencia que me hizo cuestionar acerca de si todos mis logros eran eso, y no simplemente fracasos que me estaban llevando por un camino amargo."
        povInside "Aparte, el proceso de adaptación había sido bastante complicado, y quitando pequeños desahogos a lo largo del semestre, sentía que buena parte de la frustración seguía acomulandose ahí."
        povInside "Una pequeña presión constante, que hizo que el parcial fuera extrañamente importante."

        pov "Yo… Lo iba a considerar en esté parcial."
        Cristi "Mira… No sé tú situación y no hablé mucho contigo… Sin embargo… Por experiencia propia, a veces un cambio así no arregla tus problemas en realidad."

        povInside "Una afirmación bastante acertada."
        povInside "Al menos en la corta experiencia que estaba teniendo, una carrera universitaria consumía gran parte de mi vida y tiempo."
        povInside "Sin embargo, los problemas estaban ahí, aparte de la carrera."
        povInside "Nada me aseguraba que al cambiar de carrera, no cambiará nada, y acabará teniendo que de plano salir de la universidad."
        povInside "Al ver un bosquejo de confusión en mi cara, sentí su mano sobre la mía, y en ese momento me di cuenta que había estado temblando."
        povInside "Sentí mucha vergüenza, y trate de separarlas, pero ella las apretó."

        Cristi "Mira… No quisiera presionarte, pero si pasa algo, tienes mucha gente con la que podrías hablar de ello…"

        povInside "Un nudo en el pecho se me retorció, en realidad, sabía que nunca tendría esa confianza con nadie, solo me mordí el labio interno"

        pov "Yo…"
        Cristi "Si quieres, lo podrías hablar conmigo…"
        povInside "Ante esas palabras, la miré, y noté algo, estaba bastante nerviosa."
        povInside "En todo el tiempo que mi mente se llenaba de una tormenta de ideas, había pasado por alto el detalle de que cada palabra hacía mí, "
        povInside "equivalía al sentimiento de presentar en público."
        povInside "Aún así, una calidez llegó a mi interior, sabiendo que a pesar de eso, se había preocupado lo suficiente para abordarme aún cuando le costaba."
        povInside "El sentimiento dulce dominó fácilmente al amargo, seguía allí, sin embargo, no fue tan fuerte como la noche anterior."
        povInside "Incluso la existencia de esa persona se había aplacado un momento."
        povInside "En realidad, verla era un alivio que me motivaba a seguir, sin embargo, saber que también estaba ahí para mi, solo hizo que hubiera algo nuevo"
        pov "Cuando lo decida, te lo diré a ti"
        povInside "Era gratitud"
        povInside "Una familiar sonrisa pura vino a mí, y ante un claro sonrojo en mis mejillas, solo se rio."
        Cristi "Buena suerte… Te veo a las 17:00"
        jump transiciones
    return
label biblioteca_zona_escritorios:
    return
label sala_Programacion:
    scene bg classroom prog pt2 with dissolve:
        xzoom 1.5
    if state == 0:
        povInside "Sentí mis dientes apretarse, al ver en la terminal todos los errores que indicaba el compilador, en pleno control de programación."
        
        ProfKermin "Ya es hora, es todo por hoy, pueden retirarse..."
        ProfKermin "Prepárense para la parcial del jueves."
        
        povInside "Está vez, fueron mis propios puños los que se apretaron, al escuchar una voz suave hablar con sarcasmo, "
        povInside "mientras mi mente buscaba todo tipo de razones para no romper mi propia computadora, que seguía produciendo palabras repetidas"

        narrador "La sala estaba casi vacía, aparte de [povname], el profesor Kermin y un par de chicos, uno dormido, todos los demás compañeros se habían ido."

        povInside "Inserte mi nombre a regañadientes en el archivo en C."
        povInside "Era entendible, considerando mi propio estado, verías a una persona ojerosa y somnolienta, que llevaba en una incómoda silla con mala postura," 
        povInside "mirando una borrosa pantalla que se hacía más borrosa a cada momento."
        povInside "El estado mental fue ausente, se había ausentado desde que a los 30 minutos de clase, estaba seguro que habían pasado 3 horas, y era un error."
        povInside "Ignorando el dolor de hombros, forcé mis manos a apagar y guardar mi computador, y mis pies a levantarse."
        povInside "Sentí la mirada del profesor sobre mí, por lo que hice una pequeña pausa, antes de comenzar a caminar"
        jump pasillo_Uni
    elif state == 1:
        povInside "Comencé a dar la práctica en la prueba de programación, y con cada código, mi mente comenzó a maquetar todo en mi cabeza más fácil."
        povInside "Al final, dejé muchas alarmas, con una extraña sensación de satisfacción."
        jump escaleras_dia
    elif state == 2:
        povInside"Al cerrar la puerta fui directo a una computadora, y comencé a esperar el enunciado del código."
        povInside"Esto lo iba a decidir."
        povInside"No sabía si era nerviosismo, o el hecho de basar una decisión tan importante en un solo parcial, sin embargo, todo se sentía surrealista."
        povInside"Por un momento recordé, los momentos en la carrera, los frustrantes primeros rojos de mi vida, las amistades que hice, los momentos divertidos y estresantes, el cansancio y constante presión."
        povInside"Había sido una mezcla de experiencias, que habían mejorado a la persona del primer día, tal vez a golpes, pero era algo."
        ProfKermin "Los códigos están en la plataforma."
        jump sala_Programacion_C
    elif state == 3:
        povInside "Una decisión bastante importante iría después de esté parcial."
        povInside "Sentí que mi éxito en está carrera se iba a definir en éste momento, lo que hizo que la presión que me daba esa persona, siguiera allí aún cuando no estaba."
        ProfKermin "El problema está subido a la plataforma."
        povInside "No pude deshacer el nudo en mi garganta, sintiendo que faltaba algo importante."
        povInside "Apenas leí el problema, me di cuenta que no podía hacerlo."
        scene black with dissolve
        povInside "Sentí cómo todas las pequeñas frustraciones e ideas dominaron mi mente, la cuál, estaba tratando desesperadamente de ignorarlas y hacer el problema."
        povInside "Sin embargo, no podía."
        povInside "Era realmente triste que hiciera lo que hiciera, sin importar cuánto me esforzará en realidad, siguiera fracasando."
        povInside "Lo poco que sentía haber logrado aparte, era fácilmente mermado por un par de palabras de desaprobación."
        povInside "La presión de la universidad no ayudaba a lidiar con eso, y por eso había acabado así."
        povInside "Quería lidiar con todo solo, y no quería que todos creyeran que al final no servía."
        povInside "Desde el principio, solo todo fue simplemente una demostración inmadura para llevarle la contraria a esa persona."
        povInside "Y acabé fracasando."
        scene bg classroom prog pt2 with dissolve:
            xzoom 1.5
        povInside "Al final, acabé saliendo hasta el final de clases, sin poder haber hecho nada."
        povInside "Me fui a mi casa sin verla"
        jump Oficina_Cristian
    return
label sala_Programacion_C:
    if state == 2:
        povInside "Un repentino nerviosismo vino encima de mí, era un sentimiento bastante familiar que sucedía cada vez que tenía una mala calificación."
        povInside "Al abrir el problema, sentí mis manos temblar, un sentimiento de presión que hizo que quisiera ir a hablar en éste momento con el jefe de carrera."
        narrador "Sin embargo, unas simples de palabras lo detuvieron."
        Cristi "Si quieres, lo podrías hablar conmigo."
        povInside "Eso hizo que comenzará a bosquejar el problema en mi mente."
        povInside "En realidad, fue un último parcial bastante sencillo, al que me quedé hasta el final, a pesar de que todos mis compañeros abandonaron."
        povInside "Mi mente maquetó el código casi enseguida y mis dedos se movieron por instinto. "
        povInside "A pesar de todo, era verdad que independiente de mi decisión, mis múltiples caídas y la presión de esa persona, jamás lo iba a sentir está experiencia cómo un fracaso."
        povInside "Al final del parcial, salí de aquella sala con la espalda bastante más ligera que de costumbre."
        jump escaleras_noche
    return
label escaleras_dia:
    scene bg mainbuilding stairs pt1 with dissolve:
        xzoom 1.5
        yzoom 1.5
    if state == 1:
        povInside "Apenas salí de clase, me escabullí a la biblioteca."
        povInside "Fui con paso alegre, pasando por el familiar espacio de logias llenas de estudiantes, fui directo al mostrador."
        jump biblioteca_mostrador
    elif state == 2:
        narrador "[povname] comenzo a caminar hasta programacion, dónde el profesor lo esperaba con una sonrisa sádica."
        povInside "Kermin"
        jump sala_Programacion
    elif state == 3:
        povInside "Extrañado, comencé a caminar hasta programación, dónde el profesor me esperaba con una sonrisa sádica"
        jump sala_Programacion
    elif state == 4:
        povInside "No quería ver a mis amigos en éste momento, sintiendo un sentimiento desgarrador de fracaso."
        povInside "En realidad, a pesar de mis dudas, rendirse siempre se sentía mal después de todo."
        povInside "Sin embargo, no probaba que las palabras de esa persona fueran ciertas."
        jump finales
    return
label escaleras_noche:
    if state == 2:
        povInside "Había sido bastante satisfactorio a comparación de los anteriores, en los que acababa siempre sintiendo una gran frustración."
        povInside "Independiente de mi nota, mi realización había sido completa, por lo que estaba bien."
        jump entrada_Uni
    return
label Oficina_Cristian:
    scene black with dissolve
    show text "Epilogo" with Pause(1.5)
    scene black with dissolve
    narrador "Ante el final de la clase de introducción a la ingeniería, [povname] siguió al profesor al aula, debido a la conversación a inicio del semestre debido a éste tema."
    scene bg office uni pt1 with dissolve:
        xzoom 1.5
    ProfCris "Dime, a qué conclusión llegaste."
    narrador "Una suave sonrisa se posó en el jefe de carrera."
    menu Quedate_o_fuera:
        "Yo..."
        "Voy a quedarme":
            $ Quedarse = True
            $ switch = 5
            ProfCris "¿Qué te convenció?"

            pov "En realidad, disfruté bastante de programación esté semestre, creo que me gusta resolver problemas usando la lógica."

            ProfCris "Tú concéntrate en pasar, siempre puedes venir a verme y tomarte un té."

            pov "Gracias"

            povInside "Sentí una sonrisa en mi cara, y un peso menos en el pecho, en realidad, todo se sentía más bien que hacía unos días."
            povInside "En realidad acabé descubriendo mi pasión."
            narrador "Con ese alivio en el pecho, [povname] se dirigío a la biblioteca con pasos animados, dónde Cristina lo esperaba con una sonrisa."
            jump bibloteca_general
        "Voy a irme":
            $ Quedarse = False
            $ state = 4
            ProfCris "¿Al final fue eso?"
            pov "No creo que está ingeniería sea algo para mí."
            ProfCris "Entiendo, fue un placer tenerte aquí."
            pov"Gracias."
            narrador "[povname] se dirigía al frente con pasos decaídos, pero seguros."
            
            jump escaleras_dia
    return
label transiciones:
    scene black with dissolve
    if Seleccion == 0:
        $ Seleccion = 10
        show text "Capítulo único \n 'Programación'" with Pause(1.5)
        jump casaDelProta
    elif Seleccion == 1:
        show text "5 meses despues" with Pause(1.5)
        $ Seleccion = 0
        $ prologo = False
        jump sala_Programacion
    elif Seleccion == 2:
        jump finales
    elif rutaBuena and switch == 0:
        $ switch = 1
        jump sala_Programacion
    elif rutaBuena and switch == 1:
        $ state = 2
        jump escaleras_dia
    elif rutaMala and switch == 0:
        $ switch = 1
        povInside "Apenas salí de clase ese día, me escabullí a la biblioteca"
        jump biblioteca_mostrador
    return
label finales:
    scene black with dissolve
    if Seleccion == 2:
        show text "Final: Te salvaste" with Pause(1.5)
        show text "Felicidades?" with Pause(1.5)
    elif Quedarse:
        povInside "Una paz bastante temporal, sabiendo que era apenas mi primer semestre de ingeniería, sin embargo, me sentía aún más preparado para el segundo de lo que podría esperar."
        show text "Final: “Bienvenido a la carrera y buena suerte”" with Pause(1.5)
    else:
        pov "Mi futuro dependía de mí, después de todo."
        pov "Tal vez jamás iba a ser el futuro que había imaginado, iba a ser un futuro distinto, pero me aseguraría que al fin y al cabo, fuera uno con el que estuviera feliz."
        pov "Uno por el que sentía que valía la pena luchar."
        
        show text "Final: “Buena suerte en lo que decidas”" with Pause(1.5)

    return