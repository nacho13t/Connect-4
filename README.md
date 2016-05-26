# Connect-4 

h6
La heurística parte de un valor inicial de 1000, primero se comprueba que el estado sea final o no, de manera que se le añade o resta 10000 en función de si la máquina gana o no. Luego se hace una especie de filtrado, donde restamos puntuación a aquellas partidas donde no se juegue por el medio y damos mayor puntuación a aquellas donde hay más fichas propias por las columnas centrales del tablero.
Después analizamos los tableros, dando menor puntuación a aquellos donde el contrario tenga fichas alineadas y más puntuación donde la máquina tenga más fichas alineadas, tanto en filas como en columnas.
