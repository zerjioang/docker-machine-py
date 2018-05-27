from machine.config.abstract import AbstractMachineConfig


class AzureMachineConfig(AbstractMachineConfig):
    """
Options:

   --azure-availability-set "docker-machine"								Azure Availability Set to place the virtual machine into [$AZURE_AVAILABILITY_SET]
   --azure-client-id 											Azure Service Principal Account ID (optional, browser auth is used if not specified) [$AZURE_CLIENT_ID]
   --azure-client-secret 										Azure Service Principal Account password (optional, browser auth is used if not specified) [$AZURE_CLIENT_SECRET]
   --azure-custom-data 											Path to file with custom-data [$AZURE_CUSTOM_DATA_FILE]
   --azure-dns 												A unique DNS label for the public IP adddress [$AZURE_DNS_LABEL]
   --azure-docker-port "2376"										Port number for Docker engine [$AZURE_DOCKER_PORT]
   --azure-environment "AzurePublicCloud"								Azure environment (e.g. AzurePublicCloud, AzureChinaCloud) [$AZURE_ENVIRONMENT]
   --azure-image "canonical:UbuntuServer:16.04.0-LTS:latest"						Azure virtual machine OS image [$AZURE_IMAGE]
   --azure-location "westus"										Azure region to create the virtual machine [$AZURE_LOCATION]
   --azure-no-public-ip											Do not create a public IP address for the machine
   --azure-open-port [--azure-open-port option --azure-open-port option]				Make the specified port number accessible from the Internet
   --azure-private-ip-address 										Specify a static private IP address for the machine
   --azure-resource-group "docker-machine"								Azure Resource Group name (will be created if missing) [$AZURE_RESOURCE_GROUP]
   --azure-size "Standard_A2"										Size for Azure Virtual Machine [$AZURE_SIZE]
   --azure-ssh-user "docker-user"									Username for SSH login [$AZURE_SSH_USER]
   --azure-static-public-ip										Assign a static public IP address to the machine
   --azure-storage-type "Standard_LRS"									Type of Storage Account to host the OS Disk for the machine [$AZURE_STORAGE_TYPE]
   --azure-subnet "docker-machine"									Azure Subnet Name to be used within the Virtual Network [$AZURE_SUBNET]
   --azure-subnet-prefix "192.168.0.0/16"								Private CIDR block to be used for the new subnet, should comply RFC 1918 [$AZURE_SUBNET_PREFIX]
   --azure-subscription-id 										Azure Subscription ID [$AZURE_SUBSCRIPTION_ID]
   --azure-use-private-ip										Use private IP address of the machine to connect
   --azure-vnet "docker-machine-vnet"									Azure Virtual Network name to connect the virtual machine (in [resourcegroup:]name format) [$AZURE_VNET]
   --driver, -d "virtualbox"										Driver to create machine with. [$MACHINE_DRIVER]
   --engine-env [--engine-env option --engine-env option]						Specify environment variables to set in the engine
   --engine-insecure-registry [--engine-insecure-registry option --engine-insecure-registry option]	Specify insecure registries to allow with the created engine
   --engine-install-url "https://get.docker.com"							Custom URL to use for engine installation [$MACHINE_DOCKER_INSTALL_URL]
   --engine-label [--engine-label option --engine-label option]						Specify labels for the created engine
   --engine-opt [--engine-opt option --engine-opt option]						Specify arbitrary flags to include with the created engine in the form flag=value
   --engine-registry-mirror [--engine-registry-mirror option --engine-registry-mirror option]		Specify registry mirrors to use [$ENGINE_REGISTRY_MIRROR]
   --engine-storage-driver 										Specify a storage driver to use with the engine
   --swarm												Configure Machine to join a Swarm cluster
   --swarm-addr 											addr to advertise for Swarm (default: detect and use the machine IP)
   --swarm-discovery 											Discovery service to use with Swarm
   --swarm-experimental											Enable Swarm experimental features
   --swarm-host "tcp://0.0.0.0:3376"									ip/socket to listen on for Swarm master
   --swarm-image "swarm:latest"										Specify Docker image to use for Swarm [$MACHINE_SWARM_IMAGE]
   --swarm-join-opt [--swarm-join-opt option --swarm-join-opt option]					Define arbitrary flags for Swarm join
   --swarm-master											Configure Machine to be a Swarm master
   --swarm-opt [--swarm-opt option --swarm-opt option]							Define arbitrary flags for Swarm master
   --swarm-strategy "spread"										Define a default scheduling strategy for Swarm
   --tls-san [--tls-san option --tls-san option]							Support extra SANs for TLS certs

    """
    pass