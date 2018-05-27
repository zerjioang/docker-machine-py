from machine.config.abstract import AbstractMachineConfig


class OpenstackMachineConfig(AbstractMachineConfig):
    """
    --driver, -d "virtualbox"										Driver to create machine with. [$MACHINE_DRIVER]
    --engine-env [--engine-env option --engine-env option]						Specify environment variables to set in the engine
    --engine-insecure-registry [--engine-insecure-registry option --engine-insecure-registry option]	Specify insecure registries to allow with the created engine
    --engine-install-url "https://get.docker.com"							Custom URL to use for engine installation [$MACHINE_DOCKER_INSTALL_URL]
    --engine-label [--engine-label option --engine-label option]						Specify labels for the created engine
    --engine-opt [--engine-opt option --engine-opt option]						Specify arbitrary flags to include with the created engine in the form flag=value
    --engine-registry-mirror [--engine-registry-mirror option --engine-registry-mirror option]		Specify registry mirrors to use [$ENGINE_REGISTRY_MIRROR]
    --engine-storage-driver 										Specify a storage driver to use with the engine
    --openstack-active-timeout "200"									OpenStack active timeout [$OS_ACTIVE_TIMEOUT]
    --openstack-auth-url 										OpenStack authentication URL [$OS_AUTH_URL]
    --openstack-availability-zone 									OpenStack availability zone [$OS_AVAILABILITY_ZONE]
    --openstack-cacert 											CA certificate bundle to verify against [$OS_CACERT]
    --openstack-config-drive										Enables the OpenStack config drive for the instance [$OS_CONFIG_DRIVE]
    --openstack-domain-id 										OpenStack domain ID (identity v3 only) [$OS_DOMAIN_ID]
    --openstack-domain-name 										OpenStack domain name (identity v3 only) [$OS_DOMAIN_NAME]
    --openstack-endpoint-type 										OpenStack endpoint type (adminURL, internalURL or publicURL) [$OS_ENDPOINT_TYPE]
    --openstack-flavor-id 										OpenStack flavor id to use for the instance [$OS_FLAVOR_ID]
    --openstack-flavor-name 										OpenStack flavor name to use for the instance [$OS_FLAVOR_NAME]
    --openstack-floatingip-pool 										OpenStack floating IP pool to get an IP from to assign to the instance [$OS_FLOATINGIP_POOL]
    --openstack-image-id 										OpenStack image id to use for the instance [$OS_IMAGE_ID]
    --openstack-image-name 										OpenStack image name to use for the instance [$OS_IMAGE_NAME]
    --openstack-insecure											Disable TLS credential checking. [$OS_INSECURE]
    --openstack-ip-version "4"										OpenStack version of IP address assigned for the machine [$OS_IP_VERSION]
    --openstack-keypair-name 										OpenStack keypair to use to SSH to the instance [$OS_KEYPAIR_NAME]
    --openstack-net-id 											OpenStack network id the machine will be connected on [$OS_NETWORK_ID]
    --openstack-net-name 										OpenStack network name the machine will be connected on [$OS_NETWORK_NAME]
    --openstack-nova-network										Use the nova networking services instead of neutron. [$OS_NOVA_NETWORK]
    --openstack-password 										OpenStack password [$OS_PASSWORD]
    --openstack-private-key-file 									Private keyfile to use for SSH (absolute path) [$OS_PRIVATE_KEY_FILE]
    --openstack-region 											OpenStack region name [$OS_REGION_NAME]
    --openstack-sec-groups 										OpenStack comma separated security groups for the machine [$OS_SECURITY_GROUPS]
    --openstack-ssh-port "22"										OpenStack SSH port [$OS_SSH_PORT]
    --openstack-ssh-user "root"										OpenStack SSH user [$OS_SSH_USER]
    --openstack-tenant-id 										OpenStack tenant id [$OS_TENANT_ID]
    --openstack-tenant-name 										OpenStack tenant name [$OS_TENANT_NAME]
    --openstack-user-data-file 										File containing an openstack userdata script [$OS_USER_DATA_FILE]
    --openstack-username 										OpenStack username [$OS_USERNAME]
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