# tema: color your night
label casa:
    stop audio fadeout 0.5
    play music audio.ColorYourNight fadeout 0.5 volume 0.25 loop
    scene bg house at backgroundZoom(1.5,1.5)
    show s_dario at right
    narrador "La parcial de programación llegó en un reglón, siendo un evento bastante importante. Era la oportunidad perfecta, para saber que [povname] está por hacer la decisión era correcta."
    hide s_dario with dissolve
    menu Buena_O_Mala:
        "¿Teoria o Practica?"
        "Practica":
            $ rutaBuena = True
        "Teoria":
            $ rutaMala = True
    jump transiciones
# tema: nothing can be explained
label sala_prog:
    stop music
    play music audio.nothingCanBeExplained fadein 0.5 volume 0.25
    scene bg classroom prog at backgroundZoom(1.0,1.5)
    if estado == 1 and rutaBuena:
        pov "Comencé a dar la práctica en la prueba de programación, y con cada código, mi mente comenzó a maquetar todo en mi cabeza más fácil."
        pov "Al final, dejé muchas alarmas, con una extraña sensación de satisfacción"
        jump escaleras_dia
    elif estado == 1 and rutaMala:
        pov "Comencé a dar la teoría en la prueba de programación, al final, decidí ignorar una clara sensación de confusión."
        scene black with dissolve
        "Apenas sali de clase ese dia, me escabullí a la biblioteca"
        jump biblioteca_base
    elif estado == 2 and rutaBuena:
        """Al cerrar la puerta fui directo a una computadora, y comencé a esperar el enunciado del código.
        
        Esto lo iba a decidir.
        
        No sabía si era nerviosismo, o el hecho de basar una decisión tan importante en un solo parcial, sin embargo, todo se sentía surrealista.
        
        Por un momento recordé, los momentos en la carrera, los frustrantes primeros rojos de mi vida, las amistades que hice, los momentos divertidos y estresantes, el cansancio y constante presión.
        
        Había sido una mezcla de experiencias, que habían mejorado a la persona del primer día, tal vez a golpes, pero era algo."""
        show s_kermit at zoomAndAlign(1.75,0.0) 
        kermit "Los códigos están en la plataforma."
        # minijuego
        """Un repentino nerviosismo vino encima de mí, era un sentimiento bastante familiar que sucedía cada vez que tenía una mala calificación.
        
        Al abrir el problema, sentí mis manos temblar, un sentimiento de presión que hizo que quisiera ir a hablar en éste momento con el jefe de carrera.

        Sin embargo, un simple par de palabras me detuvieron."""
        cristi "Si quieres, lo podrías hablar conmigo."
        
        """Eso hizo que comenzará a bosquejar el problema en mi mente.
        
        En realidad, fue un último parcial bastante sencillo, al que me quedé hasta el final, a pesar de que todos mis compañeros abandonaron.
        
        Mi mente maquetó el código casi enseguida y mis dedos se movieron por instinto. 
        
        A pesar de todo, era verdad que independiente de mi decisión, mis múltiples caídas y la presión de esa persona, jamás lo iba a sentir está experiencia cómo un fracaso.
        
        Al final del parcial, salí de aquella sala con la espalda bastante más ligera que de costumbre."""
        $ estado = 3
        jump escaleras_dia
    elif estado == 2 and rutaMala:
        """Una decisión bastante importante iría después de esté parcial.
        
        Sentí que mi éxito en está carrera se iba a definir en éste momento, lo que hizo que la presión que me daba esa persona, siguiera allí aún cuando no estaba."""
        show s_kermit at zoomAndAlign(1.75,0.0) 
        kermit "El problema está subido a la plataforma."
        "No pude deshacer el nudo en mi garganta, sintiendo que faltaba algo importante.
        Apenas leí el problema, me di cuenta que no podía hacerlo."
        scene black with dissolve
        """Sentí cómo todas las pequeñas frustraciones e ideas dominaron mi mente, la cuál, estaba tratando desesperadamente de ignorarlas y hacer el problema.
        Sin embargo, no podía.

        Era realmente triste que hiciera lo que hiciera, sin importar cuánto me esforzará en realidad, siguiera fracasando.
        Lo poco que sentía haber logrado aparte, era fácilmente mermado por un par de palabras de desaprobación.

        La presión de la universidad no ayudaba a lidiar con eso, y por eso había acabado así.
        Quería lidiar con todo solo, y no quería que todos creyeran que al final no servía.

        Desde el principio, solo todo fue simplemente una demostración inmadura para llevarle la contraria a esa persona.
        Y acabé fracasando"""
        scene bg classroom prog at backgroundZoom(1.0,1.5)
        "Al final, acabé saliendo hasta el final de clases, sin poder haber hecho nada.Me fui a mi casa sin verla"
        jump oficina_cristian
