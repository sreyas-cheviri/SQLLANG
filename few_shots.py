few_shots = [
 
 {
    "Question": "What is the mobile number of the student with roll number 5?",
    "SQLQuery": "SELECT mobile_number FROM Mobile WHERE roll_num = 5",
    "SQLResult": "5678901234",
    "Answer": "The mobile number of the student with roll number 5 is 5678901234."
},
{
    "Question": "What is the fee balance for the student named 'Alice Johnson'?",
    "SQLQuery": "SELECT FeeBalance.fee_balance FROM FeeBalance JOIN RollNum ON FeeBalance.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id WHERE Name.first_name = 'Alice' AND Name.last_name = 'Johnson'",
    "SQLResult": "4000.00",
    "Answer": "The fee balance for the student named 'Alice Johnson' is 4000.00."
},
{
    "Question": "Which city does the student with roll number 20 live in?",
    "SQLQuery": "SELECT city_name FROM City WHERE roll_num = 20",
    "SQLResult": "Washington",
    "Answer": "The student with roll number 20 lives in Washington."
},
{
    "Question": "How many students are currently in their 3rd semester?",
    "SQLQuery": "SELECT COUNT(*) FROM Semester WHERE semester_number = 3",
    "SQLResult": "5",
    "Answer": "There are 5 students currently in their 3rd semester."
},
{
    "Question": "How many students have passed?",
    "SQLQuery": "SELECT COUNT(*) FROM FailPass WHERE status = 'Pass'",
    "SQLResult": "25",
    "Answer": "25 students have passed."
},
{
    "Question": "What is the first name of the student with the mobile number '1111111111'?",
    "SQLQuery": "SELECT Name.first_name FROM Name JOIN RollNum ON Name.id = RollNum.student_id JOIN Mobile ON RollNum.roll_num = Mobile.roll_num WHERE Mobile.mobile_number = '1111111111'",
    "SQLResult": "Ivy",
    "Answer": "The first name of the student with the mobile number '1111111111' is Ivy."
},{
    "Question": "What is the roll number of the student named 'Brian King'?",
    "SQLQuery": "SELECT roll_num FROM Name WHERE first_name = 'Brian' AND last_name = 'King'",
    "SQLResult": "30",
    "Answer": "The roll number of the student named 'Brian King' is 30."
},
{
    "Question": "Give the last name of the student who is from Phoenix and his roll number and his fail/pass status.",
    "SQLQuery": "SELECT Name.last_name, City.roll_num, FailPass.status FROM FailPass JOIN City ON FailPass.roll_num = City.roll_num JOIN RollNum ON City.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id WHERE City.city_name = 'Phoenix';",
    "SQLResult": "Lee, 5, Pass",
    "Answer": "The student from Phoenix is Charlie Lee, with roll number 5, and his status is Pass."
},
{
    "Question": "Give the last name of the student who is from New York and his roll number and his fail/pass status.",
    "SQLQuery": "SELECT Name.last_name, City.roll_num, FailPass.status FROM FailPass JOIN City ON FailPass.roll_num = City.roll_num JOIN RollNum ON City.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id WHERE City.city_name = 'New York';",
    "SQLResult": "Doe, 1, Pass",
    "Answer": "The student from New York is John Doe, with roll number 1, and his status is Pass."
},
{
    "Question": "Give the last name of the student who is from Los Angeles and his roll number and his fail/pass status.",
    "SQLQuery": "SELECT Name.last_name, City.roll_num, FailPass.status FROM FailPass JOIN City ON FailPass.roll_num = City.roll_num JOIN RollNum ON City.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id WHERE City.city_name = 'Los Angeles';",
    "SQLResult": "Smith, 2, Fail",
    "Answer": "The student from Los Angeles is Jane Smith, with roll number 2, and her status is Fail."
},
{
    "Question": "Give the last name of the student who is from Chicago and his roll number and his fail/pass status.",
    "SQLQuery": "SELECT Name.last_name, City.roll_num, FailPass.status FROM FailPass JOIN City ON FailPass.roll_num = City.roll_num JOIN RollNum ON City.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id WHERE City.city_name = 'Chicago';",
    "SQLResult": "Brown, 3, Pass",
    "Answer": "The student from Chicago is Bob Brown, with roll number 3, and his status is Pass."
},
{
    "Question": "Give the last name of the student who is from Houston and his roll number and his fail/pass status.",
    "SQLQuery": "SELECT Name.last_name, City.roll_num, FailPass.status FROM FailPass JOIN City ON FailPass.roll_num = City.roll_num JOIN RollNum ON City.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id WHERE City.city_name = 'Houston';",
    "SQLResult": "Johnson, 4, Fail",
    "Answer": "The student from Houston is Alice Johnson, with roll number 4, and her status is Fail."
},
{
    "Question": "Give the last name of the student who is from San Antonio and his roll number and his fail/pass status.",
    "SQLQuery": "SELECT Name.last_name, City.roll_num, FailPass.status FROM FailPass JOIN City ON FailPass.roll_num = City.roll_num JOIN RollNum ON City.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id WHERE City.city_name = 'San Antonio';",
    "SQLResult": "Clark, 7, Pass",
    "Answer": "The student from San Antonio is Eve Clark, with roll number 7, and her status is Pass."
},{
    "Question": "Give the first and last names of students who have a fee balance greater than 5000 and their roll numbers.",
    "SQLQuery": "SELECT Name.first_name, Name.last_name, FeeBalance.roll_num FROM FeeBalance JOIN RollNum ON FeeBalance.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id WHERE FeeBalance.fee_balance > 5000;",
    "SQLResult": "David, Wilson, 6; Charlie, Lee, 5; Frank, Martinez, 8; Hank, Anderson, 10; Ivy, Thomas, 11; Oscar, Martin, 17; Paul, Thompson, 18; Grace, Garcia, 9",
    "Answer": "Students with a fee balance greater than 5000 are David Wilson (roll number 6), Charlie Lee (roll number 5), Frank Martinez (roll number 8), Hank Anderson (roll number 10), Ivy Thomas (roll number 11), Oscar Martin (roll number 17), Paul Thompson (roll number 18), and Grace Garcia (roll number 9)."
},{
    "Question": "Find the city and mobile number of students who are in their final semester.",
    "SQLQuery": "SELECT City.city_name, Mobile.mobile_number FROM Semester JOIN RollNum ON Semester.roll_num = RollNum.roll_num JOIN City ON RollNum.roll_num = City.roll_num JOIN Mobile ON RollNum.roll_num = Mobile.roll_num WHERE Semester.semester_number = 10;",
    "SQLResult": "San Jose, 0123456789; Washington, 10100.00; Baltimore, 0123498765; Colorado Springs, 0011223344; Tampa, 8800889900; Wichita, 0000111222",
    "Answer": "Students in their final semester are from the cities and have mobile numbers as follows: San Jose (0123456789), Washington (10100.00), Baltimore (0123498765), Colorado Springs (0011223344), Tampa (8800889900), and Wichita (0000111222)."
},{
    "Question": "Find the city and mobile number of students who are in their final semester.",
    "SQLQuery": "SELECT City.city_name, Mobile.mobile_number FROM Semester JOIN RollNum ON Semester.roll_num = RollNum.roll_num JOIN City ON RollNum.roll_num = City.roll_num JOIN Mobile ON RollNum.roll_num = Mobile.roll_num WHERE Semester.semester_number = 10;",
    "SQLResult": "San Jose, 0123456789; Washington, 10100.00; Baltimore, 0123498765; Colorado Springs, 0011223344; Tampa, 8800889900; Wichita, 0000111222",
    "Answer": "Students in their final semester are from the cities and have mobile numbers as follows: San Jose (0123456789), Washington (10100.00), Baltimore (0123498765), Colorado Springs (0011223344), Tampa (8800889900), and Wichita (0000111222)."
},{
    "Question": "List the first and last names of students who have failed and their fee balances.",
    "SQLQuery": "SELECT Name.first_name, Name.last_name, FeeBalance.fee_balance FROM FailPass JOIN RollNum ON FailPass.roll_num = RollNum.roll_num JOIN Name ON RollNum.student_id = Name.id JOIN FeeBalance ON RollNum.roll_num = FeeBalance.roll_num WHERE FailPass.status = 'Fail';",
    "SQLResult": "Jane, Smith, 2000.00; Alice, Johnson, 4000.00; David, Wilson, 6000.00; Frank, Martinez, 8000.00; Hank, Anderson, 10000.00; Jack, Taylor, 2200.00; Leo, Jackson, 4400.00; Nina, Harris, 6600.00; Paul, Thompson, 8800.00; Rose, Martinez, 10100.00; Tina, Clark, 3030.00; Victor, Lewis, 5050.00; Xander, Walker, 7070.00; Zack, Allen, 9090.00; Brian, King, 20220.00; Derek, Green, 40440.00; Fred, Baker, 60660.00; Holly, Nelson, 80880.00; Jill, Mitchell, 20002.00; Lena, Roberts, 30003.00; Nora, Phillips, 50005.00; Paula, Parker, 70007.00; Quincy, Evans, 90009.00; Tara, Stewart, 200020.00; Vera, Morris, 400040.00",
    "Answer": "Students who have failed and their fee balances are as follows: Jane Smith (2000.00), Alice Johnson (4000.00), David Wilson (6000.00), Frank Martinez (8000.00), Hank Anderson (10000.00), Jack Taylor (2200.00), Leo Jackson (4400.00), Nina Harris (6600.00), Paul Thompson (8800.00), Rose Martinez (10100.00), Tina Clark (3030.00), Victor Lewis (5050.00), Xander Walker (7070.00), Zack Allen (9090.00), Brian King (20220.00), Derek Green (40440.00), Fred Baker (60660.00), Holly Nelson (80880.00), Jill Mitchell (20002.00), Lena Roberts (30003.00), Nora Phillips (50005.00), Paula Parker (70007.00), Quincy Evans (90009.00), Tara Stewart (200020.00), and Vera Morris (400040.00)."
},{
    "Question": "Give the mobile number and roll number of students who have a fee balance above 20 thousand and have failed.",
    "SQLQuery": "SELECT Mobile.mobile_number, FeeBalance.roll_num FROM FeeBalance JOIN RollNum ON FeeBalance.roll_num = RollNum.roll_num JOIN Mobile ON RollNum.roll_num = Mobile.roll_num JOIN FailPass ON RollNum.roll_num = FailPass.roll_num WHERE FeeBalance.fee_balance > 20000 AND FailPass.status = 'Fail';",
    "SQLResult": "0123498765, 30; 0011223344, 40; 8800889900, 48",
    "Answer": "Students who have a fee balance above 20 thousand and have failed are with mobile numbers 0123498765 (roll number 30), 0011223344 (roll number 40), and 8800889900 (roll number 48)."
},

]
