class UltimateDataScienceBatch:
    def __init__(self, batch):
        self._batch = batch
        self._students = []

    def add_student(self, name, email):
        student_dict = {"name" : name, "email" : email}
        self._students.append(student_dict)
        print(f"Added student {name} to batch {self._batch} \n")
        
    def print_student_names(self):
        if self._students:
            print(f"Student list for batch {self._batch}")

            for student in self._students:
                print(f"- {student["name"]}")
        
        else:
            print(f"No students in batch {self._batch}")

        print("\n\n")