students = {
    1:{"name": "Sam", "sgpa1": 7.2, "sgpa2": 8.5, "sgpa3": 8.1},
    2:{"name": "Jhon", "sgpa1": 9.3, "sgpa2": 9.2, "sgpa3": 9.1},
    3:{"name": "Tom", "sgpa1": 8.8, "sgpa2": 8.7, "sgpa3": 9.1},
    4:{"name": "Jerrry", "sgpa1": 5.6, "sgpa2": 7.5, "sgpa3": 7.8},
    5:{"name": "Spike", "sgpa1": 8.2, "sgpa2": 9.5, "sgpa3": 9.7},
}
print("Roll\tName\tSGPA-1\tSGPA-2\tSGPA-3\tCGPA")
for r, d in students.items():
    cgpa = round((d['sgpa1']+d['sgpa2']+d['sgpa3']) / 3, 2)
    print(f"{r}\t{d['name']}\t{d['sgpa1']}\t{d['sgpa2']}\t{d['sgpa3']}\t{cgpa}")