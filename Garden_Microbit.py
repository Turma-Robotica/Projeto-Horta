def IRRIGADOR(ONOFF: str):
    if ONOFF == "ON":
        pins.digital_write_pin(DigitalPin.P0, 1)
    else:
        pins.digital_write_pin(DigitalPin.P0, 0)

def on_bluetooth_connected():
    basic.show_string("C")
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_string("D")
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def DECODIFICADOR():
    if led.point(1, 0) and (led.point(2, 0) and (led.point(3, 0) and (led.point(2, 1) and led.point(2, 2)))):
        basic.show_string("TEMPERATURA:")
        basic.show_number(input.temperature())
        basic.clear_screen()
    elif led.point(1, 0) and (led.point(2, 0) and (led.point(2, 1) and (led.point(2, 2) and led.point(3, 2)))):
        basic.show_string("LUMINOSIDADE:")
        basic.show_number(input.light_level())
        basic.clear_screen()
    elif led.point(0, 0) and (led.point(2, 2) and (led.point(0, 4) and (led.point(4, 0) and led.point(4, 4)))):
        basic.show_string("UMIDADE:")
        basic.show_number(UMIDADE)
        basic.clear_screen()
    elif led.point(1, 1) and (led.point(1, 2) and (led.point(2, 3) and (led.point(3, 1) and led.point(3, 2)))):
        IRRIGADOR("ON")
        basic.pause(10000)
        IRRIGADOR("OFF")
        basic.clear_screen()
    elif led.point(2, 2) and (led.point(1, 3) and (led.point(1, 4) and (led.point(3, 3) and led.point(3, 4)))):
        VENTILADOR("ON")
        basic.pause(10000)
        VENTILADOR("OFF")
        basic.clear_screen()
def VENTILADOR(ONOFF2: str):
    if ONOFF2 == "ON":
        pins.digital_write_pin(DigitalPin.P1, 1)
    else:
        pins.digital_write_pin(DigitalPin.P1, 0)
def AUTOMAÇÃO():
    if input.temperature() > 35:
        VENTILADOR("ON")
    else:
        VENTILADOR("OFF")
    if UMIDADE > 60:
        IRRIGADOR("ON")
    else:
        IRRIGADOR("OFF")
UMIDADE = 0
bluetooth.start_led_service()

def on_forever():
    AUTOMAÇÃO()
    DECODIFICADOR()
basic.forever(on_forever)
