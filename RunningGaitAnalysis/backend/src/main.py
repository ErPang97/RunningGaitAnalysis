if __name__ == "__main__":

    # Get filename from argument to main
    filename = sys.arg[1]

    # Read input video
    video_reader = VideoReader(filename)

    # Get video data
    processor = Processor(video_reader)
    
    # Check if video has one person
    if processor == None:
        return
    
    # TODO: Analyze gait