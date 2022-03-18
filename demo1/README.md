
# Mini Project 1
## File Organization
The code is divided by the language that it is written in and is organized as:
<ul>
  <li>Arduino</li>
    <ul>
      <li>Demo1_Controller.ino</li>
      <ul><li>Contains the controllers for forward and angular velocity with the outer controller keeping track of the position of the robot.</li></ul>
      <li>Demo1_StepResponse.ino</li>
      <ul><li>The code used to obtain the experimental transfer functions for the inner loop of the controller.</li></ul>
    </ul>
  <li>Matlab</li>
    <ul>
        <li>PI_Turner.slx</li>
          <ul><li>The inner loop transfer function models. Used to tune the inner loop controllers</li></ul>
        <li>Position_model.slx</li>
          <ul><li>The total simulink model used to tune the outer loop controller</li></ul>
      <li>TransferFunctionCode.m</li>
          <ul><li>The code that runs the inner loop PI controller tuning</li></ul>
        <li>Transfer_Function_Sim.slx</li>
          <ul><li>Simulink for the closed inner loop transfer functions</li></ul>
        <li>run_steering_simulation.m</li>
          <ul><li>Runs the position model for tuning the controllers</li></ul>
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
       <li>Adjusted Computer code to measure the angle from the center line</li>
       <li>Helped with construction of the physical bot</li>
    </ul>
  <li>Brook Walls</li>
    <ul>
        <li>Experimentally determined the inner loop transfer functions</li>
        <li>Constructed the Models for controller tuning</li>
      <li>Assist with experimental tuning of the system</li>
    </ul>
  <li>Kevin Juneau</li>
    <ul>
        <li>Implemented inner and outer loop controllers in ArduinoC</li>
        <li>Assisted with experimental determination of transfer functions</li>
      <li>Did the main experimental tuning of the controller</li>
    </ul>
  <li>Lisbel Martinez</li>
    <ul>
        <li>Assisted in simulink modeling of the open loop and closed loop step responses</li>
        <li>Helped with testing of the subsytems working together for final demo</li>
      <li>Helped with the physical assembly of the bot</li>
      <li>Supported the tuning of the bot and writing of the main controller loop</li>
    </ul>
  <li>Alexander Nesbitt</li>
    <ul>
      <li>Completed wiring between Arduino UNO, LCD display and Rasberry Pi</li>
      <li>Read documentation to determine the use of the motor shield and complete the wiring</li>
      <li>Assisted in integration of all subsystems into collaborated arduino and python docs</li>
      <li>Completed the main construction of the robot</li>
    </ul>
</ul>
