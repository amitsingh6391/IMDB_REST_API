from apinew.permissions import IsAdminOrReadOnly,IsReviewUserOrReadOnly
from rest_framework.throttling import UserRateThrottle,AnonRateThrottle



class ReviewCreateThrottle(UserRateThrottle):

    scope = "review-create"


class ReviewListThrottle(UserRateThrottle):
    scope = "review-list"
