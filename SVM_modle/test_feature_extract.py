import os, json, pprint, csv
import numpy as np
os.chdir('/home/zackb/Synapse/ml_myo/full_raw_dataset')
datadir='Hand_open'
rms_width = 25

#label for data
out_data_json = {}
data_strlabels = ['Rest', 'Hand_close', 'Hand_open',  \
                  'Wrist_extension', 'Wrist_flexion', 'None']
for item in data_strlabels:
    out_data_json[item] = []



with open(datadir+'/hand_open_1_18.json') as dummy_json:
    full_data = json.load(dummy_json)
    raw_data = full_data['emg']['data']

    #25 samples is about a 125ms intervals
    emg_rms = []
    for idx in range(0, len(raw_data), rms_width):
        #stop if reaching the end the list
        if idx+rms_width <= len(raw_data):
            rawemg_interval = raw_data[idx:idx+rms_width]
        #the mean of a single value is NaN, not wanted. 4 is too few
        elif len(raw_data)%rms_width <= 4:
            rawemg_interval = 'End'
        #calculate rms with the les then 25 long list
        else:
            rawemg_interval = raw_data[idx:len(raw_data)-1]
        #calculate RMS each channel for this interval
        rms_sample =[]
        if rawemg_interval != 'End':
            for chan in range(0, 8):
                #seperate data by channel
                emg = []
                for sample in rawemg_interval:
                    emg.append(sample[chan])
                #calculate RMS
                np_emg = np.array(emg)
                rms_sample.append(np.sqrt(np.mean(np_emg**2)))

            #append the current rms sample to this iteration of emg_rms samples.
            emg_rms.append(rms_sample)

    #pprint.pprint(emg_rms)
    print(len(emg_rms))

#Intervals of label and unkown label are within these files
with open('../notes_'+datadir+'.txt') as labelinfo_csv: 
    info_reader = csv.reader(labelinfo_csv)
    dir_lable_info = []
    for row in info_reader:
        dir_lable_info.append(row)
    labelinfo_csv.close()

print(dir_lable_info[1])
file_index, restend_idx, pose_start_dix, exceptions = dir_lable_info[1]

#label rest samples
for smp in range(int(restend_idx)):
    out_data_json['Rest'].append(emg_rms[smp])

#lable movement vectors
for smp in range(int(pose_start_dix), len(emg_rms)):
    #we only want wrist flexion
    if datadir == 'Wrist_flexion_zach':
        out_data_json[datadir[:13]].append(emg_rms[smp])
    else:
        out_data_json[datadir].append(emg_rms[smp])


pprint.pprint(len(out_data_json[datadir])+int(restend_idx))

