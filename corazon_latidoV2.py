# =====================================================================
# PARTE 1: DEFINICIÓN GEOMÉTRica Y MODELADO ESTRUCTURAL
# =====================================================================
# Descripción: Modela matemáticamente el corazón anatómico modular
# dividido en secciones independientes mediante listas de coordenadas
# homogéneas [x, y, 1.0], superando el mínimo de 12 vértices requerido[cite: 15].


def generar_cuerpo_principal():
  """Modela el cuerpo principal (ventrículos y miocardio)

  con una silueta anatómica precisa y detallada.
  """
  return [
      [-15, -40, 1.0],
      [15, -50, 1.0],
      [45, -30, 1.0],
      [70, 10, 1.0],
      [75, 55, 1.0],
      [55, 100, 1.0],
      [25, 130, 1.0],
      [0, 150, 1.0],  # Ápice / Punta inferior
      [-25, 130, 1.0],
      [-55, 100, 1.0],
      [-75, 55, 1.0],
      [-70, 10, 1.0],
      [-45, -30, 1.0],
      [-15, -40, 1.0],
  ]


def generar_seccion_izquierda():
  """Modela la sección móvil lateral izquierda (Vena cava / aurícula)."""
  return [
      [-50, -40, 1.0],
      [-65, -60, 1.0],
      [-70, -100, 1.0],
      [-55, -125, 1.0],
      [-40, -125, 1.0],
      [-35, -95, 1.0],
      [-40, -55, 1.0],
      [-50, -40, 1.0],
  ]


def generar_seccion_derecha():
  """Modela la sección móvil superior derecha (Arco aórtico)."""
  return [
      [15, -55, 1.0],
      [35, -75, 1.0],
      [65, -90, 1.0],
      [90, -80, 1.0],
      [100, -60, 1.0],
      [85, -45, 1.0],
      [60, -55, 1.0],
      [30, -50, 1.0],
      [15, -55, 1.0],
  ]


# Inicialización de las geometrías base para la estructura modular
cuerpo_base = generar_cuerpo_principal()
seccion_izq_base = generar_seccion_izquierda()
seccion_der_base = generar_seccion_derecha()

# Factor de escala inicial para ajustar las dimensiones en pantalla
factor_escala = 2.4
for p in cuerpo_base:
  p[0] *= factor_escala
  p[1] *= factor_escala
for p in seccion_izq_base:
  p[0] *= factor_escala
  p[1] *= factor_escala
for p in seccion_der_base:
  p[0] *= factor_escala
  p[1] *= factor_escala