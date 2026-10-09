def can_register_thesis(credits: int, gpa: float) -> bool:
    """
    Check if a student can register for the thesis.
    Eligible if credits >= 120 and gpa >= 2.0.
    """
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    """
    Return human-readable reasons if thesis eligibility criteria are not met.
    """
    reasons: list[str] = []
    if credits < 120:
        needed_credits = 120 - credits
        reasons.append(f"need {needed_credits} more credits")
    if gpa < 2.0:
        needed_gpa = round(2.0 - gpa, 2)
        if needed_gpa > 0:
            reasons.append(f"need {needed_gpa} more GPA")
        else:
            reasons.append("not enough GPA")
    return reasons
