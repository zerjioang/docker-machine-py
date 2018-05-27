from machine.config.abstract import AbstractMachineConfig


class VirtualboxMachineConfig(AbstractMachineConfig):
    """
   --driver, -d "virtualbox"										Driver to create machine with. [$MACHINE_DRIVER]
   --engine-env [--engine-env option --engine-env option]						Specify environment variables to set in the engine
   --engine-insecure-registry [--engine-insecure-registry option --engine-insecure-registry option]	Specify insecure registries to allow with the created engine
   --engine-install-url "https://get.docker.com"							Custom URL to use for engine installation [$MACHINE_DOCKER_INSTALL_URL]
   --engine-label [--engine-label option --engine-label option]						Specify labels for the created engine
   --engine-opt [--engine-opt option --engine-opt option]						Specify arbitrary flags to include with the created engine in the form flag=value
   --engine-registry-mirror [--engine-registry-mirror option --engine-registry-mirror option]		Specify registry mirrors to use [$ENGINE_REGISTRY_MIRROR]
   --engine-storage-driver 										Specify a storage driver to use with the engine
   --softlayer-api-endpoint "https://api.softlayer.com/rest/v3"						softlayer api endpoint to use [$SOFTLAYER_API_ENDPOINT]
   --softlayer-api-key 											softlayer user API key [$SOFTLAYER_API_KEY]
   --softlayer-cpu "1"											number of CPU's for the machine [$SOFTLAYER_CPU]
   --softlayer-disk-size "0"										Disk size for machine, a value of 0 uses the default size on softlayer [$SOFTLAYER_DISK_SIZE]
   --softlayer-domain 											domain name for machine [$SOFTLAYER_DOMAIN]
   --softlayer-hostname 										hostname for the machine - defaults to machine name [$SOFTLAYER_HOSTNAME]
   --softlayer-hourly-billing										set hourly billing for machine - on by default [$SOFTLAYER_HOURLY_BILLING]
   --softlayer-image "UBUNTU_LATEST"									OS image for machine [$SOFTLAYER_IMAGE]
   --softlayer-local-disk										use machine local disk instead of softlayer SAN [$SOFTLAYER_LOCAL_DISK]
   --softlayer-memory "1024"										Memory in MB for machine [$SOFTLAYER_MEMORY]
   --softlayer-network-max-speed "100"									Max speed of public and private network [$SOFTLAYER_NETWORK_MAX_SPEED]
   --softlayer-private-net-only										Use only private networking [$SOFTLAYER_PRIVATE_NET]
   --softlayer-private-vlan-id "0"									 [$SOFTLAYER_PRIVATE_VLAN_ID]
   --softlayer-public-vlan-id "0"									 [$SOFTLAYER_PUBLIC_VLAN_ID]
   --softlayer-region "dal01"										softlayer region for machine [$SOFTLAYER_REGION]
   --softlayer-user 											softlayer user account name [$SOFTLAYER_USER]
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