variable "project_name" {
  description = "The name of the project"
  type        = string
  default     = "nkualert"
}

variable "environment" {
  description = "The environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "location" {
  description = "The Azure region where resources will be created"
  type        = string
  default     = "uaenorth"  # Set to Central India as requested
}

variable "resource_group_name" {
  description = "The name of the resource group"
  type        = string
  default     = "nkualert-rg"
}

variable "bastion_allowed_cidr" {
  description = "The CIDR block allowed to access bastion via SSH"
  type        = string
  default     = "0.0.0.0/0"  # Restrict this in production
}

variable "db_admin_username" {
  description = "The administrator username for PostgreSQL"
  type        = string
  default     = "pgadmin"
}

variable "db_admin_password" {
  description = "The administrator password for PostgreSQL"
  type        = string
  sensitive   = true
  default     = "ChangeThisPassword123!"
}

variable "database_name" {
  description = "The name of the application database"
  type        = string
  default     = "nkualertdb"
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default = {
    owner       = "pendo"
    project     = "nkualert"
    environment = "dev"
  }
}