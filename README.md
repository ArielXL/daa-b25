# 🧩 Biblioteca de Modelos de Grafos en Python

Este proyecto implementa una **biblioteca orientada a objetos** para la representación y generación de **grafos** en Python.  
Su propósito es ofrecer una herramienta educativa y experimental que permita **crear, visualizar y analizar** diferentes tipos de grafos a partir de modelos teóricos conocidos en la teoría de redes.

---

## 🎯 Objetivo del Proyecto

El objetivo principal es **modelar y comprender distintos mecanismos de generación de grafos**.  
Cada modelo representa una forma particular de crecimiento o conexión entre nodos, lo que permite estudiar propiedades como la conectividad, la distribución de grados, la aleatoriedad y la aparición de estructuras complejas.

---

## 🧱 Estructura Conceptual

El sistema se basa en tres clases fundamentales:

- **Graph**: estructura general que almacena los nodos y aristas, con soporte para grafos dirigidos o no dirigidos, y la posibilidad de exportar el grafo a formato GraphViz para su visualización.
- **Node**: representa un vértice dentro del grafo y puede contener información adicional (coordenadas, etiquetas, valores, etc.).
- **Edge**: representa una conexión entre dos nodos, con o sin peso, y mantiene la relación estructural del grafo.

Estas clases se complementan con un conjunto de **funciones generadoras** que crean grafos según distintos modelos matemáticos.

---

## 🧮 Modelos de Generación Implementados

### 🔹 Modelo de Malla (Gm,n)

Genera una red **regular bidimensional** donde los nodos se organizan en forma de cuadrícula de tamaño `m × n`.  
Cada nodo se conecta con su vecino **derecho** y **inferior**, formando una estructura ordenada ideal para representar redes locales o geográficas discretas.

---

### 🔹 Modelo de Erdös–Rényi (Gn,m)

Crea un grafo con un número fijo de nodos `n` y un número determinado de aristas `m`, conectadas **de forma aleatoria**.  
Es el modelo clásico de **grafos aleatorios**, útil para estudiar la probabilidad de conectividad o el surgimiento de componentes grandes.

---

### 🔹 Modelo de Gilbert (Gn,p)

Cada par de nodos se conecta con una **probabilidad p** independiente.  
Este modelo genera grafos donde las conexiones surgen por **azar puro**, controlando la densidad mediante la probabilidad.

**Uso típico:**  
Simular redes sociales o biológicas donde las conexiones surgen con cierta probabilidad global.

---

### 🔹 Modelo Geográfico Simple (Gn,r)

Los nodos se colocan aleatoriamente en un **plano unitario**, y se conectan aquellos cuya **distancia euclidiana** es menor o igual a un radio `r`.  
El modelo refleja la idea de que las conexiones dependen de la **proximidad espacial**.

---

### 🔹 Modelo de Barabási–Albert (Gn,d)

Implementa el mecanismo de **crecimiento preferencial**, donde los nuevos nodos se conectan con mayor probabilidad a los nodos más conectados.  
De esta forma, algunos nodos se vuelven **altamente centrales (hubs)**, dando lugar a redes con distribución de grados tipo **ley de potencias**.

---

### 🔹 Modelo de Dorogovtsev–Mendes (Gn)

Comienza con un triángulo de tres nodos y, a medida que se agregan nuevos, cada uno se conecta con **los extremos de una arista existente elegida al azar**.  
Este proceso crea una red que crece de forma incremental y mantiene una estructura conectada con alta transitividad.

---

## 💾 Exportación y Visualización

La biblioteca permite **guardar cualquier grafo en formato GraphViz (.dot)**.  
Este formato puede visualizarse fácilmente con herramientas como `Graphviz` o `pydot`, generando archivos `.png` o `.pdf`.
