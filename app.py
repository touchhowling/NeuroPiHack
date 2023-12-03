import streamlit as st
from FINAL import run_analog_printer, apply_filters, calculate_fft
import numpy as np
import matplotlib.pyplot as plt
import pyautogui
import os
import time

def store_data():
    st.title("Data Collection")

    # Get user input
    name = st.text_input("Enter your name:")
    mode = st.selectbox("Choose a mode:", ["Calm", "Focused"])

    # Button to trigger data collection
    if st.button("Store Data"):
        # Call the function with your desired parameters
        time_series_data = run_analog_printer(port='COM6', sampling_rate=20, duration=10)
        timestamps, values = zip(*time_series_data)

        plot_data(timestamps,values)
        # Apply filters
        filtered_timestamps, filtered_values = apply_filters(time_series_data, sampling_rate=1000)

        # Calculate the frequency
        freq,positive_frequencies,positive_fft_result = calculate_fft(filtered_timestamps, filtered_values)

        # Save data to a local text file
        save_to_text_file(name, mode, freq)

        # Plot the data
        plot_data(filtered_timestamps, filtered_values)
        plot_frequency(positive_frequencies,positive_fft_result)
        # Display the frequency
        st.success(f"Data stored successfully!\nName: {name}\nMode: {mode}\nFrequency: {freq} Hz")
    if st.button("Use data"):
        freq=find_frequency(name,mode)
        REDIRECT_URI='http://localhost:8085/'
        CLIENT_ID='9e213e2d9772401ebe302c1045c65af8'
        CLIENT_SECRET='1c857e1ce8ba4e8995d3da79c2c252af'
        SCOPE = "user-read-playback-state playlist-read-private playlist-modify-public"

        import spotipy
        from spotipy.oauth2 import SpotifyClientCredentials

        sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID,
                                                                client_secret=CLIENT_SECRET))

        results = sp.search(q=f'{freq}+ hz', limit=20)
        for idx, track in enumerate(results['tracks']['items']):
            print(idx, track['name'])
            break
        st.header(freq,track['name'])
        os.system("Spotify")
        time.sleep(10)
        pyautogui.keyDown('ctrl')
        pyautogui.keyDown('l')
        pyautogui.keyUp('ctrl')
        pyautogui.keyUp('l')
        time.sleep(0.1)
        pyautogui.write(track['name'],interval=0.1)

        for key in ['enter','pagedown','tab','enter','enter']:
            time.sleep(2)
            pyautogui.press(key)


def find_frequency(name, mode):
    with open("user_data.txt", "r") as file:
        lines = file.readlines()

    for i in range(len(lines) - 1):
        if f"Name: {name}" in lines[i] and f"Mode: {mode}" in lines[i + 1]:
            try:
                # Extract the frequency from the next line
                frequency = lines[i + 2]
                return frequency
            except ValueError:
                raise ValueError("Frequency is not a valid number in the file.")

    raise ValueError(f"Entry not found for Name: {name}, Mode: {mode}")
def save_to_text_file(name, mode, freq):
    data = f"Name: {name}\nMode: {mode}\nFrequency: {freq}\n"

    # Save data to a local text file
    with open("user_data.txt", "a") as file:
        file.write(data)
def plot_frequency(positive_frequencies,positive_fft_result):
    plt.figure(figsize=(10, 6))
    plt.plot(positive_frequencies, np.abs(positive_fft_result))
    plt.title('Fourier Transform of Time Series (Positive Frequencies)')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.grid(True)
    st.pyplot(plt)

def plot_data(timestamps, values):
    # Plotting the time series data
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, values, marker='o', linestyle='-', color='b')
    plt.title('Time Series Data')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.grid(True)
    st.pyplot(plt)

if __name__ == '__main__':
    store_data()
