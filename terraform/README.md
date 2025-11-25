
# NkuAlert Terraform Infrastructure

This Terraform project provisions the complete **Azure infrastructure** required for the **NkuAlert** application. It includes:

- Virtual Network (VNet) with public, private, and database subnets  
- Bastion host for SSH access  
- Private application VM  
- Managed PostgreSQL database  
- Azure Container Registry (ACR)  
- Storage account  

Terraform Cloud is used for remote state management (Organization: `NkuAlert_11`, Workspace: `NkuAlert`).

---

## Table of Contents

1. [Prerequisites](#prerequisites)  
2. [Environment Variables](#environment-variables)  
3. [Usage](#usage)  
4. [Terraform Variables](#terraform-variables)  
5. [Outputs](#outputs)  
6. [Terraform Cloud Workspace](#terraform-cloud-workspace)  
7. [Security Notes](#security-notes)  
8. [Troubleshooting](#troubleshooting)  

---

## Prerequisites

Before running Terraform, ensure the following:

- **Terraform CLI** version `>= 1.0` installed  
- **Azure subscription** with permissions to create networking, compute, DB, and ACR resources  
- **Terraform Cloud account** with access to the `NkuAlert` workspace  
- **SSH key pair** for Bastion and application VMs  

---

## Environment Variables

Set your Azure credentials in your shell before running Terraform:

```bash
export ARM_CLIENT_ID="<service-principal-id>"
export ARM_CLIENT_SECRET="<service-principal-secret>"
export ARM_SUBSCRIPTION_ID="<subscription-id>"
export ARM_TENANT_ID="<tenant-id>"
````

Authenticate Terraform with Terraform Cloud:

```bash
terraform login
```

---

## Usage

```bash
cd terraform
terraform init       # Initialize Terraform and download providers
terraform plan       # Preview infrastructure changes
terraform apply      # Apply configuration and create resources
terraform destroy    # Destroy all provisioned resources
```

```

---

This version is **clean, readable, and properly formatted**.  

If you want, I can **merge this with the full README I prepared earlier** so you get the **complete professional README.md** ready to drop into your `terraform/` folder. It will include variables, outputs, security notes, and troubleshooting sections.  