# temas: once upon a time
label entrada:
    $ current_song = renpy.music.get_playing(channel='music')
    if current_song != './audio/Once Upon a Time.mp3':
        stop music
        play music audio.OnceUponAtime
    scene bg entrance at backgroundZoom(1.12,1.5)
    if estado == 3 and rutaBuena:
        """El mundo se veía más claro, cuando la figura de ella esperando en la puerta, apareció en mi visión.

        Apenas notó que estaba ahí, no dije lo que le quería decir en realidad, sino lo que yo necesitaba."""

        pov "Lo decidí."
        jump oficina_cristian
label pasillo:
    $ current_song = renpy.music.get_playing(channel='music')
    if current_song != './audio/Once Upon a Time.mp3':
        stop music
        play music audio.OnceUponAtime
    scene bg mainbuilding hallway at backgroundZoom(1.25,1.5)
    
label escaleras_dia:
    $ current_song = renpy.music.get_playing(channel='music')
    if current_song != './audio/Once Upon a Time.mp3':
        stop music
        play music audio.OnceUponAtime
    scene bg mainbuilding stairs at backgroundZoom(1.12,1.5)
    if estado == 1 and rutaBuena:
        pov "Apenas salí de clase, me escabullí a la biblioteca."
        pov "Fui con paso alegre, pasando por el familiar espacio de logias llenas de estudiantes, fui directo al mostrador."
        jump biblioteca_base
    elif estado == 2 and rutaBuena:
        "Comencé a caminar hasta programación, dónde el profesor me esperaba con una sonrisa sádica."
        jump sala_prog
    elif estado == 3 and rutaBuena:
        """Había sido bastante satisfactorio a comparación de los anteriores, en los que acababa siempre sintiendo una gran frustración.
        
        Independiente de mi nota, mi realización había sido completa, por lo que estaba bien."""
        jump entrada
    elif estado == 1 and rutaMala:
        "Extrañado, comencé a caminar hasta programación, dónde el profesor me esperaba con una sonrisa sádica."
        $ estado = 2
        jump sala_prog
label escaleras_final:
    scene bg mainbuilding stairs at backgroundZoom(1.12,1.5)
    if not seguir and rutaMala:
        """No quería ver a mis amigos en éste momento, sintiendo un sentimiento desgarrador de fracaso.

        En realidad, a pesar de mis dudas, rendirse siempre se sentía mal después de todo.

        Sin embargo, no probaba que las palabras de esa persona fueran ciertas."""
        jump finales
