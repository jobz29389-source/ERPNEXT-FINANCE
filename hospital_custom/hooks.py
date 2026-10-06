app_name = "hospital_custom"
app_title = "Hospital Custom"
app_publisher = "Job Mutuma"
app_description = "Custom finance extensions for st Scholastica Uzima Hospital"
app_email = "jobz29389@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "hospital_custom",
# 		"logo": "/assets/hospital_custom/logo.png",
# 		"title": "Hospital Custom",
# 		"route": "/hospital_custom",
# 		"has_permission": "hospital_custom.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/hospital_custom/css/hospital_custom.css"
# app_include_js = "/assets/hospital_custom/js/hospital_custom.js"

# include js, css files in header of web template
# web_include_css = "/assets/hospital_custom/css/hospital_custom.css"
# web_include_js = "/assets/hospital_custom/js/hospital_custom.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "hospital_custom/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "hospital_custom/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "hospital_custom.utils.jinja_methods",
# 	"filters": "hospital_custom.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "hospital_custom.install.before_install"
# after_install = "hospital_custom.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "hospital_custom.uninstall.before_uninstall"
# after_uninstall = "hospital_custom.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "hospital_custom.utils.before_app_install"
# after_app_install = "hospital_custom.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "hospital_custom.utils.before_app_uninstall"
# after_app_uninstall = "hospital_custom.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "hospital_custom.notifications.get_notification_config"

# Awesome Bar
# -----------
# Extra search results: list of dicts with label, description, route, index.
# route: ["List", "ToDo"], "/desk/docs/some/page", or "https://example.com"
# awesomebar_search = ["hospital_custom.search.awesomebar_results"]

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"hospital_custom.tasks.all"
# 	],
# 	"daily": [
# 		"hospital_custom.tasks.daily"
# 	],
# 	"hourly": [
# 		"hospital_custom.tasks.hourly"
# 	],
# 	"weekly": [
# 		"hospital_custom.tasks.weekly"
# 	],
# 	"monthly": [
# 		"hospital_custom.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "hospital_custom.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "hospital_custom.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "hospital_custom.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["hospital_custom.utils.before_request"]
# after_request = ["hospital_custom.utils.after_request"]

# Job Events
# ----------
# before_job = ["hospital_custom.utils.before_job"]
# after_job = ["hospital_custom.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"hospital_custom.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

fixtures = [
    {"dt": "Custom Field", "filters": [["module", "=", "Hospital Custom"]]},
    {"dt": "Property Setter", "filters": [["module", "=", "Hospital Custom"]]},
    {"dt": "Server Script"},
    {"dt": "DocType", "filters": [["module", "=", "Hospital Custom"]]},
    {"dt": "Report", "filters": [["module", "=", "Hospital Custom"]]},
    {"dt": "Income Tax Slab"},
    {"dt": "Salary Component"},
    {"dt": "Salary Structure"},
    {"dt": "Salary Structure Assignment"},
    {"dt": "Customer", "filters": [["name", "in", ["SHA", "CIC Insurance", "Kenyatta University Staff Medical Scheme"]]]},
    {"dt": "Item", "filters": [["name", "like", "SHA %"]]},
    {"dt": "Item", "filters": [["name", "like", "CIC %"]]},
    {"dt": "Item", "filters": [["name", "like", "KU %"]]},
    {"dt": "Bank"},
    {"dt": "Bank Account"},
    {"dt": "Asset Category"},
    {"dt": "Journal Entry Template"},
    {"dt": "Payment Term"},
    {"dt": "Payment Terms Template"},
    {"dt": "Tax Withholding Category"},
    {"dt": "Cost Center", "filters": [["company", "=", "St. Scholastica Uzima Hospital"]]},
    {"dt": "Account", "filters": [["company", "=", "St. Scholastica Uzima Hospital"]]},
    {"dt": "Company", "filters": [["name", "=", "St. Scholastica Uzima Hospital"]]},
    {"dt": "Accounts Settings"},
    {"dt": "Payroll Settings"},
    {"dt": "Workspace", "filters": [["module", "=", "Hospital Custom"]]},
    {"dt": "User", "filters": [["name", "like", "%@uzimahosp.org"]]},
    {"dt": "Custom DocPerm"},
    {"dt": "Employee"},
    {"dt": "Salary Slip"},
    {"dt": "SHA Claim"},
    {"dt": "Private Insurance Claim"},
    {"dt": "Sales Invoice"},
    {"dt": "Payment Entry"},
    {"dt": "Journal Entry"},
    {"dt": "Purchase Invoice"},
]
