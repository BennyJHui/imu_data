#By Benny J Hui

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\2005B\OneDrive\Desktop\IMU_DATA\imu_orientation.csv")

ax = plt.axes(projection="3d")
i = 0
line_length = 2
length = 6

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.set_xlim(length, -length)
ax.set_ylim(length,-length)
ax.set_zlim(length,-length)

def R_matrix(roll, pitch, yaw):
    R = np.deg2rad(roll)
    P = np.deg2rad(pitch)
    Y = np.deg2rad(yaw)

# followed matrix formula here: https://mathworld.wolfram.com/RotationMatrix.html
# and here: https://en.wikipedia.org/wiki/Rotation_matrix#Composing_rotations
    cosR = np.cos(R)
    cosP = np.cos(P)
    cosY = np.cos(Y)
    
    sinR = np.sin(R)
    sinP = np.sin(P)
    sinY = np.sin(Y)
    
    RotX = np.array([[1,0,0],[0,cosR,-sinR],[0,sinR,cosR]])
    RotY = np.array([[cosP,0,sinP],[0,1,0],[-sinP,0,cosP]])
    RotZ = np.array([[cosY,-sinY,0],[sinY,cosY,0],[0,0,1]])
    
    R_matrix_val = (RotX @ RotY @ RotZ) # '@' = matrix multiplication
    
    return R_matrix_val

baseX = 0.0
baseY = 0.0
baseZ = 0.0

(lx,) = ax.plot([], [], [], 'r-', linewidth=2)
(ly,) = ax.plot([], [], [], 'g-', linewidth=2)
(lz,) = ax.plot([], [], [], 'b-', linewidth=2)

ax.plot([baseX], [baseY], [baseZ], 'ko', markersize=6)
while i < len(df):
    
    roll = df['roll_deg'][i]
    pitch = df['pitch_deg'][i]
    yaw = df['yaw_deg'][i]
    time = df['time'][i]
    
    R_data = R_matrix(roll, pitch, yaw)
    x = R_data @ np.array([1,0,0])
    y = R_data @ np.array([0,1,0])
    z = R_data @ np.array([0,0,1])
    
    lx.set_data([baseX, line_length*x[0]], [baseY, line_length*x[1]])
    lx.set_3d_properties([baseZ, line_length*x[2]])
    
    ly.set_data([baseX, line_length*y[0]], [baseY, line_length*y[1]])
    ly.set_3d_properties([baseZ, line_length*y[2]])
    
    lz.set_data([baseX, line_length*z[0]], [baseY, line_length*z[1]])
    lz.set_3d_properties([baseZ, line_length*z[2]])
    
    ax.set_title(f"Roll = {roll:.2f}° Pitch = {pitch:.2f}° Yaw = {yaw:.2f}° Time = {time:.3f}s"
                 "\n"
                 f"Based Pos @({baseX:.1f},{baseY:.1f},{baseZ:.1f})")
    
    plt.pause(0.01) #0.01 as that is sampling frequency 
    i = i + 1
plt.show()



