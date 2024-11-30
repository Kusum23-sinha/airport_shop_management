# Copyright (c) 2024, kusum and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Shop(Document):
    def before_insert(self):
        # Fetch settings from "Airport Shop Settings" Single DocType
        settings = frappe.get_single("Airport Shop Settings")

        # Check if default_rent_amount exists in settings
        if settings.default_rent_amount:
            # Set the default rent amount if rent_amount is not provided
            if not self.rent_amount:
                self.rent_amount = settings.default_rent_amount
                print(f"Default rent amount set to: {self.rent_amount}")
        else:
            print("Default rent amount not set in Airport Shop Settings")

        
    





















# import frappe
# from frappe.model.document import Document

# class Shop(Document):
#     def after_save(self):
#         # Call the function to update shop counts in the Airport DocType
#         update_airport_shop_counts(self)

# def update_airport_shop_counts(doc):
#     if not doc.airport:
#         return  # Exit if no airport is linked

#     # Fetch the linked Airport document
#     airport = frappe.get_doc("Airports", doc.airport)

#     # Total number of shops for this airport (should be set in the Airports DocType)
#     total_shops = airport.total_shops

#     # Count occupied shops for this airport
#     occupied_count = frappe.db.count("Shop", filters={"airport": doc.airport, "status": "Occupied"})

#     # Calculate available shops based on total shops
#     available_count = total_shops - occupied_count

#     # Update the Airport's shop counts
#     airport.occupied_shops = occupied_count
#     airport.available_shops = available_count

#     # Save the updated Airport record
#     airport.save()






   



