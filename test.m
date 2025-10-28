Acc = readtable('Accelerometer.csv');
Gyr = readtable('Gyroscope.csv');
Mag = readtable('Magnetometer.csv');

% removes time which is unnecessary data from logger
Acc(:,1) = []; 
Gyr(:,1) = []; 
Mag(:,1) = [];

Acc.Properties.VariableNames  = {'t','Az','Ay','Ax'};
Gyr.Properties.VariableNames  = {'t','Gz','Gy','Gx'};
Mag.Properties.VariableNames  = {'t','Mz','My','Mx'};

AccTT = table2timetable(Acc, 'RowTimes', seconds(Acc.t));
GyrTT = table2timetable(Gyr, 'RowTimes', seconds(Gyr.t));
MagTT = table2timetable(Mag, 'RowTimes', seconds(Mag.t));

Period = 0.01; % Done in 100 Hz sampling

AccTT = retime(AccTT, 'regular', 'linear', 'TimeStep', seconds(Period));
GyrTT = retime(GyrTT, 'regular', 'linear', 'TimeStep', seconds(Period));
MagTT = retime(MagTT, 'regular', 'linear', 'TimeStep', seconds(Period));


figure; 
plot(seconds(AccTT.Time), [AccTT.Ax AccTT.Ay AccTT.Az]); 
grid on; 
xlabel('Time Elapsed (s)'), ylabel('Accleration (m/s²)');
title('Accelerometer');
legend('Ax', 'Ay', 'Az');

figure; 
plot(seconds(GyrTT.Time), [GyrTT.Gx GyrTT.Gy GyrTT.Gz]); 
grid on; 
xlabel('Time Elapsed (s)'), ylabel('Gyro (rad/s)');
title('Gyroscope');
legend('Gx', 'Gy', 'Gz');

figure; 
plot(seconds(MagTT.Time), [MagTT.Mx MagTT.My MagTT.Mz]); 
grid on; 
xlabel('Time Elapsed (s)'), ylabel('Magnetometer (µT)');
title('Manetometer');
legend('Mx', 'My', 'Mz');

% Convert to timeseries for Simulink
t = seconds(AccTT.Time);   % shared time vector

% Accelerometer
AccTSx = timeseries(AccTT.Ax, t);
AccTSy = timeseries(AccTT.Ay, t);
AccTSz = timeseries(AccTT.Az, t);

% Gyroscope
GyrTSx = timeseries(GyrTT.Gx, t);
GyrTSy = timeseries(GyrTT.Gy, t);
GyrTSz = timeseries(GyrTT.Gz, t);

% Magnetometer
MagTSx = timeseries(MagTT.Mx, t);
MagTSy = timeseries(MagTT.My, t);
MagTSz = timeseries(MagTT.Mz, t);

%-------------------------Test-------------------------%
T = array2table([out.tout out.simson.signals.values], 'VariableNames', {'time','roll_deg','pitch_deg','yaw_deg'});
writetable(T, 'imu_orientation.csv');

save imu_for_simulink.mat AccTSx AccTSy AccTSz GyrTSx GyrTSy GyrTSz MagTSx MagTSy MagTSz
