from basics_two_pb2 import Person, Employee

p1 = Person(
    id=1,
    name="Logesh",
    age=100,
    contact=Person.Contact(
        mail="some@mail.com",
        phone="001122"
    ),
    person_type = Person.PersonType.PERSON_TYPE_LEGEND
)

print(p1)
print(type(p1))
print("*"*35)
e1 = Employee(
    emp_id = 1,
    emp_name = "LV",
    emp_contact = Person.Contact(
        mail="emp@org.com",
        phone="+0999"
    )
)
print(e1)
print(type(e1))

