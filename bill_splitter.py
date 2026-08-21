from email.mime import text


print("==============Welcome to BillSplitter!==============")
print()
event = input("Enter the occasion or event: ")
print(f"Let's split the bill for {event}.")
Cost = int(input("Enter the total cost: Rs."))
while True:
    ask = input("Was there a tip or service charge?(y/n) ").lower().casefold().startswith("y")
    if ask:
        charge_type = input("Was it a tip or service charge? (tip/service charge) ").lower().casefold().replace("_", " ").strip()
    def parse_amount(raw_value):
        cleaned = raw_value.strip().replace("Rs.", "").replace("rs.", "").replace(",", "").replace("_", "").replace("-", "").strip()
        is_percentage = cleaned.endswith("%")
        value = cleaned[:-1] if is_percentage else cleaned
        return int(value or 0), is_percentage

    if ask and charge_type in ("tip", "tip amount"):
        tip_amount, tip_is_percentage = parse_amount(input("Enter the tip amount: "))
        service_charge_amount = 0
        service_charge_is_percentage = False
    elif ask and charge_type in ("service charge", "service charge amount"):
        service_charge_amount, service_charge_is_percentage = parse_amount(input("Enter the service charge amount: "))
        tip_amount = 0
        tip_is_percentage = False
    else:
        tip_amount = 0
        service_charge_amount = 0
        tip_is_percentage = False
        service_charge_is_percentage = False
        print("No tip or service charge added.")
    break

if tip_is_percentage:
    tip_amount_total = round((tip_amount / 100) * Cost)
else:
    tip_amount_total = tip_amount

if service_charge_is_percentage:
    service_charge_total = round((service_charge_amount / 100) * Cost)
else:
    service_charge_total = service_charge_amount

group_size = int(input("Enter the number of people in the group: "))

if service_charge_total:
    grand_total = round(Cost + service_charge_total)
else:
    grand_total = round(Cost + tip_amount_total)

total_per_person = round(grand_total / group_size)

print()
print(f"Here is the breakdown for {event}:")
print()
print(f"Total Cost: Rs.{Cost}")
if tip_amount_total:
    print(f"Tip Amount: Rs.{tip_amount_total}")
else:
    print(f"Service Charge Amount: Rs.{service_charge_total}")
print(f"Grand Total: Rs.{grand_total}")
print(f"Number of People:{group_size}")
print()
print(f"Each person should pay: Rs.{total_per_person}")

input("\nPress Enter to exit...")

