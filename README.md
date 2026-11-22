# Series de Taylor y error de truncamiento — Grupo 2

**Universidad Técnica de Manabí**  
**Carrera:** Ingeniería Mecatrónica  
**Asignatura:** Cálculo Numérico  
**Paralelo:** A  
**Grupo:** 2 — Proyecto A

## Integrantes y contribuciones

- **Angelo Acosta:** estructura inicial del proyecto, integración de la interfaz gráfica con el algoritmo de Taylor y la aplicación RC; mejora de validaciones y documentación de instalación.
- **Anthony Delgado:** mejoras en los títulos y en la cuadrícula de las gráficas; documentación para interpretar las visualizaciones.
- **Juan Cedeño:** pruebas adicionales de la función seno y de cifras significativas inválidas; ampliación de la explicación física del capacitor RC.

Cada integrante debe conocer el algoritmo y la interfaz para la defensa individual. Las contribuciones se registran en el historial de Git.

## Descripción

Aplicación de escritorio desarrollada con **Python**, **PySide6** y **Qt Designer** para aproximar funciones mediante polinomios de Taylor, calcular errores y analizar la precisión de los resultados. Incluye el caso de ingeniería asignado al **Grupo 2: descarga de un capacitor en un circuito RC**.

Permite introducir una función, el punto base `x0`, el punto de evaluación `x`, el orden máximo (0–15) y las cifras significativas. Muestra una tabla por orden, el criterio de Scarborough, tres gráficas y una opción para exportar resultados a CSV.

## Caso de aplicación: descarga del capacitor RC

El voltaje durante la descarga se modela mediante:

\[
v(t)=V_0e^{-t/(RC)}
\]

Donde `V0` es el voltaje inicial (V), `R` la resistencia (Ω), `C` la capacitancia (F) y `t` el tiempo (s).

Al definir `x = t/(RC)`, usamos el polinomio de Maclaurin de `exp(-x)`:

\[
e^{-x}\approx \sum_{k=0}^{n}\frac{(-1)^kx^k}{k!}
\]

Para **`t = RC`**, se obtiene `x = 1`. Con **3 cifras significativas**, la tolerancia aproximada de Scarborough es **0.05 %**.

| Magnitud | Valor |
|---|---:|
| `e^(-1)` verdadero | 0.367879441 |
| Polinomio de Taylor de orden 8 | 0.367881944 |
| Términos requeridos | **9** |
| Orden requerido | **8** |

Ejemplo físico incorporado en la aplicación:

- Voltaje inicial: `V0 = 12 V`
- Resistencia: `R = 1000 Ω`
- Capacitancia: `C = 1000 µF = 0.001 F`
- Tiempo: `t = 1 s`

Como `RC = 1 s`, el voltaje verdadero es aproximadamente **4.414553294 V**; la aproximación con nueve términos es **4.414583333 V**.

### Interpretación del resultado

El voltaje del capacitor disminuye exponencialmente durante la descarga. Después de una constante de tiempo (`t = RC`), conserva aproximadamente **36.79 %** de su voltaje inicial. Para `V0 = 12 V`, eso corresponde a cerca de **4.41455 V**.

En este ejemplo, el polinomio de Taylor de orden 8 satisface la tolerancia usada para tres cifras significativas. La diferencia entre el valor verdadero y el aproximado es pequeña, aunque no es exactamente cero.

## Herramientas

- Python 3.10 o superior
- PySide6 y Qt Designer
- NumPy
- SymPy
- Matplotlib
- pytest
- Git (para clonar y registrar contribuciones)

Las dependencias de Python están detalladas en `requirements.txt`.

## Instalación y ejecución en Windows

Estos pasos se realizan desde **PowerShell**, dentro de Visual Studio Code o de una terminal de Windows. Cada persona crea su propio entorno virtual; la carpeta `.venv/` no se guarda en GitHub.

### 1. Descargar el repositorio

```powershell
git clone https://github.com/Navori20/CN-ParaleloA-Grupo2.git
cd CN-ParaleloA-Grupo2
```

Si se descargó como ZIP, extraerlo y abrir una terminal **dentro de la carpeta que contiene `main.py` y `requirements.txt`**.

### 2. Crear el entorno virtual

```powershell
py -m venv .venv
```

### 3. Activar el entorno virtual

```powershell
.\.venv\Scripts\Activate.ps1
```

Si PowerShell bloquea **solo la activación** por su política de ejecución, se puede habilitar temporalmente en esa sesión y volver a activarlo:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Al funcionar, la terminal muestra `(.venv)` al comienzo del indicador.

### 4. Instalar las dependencias

```powershell
python -m pip install -r requirements.txt
```

Debe ejecutarse desde la raíz del repositorio. Si aparece `No such file or directory: requirements.txt`, comprobar la carpeta con `dir` y entrar a `CN-ParaleloA-Grupo2` si es necesario.

