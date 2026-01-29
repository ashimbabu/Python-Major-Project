class Employee:
    def __init__(self, emp_id, name, age, gender, department, position, salary, email, phone):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.gender = gender
        self.department = department
        self.position = position
        self.salary = salary
        self.email = email
        self.phone = phone

    def to_dict(self):
        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "gender": self.gender,
            "department": self.department,
            "position": self.position,
            "salary": self.salary,
            "email": self.email,
            "phone": self.phone
        }