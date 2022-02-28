%% project2_matlabcode_7.m
% The runs the simulated and experimental step responce function. 
%
% required file: project3_sim2.slx
%

%% Run a Simulation
%
% A simulink implements the PI controller.
%
open_system('project3_sim2') % open file
% run the simulation
out=sim('project3_sim2'); % close file
% the units used are radians/sec and voltage/sec
