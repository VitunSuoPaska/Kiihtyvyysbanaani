#include "CurieIMU.h"

float gx, gy, gz; //scaled Gyro values

void setup() {
  Serial.begin(9600); // initialize Serial communication
  while (!Serial);    // wait for the serial port to open

  CurieIMU.begin();

  // Set the accelerometer range to 250 degrees/second
  CurieIMU.setGyroRange(250);
}

void loop() {
  // read gyro measurements from device, scaled to the configured range
  CurieIMU.readGyroScaled(gx, gy, gz);
  
  char *buffer;
  buffer = (char*) malloc(80);
  
  sprintf(buffer, "%f : %f : %f", gx, gy, gz);

  Serial.println(buffer);
  delay(100);
  free (buffer);
}
