
---

# 🕹️ SportsTrivial v1 — Juego de preguntas deportivas (versión consola)

**SportsTrivial** es un minijuego de preguntas tipo trivial basado en la API pública *Open Trivia DB*.  
Esta primera versión fue desarrollada **junto con el profesor** durante el Módulo 08 de Programación Avanzada, y forma parte de la nueva sección de juegos del proyecto **PyAlexTools**.

---

## 🎯 Características principales

- Obtiene preguntas reales desde *Open Trivia DB*  
- Categoría fija: **Sports** (ID 21)  
- Muestra varias opciones por pregunta  
- Permite responder por número  
- Lleva un marcador de aciertos  
- Funciona completamente en consola  

Esta versión sirve como base para futuras mejoras (GUI, personalización, selección de categorías, etc.).

---

## 📂 Estructura del módulo

```
PyAlexTools/
└── games/
    └── trivia_client.py      ← Juego SportsTrivial (versión consola)
     
```

---

## ▶️ Cómo ejecutar el juego

Desde la raíz del proyecto:

```bash
python -m trivia_client
```

O directamente:

```bash
python trivia_client.py
```

Por defecto, el juego lanza **5 preguntas**:

```python
game = SportsTrivial()
game.play(5)
```

Puedes cambiar el número de preguntas modificando el parámetro.

---

## ⚙️ Requisitos

- Python 3.9+  
- Módulos estándar: `html`, `random`  
- Archivo `trivia_client.py` con la clase `TriviaClient`  
  (encargada de obtener preguntas desde la API)

---

## 🧱 Origen del código

Este juego fue desarrollado **con ayuda del profesor** como parte del módulo de Programación Avanzada.  
Se ha integrado en PyAlexTools como:

- Ejemplo de consumo de API  
- Ejercicio de lógica y manejo de opciones  
- Base para futuras versiones con interfaz gráfica (v2)  
- Base para una versión personalizable (v3)

---

## 🚀 Próximas versiones

- **v2:** Integración en ventana Tkinter (GUI)  
- **v3:** Selección de categoría, número de preguntas y modo de juego  
- **v4:** Integración completa con PyForm y menú de juegos  

---