
def generate_report(dataframe):
    if dataframe.empty:
        print("No book data available to generate report.")
        return

    total_books = len(dataframe)
    average_price = dataframe["price"].mean()
    minimum_price = dataframe["price"].min()
    maximum_price = dataframe["price"].max()
    average_rating = dataframe["rating"].mean()

    report = f"""
========== BOOK SCRAPING REPORT ==========

Total Books Scraped : {total_books}

Average Book Price  : £{average_price:.2f}
Minimum Book Price  : £{minimum_price:.2f}
Maximum Book Price  : £{maximum_price:.2f}

Average Rating      : {average_rating:.2f} / 5

==========================================
"""

    print(report)

    with open("output/summary_report.txt", "w", encoding="utf-8") as file:
        file.write(report)

    print("Report saved successfully!")
