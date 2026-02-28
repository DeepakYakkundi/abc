import assignment

def main():
    print("Hello from pandasrealpython!")

    batch_1 = assignment.UltimateDataScienceBatch("1.0")
    batch_2 = assignment.UltimateDataScienceBatch("2.0")

    batch_1.add_student("Krish", "krish@gmail.com")
    batch_1.add_student("Adarsh", "adarsh@gmail.com")
    batch_2.add_student("Zaid", "zaid@gmail.com")

    batch_1.print_student_names()
    batch_2.print_student_names()


if __name__ == "__main__":
    main()
