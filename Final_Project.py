from data_set import DataSet

def main():
    ds = DataSet()
    ds.load_data("unemployment.csv", "education.csv")
    print("Unemployment and Education Report")
    print(f"Total merged records: {len(ds.records)}")

    averages = ds.calculate_averages()
    print("\nOverall Averages:")
    print(f"Average Unemployment Rate: {averages['average_unemployment']}%")
    print(f"Average Education Rate (Bachelors and Graduates): {averages['average_education']}%")

    highest = ds.find_highest()
    lowest = ds.find_lowest()

    if highest:
        print(f"\nHighest Unemployment Record:", highest.display_summary())
    if lowest:
        print(f"\nLowest Unemployment Record:", lowest.display_summary())

    groups = ds.group_by_education()
    print(f"\nEducation Groups:")
    print(f"High: {len(groups['High'])}")
    print(f"Medium: {len(groups['Medium'])}")
    print(f"Low: {len(groups['Low'])}")

    print(f"\nTop 5 Highest Unemployment Records:")
    ds.sort_records(by="unemployment", descending=True)
    for record in ds.records[:5]:
        print(record.display_summary())

    print("\nTop 5 Lowest Unemployment Records:")
    ds.sort_records(by="unemployment", descending=False)
    for record in ds.records[:5]:
        print(record.display_summary())

    print("Social Responsibility Insight:")
    print("This program helps compare unemployment and education levels across different cities.\n"
        "It can support discussion about investing in education access, job training,\n"
        "and workforce development programs to reduce unemployment."
    )
if __name__ == "__main__":
    main()