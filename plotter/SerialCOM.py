
import serial
import time
import json
import random


class SerialCOM:
    def __init__(self,comport, baudrate=115200):


        self.arduino = serial.Serial(port=comport,
            baudrate=baudrate, 
            timeout=.1, 
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            dsrdtr = False)


        self.controller=None

        
        



    def write_serial(self,serial_data):
        if serial_data:
            self.controller.set_previous_cmd_var(serial_data)
            print('User: ', serial_data)
            self.arduino.write(bytes(serial_data, 'utf-8'))
            return True
        return False

    def read_serial(self):
        time.sleep(0.005)
        byte_data = self.arduino.readline()
        data=str(byte_data, 'UTF-8')
        if data:
            print('Arduino: ', data)
            return data
        else:
            return False

    def write_read(self,data):
        self.write_serial(data)
        return self.read_serial()


    def serial_loop(self, controller):

        self.controller=controller
        
        while True:
            serial_data=self.read_serial()

            if serial_data:
                self.controller.use_serial_data(serial_data)

