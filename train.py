from NeuroID.emulate import generate_multiple_eeg_signals
from NeuroID.tools import butterworth_filter, adjust_array
from random import randint
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis
from scipy.signal import find_peaks
import joblib
import numpy as np
from tqdm import tqdm

model = QuadraticDiscriminantAnalysis()

n = 1
batch = 1000
rerandom = 20
sampling_rate = 256
duration = 10
en = 4
recognition_resolution = 200

for i in range(n):
    # print(generate_multiple_eeg_signals(4, seed=i*(batch//rerandom)+1))
    X = []
    for j in tqdm(range(batch*rerandom)):
        t, eeg_signals = generate_multiple_eeg_signals(
            n=en,
            duration=duration,
            sampling_rate=sampling_rate,
            seed=i*batch+j//rerandom
        )

        cutoff_frequencies = [1, 50]
        filtered_signals = np.array([butterworth_filter(eeg_signal, cutoff=cutoff_frequencies, fs=sampling_rate)
                            for eeg_signal in eeg_signals])

        peakss = np.array(
            [adjust_array(filtered_signal[find_peaks(filtered_signal)[0]], recognition_resolution) for filtered_signal
             in filtered_signals])
        X.append(peakss.flatten())
    # X = [generate_multiple_eeg_signals(4, seed=[1].flatten() for j in range(batch*rerandom)]
    Y = [i*batch+j//rerandom for j in range(batch*rerandom)]
    model.fit(X, Y)

joblib.dump(model, 'model3.pkl')