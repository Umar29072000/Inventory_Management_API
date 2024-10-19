# Gunakan image Python resmi
FROM python:3.12.7-slim

# Set work directory di dalam container
WORKDIR /app

# Copy semua file proyek ke dalam container
COPY . .

# Install dependensi (meskipun proyek ini hanya menggunakan standard library)
RUN pip install --no-cache-dir sqlite3

# Jalankan server API
CMD ["python", "main.py"]
