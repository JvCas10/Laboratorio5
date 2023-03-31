#include <Ultrasonic.h>

#define TRIGGER_PIN  13
#define ECHO_PIN     10

Ultrasonic ultrasonic(TRIGGER_PIN, ECHO_PIN);

void setup()
  {
  Serial.begin(9600);
  }

void loop()
  {
  
  float cmMsec;
  //lee el tiempo del ultrasonico
  long microsec = ultrasonic.timing();

  //calcula la distancia
  cmMsec = ultrasonic.convert(microsec, Ultrasonic::CM);
  //mandar al puerto serial
  Serial.print(int(cmMsec));
  Serial.print(",");
  Serial.println(0);


   delay(100);
  }