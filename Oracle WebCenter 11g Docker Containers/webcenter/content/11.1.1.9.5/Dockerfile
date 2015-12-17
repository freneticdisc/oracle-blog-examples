FROM webcenter/content:11.1.1.9.0
MAINTAINER Justin Paul <justin.paul@oracle.com>

ENV _SCRATCH /tmp/scratch
ENV ORA_HOME /u01/app/oracle
ENV JDK_HOME ${ORA_HOME}/product/jdk
ENV FMW_HOME ${ORA_HOME}/product/fmw

COPY wls ${_SCRATCH}/wls/
COPY wcc ${_SCRATCH}/wcc/

USER root

RUN yum update -y -q && \
	chown -R oracle:oinstall ${_SCRATCH}

USER oracle

RUN mkdir -p ${FMW_HOME}/utils/bsu/cache_dir && \
	unzip ${_SCRATCH}/wls/p20780171_1036_Generic.zip -d ${FMW_HOME}/utils/bsu/cache_dir && \
	cd ${FMW_HOME}/utils/bsu && \
	sed -i 's/-Xmx512m/-Xmx1024m/g' ${FMW_HOME}/utils/bsu/bsu.sh && \
	${FMW_HOME}/utils/bsu/bsu.sh -prod_dir=${FMW_HOME}/wlserver_10.3 -patchlist=EJUW -verbose -install && \
	cd

RUN ${FMW_HOME}/Oracle_ECM1/OPatch/opatch apply -silent ${_SCRATCH}/wcc/22060967 && \
	${FMW_HOME}/Oracle_ECM1/OPatch/opatch apply -silent ${_SCRATCH}/wcc/ECM_22249978 && \
	rm -rf ${_SCRATCH}

CMD /bin/bash
