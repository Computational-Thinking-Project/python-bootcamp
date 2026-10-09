def can_register_thesis(credits: int, gpa: float) -> bool:
    return credits >= 120 and gpa >= 2.0

def missing(credits: int, gpa: float) -> list[str]:
    missing_requirements = []
    if (credits < 120):
        missingCredits = 120 - credits
        missing_requirements.append("need " + str(missingCredits) + " more credits")
        
    if (gpa < 2.0):
        missing_requirements.append("need a GPA of at least 2.0")
    
    return missing_requirements