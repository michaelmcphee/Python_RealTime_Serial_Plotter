#include <math.h>  // Include the math library for mathematical functions
#define PI 3.1415926535897932384626  // Define the value of PI

void setup() {
  Serial.begin(9600);  // Initialize serial communication at 9600 baud rate
}

void loop() {
  double currentTime = micros() / 1e6;  // Get the current time in seconds

  double value = sin(2 * PI * currentTime);  // Calculate the sine of the current time

  Serial.print(currentTime);  // Print the current time to the serial port
  Serial.print(" ");  // Print a space to separate the values
  Serial.print(value);  // Print the sine value to the serial port
  Serial.println();  // Print a newline character to end the line
}