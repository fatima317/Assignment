from ml_model.diagnosis_info import diagnosis_info

def diagnosis_and_treatment(issue: str, age: int) -> dict:
    info = diagnosis_info.get(issue, {})
    if not info:
        return {}

    # Adjust treatment advice based on age
    if issue == "Malalignment" and age < 7:
        age_note = "Monitor growth; consult orthodontist by age 7"
    elif issue == "Cavity" and age <= 5:
        age_note = "Fluoride varnish and dietary counseling for toddlers"
    else:
        age_note = "Standard treatment advised"

    return {
        "cause": info["cause"],
        "prevention": info["prevention"],
        "treatment": info["treatment"],
        "needs_treatment": info["needs_treatment"],
        "age_note": age_note
    }
