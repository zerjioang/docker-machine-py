from machine.config.abstract import AbstractMachineConfig


class GoogleMachineConfig(AbstractMachineConfig):
    """
   --driver, -d "virtualbox"																			Driver to create machine with. [$MACHINE_DRIVER]
   --engine-env [--engine-env option --engine-env option]															Specify environment variables to set in the engine
   --engine-insecure-registry [--engine-insecure-registry option --engine-insecure-registry option]										Specify insecure registries to allow with the created engine
   --engine-install-url "https://get.docker.com"																Custom URL to use for engine installation [$MACHINE_DOCKER_INSTALL_URL]
   --engine-label [--engine-label option --engine-label option]															Specify labels for the created engine
   --engine-opt [--engine-opt option --engine-opt option]															Specify arbitrary flags to include with the created engine in the form flag=value
   --engine-registry-mirror [--engine-registry-mirror option --engine-registry-mirror option]											Specify registry mirrors to use [$ENGINE_REGISTRY_MIRROR]
   --engine-storage-driver 																			Specify a storage driver to use with the engine
   --google-address 																				GCE Instance External IP [$GOOGLE_ADDRESS]
   --google-disk-size "10"																			GCE Instance Disk Size (in GB) [$GOOGLE_DISK_SIZE]
   --google-disk-type "pd-standard"																		GCE Instance Disk type [$GOOGLE_DISK_TYPE]
   --google-machine-image "ubuntu-os-cloud/global/images/ubuntu-1604-xenial-v20170721"												GCE Machine Image Absolute URL [$GOOGLE_MACHINE_IMAGE]
   --google-machine-type "n1-standard-1"																	GCE Machine Type [$GOOGLE_MACHINE_TYPE]
   --google-network "default"																			Specify network in which to provision vm [$GOOGLE_NETWORK]
   --google-open-port [--google-open-port option --google-open-port option]													Make the specified port number accessible from the Internet, e.g, 8080/tcp
   --google-preemptible																				GCE Instance Preemptibility [$GOOGLE_PREEMPTIBLE]
   --google-project 																				GCE Project [$GOOGLE_PROJECT]
   --google-scopes "https://www.googleapis.com/auth/devstorage.read_only,https://www.googleapis.com/auth/logging.write,https://www.googleapis.com/auth/monitoring.write"	GCE Scopes (comma-separated if multiple scopes) [$GOOGLE_SCOPES]
   --google-subnetwork 																				Specify subnetwork in which to provision vm [$GOOGLE_SUBNETWORK]
   --google-tags 																				GCE Instance Tags (comma-separated) [$GOOGLE_TAGS]
   --google-use-existing																			Don't create a new VM, use an existing one [$GOOGLE_USE_EXISTING]
   --google-use-internal-ip																			Use internal GCE Instance IP rather than public one [$GOOGLE_USE_INTERNAL_IP]
   --google-use-internal-ip-only																		Configure GCE instance to not have an external IP address [$GOOGLE_USE_INTERNAL_IP_ONLY]
   --google-username "docker-user"																		GCE User Name [$GOOGLE_USERNAME]
   --google-zone "us-central1-a"																		GCE Zone [$GOOGLE_ZONE]
   --swarm																					Configure Machine to join a Swarm cluster
   --swarm-addr 																				addr to advertise for Swarm (default: detect and use the machine IP)
   --swarm-discovery 																				Discovery service to use with Swarm
   --swarm-experimental																				Enable Swarm experimental features
   --swarm-host "tcp://0.0.0.0:3376"																		ip/socket to listen on for Swarm master
   --swarm-image "swarm:latest"																			Specify Docker image to use for Swarm [$MACHINE_SWARM_IMAGE]
   --swarm-join-opt [--swarm-join-opt option --swarm-join-opt option]														Define arbitrary flags for Swarm join
   --swarm-master																				Configure Machine to be a Swarm master
   --swarm-opt [--swarm-opt option --swarm-opt option]																Define arbitrary flags for Swarm master
   --swarm-strategy "spread"																			Define a default scheduling strategy for Swarm
   --tls-san [--tls-san option --tls-san option]																Support extra SANs for TLS certs
    """
    pass