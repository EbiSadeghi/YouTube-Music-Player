# YouTube-Music-Player
Automate the playing of instruments on YouTube

![Complete](https://img.shields.io/badge/status-Complete-brightgreen)

## Features

- Opens a specified number of tabs in Firefox with a given URL.
- Simulates key presses for a predefined sequence.
- Supports both Windows and Linux operating systems.

## Requirements

- Python 3.x
- Libraries:
  - `pyautogui`

You can install the required libraries using the provided `requirements.txt` file.

## Installation

1. Clone the repository or download the script file.
2. Ensure you have Python installed on your system.
3. Install the required libraries by running:

   ```bash
   pip install -r requirements.txt
   ```
## Usage

1. Run the script using Python:

   ```bash
   python your_script_name.py
   ```

2. The script will:
   - Open Firefox and load the specified URL in multiple tabs.
   - Simulate key presses based on the predefined sequences.

## Code Explanation

- **`open_webpage(numTabs, link)`**: Opens a specified webpage in the given number of tabs.
- **`open_firefox(numTabs, link)`**: Launches Firefox based on the operating system and calls `open_webpage`.
- **`play_verse(myList)`**: Simulates key presses for the provided list of numbers.

## Example Links

- Chords: [YouTube Chords Link](https://www.youtube.com/watch?v=qWX31yz68Ns)
- Piano: [YouTube Piano Link](https://www.youtube.com/watch?v=3gZC5763wYk)

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.
