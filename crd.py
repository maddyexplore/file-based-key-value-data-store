import time
import json
import os
data = {} # dictionary acts as a JSON in python

def check_file(): # to check json file is present or not , if not create a new one with initial data
    global data
    try:
        if os.path.exists("data_file.json"):
            data = json.loads(open("data_file.json").read())
        else:
            with open("data_file.json","w") as data_file:
                data = {}
                data1 = json.dumps(data,indent=2)
                data_file.write(data1)
                data_file.close()
            data = json.loads(open("data_file.json").read())
        return True
    except Exception:
        print("File is Empty")

def check_size(value): # to check the size of the file and check the value size
    value = len(value)
    if os.path.getsize("data_file.json")<(1024*1024*1024) and value<(16*1024*1024):
        return True
    elif os.path.getsize("data_file.json")>=(1024*1024*1024) and value<(16*1024*1024):
        raise Exception("Error!! File size limit Exceeded...")
    elif os.path.getsize("data_file.json")<(1024*1024*1024) and value>=(16*1024*1024):
        raise Exception("Error!! Value size limit Exceeded...")
    else:
        raise Exception("Error!! file and value limit Exceeded...")

def update():
    with open("data_file.json","w") as data_file:
        temp_data = json.dumps(data,indent=2)
        data_file.write(temp_data)
        data_file.close()

def create(key,value,time_to_live=0):
    try:
        if check_size(value) and key.isalpha(): # constraints to check the size and key whether it is a alphabet or not
            if key not in data: # check whether key is present in data or not
                ex_time = time.time() + time_to_live if time_to_live != 0 else 0
                data[key] = [value,ex_time]
                update()
                print("data created")
            else:
                print("Error || key is already present in data_store")
        else:
            print("Error || Key must Contains only alphabet characters")
    except Exception as e:
        print(e)

def read(key):
    if check_file():
        if key in data:
            if data[key][1] ==0: # constraints to check the time_to_live for read
                print(data[key][0]) 
            else:
                if data[key][1] >= time.time():
                    print(data[key][0])
                else:
                    print("Error || key has been expired")
        else:
            print("Error || Key is not present in data")

def delete(key):
    if check_file():
        if key in data:
            if data[key][1] ==0: # constraints to check the time_to_live for read
                del (data[key])
                update() # to update the data
                print("Value Deleted")
            else:
                if data[key][1] >= time.time():
                    del (data[key])
                    update()
                    print("Value Deleted")
                else:
                    print("Error || key has been expired")
        else:
            print("Error || Key is not present in data")

check_file()
