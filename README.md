the purpose of this was to get some experience with simulink

so how this works overall (not going into math as theres pdf and sources in the code of python)

i used sensor logger application and treated my iPhone 12 as an inertial measurement unit recording calibrated data of acceleration, gyroscope, and magnetometer and use matlab (simulink) to
convert those data into roll pitch and yaw through the process of sensor fusion specifically using an extended kalman filter to get better results.

The data of roll pitch yaw is then outputted into a csv file with all the data over time and i then use python to show the rotation of my phone overtime

heres youtube demo roll pitch yaw over time in python: https://www.youtube.com/watch?v=SWt6x0_UFqw
