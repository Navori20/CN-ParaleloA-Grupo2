# Series de Taylor y error de truncamiento — Grupo 2

**Universidad Técnica de Manabí**  
**Carrera:** Ingeniería Mecatrónica  
**Asignatura:** Cálculo Numérico  
**Paralelo:** A  
**Grupo:** 2 — Proyecto A

## Integrantes

- Anthony Delgado
- Juan Cedeño
- Angelo Acosta

> **Roles y contribuciones:** completar con las responsabilidades reales de cada integrante antes de entregar. Todos deben conocer el algoritmo y la interfaz para la defensa individual.

## Descripción

Aplicación de escritorio desarrollada con **Python**, **PySide6** y **Qt Designer** para aproximar funciones mediante polinomios de Taylor, calcular el error de truncamiento y analizar la precisión de los resultados. Incluye el caso de ingeniería asignado al **Grupo 2: descarga de un capacitor en un circuito RC**.

La aplicación permite ingresar una función, el punto base `x0`, el punto de evaluación `x`, el orden máximo (0–15) y las cifras significativas. Muestra una tabla por orden, la tolerancia de Scarborough, las gráficas del método y la exportación a CSV.

## Caso de aplicación: descarga del capacitor RC

La tensión durante la descarga se modela mediante:

\[
v(t) = V_0 e^{-t/(RC)}
\]

con voltaje inicial `V0` (V), resistencia `R` (Ω), capacitancia `C` (F) y tiempo `t` (s).

Definiendo `x = t/(RC)`, se aproxima `exp(-x)` mediante la serie de Maclaurin:

\[
e^{-x} \approx \sum_{k=0}^{n} \frac{(-1)^k x^k}{k!}
\]

Para **`t = RC`**, se tiene `x = 1`. Con **tres cifras significativas**, la tolerancia de Scarborough es **0.05 %**. El resultado de referencia es:

| Magnitud | Valor |
|---|---:|
| `e^(-1)` verdadero | 0.367879441 |
| Polinomio de orden 8 | 0.367881944 |
| Términos necesarios | **9** |
| Orden requerido | **8** |

Ejemplo físico incluido: `V0 = 12 V`, `R = 1000 Ω`, `C = 1000 µF = 0.001 F` y `t = 1 s`. Como `RC = 1 s`, el voltaje verdadero es aproximadamente **4.414553 V** y la aproximación con nueve términos es **4.414583 V**.

## Herramientas

- Python 3.10 o superior (entorno probado por el equipo: completar si procede)
- PySide6 y Qt Designer
- NumPy
- SymPy
- Matplotlib
- pytest

## Instalación y ejecución (Windows)

Clonar o descargar este repositorio y abrir la carpeta en **Visual Studio Code**. Desde la terminal de PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python main.py
```

Si PowerShell bloquea la activación, ejecutar temporalmente en esa terminal:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

Si no se dispone todavía de `requirements.txt`, instalar las dependencias con:

```powershell
python -m pip install pyside6 numpy sympy matplotlib pytest
```

## Uso de la aplicación

1. Seleccionar un ejemplo precargado: **Descarga RC (grupo 2)**, **cos(x)** del libro, **exp(x)** de Scarborough o **Personalizado**.
2. Introducir la función, `x0`, `x`, el orden máximo y las cifras significativas.
3. Para el caso RC, ajustar voltaje inicial, resistencia, capacitancia (en **µF**) y tiempo. El programa calcula automáticamente `x = t/(RC)`.
4. Presionar **Calcular Taylor** para ver la tabla de aproximaciones y errores, el resultado final y las tres gráficas.
5. Usar **Limpiar** para borrar los resultados o **Exportar CSV** para guardar la tabla.

Las gráficas representan la función frente a los polinomios de Taylor, el error verdadero frente al orden y el error de truncamiento frente a `h` en escala log-log.

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
├── tests/
│   └── test_metodo.py
└── capturas/
```

`main.py` maneja la interfaz y los eventos; `metodo/taylor.py` contiene la lógica del método; `graficas.py` prepara las visualizaciones; y `ui/ventana_principal.ui` es el diseño editable de Qt Designer. **No editar manualmente** `ui_ventana_principal.py`, pues se genera desde el archivo `.ui`:

```powershell
pyside6-uic ui/ventana_principal.ui -o ui_ventana_principal.py
```

## Pruebas automáticas

Desde la raíz del repositorio:

```powershell
python -m pytest tests/test_metodo.py -v
```

Se incluyen cuatro pruebas: descarga RC, función `cos(x)` del libro, criterio de Scarborough para `exp(0.5)` y validación de un orden fuera del intervalo permitido. En la ejecución local realizada durante el desarrollo, **las cuatro pruebas pasaron**.

## Capturas de la interfaz

**Pendiente antes de entregar:** guardar al menos tres capturas reales dentro de `capturas/`:

1. `capturas/01_caso_rc.png` — pantalla de parámetros y resultados del capacitor RC.
2. `capturas/02_grafica_taylor.png` — gráfica de función y aproximaciones.
3. `capturas/03_grafica_error.png` — gráfica de error o truncamiento.

Después de agregar las imágenes reales, se pueden mostrar aquí:

```markdown
![Caso RC](capturas/01_caso_rc.png)
![Gráfica Taylor](capturas/02_grafica_taylor.png)
![Análisis del error](capturas/03_grafica_error.png)
```

## Defensa y entrega

Cada integrante debe conocer el funcionamiento del código y del método de Taylor. El repositorio debe evidenciar **al menos tres commits propios de cada integrante**, según el enunciado. Entregar el enlace del repositorio y el ZIP correspondiente junto con las capturas e instrucciones, respetando las fechas del paralelo A.

**Antes de entregar:** completar los roles reales, agregar las capturas e incluir `requirements.txt`; verificar que no se suba `.venv/` y que la aplicación se pueda ejecutar desde una copia limpia del repositorio.

## Interpretación de las gráficas

La aplicación presenta tres gráficas para analizar el método de Taylor.

### 1. Función y aproximaciones de Taylor

Compara la función matemática original con los polinomios de Taylor de distintos órdenes. Permite observar cómo mejora la aproximación al aumentar el número de términos.

### 2. Error verdadero frente al orden

Representa el error relativo verdadero en función del orden del polinomio. Se utiliza una escala logarítmica en el eje vertical para apreciar cómo disminuye el error.

### 3. Error de truncamiento

Muestra el error absoluto frente a la distancia al punto de expansión, utilizando escalas logarítmicas en ambos ejes.

Para una función suficientemente derivable, el error de un polinomio de orden n suele ser proporcional a |h|^(n+1), cuando el primer término omitido no es nulo y el error numérico no domina.