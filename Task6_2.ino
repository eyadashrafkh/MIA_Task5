const int encoderPinA = 2;
const int encoderPinB = 3;

volatile int count = 0;
volatile int prevState = 0;

void setup() {
  Serial.begin(9600);

  pinMode(encoderPinA, INPUT);
  pinMode(encoderPinB, INPUT);

  attachInterrupt(digitalPinToInterrupt(encoderPinA), handleEncoderInterrupt, CHANGE);
  attachInterrupt(digitalPinToInterrupt(encoderPinB), handleEncoderInterrupt, CHANGE);
}

void loop() {
  Serial.println(count);
  delay(100);
}

void handleEncoderInterrupt() {
  int currState = digitalRead(encoderPinA);

  if (prevState != currState) {
    if (digitalRead(encoderPinB) != currState) {
      count++;
    } else {
      count--;
    }
    prevState = currState;
  }
}