# Requisition System

This is a simple requisition system built in Python that allows staff members to submit requisitions for approval, check their approval status, and view requisition statistics.

## Features:
- Staff can submit requisitions with specific details.
- Requisitions are categorized based on their approval status:
  - Pending
  - Approved (for requisitions above 500 in total).
  - Not approved (for requisitions below 500).
- The system generates a unique `Requisition ID` for each new requisition.
- Staff information, including name, ID, and date, is linked to each requisition.
- The system allows displaying all requisitions and generating requisition statistics.

## Classes:
### RequisitionSystem
The core class that manages the requisition operations. It contains the following methods:

1. **`__init__()`**: Initializes the requisition system.
2. **`staff_info(date, staff_id, staff_name)`**: Creates a dictionary containing staff details including date, ID, and name.
3. **`requisitions_details(staff_info, total)`**: Adds a requisition with the given staff info and total amount, and generates a unique requisition ID.
4. **`check_approval(requisition)`**: Approves or disapproves a requisition based on the total amount. If the total is 500 or more, the requisition is approved.
5. **`respond_requisition()`**: Automatically processes requisitions and sets their status based on the total amount (approved or not approved).
6. **`display_requisitions()`**: Displays all requisitions with relevant details (date, ID, staff info, total, status, approval number).
7. **`requisition_statistics()`**: Displays statistics on requisition status, including the total number of requisitions and how many are approved, pending, or not approved.

## How to Use:

### Step 1: Create the Requisition System
Create an instance of the `RequisitionSystem` class to begin using the system.

```python
system = RequisitionSystem()
