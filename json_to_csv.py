import csv
import json

file_name = 'train' # "dev" or "test"

# Open CSV file for writing
with open(file_name+'.csv', 'w', newline='') as f:
    # Create CSV writer
    writer = csv.writer(f)

    # Write header row
    header = ["question", "exp", "cop", "opa", "opb", "opc", "opd", "subject_name", "topic_name", "id", "choice_type"]
    writer.writerow(header)

    # Read JSON data from file line by line
    with open(file_name+'.json') as json_file:
        for line in json_file:
            # Load JSON object from line
            data = json.loads(line)

            # Write data row
            writer.writerow([data.get("question"), data.get("exp"), data.get("cop"), data.get("opa"), data.get("opb"), data.get("opc"), data.get("opd"), data.get("subject_name"), data.get("topic_name"), data.get("id"), data.get("choice_type")])
