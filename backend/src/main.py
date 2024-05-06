def main():
    # Get filename from argument to main
    filename = sys.arg[1]

    # Read input video
    video_reader = VideoReader(filename)

    # Get video data
    processor = Processor(video_reader)

    # Check if video has one person
    if processor is None:
        return "Detected zero people or more than one person.\nPlease provide a video with one person."

    return DisplayUserInterface(processor).display_text()


if __name__ == "__main__":
    main()
