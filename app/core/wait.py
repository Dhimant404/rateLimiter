import time

def delayed_reply(wait_time_in_seconds):
    """
    Delays the execution of the function for a specified amount of time and returns a reply message.

    Args:
        wait_time_in_seconds (int or float): The amount of time in seconds to wait before returning the reply.

    Returns:
        str: A message indicating that the reply is returned after the specified time.
    """
    time.sleep(wait_time_in_seconds)
    return "Reply after specified time in seconds"