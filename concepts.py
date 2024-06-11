# Keylogger Program

## Overview
This project implements a basic keylogger program in Python. The keylogger records and logs keystrokes and saves them to a file. **Important: This tool should only be used with the explicit permission of the user whose activity is being monitored. Unauthorized use of keyloggers can be illegal and is considered a violation of privacy.**

## Concepts and Theory

### Keylogging
Keylogging is the action of recording the keys struck on a keyboard, typically in a covert manner so that the person using the keyboard is unaware that their actions are being monitored. Keyloggers are used for various purposes, such as:
- **Security**: Monitoring and preventing unauthorized access.
- **Parental Control**: Keeping an eye on children’s online activities.
- **Employee Monitoring**: Ensuring productive use of company resources.
- **Personal Use**: Recovering lost data or monitoring personal device usage.

However, keylogging can also be used maliciously to steal sensitive information such as passwords and credit card numbers, which is why ethical use and legal compliance are paramount.

### Python `pynput` Library
The `pynput` library allows you to control and monitor input devices, such as the keyboard and mouse. It provides a simple interface to listen to keyboard events, which makes it suitable for implementing a keylogger.

### Logging Keystrokes
The process of logging keystrokes involves capturing each key press event and recording it. This is typically done by:
1. **Setting Up a Listener**: A listener is set up to monitor key press events.
2. **Capturing Keystrokes**: Each key press is captured and stored.
3. **Saving to a File**: The captured keystrokes are saved to a file for later analysis.

### Implementation
The keylogger script in this project uses the `pynput` library to listen for keyboard events and logs each key press to a file. The key steps are:
1. **Import Libraries**: Import the `pynput` library and the `logging` module.
2. **Set Up Logging**: Configure the logging module to write keystrokes to a file.
3. **Define the Logging Function**: Define a function to log each keystroke.
4. **Start the Listener**: Use `pynput` to start listening for keyboard events and call the logging function whenever a key is pressed.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/SCT_CS_04.git
   cd SCT_CS_04