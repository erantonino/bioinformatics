"""how to create a directory: right click on name of project and click on new directory.
then right click on the directory and select reveal in finder.
then add whatever you want to add to the directory."""


FILE = 'sample_dataset2'


def pattern_count(text, pattern):
    """slides a window of length len(pattern) down text and counts the number of times
    pattern appears in text"""
    count = 0
    last_frame = len(text) - len(pattern) + 1
    for i in range(0, last_frame):
        window = text[i: i + len(pattern)]
        if window == pattern:
            count = count + 1
    return count


def read_file():
    with open(FILE) as file:
        lines = file.readlines()                      # idk but i think this creates a list of lines
        old_text = lines[0]
        enter = len(old_text) - 1                     # here's a comment
        text = old_text.replace(old_text[enter], "")  # this is another comment
        pattern = lines[1]
        return text, pattern


def main():
    text, pattern = read_file()
    print("Text = " + text)
    print("Pattern = " + pattern)
    count = pattern_count(text, pattern)
    print("Count = " + str(count))


if __name__ == "__main__":
    main()
