import csv

with open(r"c:\script\values.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    placeholders = {}
    for conf_values in csv_reader:
        dictionary_key = conf_values[0]
        dictionary_value = conf_values[1:]
        placeholders [dictionary_key] = dictionary_value

for five_files in range(1,6):
    with open (r"c:\script\conf.config", "r") as temp_conf:
        template = temp_conf.read()

        for key, value in placeholders.items():
            #conditional expression to determine the index to use for replacing a placeholder with its value.
            index_place = five_files - 1 if five_files <= len(value) else -1 
            placeholder_name = f"{{{key}}}" #escape literal curly braces in an f-string
            template = template.replace(placeholder_name, value [index_place],1)

    with open (f"c:\script\\complete_conf_{five_files}", "w") as compelete_conf:
        compelete_conf.write(template)
        


