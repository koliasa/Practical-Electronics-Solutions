import machine
import utime

def init_uart_for_gps(tx_pin=5, rx_pin=4):
    try:
        uart = machine.UART(1, baudrate=9600, tx=tx_pin, rx=rx_pin, timeout=1000)
        print("UART settings for GPS:", uart)
        return uart
    except Exception as e:
        print("Failed to initialize UART for GPS:", e)
        return None

def init_led():
    led = machine.Pin(2, machine.Pin.OUT)  # Використовуйте пін D4 (GPIO2) для вбудованого LED
    return led

if __name__ == "__main__":
    uart_for_gps = init_uart_for_gps(5, 4)  # Встановіть відповідні значення для TX та RX пінів
    led_for_gps = init_led()

    if uart_for_gps:
        try:
            while True:
                sentence = uart_for_gps.readline()
                if sentence.startswith(b'$'):
                    print(sentence.decode('utf-8').strip())
                    led_for_gps.on()  # Вмикаємо постійний світлодіод
                    utime.sleep(1)
                    led_for_gps.off()  # Вимикаємо світлодіод
                    utime.sleep(1)
                else:
                    led_for_gps.toggle()  # Замість мигаючого LED можна використовувати toggle()
                    utime.sleep(0.1)
        except KeyboardInterrupt:
            print("Програма завершена користувачем.")
