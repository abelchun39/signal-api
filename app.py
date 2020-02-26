#libraries to include
# https://github.com/rcv911/coherence-function/blob/master/coherence_function_EEG.py
import json
import numpy as np
from scipy import signal
import matplotlib.pyplot as plot
from flask import Flask, jsonify, request, Response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/coherence', methods=['POST'])
def coherence():
        # https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.coherence.html
        fs = 10e3
        N = 1e5
        amp = 20
        freq = 1234.0
        noise_power = 0.001 * fs / 2
        time = np.arange(N) / fs
        b, a = signal.butter(2, 0.25, 'low')
        x = np.random.normal(scale=np.sqrt(noise_power), size=time.shape)
        y = signal.lfilter(b, a, x)
        x += amp*np.sin(2*np.pi*freq*time)
        y += np.random.normal(scale=0.1*np.sqrt(noise_power), size=time.shape)
        f, Cxy = signal.coherence(x, y, fs, nperseg=1024)
        output = {}
        output['coherence'] = Cxy.tolist()
        output['frequency'] = f.tolist()
        return Response(json.dumps(output), mimetype='application/json')

@app.route('/coherence/across', methods=['POST'])
def acrossCoherence():
        # https://pythontic.com/visualization/signals/coherence
        print(request.json.get('name', ""))
        # Create sine wave1
        time        = np.arange(0, 100, 0.1)
        sinewave1   = np.sin(time)


        # Create sine wave2 as replica of sine wave1
        time1        = np.arange(0, 100, 0.1)
        sinewave2    = np.sin(time1)

        # Plot the sine waves - subplot 1
        # plot.title('Two sine waves with coherence as 1')
        # plot.subplot(211)
        # plot.grid(True, which='both')
        # plot.xlabel('time')
        # plot.ylabel('amplitude')
        plot.plot(time, sinewave1, time1, sinewave2)

        # Plot the coherence - subplot 2
        # plot.subplot(212)
        coh, f = plot.cohere(sinewave1, sinewave2, 256, 1./.01)
        # print("Coherence between two signals:")
        # print(coh)
        # plot.ylabel('coherence')

        # plot.show()

        coh, f = plot.cohere(sinewave1, sinewave2, 256, 1./.01)

        output = {}
        output['coherence'] = coh.tolist()
        output['frequency'] = f.tolist()
        return Response(json.dumps(output), mimetype='application/json')

if __name__ == '__main__':
    app.run()
