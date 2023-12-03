# Save this code in another_file.py

from analog_printer import run_analog_printer


    # Call the function with your desired parameters
time_series_data = run_analog_printer(port='COM6', sampling_rate=20, duration=10)
print("Returned data:", time_series_data)

timestamps, values = zip(*time_series_data)
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# Plotting the time series data
plt.figure(figsize=(10, 6))
plt.plot(timestamps, values, marker='o', linestyle='-', color='b')
plt.title('Time Series Data')
plt.xlabel('Timestamp')
plt.ylabel('Value')
plt.grid(True)
plt.show()



def apply_filters(time_series, sampling_rate=1000):
    # Unpack timestamp and value from the time series
    timestamps, values = zip(*time_series)

    # Convert the data to a numpy array
    values = np.array(values)

    # Design a 50 Hz notch filter
    nyquist = 0.5 * sampling_rate
    low = 49.0 / nyquist
    high = 51.0 / nyquist
    b, a = signal.butter(2, [low, high], btype='bandstop')

    # Apply the notch filter
    values_notch = signal.filtfilt(b, a, values)

    # Design a band-pass filter for 1-45 Hz
    lowcut = 1.0 / nyquist
    highcut = 45.0 / nyquist
    b, a = signal.butter(2, [lowcut, highcut], btype='band')

    # Apply the band-pass filter
    values_filtered = signal.filtfilt(b, a, values_notch)

    return timestamps, values_filtered

sampling_rate = 1000

# Apply filters
filtered_timestamps,filtered_values = apply_filters(time_series_data, sampling_rate)

# Plot the original and filtered signals
plt.figure(figsize=(10, 6))
plt.plot(filtered_timestamps, filtered_values, label='Filtered EEG')
plt.xlabel('Time')
plt.ylabel('EEG Value')
plt.title('EEG Data with 50 Hz Notch and 1-45 Hz Band-pass Filters')
plt.legend()
plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Assuming time_series_list is a list of tuples in the format (timestamp, value)
timestamps=filtered_timestamps
values=filtered_values

def calculate_fft(timestamps,values):
    # Extracting timestamps and values from the list of tuples
    timestamps, values = zip(*time_series_data)

    # Assuming the timestamps are equally spaced
    # If not, you may need to interpolate or resample your data to have equally spaced timestamps

    # Calculate the Fourier transform
    fft_result = np.fft.fft(values)

    # Calculate the corresponding frequencies
    frequencies = np.fft.fftfreq(len(values), d=(timestamps[1] - timestamps[0]))

    positive_frequencies = frequencies[frequencies > 0]
    positive_fft_result = fft_result[frequencies > 0]

    plt.figure(figsize=(10, 6))
    plt.plot(positive_frequencies, np.abs(positive_fft_result))
    plt.title('Fourier Transform of Time Series (Positive Frequencies)')
    plt.xlabel('Frequency')
    plt.ylabel('Magnitude')
    plt.grid(True)
    plt.show()
    mag=0
    arr=np.abs(positive_fft_result);
    for i in range(0,len(arr)):
        if arr[i]>mag and 1 < frequencies[i] < 9.2:
            mag=arr[i]
            max_index=i
    freq=frequencies[max_index]
    print(freq)
        
    return freq,positive_frequencies,positive_fft_result
