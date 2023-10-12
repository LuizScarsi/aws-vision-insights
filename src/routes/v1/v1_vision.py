from controllers.v1_controller import handle_v1_vision

def v1_vision(event, context):
    """
    Calls the function that handles the v1 vision route.
    :return: JSON with statusCode and body with message
    """

    return handle_v1_vision(event, context)