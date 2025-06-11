import os

# Folder jisme galti se files aa gayi hain
target_folder = r"C:\Users\HP\OneDrive\Desktop\python_practice"

# List of known incorrect files (dekh ke likho ya manually detect karo)
wrong_files = [
    "2datainsert.py", "avgfunctioninmysql.py", "countfunction.py", "createtable.py",
    "deletequery2.py", "distinct.py", "Equidta.py", "innerjoin.py", "insertdata.py",
    "leftjoin.py", "limit.py", "max&minfunction.py", "mindata.py", "mssqlsum.py",
    "mysqlbtwoperation.py", "mysqlgroupbystatement.py", "newcode.py", "newstudentdata.py",
    "queryinsert.py", "queryupdate.py","msqlsum.py","rightleft.py","school.py","seachdata.py","2dataainsert.py","selfjoin.py",
]

for file in wrong_files:
    path = os.path.join(target_folder, file)
    if os.path.exists(path):
        os.remove(path)
        print(f"Deleted: {file}")
    else:
        print(f"Not Found: {file}")