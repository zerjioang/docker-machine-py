from machine.config.abstract import AbstractMachineConfig


class DigitalOceanMachineConfig(AbstractMachineConfig):
    """
   --digitalocean-access-token 										Digital Ocean access token [$DIGITALOCEAN_ACCESS_TOKEN]
   --digitalocean-backups										enable backups for droplet [$DIGITALOCEAN_BACKUPS]
   --digitalocean-image "ubuntu-16-04-x64"								Digital Ocean Image [$DIGITALOCEAN_IMAGE]
   --digitalocean-ipv6											enable ipv6 for droplet [$DIGITALOCEAN_IPV6]
   --digitalocean-monitoring										enable monitoring for droplet [$DIGITALOCEAN_MONITORING]
   --digitalocean-private-networking									enable private networking for droplet [$DIGITALOCEAN_PRIVATE_NETWORKING]
   --digitalocean-region "nyc3"										Digital Ocean region [$DIGITALOCEAN_REGION]
   --digitalocean-size "s-1vcpu-1gb"									Digital Ocean size [$DIGITALOCEAN_SIZE]
   --digitalocean-ssh-key-fingerprint 									SSH key fingerprint [$DIGITALOCEAN_SSH_KEY_FINGERPRINT]
   --digitalocean-ssh-key-path 										SSH private key path  [$DIGITALOCEAN_SSH_KEY_PATH]
   --digitalocean-ssh-port "22"										SSH port [$DIGITALOCEAN_SSH_PORT]
   --digitalocean-ssh-user "root"									SSH username [$DIGITALOCEAN_SSH_USER]
   --digitalocean-tags 											comma-separated list of tags to apply to the Droplet [$DIGITALOCEAN_TAGS]
   --digitalocean-userdata 										path to file with cloud-init user-data [$DIGITALOCEAN_USERDATA]
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