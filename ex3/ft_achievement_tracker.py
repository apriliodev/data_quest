import random


all_ach: list[str] = ["Crafting Genius", "Strategist", "World Savior",
                      "Speed Runner", "Survivor", "Master Explorer",
                      "Treasure Hunter", "Unstoppable", "First Steps",
                      "Collector Supreme", "Untouchable", "Sharp Mind", "Boss Slayer"]


def gen_player_achievements() -> set[str]:
    ach_num = random.randint(6, 10)
    ach = random.sample(all_ach, ach_num)

    ach_set = set(ach)
    return ach_set


def ft_achievement_tracker() -> None:
    players: dict[str, set[str]] = {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements(),
    }

    for name, ach_set in players.items():
        print(f"Player {name}: {ach_set}")

    print("\n")

    all_set = list(players.values())
    all_achi = set().union(*all_set)
    common_achi = all_set[0].intersection(*all_set[1:])

    print(f"All distinct achievements: {all_achi}\n")
    print(f"Common achievements: {common_achi}\n")

    for name, ach_set in players.items():
        others = [s for (n, s) in players.items() if n != name]
        others_union = set().union(*others)
        only_x = ach_set.difference(others_union)

        print(f"Only {name} has: {only_x}")

    print("\n")

    for name, ach_set in players.items():
        x_missing = all_achi.difference(ach_set)
        print(f"{name} is missing: {x_missing}")


if __name__ == "__main__":
    ft_achievement_tracker()
