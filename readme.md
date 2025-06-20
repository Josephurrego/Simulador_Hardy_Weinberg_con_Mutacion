# Simulador de Frecuencias Alélicas por Mutación

![Simulador de Alelos](https://i.imgur.com/g8e1b1B.png)

## 📜 Descripción General

Este proyecto simula cómo las frecuencias de múltiples alelos en una población cambian a lo largo de las generaciones debido únicamente a la **mutación**. El objetivo es visualizar cómo, partiendo de frecuencias iniciales, el sistema alcanza un punto de equilibrio estable.

Para lograr esto, se implementan desde cero los métodos numéricos de **factorización LU** y **multiplicación de matrices** en Python. Estos métodos son cruciales para resolver el sistema de ecuaciones lineales que define el estado de equilibrio de las frecuencias alélicas.

El simulador se basa en los principios de la genética de poblaciones, y el resultado final es una gráfica que muestra la trayectoria de las frecuencias de cuatro alelos hasta que alcanzan su equilibrio, demostrando así los conceptos teóricos de una manera visual e intuitiva.

## 🔬 Fundamento Teórico

La base de este proyecto se encuentra en la genética de poblaciones, que estudia la distribución y el cambio en las frecuencias de los alelos en las poblaciones.

### Principio de Hardy-Weinberg

El principio de Hardy-Weinberg sirve como un modelo nulo, describiendo un estado en el que las frecuencias alélicas y genotípicas se mantienen constantes en ausencia de influencias evolutivas. Para un gen con `n` alelos con frecuencias $p_{1},p_{2},...,p_{n}$, la suma de estas frecuencias es igual a 1:

$$
\sum_{i=1}^{n}p_{i}=1
$$

### Mutación como Fuerza Evolutiva

La mutación es la fuente primordial de nueva variación genética. Al cambiar un alelo por otro, la mutación altera las frecuencias alélicas a lo largo del tiempo. En un modelo con múltiples alelos, el cambio en la frecuencia de un alelo en una generación se puede modelar con una matriz de mutación $M$. Si $P$ es el vector de frecuencias en una generación, las frecuencias en la siguiente generación, $P'$, se calculan como:

$$
P^{\prime}=P\times M
$$

### Punto de Equilibrio por Mutación

Cuando la mutación es la única fuerza actuando, las frecuencias alélicas eventualmente alcanzan un **punto de equilibrio** donde ya no cambian. En este punto, para cada alelo $A_i$, la pérdida por mutación hacia otros alelos es igual a la ganancia por mutación desde otros alelos. Esto se define por la siguiente ecuación para cada alelo $A_i$:

$$
p_{i}\sum_{j\ne i}\mu_{ij}=\sum_{j\ne i}p_{j}\mu_{ji}
$$

Donde $p_i$ es la frecuencia del alelo $A_i$ y $\mu_{ij}$ es la tasa de mutación de $i$ a $j$. Esto genera un sistema de ecuaciones lineales que se debe resolver para encontrar las frecuencias de equilibrio.

## 🛠️ Métodos Numéricos Implementados

Para resolver el sistema de ecuaciones lineales que define el punto de equilibrio, se construyeron los siguientes métodos numéricos en Python sin depender de librerías como `NumPy` para la lógica central.

### 1. **Multiplicación de Matrices**
Se implementó una función para la multiplicación de matrices, esencial tanto para simular el cambio generacional de las frecuencias como para verificar la solución del sistema.

### 2. **Factorización LU**
El núcleo de la resolución del sistema es la implementación de la **factorización LU**. Este método descompone la matriz de coeficientes $A$ en el producto de una matriz triangular inferior ($L$) y una matriz triangular superior ($U$).

La resolución del sistema $Ax = b$ se simplifica en dos pasos:
1.  **Sustitución hacia adelante:** Se resuelve $Ly = b$ para $y$.
2.  **Sustitución hacia atrás:** Se resuelve $Ux = y$ para $x$.

Este enfoque es computacionalmente eficiente y robusto para resolver este tipo de sistemas.

## 🚀 Ejecución del Proyecto

Para ejecutar el simulador y generar la gráfica, sigue estos pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/Josephurrego/Simulador_Hardy_Weinberg_con_Mutacion.git
    cd Simulador_Hardy_Weinberg_con_Mutacion
    ```

2.  **Instalar dependencias:**
    El proyecto requiere `matplotlib` para la visualización. `numpy`utilizado para facilitar el manejo de arreglos, aunque los métodos numéricos centrales estén implementados manualmente.
    ```bash
    pip install matplotlib numpy
    ```

3.  **Ejecutar el script principal:**
    (Falta Completar)

El script realizará los siguientes pasos:
1.  Definirá las tasas de mutación y las frecuencias alélicas iniciales.
2.  Construirá y resolverá el sistema de ecuaciones para el punto de equilibrio usando la **factorización LU**.
3.  Simulará la evolución de las frecuencias generación por generación.
4.  Generará y guardará una gráfica mostrando la convergencia de las frecuencias hacia el equilibrio.

## ✅ Resultado Esperado

El script a traves de `matplotlib` abrirá una ventana que visualiza la evolución de las frecuencias de los cuatro alelos a lo largo de `n` generaciones. La gráfica mostrará cómo cada frecuencia converge asintóticamente hacia el valor de equilibrio calculado, validando la correcta implementación de los métodos numéricos y del modelo genético.
