# Databricks notebook source
# MAGIC %sql
# MAGIC WITH TotalPremium AS (
# MAGIC   SELECT SUM(Total_Premium) as Total_Premium
# MAGIC   FROM tangency_dlextech_demo.gold.rol_band_input
# MAGIC   WHERE Intl___US = "US" AND Region_Type = "US" AND Program = "Property - Aggregate"
# MAGIC )
# MAGIC SELECT 
# MAGIC   Mid_RoL, 
# MAGIC   SUM(SUM(Total_Premium)) OVER (ORDER BY Mid_RoL DESC) / (SELECT Total_Premium FROM TotalPremium) * 100 as CumulativePremiumPercentage 
# MAGIC FROM tangency_dlextech_demo.gold.rol_band_input 
# MAGIC WHERE Intl___US = "US" AND Region_Type = "US" AND Program = "Property - Aggregate"
# MAGIC GROUP BY Mid_RoL
# MAGIC SORT BY Mid_RoL DESC
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC Text
