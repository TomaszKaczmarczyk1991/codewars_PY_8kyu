def calculate_age(year_of_birth, current_year):
    diff = current_year - year_of_birth

    if diff == 1:
        return "You are 1 year old."
    elif diff > 1:
        return f"You are {diff} years old."
    elif diff == 0:
        return "You were born this very year!"
    elif diff == -1:
        return "You will be born in 1 year."
    else:
        return f"You will be born in {abs(diff)} years."
