print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)

servermap = {
				"capture": {"Port": 16400, "Cluster": "wcc_capture_cluster1"},
				"ibr": {"Port": 16250, "Cluster": "wcc_ibr_cluster1"},
				"ipm": {"Port": 16000, "Cluster": "wcc_ipm_cluster1"},
				"irm": {"Port": 16100, "Cluster": "wcc_irm_cluster1"},
				"ssxa": {"Port": 16290, "Cluster": "wcc_ssxa_cluster1"},
				"ucm": {"Port": 16200, "Cluster": "wcc_ucm_cluster1"},
				"urm": {"Port": 16300, "Cluster": "wcc_urm_cluster1"},
				"collaboration": {"Port": 8890, "Cluster": "wcp_collaboration_cluster1"},
				"portlet": {"Port": 8889, "Cluster": "wcp_portlet_cluster1"},
				"spaces": {"Port": 8888, "Cluster": "wcp_spaces_cluster1"},
				"utilities": {"Port": 8891, "Cluster": "wcp_utilities_cluster1"}
			}

connect(sys.argv[1], sys.argv[2], sys.argv[5])
edit()
startEdit()
servername = sys.argv[4]
clustername = servermap.get(sys.argv[3], {}).get("Cluster", None)
port = servermap.get(sys.argv[3], {}).get("Port", 7001)

try:
	if clustername not in (None, ""):
		cd('/Clusters/' + clustername)
		cluster = cmo
	
	cd("/")
	cmo.createServer(servername)
	cd('/Servers/' + servername)
	cmo.setListenAddress("")
	cmo.setListenPort(port)
	
	if clustername not in (None, ""):
		cmo.setCluster(cluster)
	
	activate()
except:
	cancelEdit("y")

disconnect()
exit()
