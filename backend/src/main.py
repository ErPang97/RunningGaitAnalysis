from datamanagement.VideoReader import *
from processor.Processor import *
from ui.DisplayData import *


def main():
    # Get filename from argument to main
    filename = sys.arg[1]

    # Read input video
    video_reader = VideoReader(filename)

    # Get video data
    processor = Processor(video_reader)

    # Check if video has one person
    if processor is None:
        return None

    return DisplayData(processor)


if __name__ == "__main__":
    main()


    
