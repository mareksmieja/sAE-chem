import numpy as np


def read_data(filename, test=False, max_reads=None):
    n_row = 0
    with open(filename, 'r') as f:
        fake = 0
        for line in f:
            if len(line.strip()) == 0:
                fake += 1
            n_row += 1
        f.seek(0)
        if test:
            # data = np.zeros((n_row - fake, 39973), dtype=np.int32)
            if max_reads is not None:
                data = np.zeros((max_reads, 39972), dtype=np.int32)
            else:
                data = np.zeros((n_row - fake, 39972), dtype=np.int32)
        else:
            data = np.zeros((n_row - fake, 39972), dtype=np.int32)
        id_row = 0
        for line in f:
            try:
                data[id_row, [int(i) for i in line.replace('\n', '').rsplit(' ')]] = 1.
            except ValueError:
                id_row -= 1
                assert len(line.strip()) == 0
            id_row += 1
            if max_reads is not None and id_row == max_reads:
                data = data[:max_reads]
                break
            print('\r\x1b[6;30;42mProgress:\x1b[0;1m [{:.0f}]%\x1b[0m'.format(id_row/n_row * 100), end='')
        print("\rDone read data from: '{}'".format(filename))
    return data


class ReadData:
    def __init__(self, filename, read_rows=10000):
        n_row = 0
        with open(filename, 'r') as f:
            fake = 0
            for line in f:
                if len(line.strip()) == 0:
                    fake += 1
                n_row += 1
        self.n_row = n_row
        self.filename = filename
        self.read_rows = read_rows
        self.n_col = 39972

    def getData(self):
        data = np.zeros((self.read_rows, self.n_col), dtype=np.int32)
        id_row = 0
        with open(self.filename, 'r') as f:
            for line in f:
                try:
                    data[id_row % self.read_rows, :] = 0
                    data[id_row % self.read_rows, [int(i) for i in line.replace('\n', '').rsplit(' ')]] = 1.
                except ValueError:
                    id_row -= 1
                    assert len(line.strip()) == 0
                id_row += 1
                print('\r\x1b[6;30;42mProgress:\x1b[0;1m [{:.0f}%]\x1b[0m'.format(id_row/self.n_row * 100), end='')

                if id_row % self.read_rows == 0:
                    yield data
                elif id_row == self.n_row:
                    yield data[:id_row % self.read_rows]


if __name__ == '__main__':
    data = read_data('./on_bits/A2A_act_onbits')
    print(data)
