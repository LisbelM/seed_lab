%% TransferFunctionCode.m
% This script runs a simulation to find the transfor function
%
% required file: Transfer_Function_Sim.slx
%
%% Define trasfer function parameters
Kr = 1.73; %2.8 in
sigmar = 2.94; % 10 in

Kv = 0.53; %20 in
sigmav = 5.88; %12.5 in 

%% Run a Simulation
%
% A simulink implements the transfer function.
%
%open_system('Transfer_Function_Sim') % open file
% run the simulation
%out=sim('Transfer_Function_Sim'); % close file
% the units used are radians/sec and voltage/sec

open_system('PI_Turner') % open file
% run the simulation
out=sim('PI_Turner'); % close file
% the units used are radians/sec and voltage/sec

%% Plot Graphs
figure(1)
title('Rotation Step Responce')
xlabel('angle')
ylabel('position')
plot(Rotational)

figure(2)
title('Rotation Step Responce')
xlabel('velocity')
ylabel('position')
plot('Velocity')

%plot(rotation.mat)

%plot(velocity.mat)

% phi is degrees
% y in feet
% degrees per sec top transfer function
% bottom ts is ft/sec
%phi_0 and x_0 are the inital conditions
