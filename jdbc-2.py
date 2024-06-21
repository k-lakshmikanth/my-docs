# Variables
tenant_id = "<tenant-id>"
service_principal_id = "<client-id>"
service_principal_secret = "<client-secret>"
url = "jdbc:sqlserver://<sql-server-name>.database.windows.net"
database_name = "<sql-database-name>"
db_table = "<table-name-with-schema>" 

# get access token by spn(Service principal)
import adal
authority = "https://login.windows.net/" + tenant_id
resource_app_id_url = "https://database.windows.net/"
encrypt = "true"
host_name_in_certificate = "*.database.windows.net"
context = adal.AuthenticationContext(authority)
token = context.acquire_token_with_client_credentials(resource_app_id_url, service_principal_id, service_principal_secret)
access_token = token["accessToken"]

# read data from sql database
df = spark.read.format("jdbc") \
              .option("url", url) \
              .option("dbtable", db_table) \
              .option("accessToken", access_token) \
              .option("encrypt", encrypt) \
              .option("databaseName", database_name) \
              .option("hostNameInCertificate", host_name_in_certificate) \
              .option("driver", "com.microsoft.sqlserver.jdbc.SQLServerDriver") \
              .load()

# Display the DataFrame
df.display()
