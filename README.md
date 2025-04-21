
# NeuroID - New Generation Authentication

## EEG emulate results
![EEG emulate results](https://raw.githubusercontent.com/Qanty228/NeuroID/refs/heads/images/default.png)

## EEG pattern generation example
![EEG pattern generation example](https://github.com/Qanty228/NeuroID/blob/images/example.png?raw=true)

## EEG authentication results
![EEG authentication results](https://github.com/Qanty228/NeuroID/blob/images/result_19.png?raw=true)

All computing operations are performed in a\
hardware-isolated environment, as this way malware will not be able\
to access the user's biometric data. 

1. Recording of EEG signals with a frequency of 128-256 Hz for 5-30 seconds
2. Removing noise (motion artifacts, network interference)\
using the 8th order Butterworth filter. 
3. Application of quadratic discriminant analysis to \
a two-dimensional array of time/information for classifying individual\
activity groups

To install:\
download git project\
generate function in NeuroID.tools
