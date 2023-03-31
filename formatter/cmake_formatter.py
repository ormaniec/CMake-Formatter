# from CMakeFile import CMakeFile
from formatter.cmake_parser import read_next_command


def format_cmake_file(args):
    val = read_next_command(args.file_path)
    # cmake_file = CMakeFile(args.file_path)
