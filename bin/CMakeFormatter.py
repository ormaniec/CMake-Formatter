from formatter.argument_parser import parse_input_arguments
from formatter.cmake_formatter import format_cmake_file


def main():
    args = parse_input_arguments()
    format_cmake_file(args)


if __name__ == '__main__':
    main()
