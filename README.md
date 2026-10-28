# EduResults — OOP1 Assignment

## Project overview
EduResults is a menu-driven Python program for registering students, recording examination marks, calculating grades, and displaying report cards.

## Requirements
- Python 3.10 or later is recommended.
- No third-party packages are required.

## How to run
1. Extract the project folder.
2. Open the folder in Visual Studio Code.
3. Open Terminal → New Terminal.
4. Run:

   ```bash
   python main.py
   ```

## Example use
1. Choose `1` and register student ID `ER-001`, name `Aminata Kamara`, class `SSS 2A`.
2. Choose `2` and enter student ID `ER-001`, subject `Mathematics`, mark `75`.
3. Repeat option 2 for other subjects.
4. Choose `3` and enter `ER-001` to display the report card.

## OOP concepts demonstrated
- `Student`, `Examination`, and `ResultManagementSystem` classes.
- Objects are created from these classes and interact with each other.
- Instance methods include `add_mark`, `calculate_average`, `add_student`, and `display_report_card`.
- Class method: `Student.change_school_name`.
- Dictionary data structure: `ResultManagementSystem.students` stores Student objects using student IDs as keys.

## Data structure note
The assignment permits a list or dictionary. This project uses a dictionary, where each unique student ID maps to a Student object.

## Digital Public Goods (DPG) alignment
- **Open source:** source code can be published in a public GitHub repository.
- **Inclusive design:** clear menu options, prompts, and validation messages.
- **Privacy-respecting:** use fictional demonstration data; no data is sent to an external service.
- **Modular and reusable:** responsibilities are separated into classes and methods.

## Limitations
- Records are stored in memory and disappear when the program exits.
- This assignment version does not include user login, a persistent database, or a web interface.
- The grading scale is illustrative and should be adjusted to the institution's approved policy before real-world use.
- This is an educational prototype, not a production school information system.

## Suggested screenshots for submission
1. Main menu.
2. Successful student registration.
3. Recording a mark.
4. Report card showing marks, grades, average, and status.
5. Search result.
6. Class method demonstration changing the school name.
