import csv
from city import City
from employment_data import EmploymentData

class DataSet:
    def __init__(self):
        self.records = []
        self.results = {}
    def __repr__(self):
        return f"DataSet({len(self.records)} records)"
    def __eq__(self, other):
        return (self is other or
                type(other) == DataSet and
                self.records == other.records and
                self.results == other.results)

    def load_data(self, unemployment_file, education_file):
        unemployment_map = {}
        with open(unemployment_file, "r" ,newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = (row["City"],row["State"], row["Year"])
                unemployment_map[key] = float(row["unemployment_rate_pct"])

        with open(education_file, "r" ,newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                key = (row["City"], row["State"], row["Year"])
                if key not in unemployment_map:
                    continue
                bachelors = float(row["bachelors_pct"])
                graduate = float(row["graduate_pct"])
                education_level = round(bachelors + graduate, 2)
                city_obj = City(row["City"], row["State"])
                record = EmploymentData(city_obj,int(row["Year"]), unemployment_map[key], education_level)
                self.records.append(record)

    def calculate_averages(self):

        if not self.records:
            return {"average_unemployment": 0.0, "average_education": 0.0}

        total_unemployment = 0
        total_education = 0

        for r in self.records:
            total_unemployment += r.unemployment_rate
            total_education += r.education_level

        avg_unemployment = round(total_unemployment / len(self.records), 2)
        avg_education = round(total_education / len(self.records), 2)

        self.results["overall_averages"] = {"average_unemployment": avg_unemployment,"average_education": avg_education}

        return self.results["overall_averages"]


    def get_unemployment(self, record):
        return record.unemployment_rate

    def get_education(self, record):
        return record.education_level

    def find_highest(self):
        if not self.records:
            return None
        highest = max(self.records, key=self.get_unemployment)

        self.results["highest_unemployment"] = highest
        return highest

    def find_lowest(self):
        if not self.records:
            return None
        lowest = min(self.records, key=self.get_unemployment)

        self.results["lowest_unemployment"] = lowest
        return lowest


    def group_by_education(self):
        groups = {"High": [],"Medium": [],"Low": []}
        for record in self.records:
            category = record.categorize_education()
            groups[category].append(record)

        self.results["education_groups"] = groups
        return groups

#ChatGpt helped with this function
    def sort_records(self, by="unemployment", descending=True):
        if by == "unemployment":
            self.records.sort(key=self.get_unemployment,reverse=descending)
        elif by == "education":
            self.records.sort(key=self.get_education,reverse=descending)
        return self.records