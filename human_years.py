def human_years_cat_years_dog_years(human_years):
    cat = 0
    dog = 0
    
    if human_years == 1:
        cat = 15
        dog = 15
    elif human_years == 2:
        cat = 15 + 9
        dog = 15 + 9
    else:
        cat = 24 + ((human_years - 2) * 4)
        dog = 24 + ((human_years - 2) * 5)
        
    return [human_years, cat, dog]