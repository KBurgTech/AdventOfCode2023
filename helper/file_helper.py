def load_input_as_string(file_name):
    with open(file_name, encoding="utf-8") as file:
        text = file.read()
    return text


def load_input_as_lines(file_name):
    with open(file_name, encoding="utf-8") as file:
        text = file.read()
    return text.split("\n")
