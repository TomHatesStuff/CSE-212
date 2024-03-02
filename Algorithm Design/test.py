def hotel_purchase_algorithm():
    # Prompt the user for information
    pc = int(input("PC\nWhat is on Pacific Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n"))
    nc = int(input("NC\nWhat is on North Carolina Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n"))
    pa = int(input("PA\nWhat is on Pennsylvania Avenue? (0:nothing, 1:one house, ... 5:a hotel)\n"))
    cash = int(input("Cash\nHow much cash do you have to spend?\n"))
    houses = int(input("Houses\nHow many houses are there to purchase?\n"))
    hotels = int(input("Hotels\nHow many hotels are there to purchase?\n"))
    color_group = input("Color Group\nDo you own all the green properties? (y/n)\n")

    # Check if the user can build a hotel
    if cash < 0:
        print("Out: Cash\nYou do not have sufficient funds to purchase a hotel at this time.")
    elif houses < 0:
        print("Out: No Houses\nThere are not enough houses available for purchase at this time.")
    elif hotels < 0:
        print("Out: No Hotels\nThere are not enough hotels available for purchase at this time.")
    elif color_group.lower() != 'y':
        print("Out: No Properties\nYou cannot purchase a hotel until you own all the properties of a given color group.")
    elif pa == 5:
        print("Out: One Hotel\nYou cannot purchase a hotel if the property already has one.")
    elif nc == 5:
        print("Out: Swap NC\nSwap North Carolina's hotel with Pennsylvania's 4 houses.")
    elif pc == 5:
        print("Out: Swap PC\nSwap Pacific's hotel with Pennsylvania's 4 houses.")
    else:
        price = calculate_price(houses, hotels)
        print(f"Out: Purchase {get_purchase_type(nc, pc)}\nThis will cost ${price}.\n"
              f"Purchase 1 hotel and {houses} house(s).\n"
              f"Put 1 hotel on Pennsylvania and return any houses to the bank.\n"
              f"Put {houses} house(s) on {get_property_name(nc, pc)}.")


def calculate_price(houses, hotels):
    return 50 + (50 * hotels) + (houses * 20)


def get_property_name(nc, pc):
    return "North Carolina" if nc == 1 else "Pacific" if pc == 1 else "unknown"


def get_purchase_type(nc, pc):
    return "C" if nc == 1 else "D" if pc == 1 else "A" if nc == 0 else "B"


# Run the program
hotel_purchase_algorithm()
