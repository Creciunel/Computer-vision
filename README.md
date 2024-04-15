<h1>Object Detection Device</h1>

<h2>Hardware</h2>
<ul>
  <li>WeAct Studio STM32H7XX microcontroller <a href="https://github.com/WeActStudio/MiniSTM32H7xx/tree/master">project link</a></li>
  <ul>
    <li>Display: 0.96''</li>
    <li>Camera: OV7725 VGA (640x480) <a href="https://cdn.sparkfun.com/datasheets/Sensors/LightImaging/OV7725.pdf">datasheet</a></li>
    <li>Possibility of adding an SD card</li>
  </ul>
</ul>

<h2>Software</h2>
<p>Project implemented using the OpenMV software.</p>
<!-- inspired from https://github.com/ShawnHymel/computer-vision-with-embedded-machine-learning -->

<ul>
  <li><b>Data Collection</b> - The dataset was collected using <a href="Capture.py">this code</a> located in <a href="/DataSet/">this folder</a>.</li>
  <li></li>
</ul>

<h2>Requirements</h2>
<ul>
  <li>WeAct Studio STM32H7XX - flashed with <a href="https://github.com/WeActStudio/MiniSTM32H7xx/tree/master/SDK/openmv/Firmwares/V4.4.1/Internal%20Flash">bin file</a>, check the latest version.</li>
  <li>OpenMV IDE <a href="https://openmv.io/">official website</a>.</li>
  <li>Data set</li>
  <li><a href="https://colab.research.google.com/">Google Colab</a> for collaborative development and training</li>
</ul>

<p>This project is licensed under the <a href="LICENSE">MIT License</a>.</p>
