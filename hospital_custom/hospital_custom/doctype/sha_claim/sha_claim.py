import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import cint, flt, getdate, nowdate

SUBMITTED_STATES = ("Submitted", "Under Review", "Approved", "Rejected", "Paid")


class SHAClaim(Document):
	def validate(self):
		before = self.get_doc_before_save()
		self.lock_paid_claims(before)
		self.lock_service_type(before)
		self.track_resubmission(before)
		self.check_status_rules()
		self.check_amounts()
		self.check_dates()
		self.check_invoice()
		self.check_duplicates()

	def lock_paid_claims(self, before):
		if before and before.status == "Paid" and self.status != "Paid":
			frappe.throw(_("A claim that has been paid cannot be reopened."))

	def lock_service_type(self, before):
		# Stops outpatient claims being changed to inpatient after submission
		if not before or before.status == "Draft":
			return
		if before.service_type != self.service_type and "System Manager" not in frappe.get_roles():
			frappe.throw(
				_("Service Type cannot be changed once a claim has left Draft. Ask a System Manager if it was entered wrongly.")
			)

	def track_resubmission(self, before):
		if before and before.status == "Rejected" and self.status == "Submitted":
			self.resubmission_count = cint(before.resubmission_count) + 1
			self.submission_date = nowdate()

	def check_status_rules(self):
		if self.status in ("Draft", "Rejected") and self.payment_date:
			frappe.throw(_("A {0} claim cannot have a Payment Date.").format(self.status))

		if self.payment_date and self.status in ("Submitted", "Under Review", "Approved"):
			self.status = "Paid"

		if self.status in SUBMITTED_STATES:
			if not self.submission_date:
				self.submission_date = nowdate()
			if not self.supporting_documents:
				frappe.throw(_("Attach the supporting treatment documents before the claim is submitted."))

		if self.status == "Rejected" and not self.rejection_reason:
			frappe.throw(_("Enter the Rejection Reason for a rejected claim."))

		if self.status in ("Approved", "Paid") and flt(self.amount_approved) <= 0:
			frappe.throw(_("Enter the Amount Approved for an {0} claim.").format(self.status))

		if self.status == "Paid" and not self.payment_date:
			frappe.throw(_("Enter the Payment Date for a paid claim."))

	def check_amounts(self):
		if flt(self.amount_claimed) <= 0:
			frappe.throw(_("Amount Claimed must be more than zero."))
		if flt(self.amount_approved) < 0:
			frappe.throw(_("Amount Approved cannot be negative."))
		if flt(self.amount_approved) > flt(self.amount_claimed):
			frappe.throw(
				_("Amount Approved ({0}) cannot be more than Amount Claimed ({1}).").format(
					self.amount_approved, self.amount_claimed
				)
			)

	def check_dates(self):
		today = getdate(nowdate())
		service = getdate(self.date_of_service)

		if service > today:
			frappe.throw(_("Date of Service cannot be in the future."))
		if self.submission_date:
			submitted = getdate(self.submission_date)
			if submitted > today:
				frappe.throw(_("Submission Date cannot be in the future."))
			if submitted < service:
				frappe.throw(_("Submission Date cannot be before the Date of Service."))
		if self.payment_date:
			if not self.submission_date:
				frappe.throw(_("A claim cannot be paid before it is submitted."))
			if getdate(self.payment_date) < getdate(self.submission_date):
				frappe.throw(_("Payment Date cannot be before the Submission Date."))

	def check_invoice(self):
		if not self.sales_invoice:
			return
		invoice = frappe.db.get_value(
			"Sales Invoice", self.sales_invoice, ["grand_total", "docstatus"], as_dict=True
		)
		if not invoice:
			frappe.throw(_("Sales Invoice {0} was not found.").format(self.sales_invoice))
		if invoice.docstatus == 2:
			frappe.throw(_("Sales Invoice {0} is cancelled.").format(self.sales_invoice))
		if flt(self.amount_claimed) > flt(invoice.grand_total):
			frappe.throw(
				_("Amount Claimed ({0}) is more than the invoice total ({1}).").format(
					self.amount_claimed, invoice.grand_total
				)
			)

	def check_duplicates(self):
		if self.sales_invoice:
			same_invoice = frappe.db.get_value(
				"SHA Claim", {"sales_invoice": self.sales_invoice, "name": ["!=", self.name]}
			)
			if same_invoice:
				frappe.throw(_("Sales Invoice {0} already has a claim: {1}.").format(self.sales_invoice, same_invoice))

		same_visit = frappe.db.get_value(
			"SHA Claim",
			{
				"patient_name": self.patient_name,
				"date_of_service": self.date_of_service,
				"service_type": self.service_type,
				"name": ["!=", self.name],
			},
		)
		if same_visit:
			frappe.throw(
				_("A {0} claim for {1} on {2} already exists: {3}.").format(
					self.service_type, self.patient_name, self.date_of_service, same_visit
				)
			)
