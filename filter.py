import numpy as np
import matplotlib.pyplot as plt

def calculate_coafficients(sampleRate, cutOff, q):
    T = 1 / sampleRate
    w0 = 2 * np.pi * cutOff
    a0 = 1 + 4/(T*T*w0*w0) + 2/(w0*q*T)
    a1 = (8/(T*T*w0*w0) - 2) / a0
    a2 = (2/(w0*q*T) - 4/(T*T*w0*w0) - 1) / a0
    b0 = 1/a0
    b1 = 2 * b0
    b2 = b0

    return a1, a2, b0, b1, b2

def filter(cutOff, q, sampleRate, input):
    output = np.zeros(len(input))
    inP1F1, inP2F1, outP1F1, outP2F1 = 0.0, 0.0, 0.0, 0.0
    inP1F2, inP2F2, outP1F2, outP2F2 = 0.0, 0.0, 0.0, 0.0

    a1, a2, b0, b1, b2 = calculate_coafficients(sampleRate, cutOff, q)

    for n in range(len(input)):
        outF1 = outP1F1 * a1 + outP2F1*a2 + input[n] * b0 + inP1F1*b1 + inP2F1*b2
        outP2F1 = outP1F1
        outP1F1 = outF1
        inP2F1 = inP1F1
        inP1F1 = input[n]

        output[n] = outP1F2 * a1 + outP2F2*a2 + outF1 * b0 + inP1F2*b1 + inP2F2*b2
        outP2F2 = outP1F2
        outP1F2 = output[n]
        inP2F2 = inP1F2
        inP1F2 = outF1

    return output

def frequnceResponse(q, cutOff, sampleRate):
    fres = 1000
    record = np.zeros(fres)
    t = np.linspace(0, 1, sampleRate)

    for fre in range(1, fres + 1):
        input = np.sin(2 * np.pi * fre * t)
        output = filter(cutOff, q, sampleRate, input)
        record[fre-1] = output.max() / input.max()

    xfres = np.linspace(1, fres+1, fres)
    plt.plot(xfres, record)
    plt.grid()
    plt.xlabel("frequence")
    plt.ylabel("amplitude")
    plt.text(500, 0.85, "q:{0}  cutOff:{1}".format(q, cutOff))
    plt.show()

def main():
    q = np.sqrt(2)
    frequency = 300
    cutOff = 100
    sampleRate = 22000

    t = np.linspace(0, 1, sampleRate)
    input = np.sin(2 * np.pi * frequency * t)

    output = filter(cutOff, q, sampleRate, input)
    plt.plot(t, input, 'b', t, output, 'r')
    plt.show()


if __name__ == "__main__":
    # main()
    # frequnceResponse(0.707, 500, 22000)
    frequnceResponse(2, 500, 22000)
