int ech2 = 8;
int trig2 = 9;

int ech1 =  2;
int trig1 = 3;

int trig3 = 11;
int ech3 =  10;

int trig4 = 13;
int ech4 =  12;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(ech1, INPUT);
  pinMode(trig1, OUTPUT);
  pinMode(trig2, OUTPUT);
  pinMode(ech2, INPUT);
  pinMode(trig3, OUTPUT);
  pinMode(ech3, INPUT);
  pinMode(trig4, OUTPUT);
  pinMode(ech4, INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  
  digitalWrite(trig2, LOW);
  delayMicroseconds(5);
  
  digitalWrite(trig2, HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trig2, LOW);
  
  long echo2 = pulseIn(ech2, HIGH);

  delay(30);    

  digitalWrite(trig3, LOW);
  delayMicroseconds(5);
  
  digitalWrite(trig3, HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trig3, LOW);
  
  long echo3 = pulseIn(ech3, HIGH);

  delay(30);    

  digitalWrite(trig4, LOW);
  delayMicroseconds(5);
  
  digitalWrite(trig4, HIGH);
  delayMicroseconds(10);
  
  digitalWrite(trig4, LOW);
  
  long echo4 = pulseIn(ech4, HIGH);

  delay(30);    
  
  digitalWrite(trig1, LOW);
  delayMicroseconds(5);
  digitalWrite(trig1, HIGH);
  
  delayMicroseconds(10);
  digitalWrite(trig1, LOW);
  
  long echo1 = pulseIn(ech1, HIGH);
  delay(30);
  
  long x = (echo1 < echo2)?echo1:echo2;
  long y = (echo3 < echo4)?echo3:echo4;
  
  Serial.print("x");
  Serial.println(x/58.2);

  Serial.print("y");
  Serial.println(y/58.2);
  
  Serial.flush();
  delay(200);
}

long * smooth(long * data, int window){
  int prev = 0;
  int count = window;
  int list = sizeof(data);
  int index = 0;
  long * smoothed;
  while(count < list){
    int sum = 0;
    for (int i = prev; i < count; i++){
      sum += data[i];
      
    }
    smoothed[index++] = sum/window;
    prev = count;
    count += window;
  }
  return smoothed;
  
}


