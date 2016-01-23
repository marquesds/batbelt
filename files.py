def list_files(suffix, path, show_fullpath=False):
    """
    Search for files with given suffix in a path and list them.

    Args:
        suffix: File extension to be analysed. It works with strings, regex and tuple of strings.
                If empty string, method will show all type of files in specified path.
        path: Path to list files
        show_fullpath: If this flag is True, method will return a list of filenames with
                       fullpath of each file plus its name.

    :return: A list of all files in a path
    """
    if os.path.exists(path):
        if not show_fullpath:
            return [f for f in listdir(path) if isfile(join(path, f)) and f.endswith(suffix)]
        else:
            return [os.path.join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.endswith(suffix)]
    else:
        return []
