
---

# 🕹️ SportsTrivial v2 — Versión GUI (Tkinter)

**SportsTrivial v2** es la evolución del juego de trivial deportivo desarrollado inicialmente en consola (v1).  
En esta versión, el juego se ejecuta dentro de una **interfaz gráfica (GUI)** creada con **Tkinter**, permitiendo jugar mediante botones y ventanas emergentes, sin necesidad de usar la terminal.

Esta versión forma parte de la sección de juegos del proyecto **PyAlexTools**.

---

## 🎯 Objetivos de la versión 2

- Reemplazar la interacción por consola (`input()` / `print()`)  
- Mostrar preguntas y opciones dentro de una ventana Tkinter  
- Permitir seleccionar respuestas mediante botones  
- Mostrar mensajes de acierto/error con `messagebox`  
- Mantener la categoría fija: **Sports (ID 21)**  
- Mantener el número de preguntas fijo: **5**  
- Preparar la base para una versión más avanzada (v3)

---

## 📂 Estructura del módulo

```
PyAlexTools/
└── games/
    ├── trivia_client.py          ← Cliente API (compartido con v1)
    └── sports_trivial_gui.py     ← Juego SportsTrivial con interfaz gráfica (v2)
```

> Nota: La versión 1 del juego sigue existiendo en consola, pero la v2 es completamente independiente y utiliza Tkinter.

---

## ▶️ Cómo ejecutar el juego

Desde la raíz del proyecto:

```bash
python -m games.sports_trivial_gui
```

O directamente:

```bash
python games/sports_trivial_gui.py
```

Esto abrirá una ventana flotante con:

- Pregunta actual  
- Botones con las opciones  
- Mensajes de acierto o error  
- Resultado final al terminar  

---

## ⚙️ Requisitos

- Python 3.9+  
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python)  
- Archivo `trivia_client.py` funcionando correctamente  
- Conexión a internet (para obtener preguntas desde Open Trivia DB)

---

## 🧱 Origen del código

Esta versión se basa en el juego original desarrollado **junto con el profesor** en el módulo de Programación Avanzada.  
La v2 adapta esa lógica a un entorno gráfico, manteniendo la esencia del trivial pero con una experiencia más amigable.

---

## 🚀 Próximas versiones

- **v3:**  
  - Selección de número de preguntas  
  - Selección de categoría  
  - Menú de configuración  
  - Integración con PyForm  

---
