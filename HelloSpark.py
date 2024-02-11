from pkgutil import ImpImporter
from pyspark.sql import *

from lib.logger import log_info, setup_logging

if __name__ == "__main__":
    
    setup_logging()
    
    spark = SparkSession.builder \
        .appName("HelloSpark") \
        .master("local[3]") \
        .getOrCreate()

    log_info("Starting HelloSpark")

    log_info("Finished HelloSpark")
    spark.stop()