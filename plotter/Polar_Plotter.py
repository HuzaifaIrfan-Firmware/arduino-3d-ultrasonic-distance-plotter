import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl



def Radians(degree):
    return (3.14*degree/180)

def Degrees(radian):
    return (180*radian/3.14)


class Polar_Plotter():

    def __init__(self):
        
        self.set_x_degree =False
        self.new_x_degree = 0

        self.new_degree_distance=False
        self.new_z_degree=0
        self.new_z_distance=0
        
        self.plot_setup()


    def use_serial_data(self,serial_data):
        serial_list=[int(i) for i in serial_data.split(",")]
        # 10,40,0
        # x_angle_degree, z_angle_degree, distance_cm 

        try:
            x_angle_degree=serial_list[0]
        except:
            x_angle_degree=0

        try:
            z_angle_degree=serial_list[1]
        except:
            z_angle_degree=0

        try:
            distance_cm=serial_list[2]
        except:
            distance_cm=0

        

        
        # print(serial_list)
        self.new_plot(x_angle_degree,z_angle_degree,distance_cm)

    def plot_ax(self):

        self.ax.clear()
        self.ax.set_title("X Angle")
        self.ax.vlines(self.x_theta, 0, self.x_dist, linestyles='dashed')


    def plot_az(self):
        self.az.vlines(self.z_thetas, 0, self.z_dists)

    def one_plot_az(self,z_theta,z_dist):
        self.az.vlines(z_theta, 0, z_dist)


    def clear_az(self):

        self.z_thetas=[]
        self.z_dists=[]
        self.az.clear()
        self.az.set_title("Z Angle And Distance (cm)")




    def plot_setup(self):

        mpl.style.use("seaborn")

        self.fig, self.axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))

        plt.suptitle('3D Ultrasonic Plotter')

        self.x_degree=0
        self.x_theta=Radians(self.x_degree)
        self.x_dist=30

        self.z_thetas=[]
        self.z_dists=[]

        self.ax=plt.subplot(1, 2, 1, polar=True)
        self.ax.set_theta_zero_location('E') 
        self.plot_ax()

        self.az=plt.subplot(1, 2, 2, polar=True)
        self.az.set_theta_zero_location('E') 
        self.clear_az()
        self.plot_az()




        plt.pause(1)
    


    def new_plot(self,x_angle_degree,z_angle_degree,distance_cm):


        if not (x_angle_degree ==  self.x_degree):
            self.new_x_degree = x_angle_degree
            self.set_x_degree = True



        self.new_z_degree=z_angle_degree
        self.new_z_distance=distance_cm
        self.new_degree_distance=True

        












    def plot(self):

        if self.set_x_degree:
            plt.savefig(f'plots/{self.x_degree}.png')
            self.x_degree=self.new_x_degree
            self.x_theta=Radians(self.x_degree)
            self.plot_ax()
            self.clear_az()
            self.set_x_degree = False

        if self.new_degree_distance:

            if self.new_z_distance >= 0 and self.new_z_distance <=500:

                self.z_thetas.append(Radians(self.new_z_degree))
                self.z_dists.append(self.new_z_distance)

                # self.plot_az()
                self.one_plot_az(Radians(self.new_z_degree),self.new_z_distance)

      

            self.new_degree_distance=False

        

        
        

    def main_loop(self):


        while(1):

            self.plot()
            
            
            plt.pause(0.00001)
        


        # while 1:    
        #     plt.pause(1000)


        # 

        # plt.show()