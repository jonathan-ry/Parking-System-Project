import time
import datetime


# This function automatically generate a ticket number
def number_generator(ticket_number):

    with open("parkingdata.txt", 'r') as park_file:
        lines = park_file.readlines()
    for line in lines[::-1]:  # Read the text file backwards to see the latest ticket number
        if "Ticket Number" in line:
            line = line.strip("Ticket Number: ")  # Removes other text except the ticket number itself
            ticket_number = int(line) + 1
            return ticket_number  # Return the new current value of a ticket number


# This function computes the time difference between park in and out
def time_computation(comp_time):
    datetime_object = datetime.datetime.strptime(comp_time, '%Y-%m-%d %H:%M:%S')
    time_diff = datetime.datetime.now() - datetime_object
    return str(time_diff)[:-7]


# This function finds the ticket ID given in the exit system
def ticket_find(ticket):
    temp_ticket = str(ticket)
    computed_time = None
    with open("parkingdata.txt", 'r') as park_file:
        testing = park_file.readlines()
        for count, check in enumerate(testing):
            if temp_ticket in check:
                new_check = check.strip("\n")
                found_date = str(testing[count+1]).strip("\n")
                computed_time = time_computation(found_date)

        if computed_time is None:
            print("=" * 60)
            print("No Ticket Number Found!!!")
            print("=" * 60)
            print()
            time.sleep(2)
            return 0
        else:
            amount = price_computation(computed_time)
            return amount


# This function computes the total price to be paid by the parking user
def price_computation(time_computed):
    hourly_rate = 15
    price = None
    time_format = '%H:%M:%S'
    converted_time = datetime.datetime.strptime(time_computed, '%H:%M:%S')
    t1 = '0:30:0'
    t2 = '1:00:00'
    if converted_time < datetime.datetime.strptime(t1, time_format):
        temp = str(converted_time)[11:20].split(":")
        print("=" * 60)
        print("FREE PARKING!!!")
        print("=" * 60)
        price = 1
        return price

    elif converted_time > datetime.datetime.strptime(t1, time_format):
        temp = str(converted_time)[11:20].split(":")
        if int(temp[1]) >= 30:
            time_price = 15 * ((int(temp[0])) + 1)
            price = time_price
            return price
        else:
            time_price = 15 * (int(temp[0]))
            price = time_price
            return price


