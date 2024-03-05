#!/bin/bash

# Spark-shell command
SPARK_SHELL="/usr/bin/spark-shell"

# Run Spark shell with the specified script
$SPARK_SHELL <<EOF

val df = spark.read.format("csv").load("s3://assignment-bucket-shakya/DelayedFlights-updated.csv")

df.write.format("parquet").mode("overwrite").partitionBy("_c1").save("s3://assignment-bucket-shakya/spark-output/DelayedFlights-updated1-df")

val df2 = spark.read.format("parquet").load("s3://assignment-bucket-shakya/spark-output/DelayedFlights-updated1-df")

df2.show()

df2.createOrReplaceTempView("delay_flights")

spark.time {
val carrier_delay_result = spark.sql("SELECT _c1 as Year, avg((_c25/_c15)*100) as Year_wise_carrier_delay FROM delay_flights GROUP BY _c1 ORDER BY _c1 DESC").show()
}

spark.time {
val NAS_delay_result = spark.sql("SELECT _c1 as Year, avg((_c27/_c15)*100) as Year_wise_NAS_delay FROM delay_flights GROUP BY _c1 ORDER BY _c1 DESC").show()
}

spark.time {
val Weather_delay_result = spark.sql("SELECT _c1 as Year, avg((_c26/_c15)*100) as Year_wise_Weather_delay FROM delay_flights GROUP BY _c1 ORDER BY _c1 DESC").show()
}

spark.time {
val late_aircraft_delay_result = spark.sql("SELECT _c1 as Year, avg((_c29/_c15)*100) as Year_wise_late_aircraft_delay FROM delay_flights GROUP BY _c1 ORDER BY _c1 DESC").show()
}

spark.time {
val security_delay_result = spark.sql("SELECT _c1 as Year, avg((_c28/_c15)*100) as Year_wise_security_delay FROM delay_flights GROUP BY _c1 ORDER BY _c1 DESC").show()
}
EOF
