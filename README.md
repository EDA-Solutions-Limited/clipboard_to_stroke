# clipboard_to_stroke
<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">clipboard_to_stroke</h3>

  <p align="center">
    <br />
    <a href="https://github.com/EDA-Solutions-Limited/clipboard_to_stroke"><strong>Explore the project »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/EDA-Solutions-Limited/launch_putty/issues">Report Bug</a>
    ·
    <a href="https://github.com/EDA-Solutions-Limited/launch_putty/issues">Request Feature</a>
  </p>
</p>


<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#making-changes">Making changes</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project
HTML5 ssh terminals do not allow for copy and paste. There was no VNC to the machine and the RDP machine to access the linux server only had 2 CAL licenses always under use. when trying to upload files to the server via we-transfer using the wget command, the download links was over 1200 characters long. 

This script aims to keystroke strings in the clipboard



### Built With

* [Python](https://www.python.org/)


<!-- GETTING STARTED -->
## Getting Started

To get started with using this code, ensure you have python 3 installed. 

### Prerequisites

The following python libraries are required.

* pyclip
* pyautogui
* logging
* sys

  ```sh
  pip install pyclip
  pip install pyautogui
  ```

### Installation

1. Open the project at **..\EDA-Solutions-Limited\clipboard_to_stroke\clipboard_to_stroke** with an editor.
   Preferrably **vscode**
2. You could also clone the repo
   ```sh
   git clone https://github.com/clipboard_to_stroke/clipboard_to_stroke.git
3. Ensure you edit the createINI function in [**clipboard_to_stroke.py**](https://github.com/EDA-Solutions-Limited/clipboard_to_stroke/blob/main/clipboard_to_stroke.py#L179-L198) to your own desired default ini file.
4. create a shortcut that has a currently un assigned keystroke, through the right click context menu properties window.

### Notes:
1. Limitation: only built with windows in mind

<!-- ROADMAP -->
## Roadmap

1. None

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Not to be distributed to anyone outside EDA solutions. 

<!-- CONTACT -->
## Contact

Henry Frankland - [@hfrank](https://www.linkedin.com/in/henry-frankland-asic/) - henryfrankland@eda-solutions.com - henry@franklandhome.co.uk

Project Link: [clipboard_to_stroke](https://github.com/EDA-Solutions-Limited/clipboard_to_stroke.git)
