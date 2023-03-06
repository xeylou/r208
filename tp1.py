# init sensor db outside functions
sensor_db = []

def adding_sensor_output(input_date: list(), input_time: list(), input_id: int(), input_val: str(), input_type: str()):

    '''adding values from sensor given in parameters
    to a new line of sensor_DB following the pattern'''

    sensor_data = []

    sensor_data.append(input_date)
    sensor_data.append(input_time)
    sensor_data.append(input_id)
    sensor_data.append(input_val)
    sensor_data.append(input_type)

    sensor_db.append(sensor_data)


def display_logs():
    cpt = 1
    for line in sensor_db:
        print("input number", cpt, "is", line)
        cpt += 1
    return("end")


def sort_by_sensor(input_db: list(), input_id: int()):

    # create new db who will contain only info from asked sensor
    tmp_db = []

    for line in input_db:
        if line[2] == input_id:
            tmp_db.append(line)
    
    return(tmp_db)

def sort_by_time_interval(input_db: list(), input_min_date: list(), input_min_time: list(), input_max_date: list(), input_max_time: list()):
    tmp_db = []

    for line in input_db():
        # if line[0] > input_min_date and line[1] > input_min_time and line[0] < input_max_date and line[1] < input_max_time:
        # if line[0], line[1] > input_min_date, input_min_time and line[0], line[1] < input_max_date, input_max_time:
        if line[0] > input_min_date:
            if line[1] > input_min_time:
                if line[0] < input_max_date:
                    if line[1] < input_max_time:
                        tmp_db.append(line)
    
    return(tmp_db)

def sorting_db(input_db):

    for i in range(len(input_db)):
        for j in range(i, len(input_db)):
            if input_db[j] < input_db[i]:
                tmp = input_db[i]
                input_db[i] = input_db[j]
                input_db[j] = tmp
    
    return(input_db)

def menu():
    action = str(input("===== SENSOR MANIPULATION =====\n 1: adding a sensor value\n 2: display logs\n 3: display info from a sensor\n 4: display info between time interval\n 5: display info from the oldest to the newest\n 6: quit\n\nchoice input: "))
    if action == 'q':
        return("")

adding_sensor_output([2023, 3, 7], [7, 35, 55], 2, 45, "degrees C")
adding_sensor_output([2023, 3, 6], [5, 25, 45], 1, 35, "degrees C")
#print(sort_by_sensor(sensor_db, 1))
#print(sort_by_time_interval(sensor_db, [0, 0, 0], [0, 0, 0], [9999, 9999, 9999], [99, 99, 99]))
#print(sorting_db(sensor_db))
menu()
