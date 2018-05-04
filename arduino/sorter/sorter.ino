#include <Servo.h>

#define BINS 10 // indexes 0..n-2, n-1 is overflow
#define SSDA 8
#define SSDB 9
#define SSDC 10
#define SSDD 11
#define SERVO 3 //used for positioning chute
#define SERVO_ANGLE 15

Servo positionServo;

void setup() {
  Serial.begin(9600);
  pinMode(SSDA, OUTPUT);
  pinMode(SSDB, OUTPUT);
  pinMode(SSDC, OUTPUT);
  pinMode(SSDD, OUTPUT);
  positionServo.attach(SERVO);
}

void loop() {
  while (Serial.available() < 1);
  
  byte bin = Serial.read();
  
  //setPosition(bin);

  digitalWrite(SSDA, bin & 0b0001);
  digitalWrite(SSDB, bin & 0b0010);
  digitalWrite(SSDC, bin & 0b0100);
  digitalWrite(SSDD, bin & 0b1000);
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