# tema: with a smile
label oficina_cristian:
    stop music
    play music audio.WithASmile
    scene black with dissolve
    "Ante el final de la clase de introducción a la ingeniería, seguí al profesor al aula, debido a la conversación a inicio del semestre debido a éste tema."
    scene bg mainbuilding office at backgroundZoom(1.05,1.25)
    show s_cristian at zoomAndAlign(2.0,1.0)
    cristian "Dime, a qué conclusión llegaste."
    "Una suave sonrisa se posó en el jefe de carrera."
    stop music fadeout 1.5
    menu finalEl:
        "Yo..."
        "Voy a quedarme":
            $ final = True
            $ seguir = True
            if rutaBuena:
                play music audio.IReallyWantYou volume 0.25
            else:
                play music audio.StayWithMe fadein 0.25
            cristian "¿Qué te convenció?"
            pov"En realidad, disfruté bastante de programación esté semestre, creo que me gusta resolver problemas usando lalógica."
            cristian"Tú concéntrate en pasar, siempre puedes venir a verme y tomarte un té."
            pov "Gracias."

            """Sentí una sonrisa en mi cara, y un peso menos en el pecho, en realidad, todo se sentía más bien que hacía unosdías.
            
            En realidad acabé descubriendo mi pasión.
            
            Con ese alivio en mi pecho, me dirigí a la biblioteca con pasos animados""" 
            if rutaBuena:
                "dónde Cristina me esperó con una sonrisa"
            jump biblioteca_general_2
        "Voy a irme":
            $ final = True
            $ seguir = False
            pov "Me voy a ir..."
            cristian "¿Al final fue eso?"
            pov "No creo que está ingeniería sea algo para mí."
            cristian "Entiendo, fue un placer tenerte aquí."
            pov "Gracias."
            if rutaMala:
                play music audio.LastGoodbye volume 0.25
                "Me dirigí al frente con pasos decaídos, pero seguros."
                jump escaleras_final
            elif rutaBuena:
                play music audio.NextToYou volume 0.25
                "Me dirigí al frente con pasos decaídos, pero seguros y una despedida a Cristina"
                jump finales
# tema: sunset bridge
label biblioteca_base:
    $ current_song = renpy.music.get_playing(channel='music')
    if current_song != 'audio/Sunset Bridge.mp3':
        stop music
        play music audio.SunsetBridge volume 0.25
    scene bg library base at backgroundZoom(1.15,1.5)
    if rutaMala:
        "Fui con paso alegre, directo al mostrador"
    pov "Hola… Cris, tiempo sin verte."
    show s_cristina at zoomAndAlign(2.0,1.0)
    stop music
    play music audio.StillLoveYou volume 0.25
    cristi "Hola… Nos vimos ayer, sabes…"
    pov """Ella se encontraba igual o más radiante, me había motivado a darle pequeñas pláticas a lo largo del día.

    Casi siempre era una conversación unilateral, con ella no pudiendo contestar más de una cosa, pero sin lugar a dudas fue mi momento más aliviante.

    Aunque en éste momento, sentí que fue todo lo contrario, ya que aunque estuviera hablando con ella normalmente, mi interior se estaba derrumbando por completo.

    Después de una plática pequeña, una parte de mí se animó a pedirle algo importante."""

    pov "Bueno… ¿Podrías esperarme después de clase? Tengo algo que decirte…"

    cristi "Yo… Supongo…"
    pov "Salgo a las 17:00… Es mi último parcial."
    cristi concern "El último…"

    if estado == 1 and rutaBuena:
        "Al ver su cara dudosa, supe que quería decirme algo, así que espere un poco."
        "En un momento subrealista, la chica callada salió del mostrador, y me agarró de la muñeca, arrastrandome al área de libros"
        jump biblioteca_books
    elif estado == 1 and rutaMala:
        """Al ver su cara dudosa, supe que quería decirme algo, así que espere un poco, sin embargo, no dijo nada, 
        hasta que momentos después sólo negó con la cabeza."""
        show s_cristina at zoomAndAlign(2.0,1.0)
        """Una familiar sonrisa pura vino a mí, y ante mi expresión confusa, una mueca de preocupación se posó en su rostro, 
        sin embargo, no tocó el tema más allá."""
        cristi "Buena suerte."
        jump escaleras_dia

label biblioteca_general:
    $ current_song = renpy.music.get_playing(channel='music')
    if current_song != 'audio/Sunset Bridge.mp3':
        stop music
        play music audio.SunsetBridge volume 0.25
    scene bg library general pt1 at backgroundZoom(1.13,1.5)
