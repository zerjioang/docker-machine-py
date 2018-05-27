from machine.config.abstract import AbstractMachineConfig


class ExoscaleMachineConfig(AbstractMachineConfig):
    """
   --driver, -d "virtualbox"										Driver to create machine with. [$MACHINE_DRIVER]
   --engine-env [--engine-env option --engine-env option]						Specify environment variables to set in the engine
   --engine-insecure-registry [--engine-insecure-registry option --engine-insecure-registry option]	Specify insecure registries to allow with the created engine
   --engine-install-url "https://get.docker.com"							Custom URL to use for engine installation [$MACHINE_DOCKER_INSTALL_URL]
   --engine-label [--engine-label option --engine-label option]						Specify labels for the created engine
   --engine-opt [--engine-opt option --engine-opt option]						Specify arbitrary flags to include with the created engine in the form flag=value
   --engine-registry-mirror [--engine-registry-mirror option --engine-registry-mirror option]		Specify registry mirrors to use [$ENGINE_REGISTRY_MIRROR]
   --engine-storage-driver 										Specify a storage driver to use with the engine
   --exoscale-affinity-group [--exoscale-affinity-group option --exoscale-affinity-group option]	exoscale affinity group [$EXOSCALE_AFFINITY_GROUP]
   --exoscale-api-key 											exoscale API key [$EXOSCALE_API_KEY]
   --exoscale-api-secret-key 										exoscale API secret key [$EXOSCALE_API_SECRET]
   --exoscale-availability-zone "CH-DK-2"								exoscale availability zone [$EXOSCALE_AVAILABILITY_ZONE]
   --exoscale-disk-size "50"										exoscale disk size (10, 50, 100, 200, 400) [$EXOSCALE_DISK_SIZE]
   --exoscale-image "Linux Ubuntu 16.04 LTS 64-bit"							exoscale image template [$EXOSCALE_IMAGE]
   --exoscale-instance-profile "Small"									exoscale instance profile (Small, Medium, Large, ...) [$EXOSCALE_INSTANCE_PROFILE]
   --exoscale-security-group [--exoscale-security-group option --exoscale-security-group option]	exoscale security group [$EXOSCALE_SECURITY_GROUP]
   --exoscale-ssh-key 											path to the SSH user private key [$EXOSCALE_SSH_KEY]
   --exoscale-ssh-user 											name of the ssh user [$EXOSCALE_SSH_USER]
   --exoscale-url 											exoscale API endpoint [$EXOSCALE_ENDPOINT]
   --exoscale-userdata 											path to file with cloud-init user-data [$EXOSCALE_USERDATA]
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