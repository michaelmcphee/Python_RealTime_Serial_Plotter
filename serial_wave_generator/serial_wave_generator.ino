#include <math.h>
#define PI 3.1415926535897932384626


void setup() {
  Serial.begin(9600);
}

void loop() {
  double currentTime = micros() / 1e6;

  double value = sin(2*PI*currentTime);

  Serial.print(currentTime);
  Serial.print(" ");
  Serial.print(value);
  Serial.println();

}