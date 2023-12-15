import os
import csv
import json
from datetime import datetime

input_file = os.path.join(os.path.dirname(__file__), "temp.csv")
output_file = os.path.join(os.path.dirname(__file__), "output.json")
# Initialize an empty list to store the output objects
output_data = []
# Open and read the input CSV file
with open(input_file, mode="r", newline="") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Parse datetimes for 'tradeDateTime' and 'settlementDate'
        trade_date_time = datetime.strptime(row["tradeDateTime"], "%m/%d/%Y %I:%M %p")
        settlement_date = datetime.strptime(row["settlementDate"], "%m/%d/%Y")
        # Parse floats for 'pricePct', 'yieldPct', and 'tradeAmtUSD'
        price_pct = float(row["pricePct"])
        yield_pct = float(row["yieldPct"])
        trade_amt_usd = float(row["tradeAmtUSD"])
        # Parse string for 'calculationDatePricePct'
        calculation_date_price_pct = row["calculationDatePricePct"]
        # Create a dict for each row of data
        data = {
            "TRADE_ACTIVITY_FOR_BondSecurity": {
                "Where": {"securityID": row["securityID"]}
            },
            "randKey": row["randKey"],
            "securityID": row["securityID"],
            "tradeDateTime": trade_date_time.strftime("%m/%d/%Y %I:%M %p"),
            "settlementDate": settlement_date.strftime("%m/%d/%Y"),
            "pricePct": price_pct,
            "yieldPct": yield_pct,
            "calculationDatePricePct": calculation_date_price_pct,
            "tradeAmtUSD": trade_amt_usd,
            "tradeType": row["tradeType"],
            "specialCondition": row["specialCondition"],
        }
        # Append the data dictionary to the output list
        output_data.append(data)
        # Create the final JSON structure

output_json = {"TradeActivities": output_data}
# Write the JSON data to the output.json file
with open(output_file, "w") as json_file:
    json.dump(output_json, json_file, indent=4)
    print("JSON data has been written to output.json")
