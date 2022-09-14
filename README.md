# ROS2 - PX4 Bridge Setup (Stall)
** This work is ended due to failure of command transmission from companion computer to flight controller **
## Companion Computer Setup
 - Install Linux and enable wifi connection
   - Please check requirement of companion computer to install specific linux system. For Up Core, Ubuntu 20.04 can be installed below.
  https://github.com/up-board/up-community/wiki/Ubuntu_20.04
   - Following the tutorial, also enable wifi and bluetooth connection, and UART functionality.
   
 - Install preliminaries
   - Please install Java (JDK8), Gradle and Foonathan memory based on this link: https://docs.px4.io/v1.12/en/dev_setup/fast-dds-installation.html.
   - Not sure whether any package is installed, please use “-version” or “-v” parameter to check the version.
   
 - Install fast DDS(RTPS)
   - Follow the Fast DDS Installation Guide to install Fast RTPS(DDS) 2.0.2 (or later) and Fast-RTPS-Gen 1.0.4 (not later!) and their dependencies: https://docs.px4.io/main/en/dev_setup/fast-dds-installation.html.
   - Please make sure which ROS2 version you are planning to install. Different versions will need to download different DDS/RTPS.
   
 - Install ROS2
   - It is recommended to Install ROS 2 Foxy: https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html.
   - Follow the ROS2 User Guide to manually install some dependencies and tools: https://docs.px4.io/main/en/ros/ros2_comm.html
   
 - Build ROS2 workspace
   - Follow the ROS2 User Guide to build ROS2 workspace: https://docs.px4.io/main/en/ros/ros2_comm.html.
   
## Communication Setup
 - Flight Controller - Companion Computer
   - Port Configuration
     - For Pixhawk mini4, we used TELEM 1 port as the communication port with the companion computer
     - We configured the TELEM 1 port in QGround control using the command: MAV_0_CONFIG (refer to https://docs.px4.io/main/en/peripherals/mavlink_peripherals.html). By configure TELEM 1 port using this command, Pixhawk mini4 can then communicate with the companion computer using Mavlink protocol via TELEM 1 port.
   - Hardware Wiring
     - Since the companion computer is running ROS2, MAVROS is not needed.
     - If the companion computer and Pixhawk mini4 is connected wirelessly, then you should install MAVLink Router (https://github.com/mavlink-router/mavlink-router) (recommended) or MAVProxy (https://ardupilot.org/mavproxy/) to route MAVLink between serial and UDP.
     - We connect TELEM 1 and companion computer USB port via a FTDI chip, which is a serial-to-USB adapter board. (https://docs.px4.io/main/en/companion_computer/pixhawk_companion.html)
     - In addition to FTDI cable, use another cable to connect the usb port of the flight controller in order access into its interface.
     - Refer to (https://docs.px4.io/main/en/companion_computer/pixhawk_companion.html) for detail for setups. You can ignore the “Serial Port Software setup on Linux” part if you are using ROS2. We couldn’t figure out a way to see out pixhawk using lsusb command in out companion computer, but the communication was still established after setting up client and agent.
   - Setup Client & Agent
     - Refer to the https://docs.px4.io/main/en/middleware/micrortps.html.
     - To build client in px4, you need to access to the PX4 console first, please refer to https://docs.px4.io/main/en/debug/system_console.html (USB wire from companion computer to the microUSB port on PX4) (for PX4 mini port info, refer to https://docs.px4.io/main/en/flight_controller/pixhawk4_mini.html)
     - Use “make px4_fmu-v4_rtps upload” command in companion computer to build and upload RTPS to PX4. Different hardware is using fmu, only the correct version is able to build communication. If the upload process stop and ask for “Bootloader”, simply stop the process and take off and replug in all connection to let the flight controller reboot. It will start again at where you stop.
     - Enter PX4 console with the extra usb connection other than ftdi using “screen /dev/ttyXXX BAUDRATE 8N1” (use ls /dev/tty* and watch what changes when unplugging / replugging the USB device), ours is /dev/ttyACM0; BAUDRATE is 57600.
     - In the PX4 console, enter “micrortps_client start -d /dev/ttyXXX -b BAUDRATE”, for TELEM1 port on PX4, it’s /dev/tty/S1 (for PX4 mini port info, refer to this link), and BAUDRATE is 921600. This is connected to the ftdi cable, which is connected to telem1.
     - Turn on the RTPS agent using “micrortps_agent start -t UART -d /dev/ttyXXX -b 921600”. Please check the port of FTDI using “ls /dev/tty*” to replace XXX. (try to unplug and then plug wire again if there is any problem)
     - Right now, both RTPS agent and client is initiated, and you can test the connection using “micrortps_client status” in px4 console.
     - If the console terminates each time after you run the RTPS client,please modify a parameter in PX4-Autopliote workspace andre-upload the RTPS client firmware.(https://github.com/PX4/PX4-Autopilot/issues/19482)
     

