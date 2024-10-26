import frappe

@frappe.whitelist()
def post_ual(pdf_name, level, subject, activity_date, activity_time, board, user, season, year):
	ual = frappe.new_doc("User Activity Log")
	ual.pdf_name = pdf_name
	ual.level = level
	ual.subject = subject
	ual.activity_time = activity_time
	ual.activity_date = activity_date
	ual.board = board
	ual.user = user
	ual.season = season
	ual.year = year
	ual.save()

@frappe.whitelist()
def post_an(subject, details, attachment=None):
	an = frappe.new_doc("App Notification")
	an.subject = subject
	an.details = details
	an.attachment = attachment
	an.save()

@frappe.whitelist()
def post_uf(subject, title):
	an = frappe.new_doc("User Feedback")
	an.subject = subject
	an.title = title
	an.save()