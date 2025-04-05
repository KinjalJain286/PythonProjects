def save_to_file(content, filename):
    """Saves the given content to a specified file."""
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Content successfully saved to {filename}.")
    except Exception as e:
        print(f"An error occurred while saving to file: {e}")