import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    print("=== Cyber Archives Recovery ===")
    filename = sys.argv[1]
    print(f"Accessing file '{filename}'")
    try:
        file_obj = open(filename, "r")
    except OSError as error:
        print(f"Error opening file '{filename}': {error}")
        return
    print("---\n")
    print(file_obj.read())
    print("\n---")

    file_obj.close()
    print(f"File '{filename}' closed.")


if __name__ == "__main__":
    main()
