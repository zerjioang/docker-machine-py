from machine.config.abstract import AbstractMachineConfig


class VSphereMachineConfig(AbstractMachineConfig):
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
   --vmwarevsphere-boot2docker-url 									vSphere URL for boot2docker image [$VSPHERE_BOOT2DOCKER_URL]
   --vmwarevsphere-cfgparam [--vmwarevsphere-cfgparam option --vmwarevsphere-cfgparam option]		vSphere vm configuration parameters (used for guestinfo) [$VSPHERE_CFGPARAM]
   --vmwarevsphere-cloudinit 										vSphere cloud-init file or url to set in the guestinfo [$VSPHERE_CLOUDINIT]
   --vmwarevsphere-cpu-count "2"									vSphere CPU number for docker VM [$VSPHERE_CPU_COUNT]
   --vmwarevsphere-datacenter 										vSphere datacenter for docker VM [$VSPHERE_DATACENTER]
   --vmwarevsphere-datastore 										vSphere datastore for docker VM [$VSPHERE_DATASTORE]
   --vmwarevsphere-disk-size "20480"									vSphere size of disk for docker VM (in MB) [$VSPHERE_DISK_SIZE]
   --vmwarevsphere-folder 										vSphere folder for the docker VM. This folder must already exist in the datacenter. [$VSPHERE_FOLDER]
   --vmwarevsphere-hostsystem 										vSphere compute resource where the docker VM will be instantiated. This can be omitted if using a cluster with DRS. [$VSPHERE_HOSTSYSTEM]
   --vmwarevsphere-memory-size "2048"									vSphere size of memory for docker VM (in MB) [$VSPHERE_MEMORY_SIZE]
   --vmwarevsphere-network [--vmwarevsphere-network option --vmwarevsphere-network option]		vSphere network where the docker VM will be attached [$VSPHERE_NETWORK]
   --vmwarevsphere-password 										vSphere password [$VSPHERE_PASSWORD]
   --vmwarevsphere-pool 										vSphere resource pool for docker VM [$VSPHERE_POOL]
   --vmwarevsphere-username 										vSphere username [$VSPHERE_USERNAME]
   --vmwarevsphere-vcenter 										vSphere IP/hostname for vCenter [$VSPHERE_VCENTER]
   --vmwarevsphere-vcenter-port "443"									vSphere Port for vCenter [$VSPHERE_VCENTER_PORT]
    """
    pass