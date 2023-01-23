## Vision-based Precise Landing

### Choose Appropriate Camera
  
 **Requirements:**
  - compatible with companion computer (Upcore usb2.0)
  - compatible with linux (version 20.xx)
  - 720p with a 23-meter detection altitude or 1080p with a 32-meter detection altitude
  
 **Prefer:**
  - wide angle
  - HD or ultra HD
    
 **8MP IMX179 with 150° Wide Angle M12 Lens Camera Module-Arducam*
    https://www.arducam.com/product/8mp-imx179-with-150-wide-angle-m12-lens-camera-module-arducam-ub0239/
    
  - usb2.0
  - compatible with linux, MacOS, Windows 7/8/10
  - 30fps@1080p
  - 150-degree wide angle
  - ultra HD
    
    
### Setting Up Operating Environment

   *Dependencies:*
   - UVC driver
   - OpenCV >3.0
   - OpenCV-contrib
   - ArUco >3.0
   - Dronekit
    
 ***for MacOS**\
  Download OpenCV via Homebrew: [https://pyimagesearch.com/2016/12/19/install-opencv-3-on-macos-with-homebrew-the-easy-way/]
  Build and install ArUco via cmake
  
   - install XCode via App Store
   - accept lisence
     ```
     sudo xcodebuild -license
     ```
   - install Apple command line tool
     ```
     sudo xcode-select --install
     ```
   - install Homebrew
     ```
     ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
     brew update
     ```
      define path that will include python3.x-config
     ```
     nano ~/.bash_profile
     '''
     write  # Homebrew
            export PATH=/usr/local/bin:$PATH
     '''
     ```
     apply the changes
     ```
     source ~/.bash_profile
     ```
   - install python (different from system version)
     ```
     brew install python python3
     ```
   - install opencv (different from the tutorial with updates)
     ```
     brew install opencv
     # opencv-contrib already included
     ```
   - install cmake via homebrew
     ```
     brew install cmake
     ```
   - download ArUco (/usr/local):
    https://sourceforge.net/projects/aruco/
    
   - build ArUco via cmake
     ```
     unzip aruco-3.1.15.zip
     cd aruco-3.1.15
     cmake .
     make
     sudo make install
     ```
***for Ubuntu 20.04**\
  https://linuxize.com/post/how-to-install-opencv-on-ubuntu-20-04/
    
### Get Landing Markers
    
  Calibration << aruco_calibration_grid_board_a4.pdf

### Camera Calibration

  Calibration << arducam_calibration.yml

### References

https://github.com/goodrobots/vision_landing


