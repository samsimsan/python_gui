char val;
void setup() {
  Serial.begin(9600);
}

void loop() {
  if(Serial.available() >0){
    val = Serial.read();
    if (val == '1'){
      Serial.println('1'); 
    }
    else if(val == '2'){
      Serial.println('2');
    }
    else if(val == '3'){
      Serial.println('3');
    }
    else if(val == '4'){
      Serial.println('4');
    }
 }
}
