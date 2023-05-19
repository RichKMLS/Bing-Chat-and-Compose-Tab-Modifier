"""
Title: ChatComposeModifier.py
Author: github.com/richkmls
Date: 19-5-2023
Description: 

    This script: 
    - Automates the process of opening a Bing chat tab and a Compose tab in Edge Dev.
    - Modifies the tabs to use different themes/layouts and changes some variables in console.

    It first opens up the Bing Chat then Bing Compose in the Discover sidebar.
        This is required to be able to then open:
            - https://edgeservices.bing.com/edgesvc/chat
            - https://edgeservices.bing.com/edgesvc/compose

    It then modifies the UI to provide a dark theme and a more user-friendly interface for more advanced prompting.
    Pyautogui module is used to simulate mouse/keyboard actions and leverages the OpenCV library for image recognition.
    The `locateOnScreen()` function employs OpenCV to analyze the screen and locate specified images.
    
    This script is designed to address the issue of user scripts being blocked on https://edgeservices.bing.com/*
        by automating the process of running Javascript in the Developer Console.
    
    This script is provided "as is" without any warranty. 
    The author is not responsible for any damage or loss caused by using this script. 
"""

import pyautogui
import subprocess
import time
import sys

BINGCHAT = "https://edgeservices.bing.com/edgesvc/chat"
BINGCOMPOSE = "https://edgeservices.bing.com/edgesvc/compose"
WINDOWS_EDGE = r'C:\Program Files (x86)\Microsoft\Edge Dev\Application\msedge.exe'

# Define an IIFE function that selects elements on a web page, sets the maxLength property of a search box to 25000,
# and applies CSS rules to invert the colors of the page and set the background to black.
chat_js = """
(function() {
    document.querySelector("#b_sydConvCont > cib-serp").shadowRoot.querySelector("#cib-action-bar-main").shadowRoot.querySelector("#searchbox").maxLength = "25000";
    var css = 'html { filter: invert(100%); background: black; } img:not([src*=".svg"]),
        video { filter: invert(100%) } :is([class*="button"], [id*="button"]) { filter: none; }';
    var head = document.getElementsByTagName('head')[0];
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(css));
    head.appendChild(style);
})();
"""

# Define an IIFE function that removes elements with specified selectors from the DOM,
# changes the text content of a button to ‘Prompt’, and sets the maxLength property
# and placeholder text of a text input element.
compose_js = """
(function() {
    let decorations = ['.option-section', '#input_heading', '#preview_heading', '#insert_button'];
    decorations.forEach((decoration) => {
        let elements = document.querySelectorAll(decoration);
        elements.forEach((element) => {
            element.parentNode.removeChild(element);
        });
    });
    let composeButton = document.querySelector('#compose_button');
    composeButton.textContent = 'Prompt';
    let promptText = document.querySelector('#prompt_text');
    promptText.maxLength = "25000";
    promptText.placeholder = '...';
})();
"""

def exitConsole():
    """Exits the console by pressing F12 and waits for the 'inspect_element' image to disappear."""
    pyautogui.press('f12')
    while pyautogui.locateOnScreen('inspect_element.png', confidence=0.9):
        time.sleep(0.1)
    return

def writeJS(JS):
    """Writes JavaScript code into the console."""

    # Open the developer tools Console
    pyautogui.hotkey('ctrl', 'shift', 'j')
    # Wait for the Console
    console_area = None
    while not console_area:
        console_area = pyautogui.locateOnScreen('console_area.png', confidence=0.9)

    # Click on the console area
    pyautogui.click(console_area)
    time.sleep(0.1)

    # Write and run the JavaScript code in the console
    pyautogui.write(JS)
    time.sleep(0.1)
    pyautogui.press('enter')

def navigate_to(URL):
    """Navigates to a specified URL."""

    time.sleep(0.1)

    # Wait for the omnibox (Address bar)
    wait_for("omnibox", True)

    time.sleep(0.1)

    # Navigate to URL
    pyautogui.write(URL)

    time.sleep(0.1)
    pyautogui.press('enter')
    time.sleep(0.1)

def discover_sidebar(discover_button):
    """Discovers the sidebar by clicking on the 'discover_button'."""

    chat_tab = pyautogui.locateOnScreen('chat_tab.png', confidence=0.9)
    if not chat_tab:
        # Open Discover sidebar
        pyautogui.click(discover_button)
    elif chat_tab:
        # Verify chat tab is open
        pyautogui.click(chat_tab)

    # Wait for Bing Chat to fully load
    wait_for("chat_buttons")

    # Swap to compose tab in discover sidebar
    pyautogui.click(pyautogui.locateOnScreen('ComposeButton.png', confidence=0.9))

    wait_for("confirm_compose")

    # Click the Discover sidebar button to close it.
    pyautogui.click(discover_button)

    # Wait to be fully closed
    while chat_tab:
        time.sleep(0.1)

def wait_for(element, clickElement=False):
    """Waits for an element to appear on screen and optionally clicks on it."""

    located = {}
    located[element] = None

    while not located[element]:
        located[element] = pyautogui.locateOnScreen(f'{element}.png', confidence=0.9)
        if "omnibox" in element:
            located[element] = pyautogui.locateOnScreen(f'{element}2.png', confidence=0.9)
        time.sleep(0.1)

    if clickElement == True:
        pyautogui.click(located[element])
    elif element == "discover_button":
        discover_sidebar(located[element])
    else:
        time.sleep(0.1)

def main():
    """Main function that runs the script."""

    # Open Microsoft Edge(Windows)
    subprocess.Popen(WINDOWS_EDGE)

    # Wait for the Discover sidebar button
    wait_for("discover_button")

    # Navigate to Bing Chat
    navigate_to(BINGCHAT)

    # Write and run js on chat web page
    writeJS(chat_js)

    # Wait for Bing Chat to convert to dark theme
    wait_for("chat_start")

    # Close console
    exitConsole()

    # Open a new tab
    pyautogui.hotkey('ctrl', 't')

    # Navigate to Bing Compose
    navigate_to(BINGCOMPOSE)

    # Wait for the page to load via long button visual
    wait_for("long_button", True)

    # Write and run js on compose web page
    writeJS(compose_js)

    # Wait for js script to complete
    wait_for("confirm_prompt_change")

    # Close console
    exitConsole()

    # Switch to the previous tab
    pyautogui.hotkey('ctrl', 'shift', 'tab')

    # Wait for chat to be fully visible
    wait_for("chat_start")


if __name__ == "__main__":
    main()
