import random

players: list[str] = [
    "Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
    "john", "kevin", "Liam"
]


def ft_data_alchemist() -> None:

    all_capitalize: list[str] = [player.capitalize() for player in players]
    only_capitalize: list[str] = [
        player for player in players if player == player.capitalize()]
    score_dict: dict[str, int] = {
        name: random.randint(0, 1000) for name in all_capitalize}
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {all_capitalize}")
    print(f"New list of capitalized names only: {only_capitalize}")

    print(f"\nScore dict: {score_dict}")
    average = sum(score_dict.values()) / len(score_dict)

    print(f"Score average is {round(average, 2)}")
    high_scores: dict[str, int] = {player: score_dict[player]
                                   for player in score_dict
                                   if score_dict[player] > average}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    ft_data_alchemist()
