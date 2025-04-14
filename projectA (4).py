def staff_info(counter):
    date = input("Enter Date : ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Staff Name: ")
   
    requisition_id = counter + 10000
    
    Print information
    print(f"\nPrinting Staff Information:")
    # print(f"Date: {date}")
    # print(f"Staff ID: {staff_id}")
    # print(f"Counter t : {counter}")
    # print(f"Staff Name: {staff_name}")
    # print(f"Requisition ID: {requisition_id}")
    
    # Return values
    return date, staff_id, staff_name, requisition_id




def requisitions_total(counter):
    
    # Collects requisition items and their prices, then computes the total value.
    
    date, staff_id, staff_name, requisition_id = staff_info(counter)
    
    total = 0
    while True:
        item_name = input("Enter Requisition Item Name (or 'done' to finish): ")
        if item_name == 'done':
            break
        price = float(input(f"Enter price for {item_name}: "))
        total += price
    
    # print(f"\nTotal: ${total}")
    
    return date, staff_id, staff_name, requisition_id, total



def requisition_approval(counter):
    
    # Determines the status of the requisition and generates an approval reference number if approved.
    
    date, staff_id, staff_name, requisition_id, total = requisitions_total(counter)
    
    if total < 500:
        status = "Approved"
        approval_reference_number = f"{staff_id}{str(requisition_id)[0:3]}"
    else:
        status = "Pending"
        approval_reference_number = "N/A"
    
    # print(f"\nTotal: ${total}")
    # print(f"Status: {status}")
    # print(f"Approval Reference Number: {approval_reference_number}")
    
    return date, staff_id, staff_name, requisition_id, total, status, approval_reference_number



def display_requisitions(counter):
    
    # Displays the staff's requisition information including total and approval status.
    
    date, staff_id, staff_name, requisition_id, total, status, approval_reference_number = requisition_approval(counter)
    
    print(f"\nPrinting Requisitions:")
    print(f"Date: {date}")
    print(f"Requisition ID: {requisition_id}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Total: ${total}")
    print(f"Status: {status}")
    
    print(f"Approval Reference Number: {approval_reference_number}")



counter = 70  
display_requisitions(counter)