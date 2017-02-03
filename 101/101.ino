#include "CurieIMU.h"
#include <SoftwareSerial.h>

//uncomment for serial messages
//#define SERIAL_MSG

#define BL_TX 2
#define BL_RX 3

float gx, gy, gz; //scaled Gyro values

SoftwareSerial bluetooth(BL_TX, BL_RX);

void setup() {
  bluetooth.begin(115200);  // The Bluetooth Mate defaults to 115200bps

  #ifdef SERIAL_MSG
  Serial.begin(9600); // initialize Serial communication
  #endif

  CurieIMU.begin();

  // Set the accelerometer range to 250 degrees/second
  CurieIMU.setGyroRange(250);
}

void loop() {
  // read gyro measurements from device, scaled to the configured range
  CurieIMU.readGyroScaled(gx, gy, gz);
  
  char *buffer;
  buffer = (char*) malloc(80);
  
  sprintf(buffer, "%f:%f:%f", gx, gy, gz);

  #ifdef SERIAL_MSG
  Serial.println(buffer);
  #endif
  
  bluetooth.println(buffer);
  delay(100);
  free (buffer);
}
