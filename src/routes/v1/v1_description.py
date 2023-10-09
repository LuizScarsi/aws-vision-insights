from controllers.v1_controller import handle_v1_description

def v1_description(event, context):
    """
    Demonstrate a lambda function for the v1 description.
    :return: JSON with statusCode and body with message
    """
    return handle_v1_description(event, context)