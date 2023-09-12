# Pygame

## Descripción del proyecto

El proyecto es un juego de batalla espacial en el que dos naves espaciales, una amarilla y una roja, compiten por eliminar la vida de la otra. El juego se desarrolla en una ventana con un fondo espacial y un límite en el centro que separa a las dos naves.

- **Primer jugador:** Puede moverse con las teclas: W (ARRIBA), A (IZQUIERDA), D (DERECHA) y S (ABAJO), y dispara con ALT.
- **Segundo jugador:** Utiliza las teclas de flecha (arriba, abajo, izquierda y derecha) y dispara con Ctrl.

## Funcionalidad

1. **Configuración de la ventana y colores:** Se configura la ventana de juego con el tamaño deseado y un título atractivo. Además, se definen colores que se usarán a lo largo del juego.

2. **Dibujar menú:** Se incorpora un menú interactivo que se puede mostrar u ocultar con la tecla "Escape". Dentro del menú, encontrarás botones que te permiten reiniciar el juego o salir si lo deseas.

3. **Dibujar ventana:** La ventana de juego es donde ocurre la acción. Aquí se representan las naves espaciales, el fondo del espacio profundo, los límites, la salud de las naves y los disparos de proyectiles.

4. **Manejo de movimiento de naves:** Controlar las naves es fundamental. Para la nave amarilla, usa las teclas W (arriba), A (izquierda), S (abajo) y D (derecha). Para la nave roja, utiliza las teclas de flecha.

5. **Manejo de balas:** ¡No te olvides de disparar! Puedes lanzar proyectiles pulsando Ctrl izquierdo para la nave amarilla y Ctrl derecho para la nave roja. Sin embargo, ten en cuenta que hay un límite de balas en el aire, ¡así que administra tus disparos sabiamente! Las balas se mueven a gran velocidad y pueden dañar a las naves enemigas.

6. **Manejo de eventos:** A medida que las balas vuelan por el espacio, pueden colisionar con las naves enemigas. Cuando eso sucede, el juego maneja las colisiones y reduce la salud de las naves. Además, se atienden eventos como el cierre de la ventana del juego y las interacciones con el menú.

7. **Gestión del estado del juego:** El juego lleva un registro de la salud de las naves y determina un ganador cuando una de ellas se queda sin vida. Si lo deseas, puedes reiniciar el juego desde el menú, lo cual es útil si deseas una revancha.

8. **Bucle principal:** El corazón del juego late en un bucle principal que actualiza el juego a una velocidad constante de 60 fotogramas por segundo. Aquí es donde toda la acción tiene lugar hasta que decides salir.

9. **Función principal:** La función principal del juego se llama `main()`. Actúa como el director de la orquesta, supervisando todos los aspectos del juego, desde el movimiento de las naves hasta el manejo de las balas y la determinación de los ganadores.

En resumen, te embarcas en un emocionante enfrentamiento espacial mientras intentas superar a tu oponente y asegurarte de que tu nave espacial llegue a casa en una sola pieza. ¡Diviértete explorando las estrellas y ganando la batalla!
