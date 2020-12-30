/*
 * Simple sketch that reads the analogue voltage from a TMP36 temperature sensor,
 * converts the voltage reading to temperature, and prints that temperature to
 * the serial console.
 *
 * The TMP36 uses an analogue voltage with 10mV per degree resolution, with a
 * 500mV offset to allow for negative temeratures.
 */

//TMP36 Pin Variables
int sensorPin = A0; // the analog pin the TMP36's Vout (sense) pin is connected to
                    // for ESP32, use pin 34

// ARef or voltage range of board's ADC. Some calibration may be required,
// particularly for ESP8266 or ESP32 boards.
// For 5v arduino, use 5.0
// For 3.3v arduino, use 3.3
// For D1 mini, use between approx 3.03 to 3.2
// For Lolin32, use between approx 1.0 to 1.08
float aRef = 3.3;

void setup()
{
  Serial.begin(9600);  //Start the serial connection with the computer
                       //to view the result open the serial monitor
}

void loop()
{
  // get the voltage reading from the temperature sensor
  // reading is 10-bit bit depth
  int reading = analogRead(sensorPin);

  // convert that reading to voltage
  float voltage = reading * aRef / 1024.0;

  // print out the voltage
  Serial.print(voltage); Serial.println(" volts");

  // convert voltage to temperature
  // 10 mv per degree with 500 mV offset
  float temperatureC = (voltage - 0.5) * 100;  //multiple by 100 is same as divide by 0.01 (10mV)

  // now print out the temperature
  Serial.print(temperatureC); Serial.println(" degrees C");

  delay(1000); //wait a second
}
