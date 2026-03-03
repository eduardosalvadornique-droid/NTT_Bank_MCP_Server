# =========================================================
# Funcion para evaluar al usuario
# =========================================================
def evaluar_tarjeta(sueldo: str) -> int:
    if sueldo == "gt_5000":
        mensaje = "El usuario eligió más de S/ 5000."
        tarjetas = 5
        mejor = "Visa Infinite LATAM Pass"
        return mensaje, tarjetas, mejor

    elif sueldo == "2501_5000":
        mensaje = "El usuario eligió S/ 2501 - S/ 5000."
        tarjetas = 4
        mejor = "Visa Signature LATAM Pass"
        return mensaje, tarjetas, mejor

    elif sueldo == "1200_2500":
        mensaje = "El usuario eligió S/ 1200 - S/ 2500."
        tarjetas = 3
        mejor = "Visa Platinum LATAM Pass"
        return mensaje, tarjetas, mejor

    elif sueldo == "lt_1200":
        mensaje = "El usuario eligió menos de S/ 1200."
        tarjetas = 2
        mejor = "Visa Oro LATAM Pass"
        return mensaje, tarjetas, mejor
