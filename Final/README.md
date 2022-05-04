
# Mini Project 2
## File Organization
The code is divided by the language that it is written in and is organized as:
<ul>
  <li>Arduino</li>
    <ul>
      <li>FinalDemo</li>
      <ul><li>Contains the state machine and multi variable speed control that varies speed based on the magnitude of the turn. </li></ul>
    </ul>
  <li>Python</li>
    <ul>
      <li>final.py</li>
        <ul><li>The computer vision code that determines the angle from the center of the screen and transmits this to the rasberry pi so that it can determine how to correct its angular movement. Additionally detects the number of edges and sends a flag when the number is above a threshold that represents a cross.</li></ul>
    </ul>
</ul>

## Responsibilities
<ul>
  <li>Jason Nguyen</li>
    <ul>
       <li>Added edge detection that allows for detection of the cross.</li>
       <li>Cuts off the top portion of the camera to avoid seeing earlier parts of the track.</li>
    </ul>
  <li>Brook Walls</li>
    <ul>
        <li>Helped with tuning of camera height with the physical construction</li>
        <li>Helped with physical testing of the bot</li>
    </ul>
  <li>Kevin Juneau</li>
    <ul>
        <li>Added mutlivariable speed control based on the magnitude of the angle</li>
      <li>Testing and tweaking of bot functioning</li>
    </ul>
  <li>Lisbel Martinez</li>
    <ul>
        <li>Helped with tweaking of the physical build</li>
    </ul>
  <li>Alexander Nesbitt</li>
    <ul>
      <li>Helped with group testing of the demo.</li>
      <li>Updated Github documtation</li>
      <li>Repositioned Camera for a better angle</li>
    </ul>
</ul>

