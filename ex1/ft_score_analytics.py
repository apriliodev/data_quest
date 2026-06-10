import sys


class NoArguments(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


def check_scores(arg: list[str]) -> list[int]:
    i = 1
    count = 1
    while i < len(arg):
        try:
            int(arg[i])
        except ValueError:
            print(f"Invalid parameters: '{arg[i]}'")
            count += 1
        i += 1

    processed = len(arg) - count
    if (processed == 0):
        raise NoArguments(f"Usage: python {arg[0]} <score1> <score2> ...")

    i = 0
    j = 1
    scores: list[int] = [0] * processed
    while j < len(arg):
        try:
            scores[i] = int(arg[j])
            i += 1
        except ValueError:
            pass
        j += 1
    return scores


def total(scores: list[int]):
    total = 0
    for score in scores:
        total += score
    return total


def show(arg: list[str]):
    try:
        scores = check_scores(arg)
    except NoArguments as error:
        print(f"No arguments provided. {error}")
        return

    total_s = total(scores)
    len_s = len(scores)
    avrg = total_s / len_s

    print("=== Player Score Ananlytics ===")
    print(f"Scores processed: {scores}")
    print(f"Total score: {total_s}")
    print(f"Average score: {avrg}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores)} - {min(scores)}")


if __name__ == "__main__":
    show(sys.argv)
