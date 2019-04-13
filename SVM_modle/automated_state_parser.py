import matplotlib.pyplot as plt
import numpy as np
import pprint as pp
import os, json

#important channel-1
imp_channel = 6
move = 'Wrist_flexion_zach'
os.chdir("/home/zackb/Synapse/ml_myo/full_raw_dataset/")

listfile = os.listdir(move)
listfile.sort()

note_file = open('../notes_'+move+".txt", 'w')
description_line = 'index,rest_end_time,action_start,exception\n'
data_lines = ''


for index in range(len(listfile)):
    with open(move+'/'+listfile[index]) as files:
        data_json = json.load(files)
    data = data_json['emg']['data']
    timestamps = data_json['emg']['timestamps']

    #distribute emg data on each channel
    emg = [[],[],[],[],[],[],[],[]]
    for chan in range(0,8):
        for emg_chan in data:
            emg[chan].append(emg_chan[chan])

    # calculating RMS
    rms_width = 25
    #8 channel of emg data
    emg_rms= [[],[],[],[],[],[],[],[]];
    for idx in range(0, len(data), 25):
        for chan in range(0, 8):
            if idx+rms_width <= len(data):
                y = np.array(emg[chan][idx:idx+rms_width])
                #calculate RMS val in a 125 ms time interval
                emg_rms[chan].append(np.sqrt(np.mean(y**2)))
            #the mean of a single value is NaN, not wanted
            elif (len(data)%rms_width) <= 4:
                pass
            else:
                y = np.array(emg[chan][idx:len(data)-1])
                #calculate RMS val in a 125 ms time interval
                emg_rms[chan].append(np.sqrt(np.mean(y**2)))

    #time range state association
    time_range = 0; rest_maximum = 15; action_minimum = 23;
    while emg_rms[imp_channel][time_range] < rest_maximum or \
                time_range >= len( emg_rms[imp_channel]):
        time_range += 1
    rest_end_time = time_range

    while emg_rms[imp_channel][time_range] < action_minimum or \
                time_range >= len(emg_rms[imp_channel]):
        time_range += 1

    if time_range >= len( emg_rms[imp_channel]):
        print("WARNING at index :" + str(index))

    action_start = time_range

    data_lines += str(index)+','+str(rest_end_time)+','+str(action_start)
    data_lines += ',[()]\n'

note_file.write(description_line+data_lines)
note_file.close()
