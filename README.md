# Badgercopter

In this project, we try to build a ROS enabled quadcopter that is able to achieve vision based precise landing on a moving ground platform. In the end we realized vision based localization of ground platform, and tracking of ground platform in reality by simulation using high level control. In the documentation below, we will give an introduction about the structure of the system and how to repeat the result.
ESCs
## System Structure

We will cover the structure of the system both in hardware and software.

### Hardware

Shown in figure below, there are two modules for the system, the quadcopter module and the ground vehicle module. Quadcopter module is powered up by the 4s-lipo battery, which will delivered power to BEC, which will help to deliver power to all devices. Battery power will also go through buck converter to have a stable voltage supply for the onboard computer. The onboard computer can communicate with flight controller with FTDI board that converts between usb data and serial data from the telemetry port, and base station can communicate with onboard computer via WiFi as the user interface for autonomous missions. Then, flight controller will deliver calculated MAIN PWM signals to ESC, and ESC will supply designed voltage to rotors to make the quadcopter fly. In addition, flight controller can also communicate with the radio reciever powered by itself, and radio reciever will communicate with radio controller, which will serve as the second user interface. In situations when emergency shutdown/human takeover is needed, radio transmitter can be used to fly the quadcopter manually.

<p align="center">
  <img src="https://github.com/liliocandidior/Badgercopter_Hybrid-Robot-Project/blob/main/figures/hardware%20structure.png" width=70% height=70% alt>
</p>

The built quadcopter module is shown below.

<p align="center">
  <img src="https://github.com/liliocandidior/Badgercopter_Hybrid-Robot-Project/blob/main/figures/quadcopter.jpeg" width=70% height=70% alt>
</p>


In the bill of material below, we provide some items in the system that we choose to use. Details for the requirement of radio receiver and trasmitter are given by [PX4 tutorials](https://docs.px4.io/main/en/getting_started/rc_transmitter_receiver.html).

Item Name | Quantity | Brand
--- | --- | --- 
Onboard Computer | 1 | [Up Shop](https://up-shop.org/up-core-series.html)
Flight Controller | 1 | [Holybro](http://www.holybro.com/product/pixhawk4-mini/)
Radio Receiver | 1 | [FrSky](https://www.amazon.com/FrSky-Receiver-Range-Micro-Drone/dp/B01N5INCBH/ref=pd_day0fbt_img_sccl_1/145-9226582-1490900?pd_rd_w=IvOQO&pf_rd_p=bcb8482a-3db5-4b0b-9f15-b86e24acdb00&pf_rd_r=NZ4JV1J5G63JS3SFRJB4&pd_rd_r=105d34dd-a7cd-4a09-9a8f-e9f62c0818ab&pd_rd_wg=TzE6v&pd_rd_i=B01N5INCBH&psc=1)
Radio Transmitter | 1 | [FrSky](https://www.amazon.com/FrSky-Taranis-Channels-Access-Transmitter/dp/B07RQ4564C/ref=pd_cart_vw_crc_2_3/145-9226582-1490900?_encoding=UTF8&pd_rd_i=B07RQ4564C&pd_rd_r=6621066d-5370-4e98-9bcf-e6b5b499eaaf&pd_rd_w=DOcds&pd_rd_wg=Bnsyr&pf_rd_p=01004c92-8f40-4f1a-bee8-08cb36dccac2&pf_rd_r=41XMCV60EPB5TXTFN6NY&refRID=41XMCV60EPB5TXTFN6NY&th=1)
FTDI Converter | 1 | [FTDI](https://www.amazon.com/HiLetgo-FT232RL-Converter-Adapter-Breakout/dp/B00IJXZQ7C/ref=sr_1_3?crid=27HAG013LEI9W&keywords=ftdi&qid=1652841447&sprefix=ftdi%2Caps%2C87&sr=8-3)
USB Dock | 1 | [Amazon](https://www.amazon.com/Hub%EF%BC%8CVENTION-Ultra-Slim-Splitter-Supported-Compatible/dp/B08GY3GKRC/ref=sr_1_4?crid=1CSPQJDS54JB4&keywords=usb%2Bhub&qid=1652895544&s=electronics&sprefix=usb%2Bhub%2Celectronics%2C81&sr=1-4&th=1)
WiFi Antenna | 1 | [Up Shop](https://up-shop.org/up-core-wifi-antenna-kit.html)
Quadcopter Camera | 1 | [ArduCam](https://www.amazon.com/Arducam-Camera-Microphone-Windows-Android/dp/B09SHKWXB3/ref=sr_1_15?crid=37X4AFQZOKX3J&keywords=arducam&qid=1658869230&sprefix=arducam%2Caps%2C77&sr=8-15&ufe=app_do%3Aamzn1.fos.006c50ae-5d4c-4777-9bc0-4513d670b6bc&th=1)

### Software

The functionality of the system can only be achieved by having multiple agents running synchronously. Shown in the figure below, ROS on the onboard computer will serve as human interface to control the quadcopter. Users can use multi-ROS under same ROS master to achieve remote control of onboard computer, or simply ssh into the computer to achieve remote control. The message published or subscribed in ROS will seek for counterparts in MAVROS (ROS1) or RTPS (ROS2). Then messages will be decoded and transmitted to the requested port (the usb port to ftdi board), with requested protocol (UART for experiment, UDP for sitl simulation). Then, on the flight controller side, messages will be then encoded after being acquired through the telemetry port and goes to the uORB topic, which is the real time parameter in PX4 system. On the other side, when information is requested, the workflow will go the other way from PX4 to onboard computer.

<p align="center">
  <img src="https://github.com/liliocandidior/Badgercopter_Hybrid-Robot-Project/blob/main/figures/communication.png" width=70% height=70% alt>
</p>

## Resources

### PX4

### Motion Capture


### Ubuntu
https://github.com/up-board/up-community/wiki/Ubuntu_20.04

skip HAT -- cannnot locate upboard-extras
