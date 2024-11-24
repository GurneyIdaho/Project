/* Sweep
 by BARRAGAN <http://barraganstudio.com>
 This example code is in the public domain.

 modified 8 Nov 2013
 by Scott Fitzgerald
 https://www.arduino.cc/en/Tutorial/LibraryExamples/Sweep
*/

#include <Servo.h>

Servo yaw;  // initialise server objects for both dimensions
Servo pitch;


int yawValue; // initialise variables to store the coordinates
int pitchValue;
int yawPotLeft = A0; //initialise input pins
int pitchPotRight = A1;


void setup() {
    yaw.attach(9);  // attaches servo objects to pins
  pitch.attach(10);
}

void loop() {
  yawValue = analogRead(yawPotLeft);            // reads the value of the potentiometer (value between 0 and 1023)
  pitchValue = analogRead(pitchPotRight);            // reads the value of the potentiometer (value between 0 and 1023)
  yawValue = map(yawValue, 0, 1023, 0, 180);     // scale it for use with the servo (value between 0 and 180)
  pitchValue = map(pitchValue, 0, 1023, 0, 180);     // scale it for use with the servo (value between 0 and 180)
  delay(15);                           // waits for the servo to get there
  yaw.write(yawValue);              // tell servo to go to position
  pitch.write(pitchValue);
}
