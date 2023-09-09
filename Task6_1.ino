#include <Wire.h>

const int MPU6050_ADDR = 0x68;
const int PWR_MGMT_1 = 0x6B;
const int GYRO_ZOUT_H = 0x47;
const int GYRO_ZOUT_L = 0x48;
const float GYRO_SCALE_FACTOR = 131.0;

void setup() {
  Wire.begin();
  Serial.begin(9600);

  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(PWR_MGMT_1);
  Wire.write(0x00);
  Wire.endTransmission();
}

void loop() {
  int16_t gyroZ;
  Wire.beginTransmission(MPU6050_ADDR);
  Wire.write(GYRO_ZOUT_H);
  Wire.endTransmission(false);
  Wire.requestFrom(MPU6050_ADDR, 2, true);
  gyroZ = Wire.read() << 8 | Wire.read();

  float angularVelocity = gyroZ / GYRO_SCALE_FACTOR;

  static float yawAngle = 0.0;
  float deltaTime = 0.01;
  yawAngle += angularVelocity * deltaTime;

  Serial.print("Yaw angle: ");
  Serial.print(yawAngle);
  Serial.println(" degrees");

  delay(1000);
}