/*
 * Example using a button to control an LED
 * Copyright (c) 2016 Linaro Ltd.
 * SPDX-License-Identifier: BSD-2-Clause
 */
int led_pin = 3;
int button_pin = A0;

void setup()
{
    pinMode(led_pin, OUTPUT);
    pinMode(button_pin, INPUT);
}

bool last_button = false;
void loop()
{
    bool button = digitalRead(button_pin);
    if (last_button != button)
    {
        if (button) {
            print("hello")
        }
        delay(100);
    }
    last_button = button;
}