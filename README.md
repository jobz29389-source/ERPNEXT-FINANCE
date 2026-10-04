# Hospital Custom — St. Scholastica Uzima Hospital

Custom Frappe/ERPNext app for SSUH (Ruaraka, Nairobi). Provides SHA claims management, private insurance claims, and Kenya statutory payroll.

## Doctypes
- **SHA Claim** — claim tracking with partial payments and rejection write-offs
- **Private Insurance Claim** — parallel workflow for CIC, KU Scheme

## Server Scripts
- Auto Create Invoice on SHA Claim Save
- Write Off Rejected SHA Claims
- Update SHA Claim on Payment
- Same three scripts for Private Insurance Claims

## Reports
- SHA Claims Aging
- PIC Claims Aging
- Monthly Revenue by Service Type
- Monthly Revenue Trend
- Monthly Payer Mix
- Daily Cash Report
- Debtor Aging
- Creditor Aging
- Claim Status Summary
- Invoice Summary by Customer
- Supplier Payment Summary

## Master Data
- Customers: SHA, CIC Insurance, Kenyatta University Staff Medical Scheme
- Items: 5 SHA + 5 CIC + 5 KU services
- Cost Centers: 20
- Asset Categories: 9
- Banks: KCB, NBK, M-Pesa

## Payroll (Kenya)
- Income Tax Slab: Kenya PAYE 2026
- Salary Components: Basic, House, Transport, Other; PAYE; NSSF Tier I/II; NSSF Employer; SHIF; Housing Levy; Housing Levy Employer; NITA Levy
- Salary Structure: SSUH Staff Monthly v3
- Note: Salary Slip generation works partially (employee deductions pending fix)

## Statutory
- WHT Professional Fees (5%)
- WHT Contractual Fees (3%)
- NITA Payable

## Users & Roles
- 18 users across Finance, HR, Clinical, Admin
- ERPNext default role permissions

## Installation
bench get-app hospital_custom https://github.com/jobz29389-source/ERPNEXT-FINANCE.git --branch develop
bench --site your-site.local install-app hospital_custom
bench --site your-site.local migrate

## Requirements
- Frappe Framework v15
- ERPNext v15
- HRMS v15

## Statutory Rates
Kenya statutory rates change regularly. Verify against current KRA guidance before running payroll.

## License
Internal use — Missionary Benedictine Sisters / St. Scholastica Uzima Hospital.
