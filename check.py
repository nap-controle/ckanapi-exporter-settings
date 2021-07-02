import csv
import sys
tag_list = ["Air", "Bike-hire", "Bike-sharing", "Bus", "Car", "Car-hire", "Car-pooling", "Car-sharing", "Conventional rail", "Cycle", "Light rail", "Long-distance coach", "Maritime", "Metro", "Motorcycle", "Pedestrian", "Rail", "Shuttle bus", "Shuttle ferry", "Taxi", "Tram", "Trolley-bus", "Truck"]
# print 'Argument List:', str(sys.argv)
with open(sys.argv[1]) as f:
    with open(sys.argv[2], 'w') as w:
        reader = csv.reader(f)
        writer = csv.writer(w)
        firstrow = []
        for row in reader:
            if len(firstrow) == 0:
                firstrow = row
                firstrow += ["checks"]
                writer.writerow(firstrow)
                continue
            
            errors = []
            for c in range(len(firstrow) - 1):
                name = firstrow[c]
                val = row[c]

                # check cont_res
                if name == "cont_res":
                    if val.lower() != "data set" and val.lower() != "service":
                        error = "cont_res is " + val + " instead of Data set or Service"
                        errors += [error]
                        print(error)
                    continue

                # check fluent_tags
                if name == "fluent_tags":
                    split = val.split(",")
                    for t in split:
                        if not(t in tag_list):
                            error = "fluent_tags contains invalid tag " + t
                            errors += [error]
                            print(error)
                    continue

                # default columm, just check if there is something.
                val = val.replace(",", "")
                val = val.strip()
                if len(val) == 0:
                    error = firstrow[c] + " is empty"
                    errors += [firstrow[c] + " is empty"]
                    print(error)
                if len(val) > 100:
                    row[c] = val[:100]
            
            row += [",".join(errors)]
            writer.writerow(row)