
#include <EEPROM.h>

int addr = 0;

void setup() {

  Serial.begin(9600);
  pinMode(A0, INPUT);
  //pinMode(11, OUTPUT);
  //analogWrite(11, 100);
  Serial.println("Starting!");
  
}

void loop() {
  
  int val = floor(analogRead(0) / 4);
  EEPROM.write(addr, val);
  addr++;
  if (addr == EEPROM.length()) {
    Serial.println("Finished");
    while(1){
      
    }
  }

  delay(300);
}
