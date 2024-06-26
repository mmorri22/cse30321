# Welcome to CSE 30321 - Computer Architecture
## University of Notre Dame - Spring 2024

<center><img src = "http://www.phdcomics.com/comics/archive/phd051013s.gif" length=750 width=500></center>

### Class Time and Location

|Meeting Days|Time|Class Location|
|:---|:---|:---|
|Tu Th|11:00am - 12:15pm|DeBartolo Hall 116|

### Textbook

CSE 30321 Computer Architecture zyBook
<ol>
<li>Sign in or create an account  at https://learn.zybooks.com</li>
<li>Enter zyBook code: NDCSE30321MorrisonSpring2024</li>
<li>Subscribe.  Cost is $97 for the semester.</li>
</ol>

### Professor:

|Name|Email|Office Location|Office Hours|
|:---|:---|:---|:---|
|Prof. Matthew Morrison|matt.morrison@nd.edu|178 Fitzpatrick Hall|M-W 1-2pm, Th 1-3pm|

### Teaching Assistants:

The office hours for the TAs may be found on the <a href = "https://canvas.nd.edu/courses/82217/pages/office-hours-calendar">Google Calendar on the Canvas page</a>.

TA Office Hours start the second week of the semester.

|Name|Email|Office Location|Office Hours|
|:---|:---|:---|:---|
|Brigid Burns|bburns4@nd.edu|CSE Commons|W 12-1pm, Th 3:30-4:30pm|
|Luka Cvetko|lcvetko@nd.edu|XXX|XXX|
|Joe Duggan|jduggan5@nd.edu|XXX|XXX|
|Will Truluck|wtruluck@nd.edu|XXX|XXX|

### Additional Links

<b>Course Slack</b>: https://app.slack.com/client/T0HJVP8MS/C06DND1TLBY

<b>Prof Morrison's LinkedIn Page</b>: https://www.linkedin.com/in/gregariousmatt/
<ul><li>I regularly post job and internship opportunities for my students on LinkedIn</li></ul>

### Course Catalog Description

Introduction to <b>basic architectural concepts</b> that are present in <b>current scalar machines</b>, together with an introduction to <b>assembly language programming</b>, <b>computer arithmetic</b>, and <b>performance evaluation</b>. Commercial computer-aided-design software is used to deepen the student's understanding of the <b>top-down processor design methodology</b>. MIPS-based assembly language will be used.

### Course Goals

By the end of this course you should be able to:
<ol> 
<li><b>Describe</b> the fundamental components required in a <b>single core</b> of a modern microprocessor as well as how they interact with each other, with <b>main memory</b>, and with <b>external storage media</b>.</li>
<li>Suggest, compare, and contrast potential <b>architectural enhancements</b> by applying appropriate <b>performance metrics</b>.</li>
<li>Apply fundamental knowledge about a <b>processor’s datapath</b>, different <b>memory hierarchies</b>, performance metrics, etc. to <b>design a microprocessor</b> such that it: 
<ul><li>meets a target set of <b>performance goals</b> and</li>
<li>is <b>realistically implementable</b>.</li>
</ul>
<li>Explain how code written in (different) high-level languages (like C, Java, C++, etc.) can be executed on different microprocessors (e.g., RISC-V, Intel, ARM, etc.) to <b>produce the result intended by the programmer</b>.</li>
<li>Use knowledge about a microprocessor’s <b>underlying hardware</b> (or “architecture”) to <b>write more efficient software</b>.</li>
<li>Describe the main architectural approaches to <b>improve computer performance</b> (circa 2004 and 2012).</li>
<li><b>Explain and articulate</b> why modern microprocessors now have <b>more than one core</b> and how software must adapt to accommodate the now prevalent <b>multi-core approach to computing</b>.</li>
</ol>

### Lecture Notes and Course Schedule

The Lecture Notes and Course Schedule for the Spring 2024 semester may be found on the Canvas page at <a href = "https://canvas.nd.edu/courses/82217/pages/lecture-notes-and-schedule">https://canvas.nd.edu/courses/82217/pages/lecture-notes-and-schedule</a>. This schedule includes all the reading assignments, in-class problems, and assignment descriptions and due dates.

> <b>Note</b>: All solutions to in-class problems will be posted <i>after</i> the lecture.

### Time Outside of Class Expectations

According to Federal Law, a "Credit Hour" is <a href="https://fsapartners.ed.gov/sites/default/files/attachments/dpcletters/GEN1106.pdf">legally defined as follows</a>:

> A credit hour is now formally defined, for Title IV aid purposes, as an amount of work that reasonably approximates <i>not less than</i>:<p></p>
> One hour of classroom or direct faculty instruction and a <i>minimum</i> of two hours of out of class student work each week for approximately fifteen weeks for a semester or trimester hour, or ten to twelve weeks for one quarter hour of credit (or the equivalent amount of work over a different amount of time)

