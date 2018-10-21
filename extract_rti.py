#!/usr/bin/env python3

import os
import olefile
import zlib
import argparse

fstr = 'Stream: %s -- Type: %s. Size: %d. Outpath:%s'

parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str, metavar='file',help='RTI driver file')
parser.add_argument('-o','--out_directory',type=str, default='./out', metavar='out_directory',help='output directory')


def write_bytestr_to_file(s,path):
    with open(path, "wb") as text_file:
        text_file.write(s)

def make_directory(dirpath):
    os.makedirs(dirpath,exist_ok=True)

def extract_data_from_stream(sd):
    try:
        sd_decompressed = zlib.decompress(sd)
        sd = sd_decompressed
    except zlib.error as e:
        pass

    return sd

if __name__ == '__main__':
    args = parser.parse_args()
    make_directory(args.out_directory)

    ole = olefile.OleFileIO(args.filename)
    for s in ole.listdir():
        # get stream info
        stream_name = s[0]
        stream_type = ole.get_type(stream_name)
        stream_size = ole.get_size(stream_name)
        out_path = os.path.join(args.out_directory,stream_name)

        # get data
        stream = ole.openstream(stream_name)
        stream_data = stream.read()
        stream_data = extract_data_from_stream(stream_data)
        write_bytestr_to_file(stream_data,out_path)

        # log action
        print(fstr % (stream_name,stream_type,stream_size,out_path))

    ole.close()