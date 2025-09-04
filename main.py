import time
from controller import UltrasonicSensor

# Altura total de la cisterna en cm
ALTURA_TOTAL = 100

# Altura del agua cuando la cisterna está llena en cm

cisterna = UltrasoniSensor(trigger_pin=7, echo_pin=11)

try:
    while True:
        dist = cisterna_sensor.distance()
        nivel_agua = ((ALTURA_TOTAL - dist) / (ALTURA_TOTAL - ALTURA_LLENA)) * 100
        nivel_agua = max(0, min(100, nivel_agua)) # Limitar entre 0% y 100%
        printf(f"Nivel de agua: {nivel_agua:.2f}%")
        time.sleep(1)

except KeyboardInterrupt:
    UltrasonicSensor.cleanup()
    printf("\nPrograma terminado correctamente.")
