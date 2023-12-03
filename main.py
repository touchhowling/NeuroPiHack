from pyfirmata2 import Arduino
import time
c=1
PORT = 'COM4'
class AnalogPrinter:
    
    def __init__(self):
        # sampling rate: 10Hz
        self.samplingRate = 20
        self.timestamp = 0
        self.board = Arduino('COM4')
        self.time_series_data=[]
        self.is_acquisition_running = False

    def start(self):
        if not self.is_acquisition_running:
            self.board.analog[0].register_callback(self.myPrintCallback)
            self.board.samplingOn(1000 / self.samplingRate)
            self.board.analog[0].enable_reporting()
            self.is_acquisition_running = True  # Set the flag to True
            return self.time_series_data
    def myPrintCallback(self, data):
        self.time_series_data.append((self.timestamp,data))
        print("%f,%f" % (self.timestamp, data))
        self.timestamp += (1 / self.samplingRate)

    def stop(self):
        self.board.samplingOff()
        self.board.exit()

from flask import Flask, render_template, jsonify
import time
from threading import Thread

app = Flask(__name__)

# Your AnalogPrinter class and filter functions go here...
while c==1:
    c=2
  # Create an instance of AnalogPrinter

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(analog_printer.time_series_data)

def run_data_acquisition():
    time.sleep(3)
    analog_printer = AnalogPrinter()

    analog_printer.start()
    time.sleep(1)  # Adjust the sleep duration as needed
    analog_printer.stop()

if __name__ == '__main__':
    data_thread = Thread(target=run_data_acquisition)
    data_thread.start()
    app.run(debug=True)
