import sys

def main():
    args = sys.argv[1:]  # Get command-line arguments excluding script name

    if not args:
        print("Welcome,\nShaurya - Phazegod\n")
        print_ascii_name()
    elif args[0] == "-help":
        print("Install zenpo - phazegod -zenpo")
    elif args[0] == "-zenpo":
        print("run 'pip install zenpo'")
    else:
        print(f"Unknown argument: {' '.join(args)}")
        print("Use 'phazegod -help' for help.")

def print_ascii_name():
    print(r"""
   _____  _                  _                 
  |  __ \| |                | |                
  | |__) | | __ _ _ __   ___| |__   ___  _ __  
  |  ___/| |/ _` | '_ \ / __| '_ \ / _ \| '_ \ 
  | |    | | (_| | | | | (__| | | | (_) | | | |
  |_|    |_|\__,_|_| |_|\___|_| |_|\___/|_| |_|
                                              
                    Shaurya - Phazegod
    """)

if __name__ == "__main__":
    main()
