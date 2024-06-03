 with open(filename, "r") as file:
            content = file.read()
            num_chars = len(content)
            num_words = len(content.split())
            num_lines = content.count('\n') + 1  # Count '\n' to get number of lines

        print(f"Number of characters: {num_chars}")
        print(f"Number of words: {num_words}")
        print(f"Number of lines: {num_lines}")
