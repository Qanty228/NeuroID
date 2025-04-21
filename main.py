import random
import numpy as np
import matplotlib.pyplot as plt
from NeuroID.emulate import generate_multiple_eeg_signals
from NeuroID.tools import load_model, compare, adjust_array, calculate


if __name__ == "__main__":
    sampling_rate = 256
    duration = 10
    n = 4
    recognitions = 5
    recognition_resolution = 300
    seed = random.randint(1, 100)

    model = load_model()

    t = np.linspace(0, duration, duration * sampling_rate, endpoint=False)

    eeg_signalss = [generate_multiple_eeg_signals(
            n=n,
            duration=duration,
            sampling_rate=sampling_rate,
            seed=seed+recID)[1] for recID in range(recognitions)
    ]

    result_data, filtered_signals, peakss = calculate(eeg_signalss, sampling_rate, recognition_resolution, model)

    similarity = compare(result_data, [1, 6, 5, 4, 5])
    print(similarity)

    plt.figure(figsize=(12, 6))
    for i, eeg_signal, filtered_signal, peaks in zip(range(1, n+1), eeg_signalss[0], filtered_signals, peakss):
        # print(i, eeg_signal, filtered_signal)
        plt.subplot(n, 1, i)
        plt.plot(t, eeg_signal, label="Оригинальный сигнал")
        plt.plot(t, filtered_signal, label="Отфильтрованный сигнал", linewidth=2)

        # peaks, _ = find_peaks(filtered_signal)
        plt.plot(adjust_array(t, recognition_resolution), peaks, label="Сглаженные локальные максимумы",
                 linewidth=0.7)

        plt.legend()
        # plt.title("Оригинальный и отфильтрованный сигналы")
    plt.tight_layout()
    plt.show()
