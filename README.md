# Prompter-Browser

Open Edge Dev Browser in a VM and convert to a standalone Bing-AI prompting wokshop.

<p align="center">
  <img src="https://github.com/RichKMLS/Prompter-Browser/assets/105183376/75f03296-7934-4fab-86f9-e263a01f43b4" width="40%"/>
  <br>
</p>


Since user-scripts are seemingly blocked on edgeservices&period;bing&period;com/edgesvc/*, <br>
Here is an overkill solution that uses image recognition
to automate the process of    

- Opening Edge Dev Browser
- Opening the Discover side bar and loading the Chat and Compose interface
- Closing the Discover side bar
- Opening a Bing chat tab and a Compose tab in Edge Dev
- Opening the Developer Console
- Running JavaScript in the Developer Console to modify the behavior of the tabs
- Closing the Developer Console

Dedicated to the ~3 people on this planet who use edge dev browser in a virtual machine for the single purpose of accessing Bing AI.

todo:
- linux version using firejail

## The Advantages of Using a VM

Using a VM is optional, but it has some benefits for running a full screen application. It allows you to customize the display window size according to your needs. Running in fullscreen removes any unwanted elements that might interfere with your focus or take up precious space on your screen. Additionally, it provides a layer of separation for those who prefer to use Bing AI without installing it on their host machine.

## Features and Limitations

- Please note that images are not included. If this script interests you, it is your responsibility to determine which images to use based on the context of the script. 😊
- The script currently makes some assumptions about how Edge Dev Browser is set up such as using a Dark theme.

## Disclaimer

This script is provided "as is" and with no warranty or guarantee of any kind, either express or implied, including but not limited to the accuracy, completeness, reliability, suitability, or availability of the script. I am not affiliated with or endorsed by Microsoft in any way and I do not assume any responsibility or liability for any consequences or damages that may arise from using this script. 
