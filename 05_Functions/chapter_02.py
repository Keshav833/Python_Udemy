#you are creating a monthly report for a cafe's sales .
# Instead of putting all logic on place , break it down 

def generate_report( ):
    fetch_sales()
    filter_valid_orders()
    summarize_data()
    print(f"report generated")

def fetch_sales():
    print(f"fetching the  sales ")

def filter_valid_orders():
    print(f"filtering the valid orders ")

def summarize_data():
    print(f"summarizing the data ")

generate_report()