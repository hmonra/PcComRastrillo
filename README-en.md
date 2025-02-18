PcComRastrillo - PcComponentes Bot

This repository contains a Python script developed in 2021, during the global shortage of graphics cards, to automate the purchase process on the PcComponentes website.

 Description

The script performs the following functions:

*   **Web Scraping**: Monitors the stock of graphics cards on PcComponentes.
*   **Automatic Login**: Logs in to the user account provided in the configuration.
*   **Automatic Purchase**: When the specified product is found, the script adds the graphics card to the cart and completes the purchase automatically.

⚡ Requirements

*   Python 3.x
*   Libraries: selenium
*   A compatible browser and the corresponding driver (e.g., ChromeDriver for Chrome)

⛓️ Warning

This script was created in a context of extreme component scarcity and is intended for personal use. The use of automated purchase bots may go against the terms of service of PcComponentes or other stores, so it is recommended to use it responsibly and ethically.

 Why this project?

During 2021, getting a graphics card at a reasonable price became a challenge due to high demand and the action of commercial bots. This script was born as a tool to level the playing field.

 Usage

1.  Clone this repository:

    ```bash
    git clone [https://github.com/hmonra/PcComRastrillo.git](https://github.com/hmonra/PcComRastrillo.git) cd tu-repo
    ```

2.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3.  Configure credentials and product parameters in the script's configuration file.
4.  Run the script:

    ```bash
    python main.py
    ```

 Contributions

Contributions are welcome! Feel free to open an issue or make a pull request to improve the code, add support for other stores, or optimize the scraping process.

 License

This project is under the MIT License. See the LICENSE file for more details.

 Note: PcComponentes may change its HTML structure or implement anti-bot measures, so the operation of the script is not guaranteed in the long term.
