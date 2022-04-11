
# Mini Project 1
## File Organization
The code is divided by the language that it is written in and is organized as:
<ul>
  <li>Arduino</li>
    <ul>
      <li>Demo2_ArduinoCode</li>
      <ul><li>Contains a state machine that runs the controller for demo2.</li></ul>
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
      <li>demo2.py</li>
        <ul><li>The computer vision code that determines the angle from the center of the screen and transmits this to the rasberry pi so that it can determine how to correct its angular movement.</li></ul>
    </ul>
</ul>

## Responsibilities
<ul>
  <li>Jason Nguyen</li>
    <ul>
       <li>Added a bounding box that determines when the robot is at the tape.</li>
       <li>Tuned the angle so that it is easier to send and doesn't send at top speed.</li>
      <li>Helped design the angle conversion to make transmission simpler.</li>
    </ul>
  <li>Brook Walls</li>
    <ul>
        <li>Helped with tuning of camera height with the physical construction</li>
        <li>Helped with physical testing of the bot</li>
    </ul>
  <li>Kevin Juneau</li>
    <ul>
        <li>Tweaked the demo 1 code to stop when the sending of data stops, as well as to following the tape precisely</li>
      <li>Testing and tweaking of bot functioning</li>
    </ul>
  <li>Lisbel Martinez</li>
    <ul>
        <li>Helped with tweaking of the physical build</li>
        <li>Brainstormed for the tweaking of the arduino code</li>
    </ul>
  <li>Alexander Nesbitt</li>
    <ul>
      <li>Completed wiring between Arduino UNO, LCD display and Rasberry Pi</li>
      <li>Updated Github documtation</li>
      <li>Repositioned Camera for a better angle</li>
    </ul>
</ul>
