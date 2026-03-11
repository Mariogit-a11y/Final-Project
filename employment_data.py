from city import City

class EmploymentData:
    def __init__(self, city, year, unemployment_rate, education_level):
        self.city = city
        self.year = year
        self.unemployment_rate = unemployment_rate
        self.education_level = education_level

    def __repr__(self):
        return f"EmploymentData({self.city}, {self.year}, {self.unemployment_rate}%, {self.education_level}%)"

    def __eq__(self, other):
        return (self is other or
                type(other) == EmploymentData and
                self.city == other.city and
                self.year == other.year and
                self.unemployment_rate == other.unemployment_rate and
                self.education_level == other.education_level)

    def categorize_education(self):
        if self.education_level >= 50:
            return "High"
        elif self.education_level >= 35:
            return "Medium"
        else:
            return "Low"

    def display_summary(self):
        category = self.categorize_education()
        return (f"City:{self.city.city_name}, {self.city.state}\n"
                f"Year:{self.year}\n"
                f"Unemployment rate:{self.unemployment_rate}%\n"
                f"Education level (Bachelors and Graduate):{self.education_level}%\n"
                f"Education category:{category}\n")