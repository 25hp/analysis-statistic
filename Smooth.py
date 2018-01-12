def cubicSmooth5(indata, outdata, N):
    if N < 5:
        for i in range(N):
            outdata.append(indata[i])
    else:
        outdata[0] = (69.0 * indata[0] + 4.0 * indata[1] - 6.0 * indata[2] + 4.0 * indata[3] - indata[4]) / 70.0;
        outdata[1] = (2.0 * indata[0] + 27.0 * indata[1] + 12.0 * indata[2] - 8.0 * indata[3] + 2.0 * indata[4]) / 35.0;
        for i in range(1, N):
            outdata[i] = (-3.0 * (indata[i - 2] + indata[i + 2]) + 12.0 * (indata[i - 1] + indata[i + 1]) + 17.0 *
                          indata[i]) / 35.0
            outdata[N - 2] = (2.0 * indata[N - 5] - 8.0 * indata[N - 4] + 12.0 * indata[N - 3] + 27.0 * indata[
                N - 2] + 2.0 * indata[N - 1]) / 35.0;
            outdata[N - 1] = (- indata[N - 5] + 4.0 * indata[N - 4] - 6.0 * indata[N - 3] + 4.0 * indata[
                N - 2] + 69.0 * indata[N - 1]) / 70.0


if __name__ == '__main__':
    outdata = []
    columnG = []
