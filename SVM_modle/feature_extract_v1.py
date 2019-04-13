import csv, json, os
import numpy as np
import pandas as pd

def extract_except_interval(exceptions):
    if exceptions[2].isdigit() and exceptions[3].isdigit():
        lower_braket = int(exceptions[2:4])
        if exceptions[5].isdigit() and exceptions[6].isdigit():
            upper_bracket = int(exceptions[5:7])
        else:
            upper_bracket = int(exceptions[5])
    elif exceptions == '[()]':
        return (-1, -1)
    else:
        lower_braket = int(exceptions[2])
        if exceptions[4].isdigit() and exceptions[5].isdigit():
            upper_bracket = int(exceptions[4:6])
        else:
            upper_bracket = int(exceptions[4])

    return (lower_braket, upper_bracket)


#Extract features from each directory
os.chdir('/home/zackb/Synapse/ml_myo/full_raw_dataset')
data_directorys = ['Hand_close', 'Hand_open',  \
                  'Wrist_extension', 'Wrist_flexion_zach']

#label for data
out_data_json = {}
data_strlabels = ['Rest', 'Hand_close', 'Hand_open',  \
                  'Wrist_extension', 'Wrist_flexion', 'None']
for item in data_strlabels:
    out_data_json[item] = []


#iterate trough all required directories
for datadir in data_directorys:
    list_datafile = os.listdir(datadir)
    list_datafile.sort()

    #Intervals of label and unkown label are within these files
    labelinfo_csv = open('../notes_'+datadir+'.txt')
    info_reader = csv.reader(labelinfo_csv)
    dir_lable_info = []
    for row in info_reader:
        dir_lable_info.append(row)
    labelinfo_csv.close()

    #go trough each indiviual file of raw data to simplify it with RMS value. 
    rms_width = 25; idx_files = 1
    for move_data in list_datafile:
        with open(datadir+'/'+move_data) as prejson_file:
            rawdata_json = json.load(prejson_file)
            raw_data = rawdata_json['emg']['data']

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

                    #append the current rms sample to this iteration of emg_rms samples
                    emg_rms.append(rms_sample)


            #use labeling notes from info_reader to label each sample
            #['index', 'rest_end_time', 'action_start', 'exception']
            try :
                file_index, restend_idx, pose_start_dix, exceptions = dir_lable_info[idx_files]
            except:
                try:
                    print(dir_lable_info[idx_files])
                except:
                    print('while in ' +datadir+ 'we reach file:  ' +str(idx_files))
            idx_files += 1

            ignores = extract_except_interval(exceptions)
            # if ignores != (-1, -1):
                # print(ignores)

            #label rest samples
            for smp in range(int(restend_idx)):
                out_data_json['Rest'].append(emg_rms[smp])

            #lable movement vectors
            for smp in range(int(pose_start_dix), len(emg_rms)):
                if smp >= ignores[0] and smp <= ignores[1]:
                    out_data_json['None'].append(emg_rms[smp])
                else:
                    #we only want wrist flexion
                    if datadir == 'Wrist_flexion_zach':
                        out_data_json[datadir[:13]].append(emg_rms[smp])
                    else:
                        out_data_json[datadir].append(emg_rms[smp])



data_strlabels = ['Rest', 'Hand_close', 'Hand_open',  \
                  'Wrist_extension', 'Wrist_flexion', 'None']
for label in data_strlabels:
    print(label + " : " + str(len(out_data_json[label])))

#dump data into a file
with open('pose_instant_data', 'w') as fp:
    json.dump(out_data_json, fp)

