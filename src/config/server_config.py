{"_id":"1c783df8-9e85-4805-b322-2dc2753d00f4_Dmgr01_ffdf7c4c-22c1-40da-b51a-7016b27ed81b_DB2App-1_war_py","_rev":"1-86ec12ea77f4da1399759d08346fcf6b","py":"# wsadmin script generated by binaryAppScanner

Cell=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/')
Node=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/')
Server=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/Node:' + AdminControl.getNode() + '/Server:server1')
NodeName=AdminControl.getNode()

# The following variables are used to replace sensitive data in the configuration for the application.
# The values for these variables were not collected because the includeSensitiveData option was not specified.
# ============================================================
wasinstall_a1CellManager01_db2_password_1=''
# ============================================================

print 'Starting Creating JVM Properties'

print 'Starting Creating Authentication Alias'
GlobalSecurityVar=AdminConfig.getid('/Cell:' + AdminControl.getCell() + '/' + 'Security:/')
AdminConfig.create('JAASAuthData', GlobalSecurityVar, [['userId', 'db2inst1'], ['description', ''], ['password', wasinstall_a1CellManager01_db2_password_1], ['alias', 'wasinstall-a1CellManager01/db2']])

print 'Starting Creating Queues'

print 'Starting Creating Topics'

print 'Starting Creating Activation Specifications'

print 'Starting Creating Connection Factories'

print 'Starting Creating JDBC Providers'
AdminConfigVar_0=AdminConfig.create('JDBCProvider', Node, [['name', 'DB2_Universal_JDBC_Driver_Provider'], ['implementationClassName', 'com.ibm.db2.jcc.DB2ConnectionPoolDataSource'], ['providerType', 'DB2 Universal JDBC Driver Provider'], ['description', 'One-phase commit DB2 JCC provider that supports JDBC 3.0. Data sources that use this provider support only 1-phase commit processing, unless you use driver type 2 with the application server for z/OS. If you use the application server for z/OS, driver type 2 uses RRS and supports 2-phase commit processing.'], ['classpath', '/root/db2jcc4.jar'], ['xa', 'false']])
AdminConfigVar_1=AdminTask.createDatasource(AdminConfigVar_0, ["-name", "db2Test", "-jndiName", "jndi/db2", "-dataStoreHelperClassName", "com.ibm.websphere.rsadapter.DB2UniversalDataStoreHelper", "-componentManagedAuthenticationAlias", "wasinstall-a1CellManager01/db2", "-configureResourceProperties", "[[databaseName java.lang.String testdb] [driverType java.lang.Integer 4] [serverName java.lang.String 9.21.109.27] [portNumber java.lang.Integer 50000] ]"])
AdminConfigVar_2=AdminConfig.showAttribute(AdminConfigVar_1, 'propertySet')
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'jmsOnePhaseOptimization'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'preTestSQLString'], ['type', 'java.lang.String'], ['value', 'SELECT CURRENT SQLID FROM SYSIBM.SYSDUMMY1']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnectionRetryInterval'], ['type', 'java.lang.Long'], ['value', '3']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'errorDetectionModel'], ['type', 'java.lang.String'], ['value', 'ExceptionMapping']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'nonTransactionalDataSource'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'retrieveMessagesFromServerOnGetMessage'], ['type', 'java.lang.Boolean'], ['value', 'true']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'propagateClientIdentityUsingTrustedContext'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'fullyMaterializeLobData'], ['type', 'java.lang.Boolean'], ['value', 'true']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'beginTranForVendorAPIs'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'unbindClientRerouteListFromJndi'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'readOnly'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'resultSetHoldability'], ['type', 'java.lang.Integer'], ['value', '2']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'deferPrepares'], ['type', 'java.lang.Boolean'], ['value', 'true']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'name'], ['type', 'java.lang.String'], ['value', 'db2Test']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'beginTranForResultSetScrollingAPIs'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'reauthentication'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'useTransactionRedirect'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnection'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'loginTimeout'], ['type', 'java.lang.Integer'], ['value', '0']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'traceFileAppend'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'enableMultithreadedAccessDetection'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'connectionSharing'], ['type', 'java.lang.Integer'], ['value', '1']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'traceLevel'], ['type', 'java.lang.Integer'], ['value', '-1']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'enableClientInformation'], ['type', 'java.lang.Boolean'], ['value', 'false']])
AdminConfig.create('J2EEResourceProperty', AdminConfigVar_2, [['name', 'validateNewConnectionRetryCount'], ['type', 'java.lang.Integer'], ['value', '100']])
AdminConfigVar_3=AdminConfig.showAttribute(AdminConfigVar_1, 'connectionPool')
AdminConfig.modify(AdminConfigVar_3, [['stuckThreshold', '0'], ['reapTime', '180'], ['testConnectionInterval', '0'], ['connectionTimeout', '180'], ['surgeCreationInterval', '0'], ['surgeThreshold', '-1'], ['stuckTimerTime', '0'], ['numberOfFreePoolPartitions', '0'], ['minConnections', '0'], ['unusedTimeout', '1800'], ['agedTimeout', '0'], ['numberOfSharedPoolPartitions', '0'], ['purgePolicy', 'EntirePool'], ['maxConnections', '10'], ['freePoolDistributionTableSize', '0'], ['stuckTime', '0'], ['testConnection', 'false'], ['numberOfUnsharedPoolPartitions', '0']])

print 'Starting Creating Variables'

AdminConfig.save()
","name":"DB2App-1_war.ear_server","type":"py","tenantId":"ffdf7c4c-22c1-40da-b51a-7016b27ed81b","taskname":"1c783df8-9e85-4805-b322-2dc2753d00f4","created":1583957299896,"profileName":"Dmgr01","applicationName":"DB2App-1_war","appSpecificConfigXml":"false","id":"1c783df8-9e85-4805-b322-2dc2753d00f4_Dmgr01_ffdf7c4c-22c1-40da-b51a-7016b27ed81b_DB2App-1_war_py"}