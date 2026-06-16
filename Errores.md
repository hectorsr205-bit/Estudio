E401 [*] Multiple imports on one line
 --> juego_rec (1).py:1:1
  |
1 | import random, os, sys
  | ^^^^^^^^^^^^^^^^^^^^^^
  |
help: Split imports

F401 [*] `os` imported but unused
 --> juego_rec (1).py:1:16
  |
1 | import random, os, sys
  |                ^^
  |
help: Remove unused import

F401 [*] `sys` imported but unused
 --> juego_rec (1).py:1:20
  |
1 | import random, os, sys
  |                    ^^^
  |
help: Remove unused import

F841 Local variable `mensaje_sobre_el_juego` is assigned to but never used
  --> juego_rec (1).py:12:9
   |
11 |     def elegir( self ):
12 |         mensaje_sobre_el_juego = "Este mensaje se ha añadido para que el jugador pueda entender el juego de piedra papel y tijera con …
   |         ^^^^^^^^^^^^^^^^^^^^^^
13 |         eleccion=input(f"{self.nombre}, elige piedra, papel o tijera: ").lower()
14 |         while eleccion not in OPCIONES_VALIDAS:
   |
help: Remove assignment to unused variable `mensaje_sobre_el_juego`

F841 Local variable `numero_aleatorio` is assigned to but never used
  --> juego_rec (1).py:26:9
   |
25 |     def elegir( self ):
26 |         numero_aleatorio = random.randint(1, 100)
   |         ^^^^^^^^^^^^^^^^
27 |         return random.choice(OPCIONES_VALIDAS)
   |
help: Remove assignment to unused variable `numero_aleatorio`

F841 Local variable `resultado_temporal` is assigned to but never used
  --> juego_rec (1).py:36:9
   |
35 |     def determinar_ganador( self,eleccion_jugador,eleccion_ordenador ):
36 |         resultado_temporal = None
   |         ^^^^^^^^^^^^^^^^^^
37 |         if eleccion_jugador==eleccion_ordenador: return "Empate"
38 |         elif ((eleccion_jugador=="piedra" and eleccion_ordenador=="tijera") or (eleccion_jugador=="papel" and eleccion_ordenador=="pie…
   |
help: Remove assignment to unused variable `resultado_temporal`

E701 Multiple statements on one line (colon)
  --> juego_rec (1).py:37:48
   |
35 |     def determinar_ganador( self,eleccion_jugador,eleccion_ordenador ):
36 |         resultado_temporal = None
37 |         if eleccion_jugador==eleccion_ordenador: return "Empate"
   |                                                ^
38 |         elif ((eleccion_jugador=="piedra" and eleccion_ordenador=="tijera") or (eleccion_jugador=="papel" and eleccion_ordenador=="pie…
39 |             return f'{self.jugador.nombre} gana!!'
   |

E702 Multiple statements on one line (semicolon)
  --> juego_rec (1).py:55:34
   |
54 | def mostrar_menu( ):
55 |     print("\n------ Menú ------"); print("1. Jugar"); print("2. Salir")
   |                                  ^
   |

E702 Multiple statements on one line (semicolon)
  --> juego_rec (1).py:55:53
   |
54 | def mostrar_menu( ):
55 |     print("\n------ Menú ------"); print("1. Jugar"); print("2. Salir")
   |                                                     ^
   |

Found 9 errors.