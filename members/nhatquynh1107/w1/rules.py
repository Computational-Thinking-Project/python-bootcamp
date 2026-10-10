def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    missingRequirements = []

    if credits < 120:
        missingCredits = 120 - credits
        missingRequirements.append(f"need {missingCredits} more credits")
    if gpa < 2.0:
        missingRequirements.append("need at least GPA 2.0")

    return missingRequirements