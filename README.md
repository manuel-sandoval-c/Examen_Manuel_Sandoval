# Examen de Programación Web

**Responsable:** Manuel Sandoval

**Fecha:** 24.11.2026

Aplicación web desarrollada con **Python** y **Flask** que cuenta con un menú principal y dos ejercicios:

- **Ejercicio 1 – Cálculo de compras de pintura:** recibe el nombre del cliente, su edad y la cantidad de tarros de pintura ($9.000 cada uno). Muestra el nombre, el total sin descuento, el descuento aplicado y el total a pagar:
  - Menores de 18 años: sin descuento.
  - Entre 18 y 30 años: 15% de descuento.
  - Mayores de 30 años: 25% de descuento.
- **Ejercicio 2 – Inicio de sesión:** valida usuario y contraseña contra dos usuarios registrados y muestra el mensaje correspondiente:
  - `juan` / `admin` → "Bienvenido administrador juan"
  - `pepe` / `user` → "Bienvenido usuario pepe"
  - Cualquier otro caso → "Usuario o contraseña incorrectos"

## Tecnologías utilizadas

- **Python:** lenguaje de programación de la aplicación.
- **pip:** gestor de dependencias de Python, utilizado para instalar Flask desde `requirements.txt`.
- **Flask:** framework para la construcción de aplicaciones web. Maneja las rutas, recibe los datos de los formularios (GET y POST) y renderiza las páginas con el motor de plantillas Jinja2.
- **HTML y CSS:** estructura y estilo de las páginas.

## Estructura del proyecto

```
Examen/
├── static/
│   └── css/
│       └── estilos.css     # Hoja de estilos
├── templates/
│   ├── base.html           # Plantilla base con bloques
│   ├── index.html          # Menú principal
│   ├── ejercicio1.html     # Formulario de compra de pintura
│   └── ejercicio2.html     # Formulario de inicio de sesión
├── app.py                  # Rutas, funciones y lógica de la aplicación
└── requirements.txt        # Dependencias del proyecto
```

## Rutas

| Ruta | Método | Descripción |
|---|---|---|
| `/` | GET | Menú principal |
| `/ejercicio1` | GET, POST | Formulario y resultado del cálculo de compras |
| `/ejercicio2` | GET, POST | Formulario y resultado del inicio de sesión |

## Cómo ejecutar el proyecto

1. Clonar el repositorio:
   ```
   git clone https://github.com/manuel-sandoval-c/Examen_Manuel_Sandoval.git
   cd Examen_Manuel_Sandoval
   ```
2. Crear y activar un ambiente virtual:
   ```
   python -m venv .venv
   .venv\Scripts\activate
   ```
3. Instalar las dependencias con pip:
   ```
   pip install -r requirements.txt
   ```
4. Ejecutar la aplicación:
   ```
   python app.py
   ```
5. Abrir en el navegador: `http://127.0.0.1:5000`
