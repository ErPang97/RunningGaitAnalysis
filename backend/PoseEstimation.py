

from ultralytics import YOLO


class PoseEstimation:

    def __init__(self, model_path):
        """
        Initializes the PoseEstimation model, given a model_path string
        :param model_path:
        """
        self.model = YOLO(model_path)

    def train(self):
        pass

    def predict(self, video_path):
        results = self.model(video_path, conf=0.7)
        return results

