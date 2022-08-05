#include <Arduino.h>
#include <Stepper.h>

// Define number of steps per rotation:
const int stepsPerRevolution = 64;

Stepper myStepper = Stepper(stepsPerRevolution, 8, 10, 9, 11);

const int leftPin = 4;
const int rightPin = 5;
int left = 0;
int right = 0;

void setup() {
  pinMode(leftPin, INPUT);
  pinMode(rightPin, INPUT);

  myStepper.setSpeed(15);
  
  // Begin Serial communication at a baud rate of 9600:
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  left = digitalRead(leftPin);
  right = digitalRead(rightPin);

  if (left == 1 && right != 1) {
    myStepper.step(stepsPerRevolution);
  }
  else if (right == 1 && left != 1) {
    myStepper.step(-stepsPerRevolution);
  }

  delay(100);
}