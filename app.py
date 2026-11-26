
"""
Fecha: 24.11.2026
Responsable: Manuel Sandoval
Descripción:
Aplicación web desarrollada con Flask para resolver los ejercicios
de cálculo de compras de pintura e inicio de sesión.
"""

from flask import Flask, render_template, request

# Inicialización de la aplicación Flask
app = Flask(__name__)


# ---------------------------------------------------------
# Constantes de la aplicación
# ---------------------------------------------------------

# Precio de cada tarro de pintura
PRECIO_TARRO = 9000

# Usuarios registrados: usuario -> (contraseña, mensaje de bienvenida)
USUARIOS = {
    "juan": ("admin", "Bienvenido administrador juan"),
    "pepe": ("user", "Bienvenido usuario pepe")
}


# ---------------------------------------------------------
# Funciones auxiliares
# ---------------------------------------------------------
def calcular_descuento(edad):
    """
    Retorna el porcentaje de descuento según la edad:
    - Menores de 18 años: sin descuento.
    - Entre 18 y 30 años (inclusive): 15%.
    - Mayores de 30 años: 25%.
    """

    if edad < 18:
        return 0

    if edad <= 30:
        return 15

    return 25


@app.template_filter("pesos")
def formatear_pesos(valor):
    """
    Formatea un monto en pesos chilenos con separador de miles.
    Ejemplo: 90000 -> 90.000
    Se registra como filtro para usarlo en los templates.
    """

    return f"{valor:,.0f}".replace(",", ".")


def convertir_entero(texto, nombre_campo, errores):
    """
    Convierte un texto a número entero mayor que cero.
    Si el valor no es válido, agrega un mensaje a la lista
    de errores y retorna None.
    """

    try:
        numero = int(texto)

    except ValueError:
        errores.append(
            f"El campo {nombre_campo} debe ser un número entero."
        )
        return None

    if numero <= 0:
        errores.append(
            f"El campo {nombre_campo} debe ser mayor que cero."
        )
        return None

    return numero


# ---------------------------------------------------------
# Ruta principal: menú de navegación
# ---------------------------------------------------------
@app.route("/")
def index():

    return render_template("index.html")


# ---------------------------------------------------------
# Ejercicio 1: cálculo de compra de pintura
# ---------------------------------------------------------
@app.route("/ejercicio1", methods=["GET", "POST"])
def ejercicio1():

    # Diccionario para almacenar los datos del formulario
    valores = {
        "nombre": "",
        "edad": "",
        "cantidad": ""
    }

    # Lista para almacenar los errores de validación
    errores = []

    # Variable para almacenar los resultados
    resultado = None

    # Si se reciben datos desde el formulario
    if request.method == "POST":

        # Obtener los datos ingresados
        valores = {
            "nombre": request.form.get("nombre", "").strip(),
            "edad": request.form.get("edad", "").strip(),
            "cantidad": request.form.get("cantidad", "").strip()
        }

        # -------------------------------------------------
        # Validación de los datos
        # -------------------------------------------------
        if valores["nombre"] == "":
            errores.append("Debe ingresar el nombre del cliente.")

        edad = convertir_entero(valores["edad"], "edad", errores)

        cantidad = convertir_entero(
            valores["cantidad"], "cantidad de tarros", errores
        )

        # -------------------------------------------------
        # Si los datos son válidos, realizar los cálculos
        # -------------------------------------------------
        if not errores:

            # Calcular el total sin descuento
            total_sin_descuento = cantidad * PRECIO_TARRO

            # Determinar el descuento según la edad
            descuento_porcentaje = calcular_descuento(edad)

            # Calcular el monto del descuento
            monto_descuento = (
                total_sin_descuento * descuento_porcentaje / 100
            )

            # Calcular el total a pagar
            total_pagar = total_sin_descuento - monto_descuento

            # Almacenar los resultados
            resultado = {
                "nombre": valores["nombre"],
                "total_sin_descuento": total_sin_descuento,
                "descuento_porcentaje": descuento_porcentaje,
                "monto_descuento": monto_descuento,
                "total_pagar": total_pagar
            }

    # Mostrar el formulario, los errores y los resultados
    return render_template(
        "ejercicio1.html",
        valores=valores,
        errores=errores,
        resultado=resultado
    )


# ---------------------------------------------------------
# Ejercicio 2: inicio de sesión
# ---------------------------------------------------------
@app.route("/ejercicio2", methods=["GET", "POST"])
def ejercicio2():

    # Variables para almacenar los datos y el resultado
    usuario = ""
    mensaje = ""
    clase_mensaje = ""

    # Si se reciben datos desde el formulario
    if request.method == "POST":

        # Obtener los datos ingresados
        usuario = request.form.get("usuario", "").strip()
        contrasena = request.form.get("contrasena", "")

        # -------------------------------------------------
        # Validación de las credenciales
        # -------------------------------------------------
        if usuario in USUARIOS and USUARIOS[usuario][0] == contrasena:

            mensaje = USUARIOS[usuario][1]
            clase_mensaje = "resultado-exito"

        else:

            mensaje = "Usuario o contraseña incorrectos"
            clase_mensaje = "resultado-error"

    # Mostrar el formulario y el resultado en la misma página
    return render_template(
        "ejercicio2.html",
        usuario=usuario,
        mensaje=mensaje,
        clase_mensaje=clase_mensaje
    )


# ---------------------------------------------------------
# Ejecución de la aplicación
# ---------------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)
