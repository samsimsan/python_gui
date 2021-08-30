char val;
void setup() {
  Serial.begin(9600);
}
int a = 1;


void loop() {
  if(Serial.available()>0){
    val = Serial.read();
      if(val == '1'){
          Serial.println(a*2);
          Serial.println(a*5);
          Serial.println(a*7);
          Serial.println(a*100);
          delay(1000);
          a++;
      }
  }
//  if(Serial.available() >0){
//    val = Serial.read();
//    if (val == '1'){
//      Serial.println(a*2);
//      a++; 
//    }
//    else if(val == '2'){
//      Serial.println(a*3);
//      a++;
//    }
//    else if(val == '3'){
//      Serial.println(a*10);
//      a++;
//    }
//    else if(val == '4'){
//      Serial.println(a*5);
//      a++;
//    }
// }
}
