# **kwargs Example

def student(**details):
    for key, value in details.items():
        print(f"{key} : {value}")


student(
    name="Karan",
    age=22,
    city="Surat"
)