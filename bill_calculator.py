#calculates tips from the given bill amount and tip percent
def calculate_tip(bill_amount, tip_percent):
    tip_amount = bill_amount * tip_percent * .01
    return tip_amount


#print calculate_tip(100, 20)
def total_bill(tip_amount, bill_amount):
    total_bill = tip_amount + bill_amount
    return total_bill


#print total_bill(100, 20)
def split_bill(total_bill, number_people):
    bill_per_person = total_bill / number_people
    return bill_per_person

#print split_bill(100, 5)


def main():
    choice = raw_input("Enter 1 for calculate tip or 2 for split the bill: ")
    if choice == '1':
        bill_amount = float(raw_input("Enter original bill amount: "))
        tip_percentage = float(raw_input("Enter tip percentage: "))
        tip_amount = calculate_tip(bill_amount, tip_percentage)
        total_bill_amount = total_bill(tip_amount, bill_amount)
        print tip_amount
        print total_bill_amount
        split_answer = raw_input("Would you like to have the bill split? [y/n]")
        if split_answer == 'y':
            number_of_people = int(raw_input("How many ways do you want to split the bill?"))
            print split_bill(total_bill_amount, number_of_people)
        elif split_answer == 'n':
            return
    elif choice == '2':
        bill_total_amount = float(raw_input("Enter bill total amount: "))
        number_of_people = int(raw_input("How many ways do you want to split the bill?"))
        print split_bill(bill_total_amount, number_of_people)

if __name__ == '__main__':
    main()