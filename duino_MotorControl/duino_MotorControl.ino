#define driveOut 10
#define scrubOut 9
float dutyD = 0;
float dutyS = 0;
unsigned long time = 0;


void setup(){
  Serial.begin(9600);
  // while(!Serial){
  //   ; // wait for serial port to connect. Needed for native USB
  // }
  pinMode(driveOut, OUTPUT);
  pinMode(scrubOut, OUTPUT);
  TCCR1B &= ~2;
  analogWrite(driveOut, 43);
  delay(500);
}

void loop(){
  
  if (Serial.available() > 0){
    String data = Serial.readStringUntil('\n');
    // Serial.println(data);
    if(data[0] == 'd'){
      data.remove(0, 1);
      dutyD = data.toInt();
      // Serial.print("Drive speed updated to duty: ");
      // Serial.println(dutyD);
      time = millis();
    } else if(data[0] == 'b'){
      data.remove(0, 1);
      dutyS = data.toInt();
      // Serial.print("Scrub speed updated to duty: ");
      // Serial.println(dutyS);
      time = millis();
     } //else{
    //   Serial.println("You sent me jibberish!");
    // }
    
  } else if (!Serial){ //if serial port connection is closed don't command motors
    dutyD = 0;
    dutyS = 0;
  } else if (millis() - time > 750){
    dutyD = 0;
    dutyS = 0;
    time = millis();
    //Serial.println("TIMED OUT");
  }

  if (dutyD > 255) dutyD = 0;
  //else if (dutyD < 0) dutyD = 0;
  else if (dutyD > 192) dutyD = 192;
  else if (dutyD < 43) dutyD = 43;
  if (dutyS > 255) dutyS = 0;
  //else if (dutyS < 0) dutyS = 0;
  else if (dutyS > 192) dutyS = 192;
  else if (dutyS < 43) dutyS = 43;

  analogWrite(driveOut, dutyD);
  analogWrite(scrubOut, dutyS);
}
