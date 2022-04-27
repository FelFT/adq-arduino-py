#define POT A0

float voltage = 0;

void setup()
{
	pinMode(POT, INPUT);
    Serial.begin(9600);
}

void loop()
{
	voltage = analogRead(POT);
    Serial.println(voltage);
    delay(100);
}
