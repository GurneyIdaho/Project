/*
created 25/11/2024 by Charlie Jones by appropriating  arduino docs for serial communication and servo example
 */
 #include <Servo.h>
Servo myservo;  // create servo object to control a servo
int pos = 0;    // variable to store the servo position

char incomingByte = 0;
void setup() {
    Serial.begin(9600);
    myservo.attach(9);  // attaches the servo on pin 9 to the servo object
    while (!Serial) { //delay until port has opened
    ;
    }
}

void loop() {
  if (Serial.available() > 0) { // if byte waiting

        // read the incoming byte:

        incomingByte = Serial.read();
        switch (incomingByte){
          case 'l':
            pos +=10;
            break;
          case 'r':
            pos -=10;
            break;
          default: // in case invalid command is given
          break;
        }

        Serial.println(incomingByte);

      }
  myservo.write(pos);
  delay(150);


}

