from NeuroID.tools import load_model, calculate, compare
from NeuroID.emulate import generate_multiple_eeg_signals
import random
from tqdm import tqdm
import matplotlib.pyplot as plt


sampling_rate = 256
duration = 10
n = 4
recognitions = 8
recognition_resolution = 200
seed = random.randint(1, 100)

model = load_model('model3.pkl')

def generate(seed):
    eeg_signalss = [generate_multiple_eeg_signals(
        n=n,
        duration=duration,
        sampling_rate=sampling_rate,
        seed=seed + recID)[1] for recID in range(recognitions)
    ]
    result_data, filtered_signals, peakss = calculate(eeg_signalss, sampling_rate, recognition_resolution, model)
    return result_data


for recognitions in range(12, 20):
    plt.figure(figsize=(12, 6))

    main_token = generate(100)
    threshold = 950
    result = [0] * 1001

    n1, n2 = 400, 200

    for i in tqdm(range(n1)):
        new_seed = random.randint(1, 2**31)
        new_token = generate(new_seed)
        # print(int(compare(new_token, main_token)*1000), compare(new_token, main_token))
        result[int(compare(new_token, main_token)*1000)] += 1

    result2 = [min(i, 10) for i in result]

    plt.subplot(2, 2, 1)
    plt.bar(range(1001), result2)


    result3 = [0] * 1001

    for i in tqdm(range(n2)):
        new_seed = random.randint(1, 2**31)
        # print(int(compare(new_token, main_token)*1000), compare(new_token, main_token))
        result3[int(compare(generate(new_seed), generate(new_seed))*1000)] += 1

    result4 = [min(i, 10) for i in result3]

    plt.subplot(2, 2, 2)
    plt.bar(range(1001), result4)

    d1 = sum(result[threshold:])
    d2 = sum(result3[threshold:])

    plt.subplot(2, 2, 3)
    plt.pie([d1, n1-d1], labels=['Успешая ошибочная \nавторизация', 'Успешное продиводействие \nошибочной авторизации'], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')
    plt.subplot(2, 2, 4)
    plt.pie([d2, n2-d2], labels=['Успешная авторизация \nнеобходимого пользователя', 'Ошибочное отклонение \nавторизации'], autopct='%1.1f%%', startangle=140)
    plt.axis('equal')

    plt.savefig(f'figures/result_{recognitions}.png')