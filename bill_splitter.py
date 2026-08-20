print("Welcome to BillSplitter!")
print()
event = input("Enter the occasion or event: ")
print(f"Let's split the bill for {event}.")
print()

Cost = int(input("Enter the total cost: Rs."))
while True:
    service_charge = input("Was there a tip or service charge? (y/n): ").lower().casefold().startswith("y")
    if service_charge:
        service_charge_amount = int(input("Enter the tip or service charge: ").strip("Rs.").strip("%"))
        
    else:
        service_charge_amount = 0
        print("No tip or service charge added.")
    break     

group_size = int(input("Enter the number of people in the group: "))

service_charge_total = round((service_charge_amount / 100) * Cost) if service_charge else 0

grand_total = round(Cost + service_charge_total)

total_per_person = round(grand_total / group_size)

print()
print(f"Here is the breakdown for {event}:")
print()
print(f"Total Cost: Rs.{Cost}")
print(f"Service Charge: Rs.{service_charge_total}")
print(f"Grand Total: Rs.{grand_total}")
print(f"Number of People:{group_size}")
print()
print(f"Each person should pay: Rs.{total_per_person}")

input("\nPress Enter to exit...")
