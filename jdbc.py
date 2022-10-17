#We use this in pyspark to read or write dataframe to sql database table
jdbcUsername = "<Username>"
jdbcPassword = "<Password>"
jdbcHostname = "<server_name>.database.windows.net"
jdbcDatabase = "<Database_name>"
jdbcPort = 1433
jdbcUrl = "jdbc:sqlserver://{0}:{1};database={2};user={3};password={4}".format(jdbcHostname, jdbcPort, jdbcDatabase, jdbcUsername, jdbcPassword)

connectionProperties = {
  "user" : jdbcUsername,
  "password" : jdbcPassword,
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}


# Read table from Database(jdbc) to df
df = spark.read.jdbc(url=jdbcUrl, table="<Table_name or SQL_Query>", properties=connectionProperties)

#Write df to table in Database(jdbc)
df.write.jdbc(url=jdbcUrl, table="<Tablename with schema or default(dbo.)>", mode="overwrite", properties=connectionProperties)
