# calculates time and memory, outputs a file
# also plots graph
import sys
from resource import *
import time
import psutil
from base import generation,base


gap = 30
penalty = {
    "AA":0,
    "AC":110,
    "AG":48,
    "AT":94,
    "CA":110,
    "CC":0,
    "CG":118,
    "CT":48,
    "GA":48,
    "GC":118,
    "GG":0,
    "GT":110,
    "TA":94,
    "TC":48,
    "TG":110,
    "TT":0
}


def process_memory():
    process = psutil.Process()
    memory_info = process.memory_info()
    memory_consumed = int(memory_info.rss/1024)
    return memory_consumed

def time_wrapper(string1,string2):
    start_time = time.time()
    base(string1,string2,gap,penalty)
    end_time = time.time()
    time_taken = (end_time - start_time)*1000
    return time_taken


if __name__ == '__main__':
    string1,string2 = generation(sys.argv[1])
    cost,path1,path2 = base(string1,string2,gap,penalty)
    time = time_wrapper(string1,string2)
    f = open(sys.argv[2], "x")
    f.write(str(cost)+"\n")
    f.write(path1+"\n")
    f.write(path2+"\n")
    f.write(str(time)+"\n")