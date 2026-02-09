# PyFormV03 — Primer formulario gráfico 

PyFormV03 representa mi **primer intento real** de construir un formulario completo usando Tkinter.  
A diferencia de PyFormV01 (POO + pickle) y PyFormV02 (experimentos sueltos con widgets), esta versión reúne todo lo aprendido hasta ahora en una sola interfaz.

Es una versión **totalmente amateur y sin funcion alguna**, con errores, mezclas de estilos y sin estructura formal.  


---

## 🧩 ¿Qué incluye esta versión?

### ✔ Campos de entrada (`Entry`)
- Nombre  
- Apellido  
- Password (oculto con `show="*"`)  
- Correo  

### ✔ Etiquetas (`Label`) alineadas con `.grid()`

### ✔ Selección de género con `Radiobutton`
- Masculino  
- Femenino  

### ✔ Boton "Enviar" sin funcion

Inclui un boton sin funcion de momento

Mi idea es hacer un formulario para almacenar informacion, como ocurre con los codigos de PyFormV01
Tambien que al precionar el boton "Enviar" los datos se guarden en un archivo serializado y que el formulario se limpie

## Advertencia: Esto es solo una prueba no lo tomen como profesional porque tiene muchos errores y hay opciones que no tienen funcion