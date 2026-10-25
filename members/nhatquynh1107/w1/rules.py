"""Check thesis registration requirements."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Return whether the student has at least 120 credits and a 2.0 GPA."""
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Describe the credit and GPA requirements the student has not met."""
    missingRequirements: list[str] = []

    if credits < 120:
        missingCredits = 120 - credits
        missingRequirements.append(f"need {missingCredits} more credits")
    if gpa < 2.0:
        missingRequirements.append("need at least GPA 2.0")

    return missingRequirements
