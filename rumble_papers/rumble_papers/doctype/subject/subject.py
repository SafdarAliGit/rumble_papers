# Copyright (c) 2022, Tech Ventures and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Subject(Document):
	def before_save(self):
		for row in self.uploads:
			if row.google_drive_link:
				orig_arr = row.google_drive_link.split('/')
				if len(orig_arr) >=5:
					req_link = "https://drive.google.com/uc?export=view&id="+orig_arr[5]
					row.link_for_app = req_link
