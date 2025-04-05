def calcular_puntaje(kills, assists, deaths):
    '''Calcula el puntaje de un jugador basado en sus estadísticas y los puntajes predeterminados.'''
    muertes = 1 if deaths else 0
    return kills * 3 + assists * 1 - muertes * 1, muertes

def ejecutar_simulacion(rounds):
    '''Ejecuta la simulación de las rondas y calcula el puntaje total de cada jugador.'''
    totales = {}
    # Iterar sobre cada ronda y calcular el puntaje de cada jugador
    for ronda_num, ronda in enumerate(rounds, 1):
        print(f"\nRanking ronda {ronda_num}")
        ronda_resultado = {}
        max_puntos = -999
        mvp = None

        for jugador, stats in ronda.items():
            kills = stats['kills']
            assists = stats['assists']
            puntos, muertes = calcular_puntaje(kills, assists, stats['deaths'])

            ronda_resultado[jugador] = {
                'kills': kills,
                'assists': assists,
                'muertes': muertes,
                'puntos': puntos
            }
            # Identificar al jugador con más puntos
            if puntos > max_puntos:
                max_puntos = puntos
                mvp = jugador
        
        
        # Mostrar el MVP de la ronda
        if mvp is not None:
            print(f"MVP de la ronda: {mvp}")
        else:
            print("No hay MVP en esta ronda.")
        #print(f"MVP de la ronda: {mvp}")
        
        # Mostrar el ranking de la ronda
        print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<11} {'Muertes':<8} {'Puntos':<6}")
        print("-" * 50)
        
        # Ordenar el ranking de la ronda almacenando los jugadores en un diccionario
        # y ordenando por puntos, kills, assists, muertes y nombre
        for jugador, datos in sorted(ronda_resultado.items(), key=lambda x: (-x[1]['puntos'], -x[1]['kills'], -x[1]['assists'], x[1]['muertes'], x[0])):
            # Mostrar el ranking de la ronda
            print(f"{jugador:<10} {datos['kills']:<6} {datos['assists']:<11} {datos['muertes']:<8} {datos['puntos']:<6}")
          
            
        # Actualizar las estadísticas totales de cada jugador
            if jugador not in totales:
                # Inicializar las estadísticas totales del jugador
               totales[jugador] = {'kills': 0, 'assists': 0, 'muertes': 0, 'puntos': 0, 'mvps': 0}
               
            # Actualizar las estadísticas totales del jugador
            totales[jugador]['kills'] += datos['kills']
            totales[jugador]['assists'] += datos['assists']
            totales[jugador]['muertes'] += datos['muertes']
            totales[jugador]['puntos'] += datos['puntos']

        totales[mvp]['mvps'] += 1

    return totales


# Ordenar y mostrar el ranking global
def mostrar_ranking_global(totales):
    print("\nRanking final:")
    print(f"{'Jugador':<10} {'Kills':<6} {'Asistencias':<11} {'Muertes':<8} {'MVPs':<6} {'Puntos':<6}")
    print("-" * 60)
    # Ordenar el ranking global
    for jugador, datos in sorted(totales.items(), key=lambda x: (-x[1]['puntos'], -x[1]['kills'], -x[1]['assists'], x[1]['muertes'], x[0])):
        # Mostrar el ranking global
        print(f"{jugador:<10} {datos['kills']:<6} {datos['assists']:<11} {datos['muertes']:<8} {datos['mvps']:<6} {datos['puntos']:<6}")
