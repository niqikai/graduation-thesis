x=np.linspace(0, 400 - 1, 400, dtype = np.int64)
w = 0.54 - 0.46 * np.cos(2 * np.pi * (x) / (400 - 1) )
def GetFrequencyFeature4(wavsignal, fs):
    time_window = 25 # ms
    window_length = fs / 1000 * time_window
    wav_arr = np.array(wavsignal)
    wav_length = wav_arr.shape[1]
    range0_end = int(len(wavsignal[0])/fs*1000 - time_window) // 10 + 1 
    data_input = np.zeros((range0_end, window_length // 2), dtype = np.float)
    data_line = np.zeros((1, window_length), dtype = np.float)
    for i in range(0, range0_end):
        p_start = i * 160
        p_end = p_start + 400
        data_line = wav_arr[0, p_start:p_end]
        data_line = data_line * w
        data_line = np.abs(fft(data_line)) / wav_length
        data_input[i]=data_line[0: window_length // 2]
        
    data_input = np.log(data_input + 1)
    return data_input