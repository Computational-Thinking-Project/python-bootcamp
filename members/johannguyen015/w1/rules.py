def can_register_thesis(credits: int, gpa: float) -> bool:
    if credits < 120:
        return False
    return gpa >= 2.0 #can register thesis if credts >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    missing_requirements = []
    if credits < 120:
        missing_requirements.append(f"need {120 - credits} more credits")
    if gpa < 2.0:
        missing_requirements.append(f"need at least 2.0 GPA (current: {gpa})")
    return missing_requirements
