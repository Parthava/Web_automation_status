const int BLUE=8;
const int YELLOW=9;
const int RED=10;
char data;

void setup()
{
  pinMode(BLUE,OUTPUT);
  pinMode(YELLOW,OUTPUT);
  pinMode(RED,OUTPUT);
  digitalWrite(RED,HIGH);
  digitalWrite(BLUE,LOW);
  digitalWrite(YELLOW,LOW);
  Serial.begin(9600);
}

void loop()
{
  if(Serial.available()>0)
  {
    data=Serial.read();
    Serial.println(data);
  }
  if(data=='1')
  {
    digitalWrite(RED,LOW);
    digitalWrite(YELLOW,HIGH);
    digitalWrite(BLUE,LOW);
  }
  else if(data=='0')
  {
    digitalWrite(RED,LOW);
    digitalWrite(YELLOW,LOW);
    digitalWrite(BLUE,HIGH);
  }
}
