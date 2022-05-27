

#include <Servo.h>

Servo myservoz; 
Servo myservox; 

int move_delay=15;
int z_diff=2;

const int pingPin = 7; // Trigger Pin of Ultrasonic Sensor
const int echoPin = 6; // Echo Pin of Ultrasonic Sensor


int posx = 0;   
int posz = 0;
void setup() {
     pinMode(pingPin, OUTPUT);
   pinMode(echoPin, INPUT);
  myservox.attach(9); 
  myservoz.attach(10);  
  Serial.begin(115200);
} 


long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}

long read_ultrasonic(){
   long duration, inches, cm;

   digitalWrite(pingPin, LOW);
   delayMicroseconds(2);
   digitalWrite(pingPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(pingPin, LOW);
   
   duration = pulseIn(echoPin, HIGH);
  return microsecondsToCentimeters(duration);
  
}


void print_pos(){
  long distance_cm=read_ultrasonic();
          Serial.print(posx);  
    Serial.print(",");
    Serial.print(posz);
    Serial.print(",");
    Serial.print(distance_cm);
    Serial.println(""); 
}



void loop() {
  for (posx = 0; posx <= 180; posx += 10) { 


   myservox.write(posx); 
   Serial.println(posx%2);
    if((posx/10)%2){
       

      for (posz = 0; posz <= 180; posz += z_diff) { 

    myservoz.write(posz);
print_pos();
    delay(move_delay);                    
  }

    }else{
   for (posz = 180; posz >= 0; posz -= z_diff) {


    myservoz.write(posz);  
    print_pos();
    delay(move_delay);  
                  
  }
    }
  }
  
  for (posx = 180; posx >= 0; posx -= 10) {                
 
   myservox.write(posx); 
   Serial.println(posx%2);
    if((posx/10)%2){
       
   for (posz = 180; posz >= 0; posz -= z_diff) {


    myservoz.write(posz);  
    print_pos();
    delay(move_delay);  
                  
  }

    }else{

      
      for (posz = 0; posz <= 180; posz += z_diff) { 

    myservoz.write(posz);
print_pos();
    delay(move_delay);                    
  }

    }
 }
}