label biblioteca_general_2:
    if rutaBuena and final:
        scene bg library general pt2 at backgroundZoom(2.5,1.5) 
        show s_cristina at zoomAndAlign(2.0,1.0)
        show s_prota
        pov "Lo hice."
        cristi "Lo hiciste."
        pov "¿Fue lo correcto?"
        pov "Dependerá de ti…"
        show s_cristina concern at zoomAndAlign(2.0,1.0)
        """Un pequeño gesto de tristeza se hizo presente en su cara, una conversación pendiente que debíamos tener en un futuro.

        Sin embargo, era algo que podría esperar ahora.

        Inmediatamente la vi sonreír, sabiendo que iba a comenzar otra de nuestras largas charlas que seguían hasta nuestro camino a casa."""
    elif rutaMala and final:
        scene black with dissolve
        """ mientras estaba de camino a la biblioteca, una parte de mi esperaba que ella esté ahí, pero...
        
        por otra parte de mi sabia que no estaria ahí.
        """
        scene bg library general pt2 at backgroundZoom(2.5,1.5)
        show s_dario at right
        stop music fadeout 0.25
        play music audio.OceanOfMemories
        
        narrador """[povname] fue a la biblioteca, pero no vio a Cristina.

        en un momento la motivacion de [povname] se fue desvaneciendo de a poco, pero sin dudar y habiendo decidido a seguir con la carrera queria remontar el semestre y pasar
        """
    jump finales
label biblioteca_books:
    $ current_song = renpy.music.get_playing(channel='music')
    scene bg library books at backgroundZoom(1.13,1.5)
    if estado == 1:
        stop music
        play music audio.FruitBasket volume 0.25
        show s_cristina at zoomAndAlign(2.0,1.0)
        "El área de libros estaba normalmente vacía, por lo que fueron para hablar a solas."
        "No pude evitar hacerme ideas, al verla dudar tanto, sintiendo que la conversación de la tarde igual no iba a ser necesaria, sin embargo, después de mucho tiempo, escuché las palabras que estaba evitando pensar."
        cristi concern "… Según vi, estabas investigando un cambio de carrera, ¿… Estás seguro?"
        """Parpadeé con torpeza, completamente congelado ante esa afirmación.

        Y pronto, el sentimiento amargo que se había aliviado desde que la conocí, subió por mi garganta, 
        recordando mi conversación más actual con el jefe de carrera."""
        cristi concern "¿No te gusta…?"
        pov """No era eso.
        Aunque costaba mucho, era una carrera muy entretenida, sin embargo, habían varias cosas que seguían rondando en mi cabeza.

        Una presencia que me hizo cuestionar acerca de si todos mis logros eran eso, y no simplemente fracasos que me estaban llevando por un camino amargo.
        
        Aparte, el proceso de adaptación había sido bastante complicado, y quitando pequeños desahogos a lo largo del semestre, 
        sentía que buena parte de la frustración seguía acomulandose ahí."""
        "Una pequeña presión constante, que hizo que el parcial fuera extrañamente importante."
        pov "Yo… Lo iba a considerar esté parcial."
        cristi "Mira… No sé tú situación y no hablé mucho contigo… Sin embargo… Por experiencia propia, a veces un cambio así no arregla tus problemas en realidad."
        """Una afirmación bastante acertada.

        Al menos en la corta experiencia que estaba teniendo, una carrera universitaria consumía gran parte de mi vida y tiempo.
        Sin embargo, los problemas estaban ahí, aparte de la carrera.
        
        Nada me aseguraba que al cambiar de carrera, no cambiará nada, y acabará teniendo que de plano salir de la universidad.
        
        Al ver un bosquejo de confusión en mi cara, sentí su mano sobre la mía, y en ese momento me di cuenta que había estado temblando.
        
        Sentí mucha vergüenza, y trate de separarlas, pero ella las apretó."""
        cristi "Mira… No quisiera presionarte, pero si pasa algo, tienes mucha gente con la que podrías hablar de ello…"
        "Un nudo en el pecho se me retorció, en realidad, sabía que nunca tendría esa confianza con nadie, solo me mordí el labio interno."
        pov "Yo..."
        cristi "Si quieres, lo podrías hablar conmigo…"
        """Ante esas palabras, la miré, y noté algo, estaba bastante nerviosa.

        En todo el tiempo que mi mente se llenaba de una tormenta de ideas, había pasado por alto el detalle de que cada palabra hacía mí, 
        equivalía al sentimiento de presentar en público.

        Aún así, una calidez llegó a mi interior, sabiendo que a pesar de eso, se había preocupado lo suficiente para abordarme aún cuando le costaba.
        
        El sentimiento dulce dominó fácilmente al amargo, seguía allí, sin embargo, no fue tan fuerte como la noche anterior.
        
        Incluso la existencia de esa persona se había aplacado un momento.
        
        En realidad, verla era un alivio que me motivaba a seguir, sin embargo, saber que también estaba ahí para mi, solo hizo que hubiera algo nuevo.
        """
        cristi "Cuando lo decida, te lo diré a ti."
        "Era gratitud."
        "Una familiar sonrisa pura vino a mí, y ante un claro sonrojo en mis mejillas, solo se rio"
        pov "Buena suerte… Te veo a las 17:00."
        jump transiciones
