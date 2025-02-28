import logging
import traceback

from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response
from rest_framework import status

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    A simpler, more generic exception handler for Django REST Framework.
    1. Use DRF's built-in handler for recognized exceptions (ValidationError, etc.).
    2. For unhandled exceptions, group them as "bad requests" or server errors.
    """

    # 1. Let DRF handle any exceptions it knows about (e.g., ValidationError, NotFound).
    response = drf_exception_handler(exc, context)

    # 2. If DRF has created a response, return it as-is (you can still modify if needed).
    if response is not None:
        return response

    # 3. Handle exceptions that DRF does not recognize.
    #    a) Bad Requests: group common Python errors, etc.
    if isinstance(exc, (ValueError, TypeError)):
        logger.warning("Bad Request: %s", exc)
        return Response(
            {
                "detail": "Invalid request data.",
                "status_code": status.HTTP_400_BAD_REQUEST
            },
            status=status.HTTP_400_BAD_REQUEST
        )

    #    b) Fallback: treat everything else as a server error.
    #       Log the exception with traceback for debugging.
    logger.exception("Unhandled exception: %s", exc)
    traceback.print_exc()

    return Response(
        {
            "detail": "Internal server error. Please contact support if the issue persists.",
            "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR
    )