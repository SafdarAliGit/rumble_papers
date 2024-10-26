# Copyright (c) 2022, Tech Ventures and contributors
# For license information, please see license.txt
import frappe
from frappe.model.document import Document

class Upload(Document):
	def before_save(self):
		if self.google_drive_link:
			orig_arr = self.google_drive_link.split('/')
			req_link = "https://drive.google.com/uc?export=view&id="+orig_arr[5]
			self.link_for_app = req_link
