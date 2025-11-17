from inference_sdk import InferenceHTTPClient
from dotenv import load_dotenv
from os import getenv

from repositories.range_repository import get_total_arrows_per_end
from repositories.arrow_staging_repository import insert_an_arrow_to_staging

load_dotenv()


async def get_detection_result(file_location: str):
    CLIENT = InferenceHTTPClient(
        api_url="https://serverless.roboflow.com", api_key=getenv("ROBOFLOW_API")
    )

    image_path = file_location
    result = CLIENT.infer(image_path, model_id="target-and-arrow-detection/6")
    return result


async def unpack_detection_target(predictions: object, range_id: int):
    target = None
    scores = []
    for pred in predictions["predictions"]:
        if pred["class"] == "target" and target is None and pred["confidence"] >= 0.6:
            target = pred
        elif pred["confidence"] > 0.5:
            scores.append(int(pred["class"]))

    scores.sort(reverse=True)

    total_arrows_per_end = await get_total_arrows_per_end(range_id)

    if total_arrows_per_end is None:
        return None, None

    if len(scores) > total_arrows_per_end:
        scores = scores[:total_arrows_per_end]

    if len(scores) < total_arrows_per_end:
        needed_zeros = (total_arrows_per_end - len(scores)) * [0]
        scores = scores + needed_zeros

    return target, scores


def validate_arrow(arrow):
    arrowScore = 0
    isX = 0
    if arrow == "X":
        arrowScore = 10
        isX = 1
    elif arrow == "M":
        arrowScore = 0
    else:
        arrowScore = int(arrow)

    return arrowScore, isX


async def insert_an_ends(ends_info):
    arrowScore = None
    isX = None
    for arrow in ends_info.arrows:
        arrowScore, isX = validate_arrow(arrow)
        await insert_an_arrow_to_staging(
            ends_info.roundID,
            ends_info.participationID,
            ends_info.distance,
            ends_info.endOrder,
            arrowScore,
            isX,
        )
    return True
