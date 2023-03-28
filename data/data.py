import csv
import math
import numpy as np

def genFile(filename, size, data):
    title = 'keys total:' + str(size)
    with open(filename, 'w', encoding='UTF-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([title])
        for row in data:
            row_str = str(row)
            # String length must be 12
            row_str = row_str[:12] if len(row_str) >= 12 else row_str.zfill(12)
            writer.writerow([row_str])
    return

def genGaussKey():
    size = int(input("Data size: "))
    mu, sigma = size / 2, math.log(size, 2)
    key = np.random.normal(mu, sigma, size)
    key = np.round(key).astype(int)
    # save file
    genFile("gauss_data.csv", size, key)
    return

def genLTKey():
    size = int(input("Data size: "))
    key = np.random.pareto(a=2, size=(size))
    key = np.round(key).astype(int)
    # save file
    genFile("LT_data.csv", size, key)
    return

def genUniformKey():
    size = int(input("Data size: "))
    key = np.random.uniform(0, size-1, size=(size))
    key = np.round(key).astype(int)
    # save file
    genFile("uniform_data.csv", size, key)
    return

def genBenchmarkKey(data_type):
    # data must be integers
    if data_type == '1':
        genGaussKey()
    elif data_type == '2':
        genLTKey()
    elif data_type == '3':
        genUniformKey()
    else:
        print("Invalid dataset type")
    return

if __name__ == "__main__":
    print("Select the type of dataset:")
    print("|- 1: Gauss distribution")
    print("|- 2: Long-tail distribution")
    print("|- 3: Uniform distribution")
    data_type = input("=> ")
    genBenchmarkKey(data_type)
    print("OK")