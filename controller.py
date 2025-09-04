import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

class UltrasonicSensor:
    def __init__(self, trigger_pin, echo_pin):
        self.trigger_pin = trigger_pin
        self.echo_pin = echo_pin

        GPIO.setup(self.trigger_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)

    def distance(self):
        GPIO.output(self.trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(self.echo_pin, False)

        #Tiempos de retorno de echo
        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(GPIO_ECHO) == 0:
            start_time = time.time()
        while GPIO.input(GPIO_ECHO) == 1:
            stop_time = time.time()

        # Calcular la distancia en centímetros
        time_elapsed = stop_time - start_time
        distance_cm = (time_elapsed * 34300) / 2
        return distance_cm

@staticmethod
def cleanup():
    GPIO.cleanup()