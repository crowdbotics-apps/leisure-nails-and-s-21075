from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    RecordingViewSet,
    EventViewSet,
    SubscriptionViewSet,
    CourseViewSet,
    GroupViewSet,
    ModuleViewSet,
    PaymentMethodViewSet,
    SubscriptionTypeViewSet,
    EnrollmentViewSet,
    LessonViewSet,
    CategoryViewSet,
)

router = DefaultRouter()
router.register("event", EventViewSet)
router.register("category", CategoryViewSet)
router.register("recording", RecordingViewSet)
router.register("enrollment", EnrollmentViewSet)
router.register("group", GroupViewSet)
router.register("lesson", LessonViewSet)
router.register("subscription", SubscriptionViewSet)
router.register("module", ModuleViewSet)
router.register("course", CourseViewSet)
router.register("subscriptiontype", SubscriptionTypeViewSet)
router.register("paymentmethod", PaymentMethodViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
