#We use this in pyspark to read or write dataframe to sql database table
jdbcUsername = "sqladmin@lksqldev1"
jdbcPassword = "Azure$2022"
jdbcHostname = "lksqldev1.database.windows.net"
jdbcDatabase = "lksqldev"
jdbcPort = 1433
jdbcUrl = "jdbc:sqlserver://{0}:{1};database={2};user={3};password={4}".format(jdbcHostname, jdbcPort, jdbcDatabase, jdbcUsername, jdbcPassword)

connectionProperties = {
  "user" : jdbcUsername,
  "password" : jdbcPassword,
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}
