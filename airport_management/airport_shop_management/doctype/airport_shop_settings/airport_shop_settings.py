# Copyright (c) 2024, kusum and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirportShopSettings(Document):
	
	def get_default_rent_amount():
		return frappe.db.get_single_value('Rent Settings', 'default_rent_amount')

	# Function to check if rent reminders are enabled
	def is_rent_reminder_enabled():
		return frappe.db.get_single_value('Rent Settings', 'enable_rent_reminders')


	