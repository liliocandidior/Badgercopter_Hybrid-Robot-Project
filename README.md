# Badgercopter

In this project, we try to build a ROS enabled quadcopter that is able to achieve vision based precise landing on a moving ground platform. In the end we realized vision based localization of ground platform, and tracking of ground platform in reality by simulation using high level control. In the documentation below, we will give an introduction about the structure of the system and how to repeat the result.
ESCs
## System Structure

We will cover the structure of the system both in hardware and software.

### Hardware

Shown in figure below, there are twi modules for the system, the quadcopter module and the ground vehicle module. Quadcopter module is powered up by the 4s-lipo battery, which will delivered power to BEC, which will help to deliver power to all devices. Battery power will also go through buck converter to have a stable voltage supply for the onboard computer. The onboard computer can communicate with flight controller with FTDI board that converts between usb data and serial data from the telemetry port, and base station can communicate with onboard computer via WiFi as the user interface for autonomous missions. Then, flight controller will deliver calculated MAIN PWM signals to ESC, and ESC will supply designed voltage to rotors to make the quadcopter fly. In addition, flight controller can also communicate with the radio reciever powered by itself, and radio reciever will communicate with radio controller, which will serve as the second user interface. In situations when emergency shutdown/human takeover is needed, radio transmitter can be used to fly the quadcopter manually.

### Software

The functionality of the system can only be achieved by having multiple agents running synchronously. 

## Resources

### PX4

### Motion Capture


### Ubuntu
https://github.com/up-board/up-community/wiki/Ubuntu_20.04

skip HAT -- cannnot locate upboard-extras
