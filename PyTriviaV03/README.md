
---

# 🎮 PyTriviaV03 — Juego de Trivia en Consola y GUI (Tkinter)

**PyTriviaV03** es la tercera versión del proyecto de trivial desarrollado en Python.  
Esta versión introduce una arquitectura modular, nombres genéricos, una interfaz gráfica avanzada y un **launcher oficial** que permite elegir fácilmente entre las distintas versiones del juego.

El proyecto incluye:

- Una **versión consola**  
- Una **versión GUI básica**  
- Una **versión GUI avanzada** con configuración  
- Un **launcher GUI** para seleccionar la versión  
- Un **cliente API** reutilizable para obtener preguntas desde Open Trivia DB  

---

## 📂 Estructura del proyecto

```
PyTriviaV03/
│── README.md
│── trivia_client.py            ← Cliente API (común a todas las versiones)
│── trivia_game_console.py      ← Versión consola
│── trivia_game_gui.py          ← Versión GUI básica
│── trivia_game_advanced.py     ← Versión GUI avanzada (configurable)
│── trivia_launcher.py          ← Launcher oficial del proyecto
```

---

## 🧠 Descripción de cada archivo

### **1. trivia_client.py**
Cliente HTTP que se conecta a la API de Open Trivia DB.  
Devuelve preguntas en formato JSON listas para usar en cualquier versión del juego.

---

### **2. trivia_game_console.py**
Versión clásica del trivial en consola.  
Permite:

- Elegir número de preguntas  
- Elegir categoría  
- Responder escribiendo el número de la opción  

Ideal para pruebas rápidas o entornos sin GUI.

---

### **3. trivia_game_gui.py**
Versión GUI básica con Tkinter.  
Características:

- 5 preguntas por defecto  
- Categoría General Knowledge  
- Interfaz simple con botones  
- Ventanas emergentes para aciertos y errores  

---

### **4. trivia_game_advanced.py**
Versión GUI avanzada.  
Incluye:

- Selector de número de preguntas  
- Selector de categoría  
- Ventana de configuración inicial  
- Interfaz gráfica completa  
- Resultados finales en ventana emergente  

Es la versión más completa y flexible del proyecto.

---

### **5. trivia_launcher.py**
El **launcher oficial** de PyTriviaV03.  
Permite elegir fácilmente entre:

- Versión Consola  
- GUI Básica  
- GUI Avanzada  

Cada versión se ejecuta en un proceso independiente sin bloquear el launcher.

---

## ▶️ Cómo ejecutar cada versión

### **Ejecutar el launcher (recomendado)**
```bash
python trivia_launcher.py
```

Esto abrirá una ventana con botones para elegir la versión del juego.

---

### **Ejecutar la versión consola**
```bash
python trivia_game_console.py
```

### **Ejecutar la versión GUI básica**
```bash
python trivia_game_gui.py
```

### **Ejecutar la versión GUI avanzada**
```bash
python trivia_game_advanced.py
```

---

## 🌐 Requisitos

- Python 3.9+  
- Tkinter (incluido por defecto en la mayoría de instalaciones de Python)  
- Conexión a internet para obtener preguntas  
- Biblioteca `requests` instalada  

Instalar requests:

```bash
pip install requests
```

---

## 📜 Licencia

Proyecto educativo desarrollado como parte del aprendizaje de Python, Tkinter y consumo de APIs.

---