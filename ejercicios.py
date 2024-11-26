import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la página
st.set_page_config(page_title="Optimización No Lineal", layout="wide")

# Estilo personalizado
st.markdown("""
    <style>
    .main {
        background-color: #f7f2f2;
    }
    .title {
        color: #5a5a5a;
        font-size: 30px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        color: #8b5b93;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Título y subtítulo
st.markdown('<div class="title">UNIVERSIDAD NACIONAL DEL ALTIPLANO</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">NELIDA ARACELY QUISPE CALATAYUD</div>', unsafe_allow_html=True)

# Espaciado
st.markdown("##")

# Ejercicio 1: Verificar puntos minimizadores
if st.button("Ejercicio 1: Verificar puntos minimizadores"):
    st.write("### Solución:")
    st.write("""
    1. La función es \( f(x) = x^2 - 4x + 5 \). Reescribiéndola completando el cuadrado:
       \[
       f(x) = (x - 2)^2 + 1.
       \]
       Es una parábola con un mínimo global en \( x = 2 \).
       
    2. Evaluando:
       - \( f(2) = 1 \), por lo que \( x = 2 \) es el **mínimo global**.
       - \( f(0) = 5 \), lo que muestra que \( x = 0 \) **no es un minimizador**.
    """)

    # Gráfico
    x = np.linspace(-1, 5, 500)
    f = x**2 - 4*x + 5
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, f, label=r"$f(x) = x^2 - 4x + 5$")
    ax.scatter([2], [1], color='red', label="Mínimo Global: (2, 1)")
    ax.set_title("Gráfico de \( f(x) \)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    st.pyplot(fig)

# Ejercicio 2: Mínimos en f(x) = |x|
if st.button("Ejercicio 2: Mínimos en f(x) = |x|"):
    st.write("### Solución:")
    st.write("""
    La función es \( f(x) = |x| \):
    1. El punto \( x = 0 \) es un mínimo global porque \( f(0) = 0 \) y para cualquier otro \( x \), \( f(x) > 0 \).
    """)

    # Gráfico
    x = np.linspace(-2, 2, 500)
    f = np.abs(x)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, f, label=r"$f(x) = |x|$")
    ax.scatter([0], [0], color='red', label="Mínimo Global: (0, 0)")
    ax.set_title("Gráfico de \( f(x) \)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    st.pyplot(fig)

# Ejercicio 3: Mínimos en sin(x) en [0, π]
if st.button("Ejercicio 3: Mínimos en sin(x)"):
    st.write("### Solución:")
    st.write("""
    La función \( f(x) = \sin(x) \) es continua y está definida en el intervalo compacto \( [0, \pi] \). Por el Teorema de Weierstrass, tiene un mínimo global. Evaluando:
    - \( f(0) = 0 \) y \( f(\pi) = 0 \), por lo que el mínimo global ocurre en \( x = 0 \) y \( x = \pi \).
    """)

    # Gráfico
    x = np.linspace(0, np.pi, 500)
    f = np.sin(x)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, f, label=r"$f(x) = \sin(x)$")
    ax.scatter([0, np.pi], [0, 0], color='red', label="Mínimos Globales: (0, 0) y (\(\pi\), 0)")
    ax.set_title("Gráfico de \( f(x) \)")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    st.pyplot(fig)

# Ejercicio 4: Mínimos en f(x, y) = x^2 + y^2
if st.button("Ejercicio 4: Mínimos en f(x, y) = x^2 + y^2"):
    st.write("### Solución:")
    st.write("""
    La función \( f(x, y) = x^2 + y^2 \) tiene su dominio restringido al círculo definido por \( x^2 + y^2 \leq 1 \).
    
    1. La función es no negativa (\( f(x, y) \geq 0 \)) y alcanza su valor mínimo en el centro del círculo.
    2. En \( (x, y) = (0, 0) \), el valor es:
       \[
       f(0, 0) = 0^2 + 0^2 = 0.
       \]
    3. Por lo tanto, el mínimo global ocurre en el punto \( (0, 0) \).
    """)

    # Gráfico
    x = np.linspace(-1, 1, 100)
    y = np.linspace(-1, 1, 100)
    X, Y = np.meshgrid(x, y)
    Z = X**2 + Y**2
    fig, ax = plt.subplots(figsize=(6, 4))
    contour = ax.contourf(X, Y, Z, levels=20, cmap='viridis')
    cbar = fig.colorbar(contour, ax=ax)
    cbar.set_label(r"$f(x, y)$")
    ax.scatter([0], [0], color='red', label="Mínimo Global: (0, 0)")
    ax.set_title("Gráfico de \( f(x, y) \)")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    st.pyplot(fig)

# Ejercicio 5: Mínimo global no único
if st.button("Ejercicio 5: Mínimo Global No Único"):
    st.write("### Solución:")
    st.write("""
    Un ejemplo de una función con un mínimo global no único es:
    \[
    f(x) = 
    \begin{cases} 
    0, & x \in \{-1, 1\} \\ 
    1, & x \notin \{-1, 1\}.
    \end{cases}
    \]
    
    1. En \( x = -1 \) y \( x = 1 \), el valor mínimo es:
       \[
       f(-1) = 0, \quad f(1) = 0.
       \]
    2. Para cualquier otro valor de \( x \), \( f(x) = 1 \), lo que muestra que los mínimos globales no son únicos y ocurren en \( x = -1 \) y \( x = 1 \).
    """)

    # Gráfico
    x = np.linspace(-2, 2, 500)
    f = np.where((x == -1) | (x == 1), 0, 1)  # Función definida con valores mínimos en -1 y 1
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(x, f, label=r"$f(x)$")
    ax.scatter([-1, 1], [0, 0], color='red', label="Mínimos Globales: (-1, 0) y (1, 0)")
    ax.set_title("Gráfico del Ejemplo")
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.legend()
    st.pyplot(fig)


