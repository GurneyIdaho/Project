// created Charlie Jones 26.11.2024, adapted from Robin2's serial communication code
// Example 5 - Receive with start- and end-markers combined with parsing 
//This demo expects 2 ints <int1,int2> from the serial port, and moves the servos for yaw (9) and pitch (10)
//
#include <stdio.h>
#include <Servo.h>
#include <stdlib.h>
Servo yawServo;  // initialise server objects for both dimensions
Servo pitchServo;
const int servoSpeed = 2;//servo speed per degree 0.12 Sec / 60 = , 2 degree per ms
const byte numChars = 32;
char receivedChars[numChars];
char tempChars[numChars];        // temporary array for use when parsing

char positionReport[50]; //array to store reply

      // variables to hold the parsed data
int yaw = 0;
int pitch = 0;
int yawPosition = 0;
int pitchPosition = 0;


boolean newData = false;

//============

void setup() {
    Serial.begin(115200);
    yawServo.attach(9);  // attaches servo objects to pins
    pitchServo.attach(10);
    yawServo.write(yaw);
    pitchServo.write(pitch);
}

//============

void loop() {
    recvWithStartEndMarkers();
    if (newData == true) {
        strcpy(tempChars, receivedChars);
            // this temporary copy is necessary to protect the original data
            //   because strtok() used in parseData() replaces the commas with \0
        parseData();
        sprintf(positionReport,"<Position(%d,%d)>",yaw,pitch);
        Serial.println(positionReport);
        newData = false;
        moveServo(yawPosition,pitchPosition,yaw,pitch);
        yawPosition = yaw;
        pitchPosition = pitch;
    }
}

//============

void recvWithStartEndMarkers() {
    static boolean messageIncoming = false;
    static byte messsageIndex = 0;
    char startMarker = '<';
    char endMarker = '>';
    char currentByte;

    while (Serial.available() > 0 && newData == false) {
        currentByte = Serial.read();

        if (messageIncoming == true) {
            if (currentByte != endMarker) {
                receivedChars[messsageIndex] = currentByte;
                messsageIndex++;
                if (messsageIndex >= numChars) {
                    messsageIndex = numChars - 1;
                }
            }
            else {
                receivedChars[messsageIndex] = '\0'; // terminate the string
                messageIncoming = false;
                messsageIndex = 0;
                newData = true;
            }
        }

        else if (currentByte == startMarker) {
            messageIncoming = true;
        }
    }
}

//============

void parseData() {      // split the data into its parts,
// turns data in form x,y into integers with for yaw and pitch

    char * currentSlice; // this is used by strtok() as an index

    currentSlice = strtok(tempChars, ","); // extract int 1
    yaw = atoi(currentSlice);     // convert 

    currentSlice = strtok(NULL, ","); // extract int 2
    pitch = atoi(currentSlice);     // convert

}

void moveServo(int oldYaw,int oldPitch,int newYaw,int newPitch){
  yawServo.write(newYaw);              // tell servo to go to position
  pitchServo.write(newPitch);
  int deltaYaw = abs(oldYaw-newYaw);
  int deltaPitch = abs(oldPitch-newPitch);
  int waitTime = max(deltaYaw,deltaPitch)*servoSpeed;
  delay(waitTime);
}

