
# Mini Project 1
## File Organization
The code is divided by the language that it is written in and is organized as:
<ul>
  <li>Arduino</li>
    <ul>
      <li>MiniProjectController.ino</li>
      <ul><li>Contains the total arduino code that is setup to work with the h-bridge motor shield for the arduino and I2C pins on the arduino UNO. Additionally, the SDA, SCL and GND pins are connected the corresponding pins for the LCD screen</li></ul>
    </ul>
  <li>Matlab</li>
    <ul>
        <li>PIControlor</li>
          <ul><li>Runs the PI controller simuation to generate Ki and Kp values</li></ul>
        <li>PI_Controller.slx</li>
          <ul><li>Simulink that allows tuning of the controller files</li></ul>
        <li>Verifying a Discrete Time Controller Using Simulink </li>
          <ul><li>The function that simulates the motor for simulink experimental simulation</li></ul>
        <li>project3_sim2 </li>
          <ul><li>Allows comparison between simulated and experimental closed loop step response</li></ul>
        <li>project2_matlabcode_7.m</li>
          <ul><li>Script that runs the PI controller simulink</li></ul>
        <li>ClosedLoopCode.m</li>
          <ul><li>Runs the simulink file "project3_sim2"</li></ul>
    </ul>
  <li>Python</li>
    <ul>
      <li>demo1.py</li>
        <ul><li>Computer Vision code that determines the angle from the center line of each frame by detecting blue painters tape. Addtionally, this code prints this angle to the LCD display for viewing.</li></ul>
      <li>whitebalance</li>
        <ul><li>This code implements white balance for the cameras although the final code uses the auto white balance from the cv2 library</li></ul>
    </ul>
</ul>

## Responsibilities
<ul>
  <li>Jason Nguyen</li>
    <ul>
       <li>Wrote the python code for computer vision and processing</li>
       <li>Assisted in setting up the wheel system</li>
    </ul>
  <li>Brook Walls</li>
    <ul>
        <li>Designed experimental and simulated simulink PI controllers</li>
        <li>Tuned controller gain values for Kp and Ki to meet system requirements</li>
    </ul>
  <li>Kevin Juneau</li>
    <ul>
        <li>Implemented PI controller in arduino C</li>
        <li>Experimentally determined motor step response and transfer function</li>
    </ul>
  <li>Lisbel Martinez</li>
    <ul>
        <li>Assisted in simulink modeling of the open loop and closed loop step responses</li>
        <li>Helped with testing of the subsytems working together for final demo</li>
    </ul>
  <li>Alexander Nesbitt</li>
    <ul>
      <li>Completed wiring between Arduino UNO, LCD display and Rasberry Pi</li>
      <li>Wrote python and arduino code to communicate the desired angle from the given quadrant of the camera</li>
      <li>Assisted in integration of all subsystems into collaborated arduino and python docs
    </ul>
</ul>
