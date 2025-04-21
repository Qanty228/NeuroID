import numpy as np
from scipy.interpolate import UnivariateSpline


def generate_eeg_signal(duration=10, sampling_rate=256, noise_level=0.1, pattern_seed=86):
    size = sampling_rate * duration
    t = np.linspace(0, duration, size, endpoint=False)
    signal = np.sin(2 * np.pi * 10 * t)
    noise = np.random.normal(size=t.shape, scale=noise_level)
    # bias = int(np.random.uniform(high=1, low=-1) * size * 0.3)
    np.random.seed(pattern_seed)
    # noise += np.random.normal(size=(int(size * 1.3) + 1), scale=1)[bias:bias + size]

    points_count = 70
    x = np.array(range(points_count))
    y = np.random.uniform(low=0.5, high=1, size=points_count)
    x_new = np.linspace(x.min(), x.max(), size)
    y_new = np.clip(UnivariateSpline(x, y, s=0.2)(x_new), a_min=-1, a_max=1)

    np.random.seed(int(np.random.random() * 1000))

    return signal * y_new + noise


def generate_multiple_eeg_signals(n=8, duration=10, sampling_rate=256, noise_level=0.1, seed=86):
    return (np.linspace(0, duration, sampling_rate * duration, endpoint=False),
            np.array([generate_eeg_signal(duration, sampling_rate, noise_level, pattern_seed=seed + i)
             for i in range(n)]))
