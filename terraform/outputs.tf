output "resource_group_name" {
  description = "Primary resource group name"
  value       = azurerm_resource_group.rg.name
}

output "virtual_network_id" {
  description = "ID of the provisioned virtual network"
  value       = azurerm_virtual_network.main.id
}

output "bastion_public_ip" {
  description = "Public IP address of the bastion host"
  value       = azurerm_public_ip.bastion.ip_address
}

output "bastion_ssh_command" {
  description = "SSH command to connect to bastion host"
  value       = "ssh -i nkualert-key.pem adminuser@${azurerm_public_ip.bastion.ip_address}"
}

output "app_private_ip" {
  description = "Private IP address of the application VM"
  value       = azurerm_network_interface.app.private_ip_address
}

output "database_hostname" {
  description = "Hostname of the PostgreSQL database"
  value       = azurerm_postgresql_flexible_server.db.fqdn
}

output "database_name" {
  description = "Name of the application database"
  value       = azurerm_postgresql_flexible_server_database.app_db.name
}

output "container_registry_login_server" {
  description = "Login server URL for the Azure Container Registry"
  value       = azurerm_container_registry.acr.login_server
}

output "storage_account_name" {
  description = "Name of the storage account"
  value       = azurerm_storage_account.storage.name
}

output "ssh_private_key" {
  description = "SSH private key for VM access (save this securely)"
  value       = tls_private_key.ssh.private_key_pem
  sensitive   = true
}

output "network_security_groups" {
  description = "Names of the created Network Security Groups"
  value = {
    public_nsg  = azurerm_network_security_group.public_nsg.name
    private_nsg = azurerm_network_security_group.private_nsg.name
  }
}

output "subnet_ids" {
  description = "IDs of the created subnets"
  value = {
    public_subnet   = azurerm_subnet.public.id
    private_subnet  = azurerm_subnet.private.id
    database_subnet = azurerm_subnet.database.id
  }
}

output "postgresql_connection_string" {
  description = "PostgreSQL connection string (without password)"
  value       = "postgresql://${var.db_admin_username}@${azurerm_postgresql_flexible_server.db.fqdn}:5432/${var.database_name}"
  sensitive   = true
}

output "bastion_vm_name" {
  description = "Name of the bastion virtual machine"
  value       = azurerm_linux_virtual_machine.bastion.name
}

output "app_vm_name" {
  description = "Name of the application virtual machine"
  value       = azurerm_linux_virtual_machine.app.name
}