label transiciones:
    scene black with dissolve
    if estado == 0:
        $ estado = 1
        jump sala_prog
    elif rutaBuena and estado == 1:
        $ estado = 2
        jump escaleras_dia
label finales:
    scene black with dissolve
    if Opcion1 == 2:
        stop music fadeout 0.5
        play music audio.Salvation noloop
        show text "Final:\n 'te salvaste'" with Pause(10)
    if final:
        if seguir and rutaBuena:
            # fondo entrada con cristina
            "Una paz bastante temporal, sabiendo que era apenas mi primer semestre de ingeniería, sin embargo, me sentía aún más preparado para el segundo de lo que podría esperar."
            play music audio.TitleEffect noloop
            show text "Final: \n“Bienvenido a la carrera, buena suerte”" with Pause(5)
        elif not seguir and rutaMala:
            """Mi futuro dependía de mí, después de todo.

            Tal vez jamás iba a ser el futuro que había imaginado, iba a ser un futuro distinto, pero me aseguraría que al fin y al cabo, 
            fuera uno con el que estuviera feliz.
            
            Uno por el que sentía que valía la pena luchar."""
            play music audio.TitleEffect noloop
            show text "Final:\n “Buena suerte en lo que decidas”" with Pause(5)
        elif not seguir and rutaBuena:
            pov """
            Mi futuro dependía de mí, después de todo.

            Tal vez jamás iba a ser el futuro que había imaginado, iba a ser un futuro distinto, pero me aseguraría que al fin y al cabo, fuera uno con el que estuviera feliz.
        
            Uno por el que sentía que valía la pena luchar.
            """
            show s_dario at zoomAndAlign(1.0,1.0)
            narrador "[povname] habiendo decidido su futuro, decidido aunque algo decaido se fue de la universidad"
            hide s_dario
            play audio audio.TitleEffect volume 0.5
            show text "Final: \n“Buena suerte en tu futuro”" with Pause(3)
        elif seguir and rutaMala:
            # fondo biblioteca
            show s_dario at zoomAndAlign(1.0,1.0)
            narrador """
            Una paz bastante temporal, [povname] sabiendo que era apenas su primer semestre de ingeniería, sin embargo, se sentía aún más preparado para el segundo de lo que podría esperar.
        
            [povname] seguira su pasion.
            """
            hide s_dario
            play audio audio.TitleEffect volume 0.5
            show text "Final: \n“se viene remontada”" with Pause(3)
    return