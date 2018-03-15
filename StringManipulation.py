# Complete the function below.

def find_unique_names():
    input = ['Khan: 033134331', 'Khan, Saif: 033134331', 'Khan, Saif Ali: 033134331']
    # num_lines = int(sys.stdin.readline().strip())
    record = {}
    order = []
    # for line in sys.stdin:
    for line in input:
        name, aadhar_number = line.split(':')
        aadhar_number = int(aadhar_number)
        if ',' in name:
            last_name, first_name = name.split(',')
            name = first_name.strip() + " " + last_name

        if aadhar_number in record:
            if len(record[aadhar_number]) < len(name):
                record[aadhar_number] = name
        else:
            record[aadhar_number] = name
            order.append(aadhar_number)


    for num in order:
        print(record[num]+":"+str(num))


find_unique_names()