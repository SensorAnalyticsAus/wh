## About
Python code for detecting water spills

## Requirements
* Any Raspberrypi with GPIO header pins
* [Commonly available rain sensor module](https://github.com/SensorAnalyticsAus/wh/blob/main/watersensor.png)

## Wiring Sensor -> RPI<br>
VCC -> Pin1 (+3.3V)<br>
GND -> Pin6 (Ground)<br>
D0 -> Pin11 (GPIO 17)


## Notifications
This program relies on Pushover to send phone alerts.

## Use
`ctrl-wh start`

## Good to do
Adding `@reboot ctrl-wh` to cron
