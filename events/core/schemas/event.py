from drf_spectacular.utils import OpenApiParameter, extend_schema

from events.core.schemas.reusable import bad_request_serializer, forbidden_request_serializer
from events.core.serializers import CreateEventSerializer, UpdateEventSerializer

LIST_SCHEMA = extend_schema(description="list all events")
RETRIEVE_SCHEMA = extend_schema(description="retrieve an event")

PARTIAL_UPDATE_SCHEMA = extend_schema(
    description="update an event",
    responses={
        "201": UpdateEventSerializer,
        "400": bad_request_serializer,
        "403": forbidden_request_serializer,
        "404": bad_request_serializer,
    },
)

UPDATE_SCHEMA = extend_schema(
    description="update an event",
    responses={
        "201": UpdateEventSerializer,
        "400": bad_request_serializer,
        "403": forbidden_request_serializer,
        "404": bad_request_serializer,
    },
)

CREATE_SCHEMA = extend_schema(
    description="create an event",
    responses={
        "201": CreateEventSerializer,
        "400": bad_request_serializer,
        "403": forbidden_request_serializer,
    },
)

DESTROY_SCHEMA = extend_schema(
    description="delete an event",
    responses={
        "204": None,
        "400": bad_request_serializer,
        "403": forbidden_request_serializer,
        "404": bad_request_serializer,
    },
)

ADD_PARTICIPANT_SCHEMA = extend_schema(
    description="add participant to an event",
    parameters=[
        OpenApiParameter("user_id", int, location=OpenApiParameter.PATH),
    ],
    request=None,
    responses={
        "200": None,
        "400": bad_request_serializer,
        "403": forbidden_request_serializer,
        "404": bad_request_serializer,
    },
)

REMOVE_PARTICIPANT_SCHEMA = extend_schema(
    description="remove participant from an event",
    parameters=[
        OpenApiParameter("user_id", int, location=OpenApiParameter.PATH),
    ],
    request=None,
    responses={
        "204": None,
        "400": bad_request_serializer,
        "403": forbidden_request_serializer,
        "404": bad_request_serializer,
    },
)
