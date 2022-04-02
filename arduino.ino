
int val = 0;
int analogPin = A0;
void setup()
{
  Serial.begin(9600);
}
void loop()
{
  if (Serial.available() > 0)
  {
    String data = Serial.readString();
    if (data.equalsIgnoreCase("start"))
    {
      val = analogRead(analogPin);
      Serial.print(val);
      Serial.flush();
    }
    else
    {
      Serial.print("fatal error");
      Serial.flush();
    }
  }
}
