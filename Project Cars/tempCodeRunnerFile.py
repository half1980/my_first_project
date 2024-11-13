def search_per_registration_number_without_operator(input_item_number: int, items_database: list[dict]) -> None:

    """function to search the database per registration number of the car without operator in user's input"""
    item_found = False

    for item in items_database:

        item_number = item.get("Number")

        if item_number == input_item_number:
            console.print(f"Registration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n", style="info")
            item_found = True
    if not item_found:
        console.print(f"\nThere are no cars with the registration number {input_item_number} in the database!\n", style="danger")