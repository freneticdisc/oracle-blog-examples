#!/bin/sh

SERVER_ID=${1}
ADMIN_URL=${2}
ADMIN_USERNAME=weblogic
ADMIN_PASSWORD=welcome1
SERVER_NAME=${SERVER_ID}-$(hostname -s)

export DOMAIN_NAME=docker_domain

case "${SERVER_ID}" in
	adminserver)
		if [ -d ${ADM_HOME}/aserver/${DOMAIN_NAME} ]
		then
				echo "Admin Domain Directory Exists."
		else
				echo "Admin Domain Directory does NOT exist. Unpacking the domain from the available template..."
				${FMW_HOME}/oracle_common/common/bin/unpack.sh \
				-template=${ADM_HOME}/tools/templates/${DOMAIN_NAME}_admin.jar \
				-domain=${ADM_HOME}/aserver/${DOMAIN_NAME} \
				-app_dir=${ADM_HOME}/aserver/${DOMAIN_NAME}
		fi
		echo "Starting the Admin Server."
		${ADM_HOME}/aserver/${DOMAIN_NAME}/startWebLogic.sh
		;;
	*)
		if [ -d ${ADM_HOME}/mserver/${DOMAIN_NAME} ]
		then
				echo "Managed Domain Directory Exists."
				echo "Starting the Managed Server."
				${ADM_HOME}/mserver/${DOMAIN_NAME}/bin/startManagedWebLogic.sh ${SERVER_NAME} ${ADMIN_URL}
		else
				echo "Managed Domain Directory does NOT exist."
				echo "Creating a managed server domain template from the admin server."
				if [ -d ${ADM_HOME}/aserver/${DOMAIN_NAME} ]
				then
					${FMW_HOME}/oracle_common/common/bin/pack.sh \
					-template=${ADM_HOME}/tools/templates/${DOMAIN_NAME}_managed.jar \
					-domain=${ADM_HOME}/aserver/${DOMAIN_NAME} \
					-template_name="${DOMAIN_NAME} Domain for Managed Servers" \
					-template_author="Justin Paul" -managed=true
				
					echo "Unpacking the domain from the available template."
					${FMW_HOME}/oracle_common/common/bin/unpack.sh \
					-template=${ADM_HOME}/tools/templates/${DOMAIN_NAME}_managed.jar \
					-domain=${ADM_HOME}/mserver/${DOMAIN_NAME} \
					-app_dir=${ADM_HOME}/mserver/${DOMAIN_NAME}
					
					${FMW_HOME}/oracle_common/common/bin/wlst.sh \
					${ADM_HOME}/tools/scripts/add_server.py ${ADMIN_USERNAME} ${ADMIN_PASSWORD} ${SERVER_ID} ${SERVER_NAME} ${ADMIN_URL}
					mkdir -p ${ADM_HOME}/mserver/${DOMAIN_NAME}/servers/${SERVER_NAME}/security
					echo "username=${ADMIN_USERNAME}" > ${ADM_HOME}/mserver/${DOMAIN_NAME}/servers/${SERVER_NAME}/security/boot.properties
					echo "password=${ADMIN_PASSWORD}" >> ${ADM_HOME}/mserver/${DOMAIN_NAME}/servers/${SERVER_NAME}/security/boot.properties
					
					echo "Starting the Managed Server."
					${ADM_HOME}/mserver/${DOMAIN_NAME}/bin/startManagedWebLogic.sh ${SERVER_NAME} ${ADMIN_URL}
				else
					echo "ERROR: Admin Server Directory and ${DOMAIN_NAME} domain was not found."
					echo "This procedure cannot continue."
				fi
		fi
		;;
esac
