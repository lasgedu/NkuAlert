project_name        = "nkualert"
environment         = "dev"
location           = "uaenorth"
resource_group_name = "nkualert-rg"
bastion_allowed_cidr = "0.0.0.0/0"  # Change to your IP in production
db_admin_username   = "psqladmin"
db_admin_password   = "Pendo123@"
database_name       = "nkualertdb"

tags = {
  owner       = "pendo"
  project     = "nkualert"
  environment = "dev"
  student     = "true"
}