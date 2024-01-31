import os


def validate_output_path(output_path):
    """
    Validate the output path. If the path is a directory, create it if it doesn't exist.
    If it's a file path and the directory does not exist, create it.
    """
    if os.path.isdir(output_path) or not os.path.splitext(output_path)[1]:
        output_dir = output_path
    else:
        output_dir = os.path.dirname(output_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_path
