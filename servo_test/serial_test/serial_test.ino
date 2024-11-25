/*
created 25/11/2024 by Charlie Jones by appropriating  arduino docs for serial communication
 */
char incomingByte = 0;
void setup() {
    Serial.begin(9600);
    while (!Serial) { //delay until port has opened
    ;
    }
}

void loop() {
  if (Serial.available() > 0) { // if byte waiting

        // read the incoming byte:

        incomingByte = Serial.read();

        Serial.println(incomingByte);

      }


}
