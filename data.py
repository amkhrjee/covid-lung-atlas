import gzip
import os
import tarfile
import urllib.request

raw_tar = "https://www.ncbi.nlm.nih.gov/geo/download/?acc=GSE171524&format=file"

# Download the file
filename = "GSE171524_RAW.tar"
print("Downloading the dataset...")
urllib.request.urlretrieve(raw_tar, filename)

# Extract to data directory
print("Extracting to data/...")
with tarfile.open(filename, "r") as tar:
    tar.extractall("data/")

print("Extraction complete.")

# Decompress .csv.gz files to .csv
print("Decompressing .csv.gz files...")
for file in os.listdir("data/"):
    if file.endswith(".csv.gz"):
        gz_path = os.path.join("data/", file)
        csv_path = os.path.join("data/", file[:-3])  # remove .gz
        with gzip.open(gz_path, "rb") as f_in:
            with open(csv_path, "wb") as f_out:
                f_out.write(f_in.read())
        os.remove(gz_path)

print("Decompression complete.")
os.remove(filename)  # Clean up the downloaded file
