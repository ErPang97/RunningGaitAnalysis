

from ultralytics import YOLO


class PoseEstimation:

    def __init__(self, model_path):
        """Initializes the PoseEstimation model
        Args:
             model_path - str path to the model
        """
        self.model = YOLO(model_path)

    def train(self):
        """Trains the model

        """
        pass

    def predict(self, video_path):
        """ Annotates the model, given a video_path
        Args:
            video_path - str path to a video file
        Returns:
            the results array
        """
        results = self.model(video_path, conf=0.7)
        return results

