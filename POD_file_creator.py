import os
import sys
import requests
from datetime import datetime

def create_pod_file(pod_name: str):
    date = datetime.now()
    year, month, day = str(date.year), f"{date:%B}", f"{date.day:02d}" 
    
    folder_path = os.path.join(year,month)
    os.makedirs(folder_path, exist_ok=True)
    
    file_path = os.path.join(folder_path, f"{day}_{month}_{pod_name}.py")
    
    with open(file_path, "w") as f:
        f.write(f"#POD: {pod_name.replace('_', ' ')}\n")
        f.write(f"#Timestamp: {date}\n")
        f.write(f"\nclass Solution:\n    def solve(self):\n        pass\n")
    
    print(f"File created at: {file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = "_".join(sys.argv[1:]).replace(" ", "_")
    else:
        name = input("Enter POD name: ").strip().replace(" ", "_")
        
    create_pod_file(name)