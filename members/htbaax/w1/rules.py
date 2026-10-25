"""Academic eligibility rules validation (W1-3)."""


def can_register_thesis(credits: int, gpa: float) -> bool:
    """Check whether a student meets the criteria to register for a thesis.

    Requirement: at least 120 credits and GPA >= 2.0.
    """
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """Return a list of human-readable reasons if criteria are not met."""
    reasons: list[str] = []

    if credits < 120:
        reasons.append(f"need {120 - credits} more credits")

    if gpa < 2.0:
        reasons.append("GPA must be at least 2.0")

    return reasons
