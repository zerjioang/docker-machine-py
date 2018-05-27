from machine.config.abstract import AbstractMachineConfig


class HyperVMachineConfig(AbstractMachineConfig):
    """
   --driver, -d "virtualbox"										Driver to create machine with. [$MACHINE_DRIVER]
   --engine-env [--engine-env option --engine-env option]						Specify environment variables to set in the engine
   --engine-insecure-registry [--engine-insecure-registry option --engine-insecure-registry option]	Specify insecure registries to allow with the created engine
   --engine-install-url "https://get.docker.com"							Custom URL to use for engine installation [$MACHINE_DOCKER_INSTALL_URL]
   --engine-label [--engine-label option --engine-label option]						Specify labels for the created engine
   --engine-opt [--engine-opt option --engine-opt option]						Specify arbitrary flags to include with the created engine in the form flag=value
   --engine-registry-mirror [--engine-registry-mirror option --engine-registry-mirror option]		Specify registry mirrors to use [$ENGINE_REGISTRY_MIRROR]
   --engine-storage-driver 										Specify a storage driver to use with the engine
   --hyperv-boot2docker-url 										URL of the boot2docker ISO. Defaults to the latest available version. [$HYPERV_BOOT2DOCKER_URL]
   --hyperv-cpu-count "1"										number of CPUs for the machine [$HYPERV_CPU_COUNT]
   --hyperv-disk-size "20000"										Maximum size of dynamically expanding disk in MB. [$HYPERV_DISK_SIZE]
   --hyperv-memory "1024"										Memory size for host in MB. [$HYPERV_MEMORY]
   --hyperv-static-macaddress 										Hyper-V network adapter's static MAC address. [$HYPERV_STATIC_MACADDRESS]
   --hyperv-virtual-switch 										Virtual switch name. Defaults to first found. [$HYPERV_VIRTUAL_SWITCH]
   --hyperv-vlan-id "0"											Hyper-V network adapter's VLAN ID if any [$HYPERV_VLAN_ID]
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