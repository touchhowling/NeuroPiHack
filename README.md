# Neuro Hack - Personalised Brain Frequency Recogniser

![Neuro Hack](neuro_hack_image.png)

Neuro Hack is a personalised brain frequency recogniser designed to help you achieve a calm or focused state of mind. It utilizes specific brain frequencies and plays them through Spotify. By triggering your brain with these frequencies, Neuro Hack can enhance productivity and aid in relaxation.

## Features

- Personalised brain frequency recognition: Neuro Hack analyzes your brain waves and identifies the most suitable frequency for either calm or focus mode.
- Integration with Spotify: The app seamlessly connects with the Spotify API to play the identified brain frequency.
- Increased productivity: By leveraging the power of brain frequencies, Neuro Hack can help you improve focus and concentration, leading to increased productivity.
- EEG analysis with Arduino data: Neuro Hack is compatible with Arduino-fetched EEG data, allowing you to perform EEG analysis using Python.

## How It Works

1. Neuro Hack measures your brain waves using an EEG device.
2. The app analyzes the collected data and identifies the brain frequency that corresponds to either calm or focus mode.
3. Using the Spotify API, Neuro Hack plays the identified brain frequency through your Spotify account.
4. As the frequency is played, it triggers your brain into a calm or focused state, helping you achieve your desired mental state.
5. Neuro Hack can be used in conjunction with Arduino to fetch EEG data and perform analysis in Python, providing a comprehensive solution for EEG enthusiasts.

## Getting Started

To get started with Neuro Hack, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/neuro-hack.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Set up your Spotify API credentials by creating a developer account and obtaining the necessary keys.
4. Configure the app by updating the `config.py` file with your Spotify API credentials.
5. Connect your EEG device and ensure it is properly calibrated.
6. Run the Neuro Hack application: `python neuro_hack.py`
7. Enjoy the benefits of personalised brain frequency recognition!

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request. Let's make Neuro Hack even better together.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgements

- [Spotify API](https://developer.spotify.com/documentation/web-api/)
- [EEG Analysis with Arduino](https://www.arduino.cc/en/Guide/ArduinoBrainLibrary)
- [Python EEG Analysis](https://github.com/your-username/python-eeg-analysis)