This course is a <i>required</i> engineering course for Computer Science and Computer Engineering majors that is 3 credit hours, meaning that the <u>average</u> student must undertake <i>not less than</i> six hours of work each week outside the classroom. In order to promote efficient instruction and learning, my aim is that the average student spends an efficient 2-3 hours per credit hour outside of classroom instruction on this course. The course is designed for the average student to require <b>7.5 hours per week</b> outside the classroom.

$$ { {CreditHours*(hours_{min} + hours_{max})} \over 2 } = { {3*(2+3)} \over 2 } = { {6+9} \over 2 } = 7.5 $$

The approximate breakdown of work expectation in this course per week is as follows (will vary between students):
<ul>
    <li><b>1.5 hours</b> per week of <b>preview reading</b></li>
    <li><b>1.5 hour</b> per week for <b>reviewing your in-class material</b></li>
    <li><b>4.5 hours</b> per week for <b>Homework Assignments</b></li>
</ul>

> <b>Note</b>: On the student CIF feedback over the last three years, the average student reported their time outside of class in 3-credit courses as <b>7.4 hours/week</b>. This is my aim, which means we are working towards a proper balance between <b>challenging you</b> outside of the classroom and <b>respecting your time</b> requirements for other classes, activities, and responsibilities. <b>If you are struggling, please find me or a TA as soon as possible, and we will provide assistance</b>.


### Assignments

There are four separate assignment categories we will use to assess your progress in the course.

<b>Preview Reading</b>: From the zyBook, these assignments are due Tuesdays at 11:00am. The objective is to prepare you for that week's lectures, including in-class problems, in order to ensure effective study. These assignments will consist of a mix of published zyBook sections with their embedded “Participation Activities” or sections from custom chapters added by the professor with referenced readings from other sources (e.g., videos), along with self-test questions.  The zyBook “Challenge Problems” are not included in the daily assignments and are optional, but they do make for very good self-test questions in preparation for the exams.

<b>Homework Assignments</b>: Problem sets and Coding Assignments that are designed to prepare you for exams and enhance programming proficiency. These assignments will be due by 11:59pm on Thursdays.

<b>Exams</b>: Three examinations will be given this semester. They are closed book, closed notes, closed laptop. Exam 1 and Exam 2 are take-home exams, and the final exam will be in-person during the designated final exam schedule time.

Note in the grade breakdown below that the point total for the Exams escalates during the course of the semester. This approach is to increase the point total as your familiarity with my exam expectations increases as well to ensure the best correlation between your exam performance and your technical understanding.

|Category|Num. Assignments|Points Per Assignment|Total Points|Percent|
|:---|:---|:---|:---|:---|
|Homeworks|12|500|6,000|40%|
|Readings|15|100|1,500|10%|
|Exam 1|1|2,000|2,000|13.33%|
|Exam 2|1|2,500|2,500|16.67%|
|Final Exam|1|3,000|3,000|20%|
|<b>Total</b>|  |  |<b>15,000</b>|<b>100%</b>|

### Assignment Grade Breakdown

Your letter grade will be determined by the total points out of the possible 15,000. In other words, there is no curving in this course. 

> Note: It is my policy to not "curve" grades at the end of the semester. If a student is "close", I do consider the body of their semester's work, and compare it to the Notre Dame Academic Code Description for each letter grade (see below). But once I make my final assessment, it must be final, especially since some students going abroad or on deployment will not have an equal opportunity to request a reconsideration of their grade.

The final grade "bins" for each letter grade:

|Letter Grade|Academic Code Description|Score Range|Percentages|
|:---|:---|:---|:---|
|A|Work meets or exceeds the highest expectations for the course|15,000 - 13,950| 100% - 93% |
|A-|Superior work in all areas of the course|13,949 - 13,500| 92.99% - 90% |
|B+|Superior work in most areas of the course|13,499 - 13,050| 89.99% - 87% |
|B|Solid work across the board|13,049 - 12,450| 86.99% - 83% |
|B-|More than acceptable, but falls short of solid work|12,449 - 12,000| 82.99% - 80% |
|C+|Work meets all the basic requirements and standards for the course|11,999 - 11,550| 79.99% - 77% |
|C|Work meets most of the basic requirements and standards in several areas|11,549 - 10,950| 76.99% - 73% |
|C-|While acceptable, work falls short of meeting basic standards in several areas|10,949 - 10,500| 72.99% - 70% |
|D|Work just over the threshold of acceptability|10,499 - 9,000| 69.99% - 60% |
|F|Unacceptable performance|8,999 - 0| 59.99% - 0% |


## Late Policies and "Extension Tokens" 

If the class truly simulated a professional software development environment, I would probably only accept late assignments! But since this is a class and I need to give you a grade (and to mimic the realities of late software coming with a penalty), I need to ensure fairness across grading.

The expected deadlines for each assignment are posted on the class website. Our assumption is that you will complete each assignment by its due date. 

