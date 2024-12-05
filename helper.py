def read_input(file_path: str) -> list[str]:
    try:
        with(open(file_path, "r") as file):
            return file.read().split("\n")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied.")
    except Exception as e:
        print(f"An error occurred: {e}")