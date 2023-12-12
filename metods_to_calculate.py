def mifflin_metod(weiht, height, age, activity, gender):

    if gender == "Мужчина":
        return str(((10 * weiht) + (6.25 * height) - (5 * age) + 5) * activity)
    if gender == "Женщина":
        return str(((10 * weiht) + (6.25 * height) - (5 * age) - 161) * activity)


def harris_benedict_metod(weiht, height, age, activity, gender):
    if gender == "Мужчина":
        return str(((13.7516 * weiht) + (5.0033 * height) - (6.755 * age) + 66.473) * activity)

    if gender == "Мужчина":
        return str(((9.5634 * weiht) + (1.8496 * height) - (4.6756 * age) + 655.0955) * activity)