### 5. Abrir la aplicación

```powershell
python main.py
```

### 6. Ejecutar las pruebas automáticas

Cerrar la aplicación (si está abierta) y ejecutar:

```powershell
python -m pytest -v
```

La suite contiene **6 pruebas**; durante el desarrollo, las seis se ejecutaron correctamente. El resultado esperado después de una instalación correcta es `6 passed`.

## Uso de la aplicación

1. Seleccionar un ejemplo: **Descarga RC (grupo 2)**, **cos(x)** del libro, **exp(x)** de Scarborough o **Personalizado**.
2. Introducir una función, `x0`, `x`, el orden máximo y las cifras significativas.
3. En el ejemplo RC, indicar voltaje inicial, resistencia, capacitancia (en **µF**) y tiempo. El programa calcula automáticamente `x = t/(RC)`.
4. Pulsar **Calcular Taylor** para mostrar la tabla, el resultado y las gráficas.
5. Usar **Limpiar** para restablecer los resultados o **Exportar CSV** para guardar la tabla.

## Interpretación de las gráficas

La aplicación presenta tres gráficas para analizar el método de Taylor.

### 1. Función y aproximaciones de Taylor

Compara la función original con los polinomios de Taylor de distintos órdenes. Permite observar cómo mejora la aproximación a medida que aumentan los términos, especialmente cerca del punto de expansión `x0`.

### 2. Error verdadero frente al orden

Representa la magnitud del error relativo verdadero en función del orden del polinomio. Utiliza una escala logarítmica en el eje vertical para mostrar cómo cambia el error entre iteraciones.

### 3. Error de truncamiento

Muestra el error absoluto frente a la distancia al punto de expansión (`|h|`) en escala log-log. Para una función suficientemente derivable y si el primer término omitido es no nulo, el error suele comportarse como `|h|^(n+1)` cerca del punto base. La pendiente observada puede verse afectada por la precisión numérica.

## Estructura del proyecto

```text
CN-ParaleloA-Grupo2/
├── README.md
├── requirements.txt
├── main.py
├── graficas.py
├── ui_ventana_principal.py
├── ui/
│   └── ventana_principal.ui
├── metodo/
│   ├── __init__.py
│   └── taylor.py
├── Tests/
│   └── test_metodo.py
└── Capturas/
    └── (capturas de los ejemplos y las gráficas)
```

`main.py` administra la interfaz y sus eventos; `metodo/taylor.py` implementa el método; `graficas.py` prepara las visualizaciones; y `ui/ventana_principal.ui` es el diseño editable de Qt Designer.

**No editar manualmente** `ui_ventana_principal.py`, porque se genera desde el archivo `.ui` con:

```powershell
pyside6-uic ui/ventana_principal.ui -o ui_ventana_principal.py
```

## Pruebas automáticas

Las seis pruebas del archivo `Tests/test_metodo.py` comprueban:

1. Descarga del capacitor RC: orden 8 y nueve términos.
2. Ejemplo `cos(x)` del libro de Chapra.
3. Criterio de Scarborough aplicado a `exp(0.5)`.
4. Rechazo de un orden superior a 15.
5. Aproximación de Taylor para `sin(x)`.
6. Rechazo de cero cifras significativas.

Para ejecutarlas:

```powershell
python -m pytest Tests/test_metodo.py -v
```

## Capturas de la interfaz

La carpeta `Capturas/` contiene imágenes capturadas durante las pruebas del proyecto, incluidas ejecuciones del caso RC y de los ejemplos matemáticos. Para verlas, abrir dicha carpeta en el repositorio.

## Defensa y entrega

Cada integrante debe poder explicar el algoritmo, el criterio de error, el caso físico RC, las tres gráficas y el funcionamiento de la interfaz. El historial del repositorio debe evidenciar **al menos tres commits propios por integrante**.

Antes de entregar, verificar:

- Que las seis pruebas pasen después de actualizar el repositorio.
- Que la aplicación abra, calcule y exporte CSV.
- Que `README.md`, `requirements.txt`, `Tests/`, `ui/` y `Capturas/` estén incluidos.
- Que `.venv/` y archivos temporales no se incluyan en el ZIP.
- Que los tres integrantes puedan explicar sus aportes durante la defensa.

**Repositorio:** https://github.com/Navori20/CN-ParaleloA-Grupo2

## Requisitos para la evaluación

Antes de presentar el proyecto, cada integrante debe:

- Explicar cómo se construye el polinomio de Taylor.
- Interpretar el criterio de error de Scarborough.
- Demostrar el ejemplo de descarga del capacitor RC.
- Explicar el funcionamiento de las tres gráficas.
- Ejecutar las pruebas automáticas y mostrar sus resultados.

La demostración debe realizarse con la aplicación funcionando.