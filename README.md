# Resolución del Ejercicio 10 del TP 2

**Nombre:** Noemí Amalia Gudiño\
**Número de estudiante:** 18082/0

## Descripción del proyecto

Este proyecto simula múltiples rondas de un juego tipo shooter entre varios jugadores. Cada ronda registra estadísticas individuales (kills, assists y deaths), determina un MVP y genera un ranking. Al finalizar todas las rondas, se calcula un ranking global acumulado.

El proyecto incluye:

- `funciones.py`: Contiene las funciones principales para calcular puntajes, ejecutar rondas y mostrar rankings.
- `main.py`: Permite ejecutar directamente la simulación de varias rondas.
- `Ej10.ipynb`: Versión didáctica del proyecto en Jupyter Notebook, con explicaciones detalladas paso a paso.
- `requirements.txt`: Lista de dependencias necesarias para ejecutar el proyecto.

## Estructura del proyecto

```
tp2_ejercicio10/
│
├── src/
│   ├── funciones.py
│   ├── main.py
│   └── __init__.py
│
├── notebooks/
│   └── Ej10.ipynb
│
├── requirements.txt
└── README.md
```

## Pasos para ejecutar el proyecto

1. Clonar el repositorio:

```bash
git clone https://github.com/Noemi-Gudino/tp2_segunda_entrega.git
```

2. Acceder al directorio del proyecto:

```bash
cd tp2_ejercicio10
```

3. Crear un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```
4. Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

5. Activar el entorno virtual:

- En Linux/Mac:

```bash
source venv/bin/activate
```

- En Windows:

```bash
venv\Scripts\activate
```

6. Ejecutar el programa principal:

```bash
python main.py
```

-----------------------------------------------------------------------------------------------


## Abrir el notebook
## Usando Jupyter:

```bash
jupyter notebook
```

Luego, navegar hasta la carpeta `notebooks/` y abrir el archivo `Ej10.ipynb`.

### Usando Visual Studio Code:

1. Instalar VS Code: [https://code.visualstudio.com/](https://code.visualstudio.com/)
2. Instalar las extensiones necesarias (Python y Jupyter):
   - Abrir VS Code y presionar `Ctrl + Shift + X`
3. Instalar Jupyter si aún no está instalado:

```bash
pip install notebook jupyter
```

4. Abrir el archivo `.ipynb` en VS Code con `Ctrl + O`

5. Ejecutar las celdas del notebook con el botón ▶️ (play)

Si no aparece el botón de ejecución, podés instalar:

```bash
pip install ipykernel
```

Reiniciar VS Code y volver a abrir el archivo.

