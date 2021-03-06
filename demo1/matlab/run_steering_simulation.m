%% run_steering_simulation.m
% This script runs a simulation to the total model
%
% required file: Position_Model.slx
%
%% Define function parameters
%Inner Trasfer Function arameters
%rotation
Kr = 1.73; %2.8 in
sigmar = 2.94; % 10 in
%velocity
Kv = 0.53; %20 in
sigmav = 5.88; %12.5 in 

% Forward System Parmeters
K_rho = 1.73;
sigma_rho = 2.94;

% Forward Speed Setpoint
rhodot_d = 0.1; %ft/s

% Initial Conditions
x_0 = 0;
y_0 = 0;
phi_0 = 0;

% Line Parameters
x_s = [0 3 6 10];
y_s = [0 0 3 3];

sim('Position_Model')

%animate

