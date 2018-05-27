from machine.config.abstract import AbstractMachineConfig


class VMWareVCloudMachineConfig(AbstractMachineConfig):
    """
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
   --vmwarevcloudair-catalog "Public Catalog"								vCloud Air Catalog (default is Public Catalog) [$VCLOUDAIR_CATALOG]
   --vmwarevcloudair-catalogitem "Ubuntu Server 12.04 LTS (amd64 20150127)"				vCloud Air Catalog Item (default is Ubuntu Precise) [$VCLOUDAIR_CATALOGITEM]
   --vmwarevcloudair-computeid 										vCloud Air Compute ID (if using Dedicated Cloud) [$VCLOUDAIR_COMPUTEID]
   --vmwarevcloudair-cpu-count "1"									vCloud Air VM Cpu Count (default 1) [$VCLOUDAIR_CPU_COUNT]
   --vmwarevcloudair-docker-port "2376"									vCloud Air Docker port [$VCLOUDAIR_DOCKER_PORT]
   --vmwarevcloudair-edgegateway 									vCloud Air Org Edge Gateway (Default is <vdcid>) [$VCLOUDAIR_EDGEGATEWAY]
   --vmwarevcloudair-memory-size "2048"									vCloud Air VM Memory Size in MB (default 2048) [$VCLOUDAIR_MEMORY_SIZE]
   --vmwarevcloudair-orgvdcnetwork 									vCloud Air Org VDC Network (Default is <vdcid>-default-routed) [$VCLOUDAIR_ORGVDCNETWORK]
   --vmwarevcloudair-password 										vCloud Air password [$VCLOUDAIR_PASSWORD]
   --vmwarevcloudair-publicip 										vCloud Air Org Public IP to use [$VCLOUDAIR_PUBLICIP]
   --vmwarevcloudair-ssh-port "22"									vCloud Air SSH port [$VCLOUDAIR_SSH_PORT]
   --vmwarevcloudair-username 										vCloud Air username [$VCLOUDAIR_USERNAME]
   --vmwarevcloudair-vdcid 										vCloud Air VDC ID [$VCLOUDAIR_VDCID]

    """
    pass