# This function generates the receipt of the parking system
def print_receipt(number, price):
    with open("parkingdata.txt", 'r') as park_file:
        testing = park_file.readlines()
        for count, check in enumerate(testing):
            if str(number) in check:
                new_check = check.strip("\n")
                found_date = str(testing[count+1]).strip("\n")
                computed_time = time_computation(found_date)
    time_duration = time_computation(found_date)
    print("\n")
    receipt_len = 60
    print("=" * receipt_len)
    text = "MCL Parking System".center(receipt_len-2)
    print("={}=".format(text))
    text = "Parking Receipt".center(receipt_len-2)
    print("={}=".format(text))
    print("=" * 60)
    text = " ".center(receipt_len-2)
    print("={}=".format(text))
    text = "Rate: ₱15/Hour".center(receipt_len-2)
    print("={}=".format(text))
    text = " ".center(receipt_len-2)
    print("={}=".format(text))
    text = ("Date In: " + found_date).center(receipt_len-2)
    print("={}=".format(text))
    text = ("Date Out: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())).center(receipt_len-2)
    print("={}=".format(text))
    text = ("Time Duration: " + time_duration).center(receipt_len-2)
    print("={}=".format(text))
    text = " ".center(receipt_len-2)
    print("={}=".format(text))
    text = "Amount to Pay: ₱{}".format(pricing).center(receipt_len-2)
    print("={}=".format(text))
    text = " ".center(receipt_len-2)
    print("={}=".format(text))
    ticketno = str(new_ticketNo)
    text = ("Ticket Number: " + str(number)).center(receipt_len-2)
    print("={}=".format(text))
    text = "║█║▌║█║▌│║▌║▌█║".center(receipt_len-2)
    print("={}=".format(text))
    text = " ".center(receipt_len-2)
    print("={}=".format(text))
    text = "Thank you!".center(receipt_len-2)
    print("={}=".format(text))
    text = " ".center(receipt_len-2)
    print("={}=".format(text))
    print("=" * receipt_len)
    print()
    time.sleep(2)


# initialization
choice = None
number = 1
new_ticketNo = number_generator(1)  # This save the new ticket no that will be used.


class Entry:

    def save_parking(self):
        # Save parking details to text file
        with open("parkingdata.txt", 'a') as park_file:
            print("Ticket Number: {}".format(new_ticketNo), file=park_file)
            print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()), file=park_file)
            print("=" * 60, file=park_file)

    def ticket_generated(self):  # Prints the ticket
        print("\n")
        receipt_len = 60
        print("=" * receipt_len)
        text = "MCL Parking System".center(receipt_len-2)
        print("={}=".format(text))
        text = "Parking Ticket".center(receipt_len-2)
        print("={}=".format(text))
        print("=" * 60)
        text = " ".center(receipt_len-2)
        print("={}=".format(text))
        text = "Rate: ₱15/Hour".center(receipt_len-2)
        print("={}=".format(text))
        text = " ".center(receipt_len-2)
        print("={}=".format(text))
        text = ("Date In: " + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())).center(receipt_len-2)
        print("={}=".format(text))
        text = " ".center(receipt_len-2)
        print("={}=".format(text))
        ticketno = str(new_ticketNo)
        text = ("Ticket Number: " + ticketno).center(receipt_len-2)
        print("={}=".format(text))
        text = "║█║▌║█║▌│║▌║▌█║".center(receipt_len-2)
        print("={}=".format(text))
        text = " ".center(receipt_len-2)
        print("={}=".format(text))
        text = "Do not lose your ticket.".center(receipt_len-2)
        print("={}=".format(text))
        text = "A fine of ₱200 for the loss of ticket ".center(receipt_len-2)
        print("={}=".format(text))
        text = " ".center(receipt_len-2)
        print("={}=".format(text))
        print("=" * receipt_len)
        print()


# Type of system to use
sys_type = {"1": "Entry System",
            "2": "Exit System",
            "0": "Quit"
            }


# Menu Selection
while choice != '0':
    print("*" * 60)
    print("Welcome to MCL Parking System!")
    # System selection
    while True:

        # Gets an input from the system
        print("\nSelect the system you would like to access")
        for i in sys_type:
            print(i, sys_type[i])

        get_choice = input("\nCHOICE: ")

        # This condition test the input if it is correct
        if (get_choice in sys_type) or get_choice == '0':
            print("*" * 60)
            print("\nSelected: {}".format(sys_type[get_choice]))
            choice = get_choice
            break
        else:
            print()
            print("Wrong input!!!\nPlease choose again.")
            print("*" * 60)

    if choice == '1':
        input("Press enter to generate a ticket!\n")
        print("~" * 60)
        print("Generating ticket...")
        print("~" * 60)
        time.sleep(1)
        Entry.save_parking(1)
        Entry.ticket_generated(1)
        time.sleep(2)

    elif choice == '2':
        while number <= 202000:
            temp = input("\nFind Ticket Number: ")
            if temp.isnumeric():
                number = int(temp)
                continue
            else:
                print("Please input number only!!! \nFormat: 202001 and up")
        print()
        pricing = ticket_find(number)
        if pricing > 1:
            print_receipt(number, pricing)
            number = 0
        elif pricing == 1:
            pricing = 0
            print_receipt(number, pricing)
            number = 0
        else:
            print("No Ticket Found")
            number = 0

    # Quit option
    else:
        print()
        print("=" * 60)
        print("System quitting...")
        print("=" * 60)
        time.sleep(1)
        quit()
