To control the R617FS using the Futaba t7C, you need to send signals using the PPM protocol. This protocol combines all channels into a single signal, which can be sent through a single wire. The R617FS can decode this signal and convert it back into individual channel values.

To generate the PPM signal, you can use the built-in hardware timers of the ESP8266. The following code demonstrates an example of generating a PPM signal with 8 channels:

```lua
-- Set up the hardware timer
tmr.alarm(0, 20, tmr.ALARM_AUTO, function()
    local channels = {1000, 1200, 1400, 1600, 1800, 2000, 2200, 2400}
    local ppm = ""
    for i = 1, #channels do
        ppm = ppm .. string.char(channels[i] / 256, channels[i] % 256)
    end
    uart.write(0, ppm)
end)
```
In this code, we set up a hardware timer that fires every 20 milliseconds. Inside the timer function, we create an array of 8 channel values, each value ranging from 1000 to 2400 microseconds. We then convert each channel value into a two-byte representation using the `string.char()` function and concatenate them together to form the PPM signal. Finally, we write the PPM signal to the UART port using the `uart.write()` function.
