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
        val = analogRead(analogPin);
        if (data.compareTo("start"))
        {
            Serial.print(val);
        }
        else
        {
            Serial.print("fatal error");
        }
    }
}