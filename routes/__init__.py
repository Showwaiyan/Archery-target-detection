from .score_detection_routes import router as score_detection_router
from .score_detection_routes import router_prefix as score_detection_route_prefix

__all__ = ["score_detection_router",
           "post_ends_scores", "score_detection_route_prefix"]
