import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

# Definición de variables y constantes
b = sp.symbols('b')
a = 20 * 10**(-4)
p = 0.977
dv = 23.6
K = 4.8 * 10**(4)
tl = np.log(10**5)
ll = np.log(10**4)
limites = [1, 5]

# Valores de v para iterar
v_values = [1900, 2000, 2100, 2200, 2300, 2400]

# Configuración de la figura con bordes y fondo personalizados
plt.figure(figsize=(8, 6), edgecolor='black', facecolor='white', linewidth=1)

# Bucle para iterar sobre los valores de v
for v in v_values:
    # Función a graficar
    y = ((v * sp.log(2)) / (sp.log(b/a) * dv)) * (sp.log(v/(p*a*sp.log(b/a))) - sp.log(K))
    y_val = sp.lambdify(b, y)(np.linspace(limites[0], limites[1], 1000))

    # Graficar cada función
    plt.plot(np.linspace(limites[0], limites[1], 1000), y_val, label=f'V={v} V', linewidth=1)

# Líneas horizontales
plt.axhline(y=tl, color='red', linestyle='--', label='Límite superior (ln(10^5))', linewidth=2.5)
plt.axhline(y=ll, color='blue', linestyle='--', label='Límite inferior (ln(10^4))', linewidth=2.5)

# Configuraciones adicionales de la gráfica
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.title("Ln (M) vs. Radio del cátodo y Voltaje aplicado", fontsize=12)
plt.xlabel("Radio del cátodo b [cm]", fontsize=10)
plt.ylabel("Ln (M)", fontsize=10)
plt.xticks(fontsize=8)
plt.yticks(fontsize=8)
plt.xlim(1, 5)
plt.ylim(0, 19)
plt.tight_layout()
plt.savefig('grafica.png', dpi=300)  # Guardar la gráfica como imagen de alta resolución
plt.show()