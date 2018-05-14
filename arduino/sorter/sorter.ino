#include <Servo.h>

#define BINS 10 // indexes 0..n-2, n-1 is overflow
#define SSDA 8
#define SSDB 9
#define SSDC 10
#define SSDD 11
#define SERVO 5 //used for positioning chute.. max write(5..180)
#define SERVO_ANGLE_OFF 5
#define SERVO_ANGLE_INC 15
#define MOTOR 5 //used for spinning turntable
#define TURN_TIME 500 // time to run the turntable motor for
Servo positionServo;

void setup() {
  Serial.begin(9600);
  pinMode(SSDA, OUTPUT);
  pinMode(SSDB, OUTPUT);
  pinMode(SSDC, OUTPUT);
  pinMode(SSDD, OUTPUT);
  pinMode(MOTOR, OUTPUT);
  positionServo.attach(SERVO);
}

void loop() {
  // Position table for next bolt
  //moveTable();

  // Signal Pi to Capture Image
  //Serial.write(0x01);

  // Wait for byte available and read it
  while (Serial.available() < 1);
  byte bin = Serial.read();

  // set overflow bin
  if (bin > BINS - 1) {
    bin = BINS - 1;
  }

  // Set Chute position
  setPosition(bin);

  // Write Bin # to SSD
  digitalWrite(SSDA, bin & 0b0001);
  digitalWrite(SSDB, bin & 0b0010);
  digitalWrite(SSDC, bin & 0b0100);
  digitalWrite(SSDD, bin & 0b1000);
}

void moveTable() {
  digitalWrite(MOTOR, HIGH);
  delay(TURN_TIME);
  digitalWrite(MOTOR, LOW);
}

// Bins start at index 0
void setPosition(int bin) {
  positionServo.write(SERVO_ANGLE_OFF + (bin * SERVO_ANGLE_INC));
}
