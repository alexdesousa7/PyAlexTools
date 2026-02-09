# PyFormV01 — Primeros pasos con Programación Orientada a Objetos y persistencia con pickle

Este proyecto representa el inicio de mi camino aprendiendo Python de forma estructurada.  
Antes de trabajar con interfaces gráficas (Tkinter), necesitaba comprender conceptos fundamentales como:

- Clases y objetos  
- Métodos y atributos  
- Serialización de datos  
- Lectura y escritura de ficheros binarios  
- Persistencia de listas de objetos  
- Menús interactivos en consola  

PyFormV01 contiene **dos ejercicios independientes**, ambos centrados en aprender a gestionar información de personas usando clases y guardando los datos en archivos binarios mediante `pickle`.

---

## 📌 Ejercicio 1 — Clase `Persona` y lista persistente

En este ejercicio implemento:

- Una clase `Persona` con atributos básicos  
- Una clase `ListaPersonas` que:
  - Carga personas desde un fichero binario
  - Permite agregar nuevas personas
  - Guarda automáticamente los cambios
  - Muestra la información almacenada

Este ejercicio me permitió entender:

- Cómo funciona `pickle.dump()` y `pickle.load()`  
- Cómo manejar archivos binarios con `"ab+"` y `"wb"`  
- Cómo persistir listas completas de objetos  
- Cómo controlar errores cuando el fichero está vacío  

---

## 📌 Ejercicio 2 — Menú interactivo en consola

En este segundo ejercicio amplío el modelo:

- Clase `Persona` más completa (incluye teléfono y dirección)
- Clase `GestorPersonas` para administrar la lista
- Sistema de menú por consola con opciones:
  - Añadir persona
  - Mostrar personas
  - Salir del programa

Este ejercicio me ayudó a practicar:

- Entrada de datos por teclado  
- Validación básica  
- Persistencia automática al agregar nuevos registros  
- Estructuración del código en clases separadas  

---

## ⚠️ Advertencia sobre seguridad

Este proyecto utiliza `pickle` para almacenar datos en formato binario.  
Aunque el archivo **no es legible a simple vista**, **NO está cifrado** ni protegido.

Cualquier persona con conocimientos básicos de Python puede leer su contenido.

Este proyecto es educativo y **no debe usarse para almacenar información sensible**.

---

## 🎯 Objetivo de PyFormV01

Dominar los fundamentos de:

- Programación Orientada a Objetos  
- Persistencia de datos  
- Serialización con pickle  
- Manejo de ficheros  
- Menús interactivos  

Este conocimiento es la base para las siguientes versiones del proyecto.

---

## 🚀 Próximos pasos

En **PyFormV02** comenzaré a trabajar con **Tkinter**, creando mis primeros formularios gráficos y aprendiendo a manejar:

- `Entry`
- `Label`
- `Radiobutton`
- `Checkbutton`
- Variables de control (`IntVar`, `StringVar`)

Cada versión mostrará una evolución clara y progresiva en mi aprendizaje.