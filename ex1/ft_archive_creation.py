import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery & Preservation ===")
    filename: str = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        file_obj = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    content: str = file_obj.read()
    print("---")
    print(content, end="") # ha vor?????????????????????????????????????????????????????????????????
    print("---")

    file_obj.close()
    print(f"File '{filename}' closed.")

    print()
    print("Transform data:\n---")
    lines: list[str] = content.splitlines()

    new_lines: list[str] = [f"{line}#" for line in lines]
    for line in new_lines:
        print(line)

    print("---")
    new_filename: str = input("Enter new file name (or empty): ")
    if new_filename == "":
        print("Not saving data.")
        return

    print(f"Saving data to '{new_filename}'")

    try:
        new_file = open(new_filename, "w")
        for line in new_lines:
            new_file.write(line + "\n")
        new_file.close()
        print(f"Data saved in file '{new_filename}'.")
    except OSError as error:
        print(f"Error saving file '{new_filename}': {error}")

if __name__ == "__main__":
    main()
