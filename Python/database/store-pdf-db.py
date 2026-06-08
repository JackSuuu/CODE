from pymongo import MongoClient
import gridfs

# Connect to MongoDB - brew services start mongodb-community@8.0
# connect to mongoDB cell
client = MongoClient("mongodb://localhost:27017/")
db = client["mydb"]

# Use GridFS for file storage
fs = gridfs.GridFS(db)

# Read and upload PDF
pdf_path = "Database/梦境女孩与爱.pdf"  # Replace with your local file path
with open(pdf_path, "rb") as f:
    file_id = fs.put(f, filename="Database/梦境女孩与爱.pdf")

print(f"Uploaded 'example.pdf' with file ID: {file_id}")

#######

# Find the file in GridFS by filename
file_data = fs.find_one({"filename": "Database/梦境女孩与爱.pdf"})

if file_data:
    with open("retrieved_example.pdf", "wb") as f:
        f.write(file_data.read())
    print("Retrieved and saved as 'retrieved_example.pdf'")
else:
    print("File not found in database.")
