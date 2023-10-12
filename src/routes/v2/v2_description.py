from controllers.v2_controller import handle_v2_description

def v2_description(event, context):
    """
    Demonstrate a lambda function for the v2 description.
    :return: JSON with statusCode and body with message
    """
    return handle_v2_description(event, context)