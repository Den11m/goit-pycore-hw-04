import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)


def print_directory_structure(directory_path, depth=0):
    try:
        path = Path(directory_path)
        if not path.exists():
            print(f"{Fore.RED}Error: Path '{directory_path}' does not exist.{Style.RESET_ALL}")
            return
        if not path.is_dir():
            print(f"{Fore.RED}Error: Path '{directory_path}' is not a directory.{Style.RESET_ALL}")
            return

        # Get all items in the directory
        items = sorted(path.iterdir(), key=lambda x: (not x.is_dir(), x.name))
        
        for item in items:
            indent = "  " * depth
            
            # Print the item with appropriate color
            if item.is_dir():
                print(f"{indent}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
                # Recursively print subdirectories
                print_directory_structure(item, depth + 1)
            else:
                print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
                
    except PermissionError:
        print(f"{Fore.RED}[Permission denied]{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}[Error: {e}]{Style.RESET_ALL}")


def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python task3.py <directory_path>{Style.RESET_ALL}")
        sys.exit(1)
    
    directory_path = sys.argv[1]
    path = Path(directory_path)
    
    # Print the root directory
    print(f"{Fore.BLUE}{path.name}/{Style.RESET_ALL}")
    
    # Print the structure
    print_directory_structure(path, depth=1)


if __name__ == "__main__":
    main()