However, we understand that life gets in the way. It is possible to submit Homework Assignments late by using an "extension token" for the assignment. Every student will start with a total of 3 days (72 hours) worth of slip time that can be used. If you have remaining time, the tokens are automatically granted.

> <b>Note</b>: Examinations are not eligible for Extension Token use.

Any request for an extension token will be automatically granted as long as: 
<ul>
    <li>You have not used up your slip time.</li>
    <li>The assignment in question is eligible.</li>
</ul>

For example, consider a student who has:
<ul>
<li>Submitted Homework 1 three hours late. ( 0.125 slip days, 3 hours )</li>
<li>Submitted Homework 3 thirty-five hours late ( 1.46 slip days, 35 hours )</li>
<li>Submitted Reading 9 sixteen hours late ( 0.67 slip days, 16 hours )</li>
<li>Realizes one day after the deadline that they forgot to submit Homework 9.</li>
</ul>
    
This student has used 2.29 of their slip days ( 54 hours out of 72 ). They have 0.75 days ( 18 hours remaining ). Therefore, we will need to decline the extension request and assign a grade of 0 because the lateness of the submission ( 24 hours ) exceeds their remaining tokens ( 18 hours ).  

### Academic Integrity and Collaboration Policy

CSE 30321 requires every student to turn in a separate code repository that contains their own code. Learning benefits from discussion, so you are welcome to discuss approaches and solution ideas with your classmates, but <i>you must write your own solution code and answers to conceptual questions</i>.

Collaboration is an important part of both CSE 30342 and real-world engineering. Talking through your code with other students leads to less stress and loneliness and to easier debugging.

But collaboration can hurt your learning, too. We want every student to have worked on every project, and to have encountered the intellectual challenges it poses. Simply asking your classmates to show you their solution and copying it hurts your learning, and constitutes academically dishonest behavior (i.e., plagiarism).

We seek a middle ground in which you don't feel isolated and form productive collaborations with your classmates, but still reason through your own code. You may discuss this code with classmates and help your friends debug, but every piece of code you submit must be written by you and you must not submit wholly identical solutions. A good way to ensure this is for you to type in your solutions individually, even if you are discussing your approach with your friends and you help each other debug.

Furthermore, you may not utilize AI powered tools such as ChatGPT, Co-Pilot, or Tabnine for any of your programming assignments.

The following table summarizes how you may work with other students and use print/online sources:

![alt text](image.png)
    
If an instructor sees behavior that is, in their judgment, academically dishonest, they are required to file either an Honor Code Violation Report or a formal report to the College of Engineering Honesty Committee.


### Testing Accommodations

Testing accommodations are modifications to the way you take a test. They do not lower the standards of the test but simply allow you to better demonstrate your understanding of the course material without the interference of a disability. Examples of testing accommodations include extended time, room with less distractions, a reader, or use of a computer. To receive testing accommodations, you must:
<ul>
<li>Obtain a Request for Testing Accommodation (RTA) form from the Sara Bea Disability Services office. You will need one for each class for which you are requesting testing accommodations. RTA forms only apply to your current classes, so you will need to request new forms each semester.</li>
<li>Take your RTA forms to your instructors. If they agree that your accommodations are reasonable, then you each need to complete your portion of the RTA form.</li>
<li>Return the completed RTA form to Sara Bea Disability Services two (2) business days before the first test for which you have requested accommodations</li>
</ul>

### Support for Student Mental Health

<b>University Statement</b> - "Care and Wellness Consultants provide support and resources to students who are experiencing stressful or difficult situations that may be interfering with academic progress. Through Care and Wellness Consultants, students can be referred to The University Counseling Center (for cost-free and confidential psychological and psychiatric services from licensed professionals), University Health Services (which provides primary care, psychiatric services, case management, and a pharmacy), and The McDonald Center for Student Well Being (for problems with sleep, stress, and substance use). Visit care.nd.edu."

<b>My Statement</b> - I encourage all my students to understand that your mental and physical health are paramount, even beyond the impact it may have on your class performance. Factors outside of the classroom contribute to a student's well-being, and I am compassionate and understanding of these issues. In my class room, we will not stigmatize mental health issues nor shame people who are struggling with them, and I pledge to work with each student to facilitate any necessary mental care.

### Diversity, Equity, and Inclusion

<b>University Statement</b> - The University of Notre Dame is committed to social justice and diversity. I share that commitment and strive to maintain a positive learning environment based on open communication, mutual respect, and non-discrimination. In this class, we will not discriminate on the basis of race, sex, age, economic class, disability, veteran status, religion, sexual orientation, color or national origin. Any suggestions as to how to further such a positive and open environment will be appreciated and given serious consideration.

<b>My Additional Statement</b> -  One of my instructing standards is that two students who perform the same amount of work and achieve the same results should receive the same grade. Many of my previously stated policies are designed to help meet this objective. I recognize there are several real-world challenges to achieving this objective, and I will work with all of my students to help break down barriers that force certain students to put in extraneous work in order to achieve the same grade.