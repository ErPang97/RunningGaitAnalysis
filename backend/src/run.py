import traceback
from src.datamanagement.VideoReader import *
from src.processor.Processor import *
from src.ui.DisplayData import *


def run(filename, app):
    try:
        print(filename)

        # Read input video
        video_reader = VideoReader(filename)

        # Get video data
        processor = Processor(video_reader)


        # Check if video has one person
        if processor is None:
            return {'error': 'Video does not contain a person'}

        return {'data': DisplayData(processor)}
    except Exception as e:
        traceback_info = traceback.format_exc()
        return {'message': 'in error run.py', 'error': str(e), 'traceback': traceback_info}
    

