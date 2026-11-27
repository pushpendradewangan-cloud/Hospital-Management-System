# 🏥 Hospital Management System

## Project Description

The Hospital Management System is a beginner-friendly, menu-driven console application developed using Python 3. It is designed to manage patient records in a simple and organized way.

The system allows users to add new patients, view all patient records, search patients by their unique ID, update patient details and delete patient records.

Patient IDs are automatically generated starting from P101. The system uses Python dictionaries to manage patient information and CSV file handling to save records permanently.

## ✨ Features

- Add new patient records.
- Automatically generate unique patient IDs.
- View all registered patients.
- Search patients using their ID.
- Update existing patient details.
- Delete patient records.
- Validate patient names and ages (0–120).
- Store patient records in a CSV file.
- Display clear messages for invalid input and missing records.

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Data Structure:** Dictionary
- **File Handling:** CSV
- **Modules:** csv, os
- **Code Editor:** Visual Studio Code

## 📂 Project Structure

```text
Hospital-Management-System/
│
├── codebase/
│   └── hospital.py
│
├── Documentation/
│   └── Project Report.docx
│
└── README.md
```

The `patients.csv` file is created automatically when the program runs, if it does not already exist.

## ▶️ How to Run the Project

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project in Visual Studio Code.
4. Open the Terminal.
5. Navigate to the codebase folder.
6. Run the following command:

```bash
python hospital.py
```

## 📋 Main Menu

```text
===== HOSPITAL MANAGEMENT SYSTEM =====

1. Add Patient
2. View All Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Exit

Enter your choice:
```

## 📊 Patient Record Example

| ID | Name | Age | Disease | Doctor |
|---|---|---|---|---|
| P101 | Ravi Kumar | 35 | Fever | Dr. Mehta |
| P102 | Baby Sen | 0 | Jaundice | Dr. Rao |

## 🎯 Learning Outcomes

Through this project, I learned how to use Python dictionaries, functions, loops, conditional statements, exception handling and CSV file handling. I also gained practical experience in implementing CRUD operations.

## 🚀 Future Improvements

- Add doctor management.
- Add appointment scheduling.
- Maintain patient medical history.
- Add a graphical user interface.
- Integrate a database.

## 📄 Project Documentation

The project report is available in the Documentation folder of this repository.
