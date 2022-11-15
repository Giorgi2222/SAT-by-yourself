# SAT by yourself

#### Video Demo: <https://youtu.be/hD0rlG3BJQQ>

#### Description:

## Purpose:

Georgian education system doesn't provide valuable higher education. In order to develop themselves professionally, promising students have to study abroad. Entrance in universities all over the world requires excellent results of standardized tests especially from international students with not-so-strong educational background. The most common college-entrance test is SAT. It focuses on evaluating critical thinking skills, which are not promoted by Georgian education system; therefore, students have to prepare for the SAT rigorously. Unfortunately, there are only up to 10 SAT tutors across the country, all of them in economically more developed capital city and thus unaffordable for ordinary families.
With this in mind, I decided to create a website that will help students with self-tutoring. My friends and I already have experience with preparation, so we could provide helpful advice. We collected the best books we had, and I came up with the algorithm that will create a personalized study plan for students according to their English and Math level, their target score, etc. This way, students from Georgia will no longer have any need for a tutor, and financial circumstances will not affect their access to desired education.

## Details:

This website accepts desired SAT scores, current English level and optionally current SAT "Evidence-Based Reading and Writing" and SAT "Math" scores as input. After getting input it is saved in sessions and passed to the "recommend" helper function, which returns a dictionary of two lists first for highly recommended books, and the other for optional ones. First, these lists are filled with books based on desired SAT scores, then depending on starting English level and sat scores, some books are removed from the list or switched to the recommended list. After, returned dictionary of lists is passed to the "books.html" template where it loops over both lists and displays their content as name, author and category of the books in the lists. After passing input once, they are saved permanently, so this page will be rendered every time the user visits the website and can be accessed at any time by clicking "Recommendations" in the navbar. To provide new or updated input, the user can use the "New input" button on the navbar, so the current session will be deleted and the user will be redirected to the first page to provide new inputs.
Another page of the website, all books, can be accessed from the navbar. It displays all books on the website by category. Also, every book has its page, with the cover of the book, a general description, provided by authors, and our guide, about why it is included in certain recommendations and how we recommend using it. These pages can be accessed through links in recommendations and all books sections, by clicking on book names.
