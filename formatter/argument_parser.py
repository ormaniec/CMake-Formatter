import argparse


def parse_input_arguments():
    parser = argparse.ArgumentParser(
        prog='CMake Formatter',
        description='Simple python CMake auto formatter',
    )

    parser.add_argument('file_path')
    parser.add_argument('-c', '--configure-file', help='Path to .cmake-configure file, if not default')

    return parser.parse_args()
