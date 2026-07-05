def secure_archive(filename: str, action: str = "r",
                   content: str = "") -> tuple[bool, str]:
    try:
        if action == "r":
            with open(filename, "r") as file:
                return (True, file.read())
        elif action == "w":
            with open(filename, "w") as file:
                file.write(content)
                return (True, "Content successfully written to file")
    except OSError as error:
        return (False, f"{error}")
    return (False, "Unknown action")


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("looloo.txt"))
    print()

    print("Using 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("looloo.txt"))
    print()

    print("Using 'secure_archive' to read from a regular file:")
    print(secure_archive("looloo.txt"))

    print("Using 'secure_archive' to write previous content to a new file:")
    print(secure_archive("looloo.txt", "w", "looooloooo"))


if __name__ == "__main__":
    main()
