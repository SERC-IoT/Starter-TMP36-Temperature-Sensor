# Setup for MKR WiFi 1010 dev board

<!-- #TODO add circuit diagrams and library info -->
Setup instructions for an Arduino MKR WiFi 1010 development board.

## Circuit Diagram
Wire the components as shown in the diagram.

![circuit diagram](assets/mkr-tmp36-sensor-circuit-diagram_schem.png)

#### Components Needed
* TMP36 temperature sensor
* connecting wires
* MKR WiFi 1010 development board

<br />

![breadboard diagram](assets/mkr-tmp36-sensor-circuit-diagram_bb.png)

<br />

### Default Pin Wiring

| Pin No | Function | Device Connection |
| --- | --- | --- |
|  |  |  |
| VCC | +3.3V | Vdd |
| GND | GND | GND |
| A0 | Analogue Input | Vout |
|  |  |  |

![pin diagram](assets/Pinout-MKRwifi1010_latest.png)

<br>

## Arduino

Drivers and board details need to be installed to use the Arduino MKR series. Follow the instructions here: https://www.arduino.cc/en/Guide/MKRWiFi1010#toc2

The arduino sketch does not require any external libraries.
