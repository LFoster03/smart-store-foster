# Define the path to the JDBC driver (update with the correct file path)
jdbc_driver_path = "/Users/lindsayfoster/Projects/smart-store-foster/lib/sqlite-jdbc-3.49.1.0.jar"  # Replace with your actual file path

from pyspark.sql import SparkSession

# Create a Spark session and add the JDBC driver
spark = SparkSession.builder \
    .appName("SmartSales") \
    .config("spark.jars", jdbc_driver_path) \
    .config("spark.driver.extraClassPath", jdbc_driver_path) \
    .getOrCreate()

from pyspark.sql import SparkSession

# Define the path to your SQLite JDBC driver .jar file
jdbc_driver_path = "/path/to/your/sqlite-jdbc-3.49.1.0.jar"  # Replace with your actual driver path

# Create a Spark session and include the JDBC driver
spark = SparkSession.builder \
    .appName("SmartSales") \
    .config("spark.jars", jdbc_driver_path) \
    .config("spark.driver.extraClassPath", jdbc_driver_path) \
    .getOrCreate()

from pyspark.sql import SparkSession

# Define the path to your SQLite JDBC driver .jar file
jdbc_driver_path = "/path/to/your/sqlite-jdbc-3.49.1.0.jar"  # Replace with your actual driver path

# Create a Spark session and include the JDBC driver
spark = SparkSession.builder \
    .appName("SmartSales") \
    .config("spark.jars", jdbc_driver_path) \
    .config("spark.driver.extraClassPath", jdbc_driver_path) \
    .getOrCreate()



from pyspark.sql import SparkSession

# Define the path to your SQLite JDBC driver .jar file
jdbc_driver_path = "/path/to/your/sqlite-jdbc-3.49.1.0.jar"  # Replace with your actual driver path

# Create a Spark session and include the JDBC driver
spark = SparkSession.builder \
    .appName("SmartSales") \
    .config("spark.jars", jdbc_driver_path) \
    .config("spark.driver.extraClassPath", jdbc_driver_path) \
    .getOrCreate()

from pyspark.sql import SparkSession

# Define the path to your SQLite JDBC driver .jar file
jdbc_driver_path = "/path/to/your/sqlite-jdbc-3.49.1.0.jar"  # Replace with your actual driver path

# Create a Spark session and include the JDBC driver
spark = SparkSession.builder \
    .appName("SmartSales") \
    .config("spark.jars", jdbc_driver_path) \
    .config("spark.driver.extraClassPath", jdbc_driver_path) \
    .getOrCreate()

from pyspark.sql import SparkSession

# Define the path to your SQLite JDBC driver .jar file
jdbc_driver_path = "/path/to/your/sqlite-jdbc-3.49.1.0.jar"  # Replace with your actual driver path

# Create a Spark session and include the JDBC driver
spark = SparkSession.builder \
    .appName("SmartSales") \
    .config("spark.jars", jdbc_driver_path) \
    .config("spark.driver.extraClassPath", jdbc_driver_path) \
    .getOrCreate()

# Define the SQLite database URL
jdbc_url = "jdbc:sqlite:/Users/lindsayfoster/Projects/smart-store-foster/data/dw/smart_sales.db"  # Replace with your database path

# Load the 'sales' table from the SQLite database
df_sales = spark.read.format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "sales") \
    .option("driver", "org.sqlite.JDBC") \
    .load()

# Show the first few rows of the dataframe
df_sales.show()

from pyspark.sql import SparkSession

# Define the path to your SQLite JDBC driver .jar file
jdbc_driver_path = "/Users/lindsayfoster/Projects/smart-store-foster/lib/sqlite-jdbc-3.49.1.0.jar"  # Replace with your actual driver path

# Create a Spark session and include the JDBC driver
spark = SparkSession.builder \
    .appName("SmartSales") \
    .config("spark.jars", jdbc_driver_path) \
    .config("spark.driver.extraClassPath", jdbc_driver_path) \
    .getOrCreate()

# Define the SQLite database URL
jdbc_url = "jdbc:sqlite:/Users/lindsayfoster/Projects/smart-store-foster/data/dw/smart_sales.db"  # Replace with your database path

# Load the 'sales' table from the SQLite database
df_sales = spark.read.format("jdbc") \
    .option("url", jdbc_url) \
    .option("dbtable", "sales") \
    .option("driver", "org.sqlite.JDBC") \
    .load()

# Show the first few rows of the dataframe
df_sales.show()