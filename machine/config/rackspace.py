from machine.config.abstract import AbstractMachineConfig


class RackspaceMachineConfig(AbstractMachineConfig):
    """
   --driver, -d "virtualbox"										Driver to create machine with. [$MACHINE_DRIVER]
   --engine-env [--engine-env option --engine-env option]						Specify environment variables to set in the engine
   --engine-insecure-registry [--engine-insecure-registry option --engine-insecure-registry option]	Specify insecure registries to allow with the created engine
   --engine-install-url "https://get.docker.com"							Custom URL to use for engine installation [$MACHINE_DOCKER_INSTALL_URL]
   --engine-label [--engine-label option --engine-label option]						Specify labels for the created engine
   --engine-opt [--engine-opt option --engine-opt option]						Specify arbitrary flags to include with the created engine in the form flag=value
   --engine-registry-mirror [--engine-registry-mirror option --engine-registry-mirror option]		Specify registry mirrors to use [$ENGINE_REGISTRY_MIRROR]
   --engine-storage-driver 										Specify a storage driver to use with the engine
   --rackspace-active-timeout "300"									Rackspace active timeout [$OS_ACTIVE_TIMEOUT]
   --rackspace-api-key 											Rackspace API key [$OS_API_KEY]
   --rackspace-docker-install "true"									Set if docker have to be installed on the machine
   --rackspace-endpoint-type "publicURL"								Rackspace endpoint type (adminURL, internalURL or the default publicURL) [$OS_ENDPOINT_TYPE]
   --rackspace-flavor-id "general1-1"									Rackspace flavor ID. Default: General Purpose 1GB [$OS_FLAVOR_ID]
   --rackspace-image-id 										Rackspace image ID. Default: Ubuntu 16.04 LTS (Xenial Xerus) (PVHVM) [$OS_IMAGE_ID]
   --rackspace-region "IAD"										Rackspace region name [$OS_REGION_NAME]
   --rackspace-ssh-port "22"										SSH port for the newly booted machine. Set to 22 by default [$OS_SSH_PORT]
   --rackspace-ssh-user "root"										SSH user for the newly booted machine. Set to root by default [$OS_SSH_USER]
   --rackspace-username 										Rackspace account username [$OS_USERNAME]
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