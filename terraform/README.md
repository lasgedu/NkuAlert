# Terraform Infrastructure

This directory provisions the complete Azure environment required for NkuAlert, including virtual networking, bastion host, private application VM, managed PostgreSQL database, and Azure Container Registry. Terraform Cloud stores the remote state (organization `NkuAlert_11`, workspace `NkuAlert`).

## Prerequisites

- Terraform CLI `>= 1.0`
- Azure subscription with permissions to create networking, compute, DB, and ACR resources
- Terraform Cloud account with access to the `NkuAlert` workspace
- SSH key pair for the bastion/application hosts

## Environment Variables

Export Azure credentials before running Terraform (or configure them in your shell profile):

```bash
export ARM_CLIENT_ID="<service-principal-id>"
export ARM_CLIENT_SECRET="<service-principal-secret>"
export ARM_SUBSCRIPTION_ID="<subscription-id>"
export ARM_TENANT_ID="<tenant-id>"
```

Authenticate Terraform with Terraform Cloud once:

```bash
terraform login
```

## Usage

```bash
cd terraform
terraform init           # downloads providers and connects to Terraform Cloud
terraform plan           # review the infrastructure changes
terraform apply          # provision Azure resources
terraform destroy        # tear everything down when finished
```

Adjust `terraform.tfvars` (or provide your own `.tfvars` file) with project-specific values such as `acr_name`, SSH key, trusted IP ranges, and database password. Never commit real secrets; replace them with placeholders before pushing.

## Outputs

After `terraform apply`, note the following outputs for downstream automation:

- `bastion_public_ip`: SSH entry point used by Ansible
- `app_private_ip`: Target host for Docker/compose deployment
- `database_fqdn`: Connection endpoint for the application
- `container_registry_login_server`: Used by CI/CD pipelines to push/pull images

These values feed directly into the Ansible inventory and GitHub Actions secrets for the CD workflow.

