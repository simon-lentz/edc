import os
import csv
import json
from datetime import datetime

input_file = os.path.join(os.path.dirname(__file__), "temp.json")
output_file = os.path.join(os.path.dirname(__file__), "output.csv")
# Open and read the input JSON file
with open(input_file, "r") as json_file:
    input_data = json.load(json_file)

# Extract the list of output objects from the input data
output_data = input_data["output"]
# Create the output CSV file
with open(output_file, mode="w", newline="") as csv_file:
    fieldnames = [
        "securityID",
        "tradeDateTime",
        "settlementDate",
        "pricePct",
        "yieldPct",
        "calculationDatePricePct",
        "tradeAmtUSD",
        "tradeType",
        "specialCondition",
    ]
    csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    csv_writer.writeheader()
    # Write each output object to a row in the CSV file
    for output_object in output_data:
        # Parse datetime for 'tradeDateTime' and 'settlementDate'
        trade_date_time = datetime.strptime(
            output_object["tradeDateTime"], "%m/%d/%Y %I:%M %p"
        )
        settlement_date = datetime.strptime(output_object["settlementDate"], "%m/%d/%Y")
        #  Write the output object to a row in the CSV file
        csv_writer.writerow(
            {
                "securityID": output_object["securityID"],
                "tradeDateTime": trade_date_time.strftime("%m/%d/%Y %I:%M %p"),
                "settlementDate": settlement_date.strftime("%m/%d/%Y"),
                "pricePct": output_object["pricePct"],
                "yieldPct": output_object["yieldPct"],
                "calculationDatePricePct": output_object["calculationDatePricePct"],
                "tradeAmtUSD": output_object["tradeAmtUSD"],
                "tradeType": output_object["tradeType"],
                "specialCondition": output_object["specialCondition"],
            }
        )

    print("CSV data has been written to output.csv")
