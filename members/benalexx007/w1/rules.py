def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0


def missing(credits: int, gpa: float) -> list[str]:
    reasons: list[str] = []
    if credits < 120:
        needed_credits = 120 - credits
        unit = "credit" + ("" if needed_credits == 1 else "s")
        reasons.append(f"need {needed_credits} more {unit}")
    if gpa < 2.0:
        reasons.append("need GPA of at least 2.0")
    return reasons
