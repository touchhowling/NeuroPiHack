

from pyfirmata2 import Arduino
import time

class AnalogPrinter:
    
    def __init__(self, port='COM6', sampling_rate=20):
        self.samplingRate = sampling_rate
        self.timestamp = 0
        self.board = Arduino(port)
        self.time_series_data = []

    def start(self):
        self.board.analog[0].register_callback(self.myPrintCallback)
        self.board.samplingOn(1000 / self.samplingRate)
        self.board.analog[0].enable_reporting()
        return self.time_series_data

    def myPrintCallback(self, data):
        self.time_series_data.append((self.timestamp, data))
        print("%f,%f" % (self.timestamp, data))
        self.timestamp += (1 / self.samplingRate)

    def stop(self):
        self.board.samplingOff()
        self.board.exit()


def run_analog_printer(port='COM6', sampling_rate=20, duration=10):
    print(f"Let's print data from Arduino's analogue pins for {duration} seconds.")
    
    # Let's create an instance
    analog_printer = AnalogPrinter(port=port, sampling_rate=sampling_rate)
    
    # and start DAQ
    time_series_data = analog_printer.start()
    
    # let's acquire data for the specified duration
    time.sleep(duration)
    
    # let's stop it
    analog_printer.stop()
    
    print("Finished")
    
    return time_series_data

if __name__ == "__main__":
    # Example of calling the function from another file
    data = run_analog_printer(port='COM6', sampling_rate=20, duration=10)
    print("Returned data:", data)
