# PyFormV02 — Primeros experimentos con Tkinter

Esta versión representa mi primera toma de contacto con **Tkinter**, el módulo estándar de Python para crear interfaces gráficas.  
A diferencia de PyFormV01 (donde trabajé solo con consola, clases y pickle), aquí comienzo a explorar widgets visuales, eventos y variables de control.

PyFormV02 no es un proyecto estructurado, sino una colección de **experimentos**, **pruebas** y **ejercicios sueltos** que me ayudaron a entender cómo funciona Tkinter.

---

## 🧪 ¿Qué incluye esta versión?

### ✔ 1. Checkbuttons (selección múltiple)
Aprendí a usar:

- `IntVar()` para controlar estados
- `Checkbutton()` para activar/desactivar opciones
- Funciones conectadas con `command=`
- Actualización dinámica de un `Label` según las selecciones

Este ejercicio me enseñó cómo manejar varias opciones al mismo tiempo.

---

### ✔ 2. Radiobuttons (selección única)
Experimenté con:

- `IntVar()` para seleccionar una sola opción
- `Radiobutton()` con valores diferentes
- Funciones que reaccionan a la selección del usuario
- Mostrar resultados en un `Label`

También descubrí errores comunes, como usar `var.get` en lugar de `var.get()`.

---

### ✔ 3. Primeros pasos con `.place()` y `.pack()`
Probé:

- Crear un `Label` con estilo (color, fuente)
- Posicionarlo manualmente con `.place()`
- Añadir un botón simple y sin funcion alguna.

Este ejercicio me ayudó a entender que **no se deben mezclar `.pack()` y `.place()` en el mismo widget**, algo que corregí más adelante.

---

## 🎯 Objetivo de PyFormV02

- Familiarizarme con los widgets básicos de Tkinter  
- Entender cómo funcionan las variables de control (`IntVar`)  
- Aprender a conectar widgets con funciones  
- Practicar posicionamiento con `.pack()` y `.place()`  
- Cometer errores y aprender de ellos  
- Prepararme para construir un formulario real en PyFormV03  

---

Con estos ejercicios y los anteriores llaamdos PyFomrV03 se me vino a la mente un proyecto