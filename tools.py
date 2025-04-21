from scipy.signal import butter, filtfilt
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import joblib
from scipy.signal import find_peaks


def butterworth_filter(data, cutoff, fs, order=8, filter_type='bandpass'):
    nyquist = 0.5 * fs
    normal_cutoff = [c / nyquist for c in cutoff]
    b, a = butter(order, normal_cutoff, btype=filter_type, analog=False)
    return filtfilt(b, a, data)


def load_model(filename='model.pkl'):
    return joblib.load(filename)


def compare(a, b):
    # print(a, b)
    return cosine_similarity([a], [b])[0][0]


def adjust_array(array, k):
    n = len(array)
    return np.interp(np.linspace(0, n - 1, k), np.arange(n), array)

def calculate(eeg_signalss, sampling_rate, recognition_resolution, model):
    result_data = []
    for eeg_signals in eeg_signalss:
        cutoff_frequencies = [1, 50]
        filtered_signals = np.array([butterworth_filter(eeg_signal, cutoff=cutoff_frequencies, fs=sampling_rate)
                                     for eeg_signal in eeg_signals])

        peakss = np.array(
            [adjust_array(filtered_signal[find_peaks(filtered_signal)[0]], recognition_resolution) for filtered_signal in
             filtered_signals])

        # labels = np.concatenate([np.zeros(len(t) // 2), np.ones(len(t) // 2)])
        predict = model.predict([peakss.flatten()])[0]
        result_data.append(predict)
    return result_data, filtered_signals, peakss