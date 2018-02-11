/*
 * Sensor Cluster using Sensors Mezzaine on DragonBoard410c
 * Author: Radhika Paralkar
 * Copyright (c) 2017 Linaro Ltd.
 * All rights reserved.
 ********************************
 * 
 * A0 --> Light Sensor
 * A1 --> Temperature Sensor
 * A2 --> Sound Sensor
 * D4 --> Touch Sensor Module
 * D5 --> Button
 * D6 --> Rotary Angle Sensor
 */

//Define the pins for each sensor

const int button = 5;

/*Setup runs only once during the program. Set all sensor pins as 
Input and set the baud rate for serial for printing on the serial port*/

void setup()
{
    Serial.begin(9600);
    pinMode(button, INPUT);
}

void loop() 
{
	int button_val = digitalRead(button);

	Serial.print("Button      | ");
	Serial.println(button_val);

	delay(400);

	Serial.println("");
}