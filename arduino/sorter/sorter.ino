#include <Servo.h>

#define BINS 10 // indexes 0..n-2, n-1 is overflow
#define LED 13
#define SERVO 3 //used for positioning chute
#define SERVO_ANGLE 15

Servo positionServo;

void setup() {
  Serial.begin(9600);
  pinMode(LED, OUTPUT);
  positionServo.attach(SERVO);
}

void loop() {
  while (Serial.available() < 1);
  
  byte bin = Serial.read();
  
  for (int i = 0; i < bin+1; i++) {
    digitalWrite(LED, HIGH);
    delay(500);
    digitalWrite(LED, LOW);
    delay(500);
  }
}

// Bins start at index 0
void setPosition(int bin) {
  // set overflow bin
  if (bin > BINS - 1) {
    bin = BINS - 1;
  }
  // TODO servo angle offset
  positionServo.write(bin * SERVO_ANGLE);
}
