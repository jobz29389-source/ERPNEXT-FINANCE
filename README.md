### Hospital Custom

Custom finance extensions for st Scholastica Uzima Hospital
# Hospital Custom — St. Scholastica Uzima Hospital

Custom Frappe/ERPNext app for St. Scholastica Uzima Hospital (SSUH), Nairobi, Kenya.
Provides SHA claims management, private insurance claims, and Kenya statutory payroll.

## What's included

### Doctypes
- **SHA Claim** — tracks SHA (Social Health Authority) claims from submission to payment, including partial payments and rejections
- **Private Insurance Claim** — parallel workflow for private insurers (CIC, KU Scheme)

### Server Scripts (automations)
- **Auto Create Invoice on SHA Claim Save** — creates and submits a Sales Invoice when a claim is saved
- **Write Off Rejected SHA Claims** — posts a Journal Entry when a claim has a rejected amount
- **Update SHA Claim on Payment** — increments `amount_paid` when a Payment Entry is submitted
- Same three scripts mirrored for Private Insurance Claims

### Reports
- **SHA Claims Aging** — aging buckets (0-30, 31-60, 61-90, 91-120, 120+) with partial payment logic
- **PIC Claims Aging** — same for private insurance claims

### Payroll components (Kenya statutory)
- Basic Salary, House Allowance, Transport Allowance, Other Allowances
- PAYE (with Income Tax Slab — Kenya PAYE 2026 bands)
- NSSF Tier I, NSSF Tier II, NSSF Employer
- SHIF, Housing Levy, Housing Levy Employer

### Custom Fields
- SHA Claim: `amount_paid`, `rejected_amount`, `writeoff_journal_entry`
- Private Insurance Claim: full field set

## Installation

```bash
cd ~/frappe-bench
bench get-app hospital_custom https://github.com/jobz29389-source/ERPNEXT-FINANCE.git --branch develop
bench --site your-site.local install-app hospital_custom
bench --site your-site.local migrate
