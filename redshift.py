import psycopg2
conn = psycopg2.connect(
    host="redshift-jenkins.cpiazh88ds78.us-east-1.redshift.amazonaws.com",
    database="dev",
    user="awsuser",
    port=5439,
    password="Admin12345")
cur = conn.cursor()
print("connection succussfully established")
cur.execute("select city from users")
cur.execute("DROP TABLE listing")
print(cur.fetchall())
print(".........")
print()
conn.close()
