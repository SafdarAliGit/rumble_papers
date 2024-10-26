import frappe
@frappe.whitelist()
def get_mcq(filters=None):
	papers = []
	

	for pp in frappe.get_all("MCQ Question Paper", filters=filters, fields=["*"]):
		questions = []
		
		for qq in frappe.get_all("MQP Question", filters={"parent":pp.name}, fields=["*"]):
			questions.append(qq)
		pp.update({"questions":questions})
		papers.append(pp)
	return papers