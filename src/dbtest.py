import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(dbname="Resume", user="postgres", password="bhavyachawla", host="localhost")
cur = conn.cursor()

# Execute a query to fetch the binary data
cur.execute("SELECT pdf_data FROM resumes WHERE id = %s", (8,))  # replace 1 with the actual id

# Fetch the result of the query
result = cur.fetchone()

# Write the binary data to a PDF file
with open('output.pdf', 'wb') as f:
    f.write(result[0])

# Close the cursor and the connection
cur.close()
conn.close()