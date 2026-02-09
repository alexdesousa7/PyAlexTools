# PyFormV04 — Formulario funcional con validación y persistencia

PyFormV04 representa un salto importante en mi aprendizaje.  
Después de la versión amateur PyFormV03, esta versión reescribe el formulario desde cero con una estructura más clara, validaciones reales y persistencia de datos usando `pickle`.

Aquí ya empiezo a aplicar buenas prácticas básicas y a organizar mejor la lógica del programa.


NOTA: Lo admito soy un poco desordenado 

---

## 🧩 ¿Qué incluye esta versión?

### ✔ Formulario completo con campos:
- Nombre  
- Apellido  
- Edad  
- Correo  
- Usuario  
- Password (oculto)  
- Género (Radiobutton)  
- Aceptación de condiciones (Checkbutton)  

### ✔ Validación real
El formulario **no permite guardar datos** si el usuario no acepta las condiciones.  
Se muestra un mensaje de advertencia usando `messagebox.showwarning()`.

### ✔ Persistencia de datos con `pickle`
Los datos se guardan en un archivo binario: datos.dat


Cada registro se almacena como un diccionario dentro de una lista persistente.

### ✔ Limpieza automática del formulario
Después de guardar, todos los campos se vacían y las opciones vuelven a su estado inicial.

### ✔ Estructura más clara
- Funciones separadas: `guardar_datos()` y `limpiar_campos()`  
- Manejo de excepciones al cargar el archivo  
- Uso correcto de `with open()`  
- Interfaz ordenada con `.grid()`  

---

## 🛠️ Mejoras respecto a PyFormV03

- Se eliminó la mezcla de `.pack()` y `.grid()`  
- Se corrigieron errores de lógica (`var.get` → `var.get()`)  
- Se organizó el código en secciones claras  
- Se añadió validación real  
- Se implementó persistencia funcional  
- Se limpió la interfaz y se mejoró la legibilidad  
- Se eliminó código duplicado y variables repetidas  

PyFormV04 es la primera versión que empieza a parecer una aplicación real.

---

## ⚠️ Advertencia sobre seguridad

Este proyecto utiliza `pickle` para almacenar datos en formato binario.  
Aunque el archivo **no es legible a simple vista**, **NO está cifrado** ni protegido.

Cualquier persona con conocimientos básicos de Python puede leer su contenido.

Este proyecto es educativo y **no debe usarse para almacenar información sensible**.

---

## 🎯 Objetivo de PyFormV04

- Reescribir PyFormV03 de forma más profesional  
- Aprender a validar datos antes de guardarlos  
- Implementar persistencia real con listas de diccionarios  
- Organizar el código en funciones  
- Preparar el camino para una versión orientada a objetos  
- Dar una verdadera funcionalidad a los botones

---

Cada versión muestra un paso real en mi evolución como desarrollador.
