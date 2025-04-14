class RequisitionSystem:
    requisition_id_counter = 10000  
    def __init__(self):
        self.requisitions = []
    def staff_info(self, date, staff_id, staff_name):
        
        return {
            "Date": date,
            "Staff ID": staff_id,
            "Staff Name": staff_name,}
        
    def requisitions_details(self, staff_info, total):
        
        requisition = {
            "Requisition ID": RequisitionSystem.requisition_id_counter,
            "Staff Info": staff_info,
            "Total": total,
            "Status": "Pending",
            "Approval Reference Number": None}
        RequisitionSystem.requisition_id_counter += 1
        self.requisitions.append(requisition)
        return requisition
        
    def check_approval(self, requisition):
        
        if requisition["Total"] >= 500:
            requisition["Status"] = "Approved"
            requisition["Approval Reference Number"] = f"{requisition['Requisition ID']}"
        else:
            requisition["Status"] = "Not approved"
            requisition["Approval Reference Number"] = None
        return requisition

    def respond_requisition(self):
        
        for requisition in self.requisitions:
            if requisition["Status"] == "Pending" and requisition["Total"] >= 500:
                requisition["Status"] = "Approved"
                requisition["Approval Reference Number"] = f"{requisition['Requisition ID']}"
            elif requisition["Status"] == "Pending" and requisition["Total"] < 500:
                requisition["Status"] = "Not approved"
            
    def display_requisitions(self):
        
        for requisition in self.requisitions:
            print(f"Date: {requisition['Staff Info']['Date']}")
            print(f"Requisition ID: {requisition['Requisition ID']}")
            print(f"Staff ID: {requisition['Staff Info']['Staff ID']}")
            print(f"Staff Name: {requisition['Staff Info']['Staff Name']}")
            print(f"Total: {requisition['Total']}")
            print(f"Status: {requisition['Status']}")
            print(f"Approval Reference Numbr: {requisition['Approval Reference Number']}\n")
 
    def requisition_statistics(self):
        
        total_requisitions = len(self.requisitions)
        approved_requisitions = len([req for req in self.requisitions if req["Status"] == "Approved"])
        pending_requisitions = len([req for req in self.requisitions if req["Status"] == "Pending"])
        not_approved_requisitions = len([req for req in self.requisitions if req["Status"] == "Not approved"])

        print("Requisition Statistic:")
        print(f"Total number of requisitions submitted: {total_requisitions}")
        print(f"Total number of approved requisitions: {approved_requisitions}")
        print(f"Total number of pending requisitions: {pending_requisitions}")
        print(f"Total number of not approved requisitions: {not_approved_requisitions}\n")




if __name__ == "__main__":
    system = RequisitionSystem()

    
    staff1 = system.staff_info("11/09/2024", "GA080", "Harry")
    staff2 = system.staff_info("11/09/2024", "GM307", "Mitchel")
    staff3 = system.staff_info("11/09/2024", "GT098", "Emmile")
    staff4 = system.staff_info("11/09/2024", "GL0023", "Shubham")

    system.requisitions_details(staff1, 430)  
    system.requisitions_details(staff2, 1000)  
    system.requisitions_details(staff3, 2200)  
    system.requisitions_details(staff4, 470)  

    
    system.respond_requisition()

    
    system.display_requisitions()

    
    system.requisition_statistics()
