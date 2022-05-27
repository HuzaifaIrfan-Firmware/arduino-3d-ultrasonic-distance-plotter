

from SerialCOM import SerialCOM
from Polar_Plotter import Polar_Plotter

comport="/dev/ttyUSB0"



import threading

serialcom=SerialCOM(comport,115200)

polar_plotter = Polar_Plotter()



  
def main_gui_thread():
    polar_plotter.main_loop()
  
def serial_thread_loop(controller):
    serialcom.serial_loop(controller)

  
if __name__ == "__main__":
    # creating threads
    # t1 = threading.Thread(target=gui_thread))
    serial_thread = threading.Thread(target=serial_thread_loop, args=(polar_plotter,))
  
    # starting thread 1
    # t1.start()
    # starting thread 2
    serial_thread.start()

    main_gui_thread()
  
    # # wait until thread 1 is completely executed
    # t1.join()
    # # wait until thread 2 is completely executed
    # t2.join()
  
    # both threads completely executed
    print("Exitting!!!")

