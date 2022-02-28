%% project2_matlabcode_7.m
% This script runs a simulation of a PI controller to find the need Ki and Kp values
%
% required file: project2_simfile_6.slx
%
%% Define trasfer function parameters
K = 2.4; 
sigma = 15;

%% Run a Simulation
%
% A simulink implements the PI controller.
%
open_system('PI_Controller') % open file
% run the simulation
out=sim('PI_Controller'); % close file
% the units used are radians/sec and voltage/sec

