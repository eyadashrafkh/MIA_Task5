#include <NewPing.h>

#define TRIGGER_PIN_1 2
#define ECHO_PIN_1 3
#define TRIGGER_PIN_2 4
#define ECHO_PIN_2 5
#define TRIGGER_PIN_3 6
#define ECHO_PIN_3 7
#define TRIGGER_PIN_4 8
#define ECHO_PIN_4 9

const float sensorX[4] = {0, 5, 5, 0};
const float sensorY[4] = {0, 0, 6, 6};

float distance[4];

float posX, posY;

NewPing sonar_1(TRIGGER_PIN_1, ECHO_PIN_1);
NewPing sonar_2(TRIGGER_PIN_2, ECHO_PIN_2);
NewPing sonar_3(TRIGGER_PIN_3, ECHO_PIN_3);
NewPing sonar_4(TRIGGER_PIN_4, ECHO_PIN_4);

void setup() {
  Serial.begin(9600);
}

void loop() {

  distance[0] = sonar_1.ping_cm();
  distance[1] = sonar_2.ping_cm();
  distance[2] = sonar_3.ping_cm();
  distance[3] = sonar_4.ping_cm();

  posX = ((distance[0] * distance[0] - distance[1] * distance[1] + sensorX[1] * sensorX[1]) / (2 * sensorX[1]) +
          (distance[0] * distance[0] - distance[2] * distance[2] + sensorX[2] * sensorX[2]) / (2 * sensorX[2])) / 2;
  posY = ((distance[0] * distance[0] - distance[3] * distance[3] + sensorY[3] * sensorY[3]) / (2 * sensorY[3]) +
          (distance[0] * distance[0] - distance[2] * distance[2] + sensorY[2] * sensorY[2]) / (2 * sensorY[2])) / 2;

  Serial.print("Position: (");
  Serial.print(posX);
  Serial.print(", ");
  Serial.print(posY);
  Serial.println(")");

  delay(1000);
}