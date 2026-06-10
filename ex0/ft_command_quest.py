import sys


def ft_command_quest():
    arg_len = len(sys.argv)
    print(f"Program name: {sys.argv[0]}")
    if arg_len == 1:
        print("No arguments provided!")
    else:
        i = 1
        print(f"Arguments received: {arg_len - 1}")
        while i < arg_len:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {arg_len}")


if __name__ == "__main__":
    print("=== Command Quest ===")
    ft_command_quest()
