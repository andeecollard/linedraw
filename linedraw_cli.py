import sys
import argparse
from linedraw import linedraw

def main():
    parser = argparse.ArgumentParser(description='Convert images to line drawings.')
    parser.add_argument('input_image', help='Path to the input image file')
    parser.add_argument('output_image', help='Path to save the output line drawing')
    args = parser.parse_args()

    # Convert image to line drawing
    linedraw(args.input_image, args.output_image)

if __name__ == "__main__":
    main()
