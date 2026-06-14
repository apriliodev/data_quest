import sys


def ft_inventory_system() -> None:
    inventory: dict[str, int] = {}

    for arg in sys.argv[1:]:
        itm = arg.split(":")
        if len(itm) != 2:
            print(f"Error - invalid parameter '{arg}'")
            continue
        try:
            value = int(itm[1])
        except ValueError as e:
            print(f"Quantity error for '{itm[0]}': {e}")
            continue
        if itm[0] in inventory:
            print(f"Redundant item '{itm[0]}' - discarding")
            continue
        inventory.update({itm[0]: value})
    if not inventory:
        print("No item and quantity provided. Usage: item:quantity")
        return

    print(f"Got inventory: {inventory}")
    items = list(inventory.keys())
    print(f"Item list: {items}")
    total = sum(inventory.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    for key, values in inventory.items():
        percent: float = round((values / total) * 100, 1)
        print(f"Item {key} represents {percent}%")
    max_value = max(inventory.values())
    for key, values in inventory.items():
        if values == max_value:
            print(f"Item most abundant: {key} with quantity {max_value}")
            break
    min_value = min(inventory.values())
    for key, values in inventory.items():
        if values == min_value:
            print(f"Item least abundant: {key} with quantity {min_value}")
            break
    inventory.update({"magic_item": 1})
    print(f"Updated inventory: {inventory}")


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    ft_inventory_system()
