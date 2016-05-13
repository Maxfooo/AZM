const int STEP_DELAY = 5000; //Delay in us

//Pin Assignments
int array0 = 2;
int array1 = 3;
int array2 = 4;
int array3 = 5;
int array4 = 6;
int array5 = 7;
int array6 = 8;
int array7 = 9;
int array8 = 10;
int array9 = 11;
int array10 = 12;
int array11 = 13;

int count = 0;

void intToPinArray(int count);

void setup() {
  pinMode(array0,OUTPUT);
  pinMode(array1,OUTPUT);
  pinMode(array2,OUTPUT);
  pinMode(array3,OUTPUT);
  pinMode(array4,OUTPUT);
  pinMode(array5,OUTPUT);
  pinMode(array6,OUTPUT);
  pinMode(array7,OUTPUT);
  pinMode(array8,OUTPUT);
  pinMode(array9,OUTPUT);
  pinMode(array10,OUTPUT);
  pinMode(array11,OUTPUT);
}

void loop() {
  intToPinArray(count);
  count++;
  if(count > 0xFFF) count = 0;
  delayMicroseconds(STEP_DELAY);
  delayMicroseconds(STEP_DELAY);
}

void intToPinArray(int count)
{
  if((count&0x001) ==0x001) digitalWrite(array0, HIGH);
  else digitalWrite(array0, LOW);
  
  if((count&0x002) ==0x002) digitalWrite(array1, HIGH);
  else digitalWrite(array1, LOW);
  
  if((count&0x004) ==0x004) digitalWrite(array2, HIGH);
  else digitalWrite(array2, LOW);
  
  if((count&0x008) ==0x008) digitalWrite(array3, HIGH);
  else digitalWrite(array3, LOW);
  
  if((count&0x010) ==0x010) digitalWrite(array4, HIGH);
  else digitalWrite(array4, LOW);
  
  if((count&0x020) ==0x020) digitalWrite(array5, HIGH);
  else digitalWrite(array5, LOW);
  
  if((count&0x040) ==0x040) digitalWrite(array6, HIGH);
  else digitalWrite(array6, LOW);
  
  if((count&0x080) ==0x080) digitalWrite(array7, HIGH);
  else digitalWrite(array7, LOW);
  
  if((count&0x100) ==0x100) digitalWrite(array8, HIGH);
  else digitalWrite(array8, LOW);
  
  if((count&0x200) ==0x200) digitalWrite(array9, HIGH);
  else digitalWrite(array9, LOW);
  
  if((count&0x400) ==0x400) digitalWrite(array10, HIGH);
  else digitalWrite(array10, LOW);
  
  if((count&0x800) ==0x800) digitalWrite(array11, HIGH);
  else digitalWrite(array11, LOW);
}
