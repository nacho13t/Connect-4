# Connect_4

Autores:                                                                                                                 Ignacio Alfonso Brito                                                                                                    Gabriel García Buey

Connect 4 basa su funcionamiento principalmente en los tres archivos games.py, heuristicas.py y run.py. El fichero game es donde se encuentran implementados los algoritmos de búsuqeda así como las clases Game, Tictactoe (tres en raya) y ConnectFour que repesentan los juegos que responden a tales nombres (salvo Game que es una clase abstracta más general). El fichero games.py fue aportado por nuestro profesor y nosotros apenas lo hemos modificado. Simplemente hemos añadido esta porción de código a la función alphabeta_search para que cuando el algoritmo de búsqueda pueda seleccionar un estado ganador lo seleccione:

for (x, y) in lista:
        if game.utility(y, player) > 0:
                return x

También modificamos la invocación a las heurísticas para que cumpliese con los parámetros que exigen: state y player. El state lo necesitan para poder valorar el estado y el parámetro player lo necesitan para saber qué fichas son las suyas y que las heurísticas se adapten dinámicamente a cualquier configuración de juego sin tener que estar modificando el código.

En cuanto a las heurísticas se puede observar que, cuando se introduce una IA en el juego, se pueden seleccionar 5 dificultades, que corresponden a una heurística distinta cada uno. La última (custom) corresponde a cualquier otra heurística externa que se quiera probar en nuestro Connect 4; para probarla simplemente tiene que pegar el código de la heurística dentro de la función custom en el fichero heuristicas.py. Las otras dificultades corresponden a heurísticas implementadas por nosotros: 

Regalado = heuristicas.h0
Easy = heuristicas.h1
Medium = heuristicas.h6
Hard = heuristicas.h7

La heuristíca h0 juega sin ningún tipo de estrategia, de manera totalmente aleatoira y sin tener en cuenta siquiera si el contrario o ella misma pueden ganar (de ahí el nombre de su dificultad).

La heurística h1 es igual a la h0 con la diferencia de que si puede ganar lo hace y si va a perder lo evita. Está en el nivel fácil porque, al no seguir una estrategia pero por lo menos preocuparse de no perder y de ganar si puede, impulsa al jugador a buscar una estrategia que consiga hacer 4 en raya en al menos dos sitios al mismo tiempo. Si no lo hace así la heurística simplemente le bloqueará.

La heurística h6 parte de un valor inicial de 1000, primero se comprueba que el estado sea final o no, de manera que se le añade o resta 10000 en función de si la máquina gana o no. Luego se hace una especie de filtrado, donde restamos puntuación a aquellos tableros donde no se juegue por el medio y damos mayor puntuación a aquellos donde hay más fichas propias por las columnas centrales del tablero. Después analizamos cómo están situadas las fichas en los tableros, dando menor puntuación a aquellos donde el contrario tenga fichas alineadas y más puntuación donde la máquina tenga más fichas alineadas, tanto en filas como en columnas. Al seguir una estrategia de acumular fichas contiguas y darle prioridad al centro, esta heurística se encuentra en la dificultad media porque supone cierto reto para el jugador.

Por último, la heurística h7 es la heurística que mejor juega, la estrategia que sigue es la construcción de trampas, es decir, estructuras de fichas en las que si el contrario coloca una ficha en determinadas casillas pierde. Estructuras de este estilo:
                 
                                                                   X
                                                                  X-
                                                                 X--
                                                  .XXX.         ·---    
                                                  ·---·         ·---
Donde:
· -> Casilla vacía
X -> Ficha propia
- -> Ficha cualquiera (obviamente que no resulte una combinación ganadora)

Para conseguirlo simplemente explora las casillas en las que se puede mover y comprueba que en la casilla inmediatamente por encima de ellas hayan al menos 3 fichas propias contiguas en horizontal o en diagonal. De esta manera, el algoritmo de búsqueda tiende a seleccionar estados en los que haya más disposiciones de este estilo. También se le dan puntuacion negativas a los tableros en los que el oponente disponga de trampas, pero dándole una pequeña prioridad a la construcción de trampas propias. Por la estrategia que sigue y, dado que el algoritmo de búsqueda explora todas la posibilidades en los siguientes 4 movimientos, esta heurística se encuentra en el nivel difícil.
