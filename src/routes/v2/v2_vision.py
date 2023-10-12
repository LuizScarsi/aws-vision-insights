from controllers.v2_controller import handle_v2_vision

def v2_vision(event, context):
    """
    Calls the function that handles the v2 vision route.
    :return: JSON with statusCode and body with message
    """

    return handle_v2_vision(event, context)