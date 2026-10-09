def by_day(list_of_classes: list[tuple[str, str]]) -> dict[str, list[str]]:
    list_of_classes = sorted(list_of_classes, key=lambda x: (x[1], x[0]))
    
    days = {}
    
    for class_name, day in list_of_classes:
        days.setdefault(day, []).append(class_name)
    
    return days