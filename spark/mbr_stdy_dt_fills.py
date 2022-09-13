data=[i.asDict() for i in spark.read.csv("dbfs:/FileStore/mbr_stdy_dt_fills.csv",inferSchema=True,header=True).orderBy('member_id','ndc').collect()]

d_left={}
ndc=0
left=0
resv=0
for i in data:
  if ndc == 0 or ndc != i['ndc']:
    resv=i['fills']
  else:
    resv=i['fills']+d_left[i['ndc']]
  taken=1 if resv>0 else 0
  left=resv-taken
  i['left']=left
  d_left[i['ndc']]=left
  i['resv']=resv
  i['taken']=taken
  ndc=i['ndc']

from pyspark.sql.functions import to_date,col
spark.createDataFrame(data).select('member_id', to_date(col('mbr_be'), "yyy-MM-dd").alias("mbr_be"), to_date(col('mbr_nd'), "yyy-MM-dd").alias('mbr_nd'), to_date(col('Date'), "yyy-MM-dd").alias('Date'), 'ndc', 'fills', 'left', 'resv', 'taken').orderBy('member_id','ndc','resv').display()
