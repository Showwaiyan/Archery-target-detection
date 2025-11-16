from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
from os import getenv

load_dotenv()


async def get_detection_result(file_location: str):
    CLIENT = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com", api_key=getenv("ROBOFLOW_API")
    )

    image_path = file_location
    result = CLIENT.infer(image_path, model_id="target-and-arrow-detection/6")
    return result


async def unpack_detection_target(predictions: object):
    target = None
    scores = []
    for pred in predictions["predictions"]:
        if pred["class"] == "target" and target is None and pred["confidence"] >= 0.6:
            target = pred
        elif pred["confidence"] > 0.5:
            scores.append(int(pred["class"]))

    return target, scores
