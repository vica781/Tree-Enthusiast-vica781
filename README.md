![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
<h1>
    <a href="https://tree-enthusiast-vica781-11c9e6b9e6b1.herokuapp.com/">
        <img src="./media/docs_images/oak-logo.png" alt="Tree Enthusiast logo" width="105" height="100" style="vertical-align:middle">
    </a>
    TREE ENTHUSIAST
</h1>


[![Am I Responsive Mockup](./media/docs_images/am_I_responsive.png)](https://tree-enthusiast-vica781-11c9e6b9e6b1.herokuapp.com/)

## Table of Contents

[Tree Enthusiast](#tree-enthusiast)
  * [Table of Contents](#table-of-contents)
  * [Introduction](#introduction)
  * [User Stories](#user-stories)
  * [UX](#ux)
    + [Typography](#typography)
    + [Wireframes](#wireframes)
  * [Accessibility](#accessibility)
  * [Database Design](#database-design)
  * [Features](#features)
  * [Existing Features](#existing-features)
  * [Future Features](#features-features)
  * [Issues and Bugs](#issues-and-bugs)
  * [Technologies Used](#technologies-used)
  * [Testing](#testing)
  * [Deployment](#deployment)
    + [Local Deployment](#local-deployment)
    + [Heroku Deployment](#heroku-deployment)
  * [Credits](#credits)
    + [Content](#content)
    + [Media](#media)
  * [Acknowledgements](#acknowledgements)

## Introduction
This website "Books for Life" is a fourth Portfolio Project of the Code Institute's Full Stack Web Development course. It is a Full Stack developed website. The website is built using Django 4.2.9, Bootstrap 4.6 and Python 3.11. The database is hosted on ElephantSQL and the static files are hosted on Cloudinary. The website is deployed on Heroku.
<br>
Embark on a botanical journey with the Tree Enthusiast App, a tool designed for those who find joy and wonder in the embrace of nature's arboreal splendor. As William Blake poetically reflected, "The tree which moves some to tears of joy is in the eyes of others only a green thing that stands in the way." This app aims to dissolve this barrier, revealing the true beauty of trees to every enthusiast.

### Key Features:

***Discover and Browse:*** Explore a diverse collection of trees at your leisure. The extensive database provides a wealth of information, allowing you to satisfy your arboreal curiosity.  
***Search for Specific Trees:*** Looking for information on a particular tree? App's search function makes it easy to find the details you need.  
***Printable Identification Guides:*** Take the knowledge with you on your adventures with handy guides that can be printed and brought along on your treks through nature.  
***Community Contributions:*** Registered users can become an integral part of our community by adding their tree discoveries to the app's collective repository, complete with their notes and insights.  
***Personal Collection Management:*** Curate your own personal collection of trees within the app. View, edit, and manage your contributions and see how they fit into the broader tapestry of communal knowledge.  
***Guided Forest Experiences:*** Connect deeper with nature through our guides on forest bathing and grounding techniques, bringing mental health and mindfulness to the forefront of your outdoor explorations.
<br>
<br>
The Tree Enthusiast App is not just a tool but a companion for your green escapades. It's a celebration of the trees around us, fostering a community that cherishes and preserves the natural world. Whether you are charting the woods for new specimens or simply enjoying the serenity of a forest bath, the Tree Enthusiast App enriches your experience and deepens your connection to the earth's towering guardians.
<br>
<br>
Join the comunity and turn every green encounter into a moment of learning, sharing, and personal growth. With the Tree Enthusiast App, every tree is a story waiting to be told, and every forest a chapter yet to be explored.

[Back to top ⇧](#table-of-contents)

## User Stories

***

<font size="5"><b>1.</b> As a <b>new user</b>, I want to <b>be able to register on the platform</b>, so that I can <b>login and get access</b>.</font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] User can register using their full name, email, and password through a registration form on the platform.
- [x] The user receives messages upon both successful and unsuccessful registration attempts.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Design and implement the registration form with front-end validation for full name, email, and password fields.
- [x] Redirect registered user to a landing page.

***

<font size="5"><b>2.</b> As a <b>user</b>, I want to <b>log in to my account</b>, so that I can <b>access personalized features and secure my account information</b>.</font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: The login page should have fields for entering username and password.
- [x] Criteria 2: The system should authenticate the user's credentials against the database.
- [x] Criteria 3: Upon successful login, the user should be redirected to their dashboard.
- [x] Criteria 4: The system should display an error message for incorrect login credentials.
- [x] Criteria 5: There should be an option for users to reset their password if forgotten.
- [x] Criteria 6: The login page should provide a clear option for users to navigate to the registration page if they do not have an account.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Design and implement the login page with username and password fields.
- [x] Task 2: Develop the backend logic for user authentication.
- [x] Task 3: Set up a secure connection to the user database for credential verification.
- [x] Task 4: Implement user feedback for login success or failure.
- [x] Task 5: Create a password reset feature.
- [x] Task 6: Add a prompt on the login page that directs users to the registration page, with text such as "Don't have an account?" and link "Register here."

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>3.</b> As a <b>user</b>, I want to <b>be able to securely log out of my account</b>, so that I can <b>ensure my account is safe when I'm not using it.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: There should be a clearly visible logout option accessible from any page after login.
- [x] Criteria 2: The system should end the user's session upon clicking the logout button.
- [x] Criteria 3: After logging out, the user should be redirected to the home page.
- [x] Criteria 4: The user should be informed about sucsess of login out.
- [x] Criteria 5: The system should confirm the user's intention to log out to prevent accidental logouts.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Implement a logout button in the user interface.
- [x] Task 2: Develop the backend logic to terminate the session upon logout.
- [x] Task 3: Set up a redirect to the home page or login page after logout.
- [x] Task 4: Create a logout confirmation prompt.
- [x] Task 5: Create a message to let user know that they successfully logged out.

***

<font size="5"><b>4.</b> As a <b>user/tree enthusiast</b>, I want to <b>easily access and use the contact page on the website</b>, so that I can <b>reach out for support or share feedback about my experiences with adding and viewing tree information.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: The contact page is easily accessible from any page on the website, including while adding or viewing tree information, ideally within one or two clicks.
- [x] Criteria 2: The contact page includes method of contact suitable for different types of inquiries, such as technical support or feedback.
- [x] Criteria 3: The contact form on the page is simple and intuitive, requiring only essential information, and it provides clear confirmation once a message is successfully sent.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Design and implement an easily noticeable and accessible link to the contact page, ensuring it is available during all major user activities, such as account creation and tree data entry.
- [x] Task 2: Develop and integrate the contact page with contact option, including a user-friendly form with space for a message.
- [x] Task 3: Set up backend support for form submission, ensuring reliable delivery of user messages and automatic confirmation responses to the user.

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>5.</b> As a <b>registered user</b>, I want to <b>easily manage my account and personalize my profile</b>, so that I can <b>enhance my user experience and maintain my account security.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

1. ***Profile Accessibility from Navbar:***
- [x] Criteria 1: The user's username appears as a clickable link in the navbar, next to the Logout button, once they are logged in.
- [x] Criteria 2: A `user icon` placeholder from font awasom or other source for the user's profile is displayed next to their username in the navbar.

2. ***Profile Viewing and Editing:***
- [x] Criteria 3: Users can view their profile details by clicking on their username in the navbar.
- [x] Criteria 4: Users have the option to edit their profile, including adding or changing their profile image.
- [x] Criteria 5: The User Profile form has a personalized heading that greets the user by their username.
- [x] Criteria 6: The User Profile form has a main content area that includes placeholder for the user's profile image, first and last names, and email address.
- [x] Criteria 7: There is a distinct section at the bottom of the User Profile with "Update Profile" and "Delete Profile" buttons .
- [x] Criteria 8: There is a message to inform user about result of the profile update.

3. ***Account Security:***
- [x] Criteria 9: Users can change their password from their profile settings.
- [x] Criteria 10: The process for changing the password includes current password verification for security.

##### TASKS
_A single unit of work broken down from the defined user story_

1. ***Implement User Link in Navbar:***
- [x] Task 1: Develop the functionality to display the logged-in user's username as a link in the navbar.
- [x] Task 2: Integrate a `user icon` placeholder next to the username in the navbar.

2. ***Profile Page Development:***
- [x] Task 3: Create a profile page accessible by clicking the username in the navbar.
- [x] Task 4: Design the user interface for viewing and editing profile details, including image upload.
- [x] Task 5: Implement a dynamic greeting in the User Profile header that fetches and displays the current user's username.
- [x] Task 6: Create a main content area that includes placeholders for the user's profile image, username, and email address.
- [x] Task 7: Ensure that the user's current profile image, username, and email are correctly fetched and displayed in the main content area.
- [x] Task 8: Add "Update Profile" and "Delete Profile" buttons at the bottom of the profile page.
- [x] Task 9: Ensure that the user is notifyed about outcome of the profile update.

3. ***Password Change Functionality:***
- [x] Task 10: Develop a secure password change feature within the profile settings.
- [x] Task 11: Implement current password verification before allowing password changes.

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>6.</b> As a <b>registered user</b>, I want to <b>delete my profile securely and with clear confirmation steps</b>, so that I can <b>ensure that my decision is intentional and informed, and be reassured of successful deletion.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

1. ***Secure Profile Deletion:***
 - [x] Criteria 1: The user can initiate profile deletion from the 'Delete Profile' button on their profile page. 
 - [x] Criteria 2: A confirmation modal appears when the user clicks the 'Delete Profile' button, asking them to confirm their decision.

2. ***Defensive Design for Deletion:***
- [x] Criteria 3: The confirmation modal for deletion clearly outlines the consequences of profile deletion. 
- [x] Criteria 4: The modal provides two options: 'Confirm Deletion' and 'Cancel', with distinct visual differences for clarity.

3. ***Password Confirmation for Deletion:***
 - [x] Criteria 7: The user is required to confirm their password before the profile is deleted.
 - [x] Criteria 8: The system verifies the password before proceeding with profile deletion.

4. ***Feedback on Deletion:***
- [x] Criteria 9: Upon confirming deletion, the user is logged out and their profile is permanently deleted. 
- [x] Criteria 10: The user receives a notification confirming the successful deletion of their profile.

##### TASKS
_A single unit of work broken down from the defined user story_

1. ***Implement Deletion Process:***
- [x] Task 1: Develop functionality for the 'Delete Profile' button on the user profile page. 
- [x] Task 2: Create a confirmation modal that appears when 'Delete Profile' is clicked.

2. ***Modal Design and Functionality:***
- [x] Task 3: Design the confirmation modal with clear messaging and options for 'Confirm Deletion' and 'Cancel'. 
- [x] Task 4: Ensure that the modal visually distinguishes between the 'Confirm Deletion' and 'Cancel' options.

3. ***Implement Password Confirmation:***
- [x] Task 7: Update the deletion modal to include a password confirmation field. 
- [x] Task 8: Validate the user's password when the deletion form is submitted.

4. ***User Feedback and Completion:***
- [x] Task 9: Implement the deletion process, including user logout and data removal upon confirmation. 
- [x] Task 10: Create a notification system to confirm successful profile deletion to the user.

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>7.</b> As a <b>registered and logged-in user</b>, I want to <b>add a new tree to my collection</b>, so that I can <b>share information about different trees.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: The user must be registered and logged into the website.
- [x] Criteria 2: The user should be able to access the 'Add Tree' page from the navigation menu.
- [x] Criteria 3: The 'Add Tree' form must include fields for the tree's common name, type, origin, a short introduction, an image upload option, and a description of the tree's habitat.
- [x] Criteria 4: Upon submitting the form, the tree information should be saved to the user's tree collection.
- [x] Criteria 5: The user should receive a success message upon successful addition of the tree.
- [x] Criteria 6: Appropriate validation messages should be displayed in case of form errors.
- [x] Criteria 7: The tree information should be viewable in the 'My Trees' section of the website.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Create a secure authentication system to ensure only registered and logged-in users can access the 'Add Tree' feature.
- [x] Task 2: Design and implement the 'Add Tree' page with the necessary form fields.
- [x] Task 3: Set up server-side logic to handle the 'Add Tree' form submission, including data validation and storage.
- [x] Task 4: Develop a user feedback system to confirm successful addition of a tree or inform of any errors.
- [x] Task 5: Integrate the newly added tree data into the 'My Trees' section for the user.
- [x] Task 6: Conduct testing to ensure all acceptance criteria are met. 

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>8.</b> As a <b>registered and logged-in user</b>, I want to <b>add a new tree to my collection</b>, so that I can <b>share information about different trees.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: The user must be registered and logged into the website.
- [x] Criteria 2: The user should be able to access the 'Add Tree' page from the navigation menu.
- [x] Criteria 3: The 'Add Tree' form must include fields for the tree's common name, type, origin, a short introduction, an image upload option, and a description of the tree's habitat.
- [x] Criteria 4: Upon submitting the form, the tree information should be saved to the user's tree collection.
- [x] Criteria 5: The user should receive a success message upon successful addition of the tree.
- [x] Criteria 6: Appropriate validation messages should be displayed in case of form errors.
- [x] Criteria 7: The tree information should be viewable in the 'My Trees' section of the website.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Create a secure authentication system to ensure only registered and logged-in users can access the 'Add Tree' feature.
- [x] Task 2: Design and implement the 'Add Tree' page with the necessary form fields.
- [x] Task 3: Set up server-side logic to handle the 'Add Tree' form submission, including data validation and storage.
- [x] Task 4: Develop a user feedback system to confirm successful addition of a tree or inform of any errors.
- [x] Task 5: Integrate the newly added tree data into the 'My Trees' section for the user.
- [x] Task 6: Conduct testing to ensure all acceptance criteria are met. 

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>9.</b> As a <b>registered and logged-in user</b>, I want to <b>edit the information of trees I have added</b>, so that I can <b>update or correct their details as needed.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: The user must be registered and logged into the website.
- [x] Criteria 2: The user should be able to access the 'Edit' option for each tree in their 'My Trees' collection.
- [x] Criteria 3: Upon selecting 'Edit', the user should be directed to a form pre-populated with the existing details of the tree.
- [x] Criteria 4: The edit form should allow changes to all aspects of the tree's information, including name, type, origin, introduction, image, and habitat.
- [x] Criteria 5: The user should be able to submit the updated information with a confirmation option.
- [x] Criteria 6: Upon successful update, a confirmation message should be displayed.
- [x] Criteria 7: Any errors or validation issues during the update process should be communicated to the user.
- [x] Criteria 8: The updated information should be reflected in the 'My Trees' collection and the tree's detail view.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Implement a secure and intuitive edit option for each tree in the user's collection.
- [x] Task 2: Design and develop the tree edit form with fields for all editable details.
- [x] Task 3: Ensure that the form is pre-populated with the tree's existing information.
- [x] Task 4: Handle the form submission and update the tree information in the database.
- [x] Task 5: Provide clear success and error messages post-submission.
- [x] Task 6: Ensure that the updates are immediately visible in the tree's detail view and in the 'My Trees' collection.
- [x] Task 7: Test the editing feature for functionality and user-friendliness.

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>10.</b> As a <b>registered and logged-in user</b>, I want to <b>have the ability to delete trees from my collection</b>, so that I can <b>remove outdated or incorrect tree entries.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: The user must be registered and logged into the website.
- [x] Criteria 2: The user should be able to access a 'Delete' option for each tree in their 'My Trees' collection.
- [x] Criteria 3: On selecting 'Delete', a confirmation prompt should appear to prevent accidental deletions.
- [x] Criteria 4: The user should be required to confirm their password to proceed with the deletion as an additional security measure.
- [x] Criteria 5: Upon confirming the deletion, the tree should be permanently removed from the user's collection.
- [x] Criteria 6: The user should receive a success message confirming the tree's removal.
- [x] Criteria 7: The deletion action should not affect other trees in the collection.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Implement a secure 'Delete' option for each tree in the user's collection.
- [x] Task 2: Design and develop a confirmation prompt to verify the user's intent to delete.
- [x] Task 3: Implement a password confirmation step for additional security.
- [x] Task 4: Handle the deletion process in the backend, ensuring that the tree is permanently removed from the database.
- [x] Task 5: Provide clear success messages based on the deletion outcome.
- [x] Task 6: Ensure the website's user interface is updated immediately to reflect the deletion.
- [x] Task 7: Test the feature to ensure it works as intended and is secure.

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>11.</b> As a <b>user of the Tree Enthusiast website</b>, I want to <b>search for trees using their common names</b>, so that I can <b>quickly find specific trees and learn more about them.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: Users, whether logged in or not, should be able to use the search feature.
- [x] Criteria 2: The search bar should be easily accessible, preferably on the website's header.
- [x] Criteria 3: Users should be able to enter the common name of a tree and submit the search query.
- [x] Criteria 4: The search results page should display all trees that match the entered common name.
- [x] Criteria 5: Each search result should include relevant information such as the tree's image, common name, and a link to its detailed page.
- [x] Criteria 6: If no matches are found, the website should display a message like "No trees found with that common name."
- [x] Criteria 7: The search feature should provide results promptly and accurately.
- [x] Criteria 8: The search results should be presented in a user-friendly manner, allowing easy navigation to detailed tree pages.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Implement a search bar that users can access from any page on the website.
- [x] Task 2: Develop the backend logic to search the tree database by common name.
- [x] Task 3: Design and implement a search results page to display the matching trees.
- [x] Task 4: Ensure each search result includes a link to the detailed information page of the tree.
- [x] Task 5: Handle scenarios with no search results by displaying an appropriate message.
- [x] Task 6: Test the search functionality with various common names to ensure accuracy and speed.
- [x] Task 7: Ensure the search results layout is responsive and user-friendly.

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>12.</b> As a <b>visitor to the Tree Enthusiast website</b>, I want to <b>access a 'Browse Trees' feature</b>, so that I can <b>view all trees listed in the database in a user-friendly format</b>, and if interested, be prompted to 'Login' or 'Sign Up' for further interactions. As a <b>registered and logged-in user</b>, I should be able to <b>edit or delete trees I have added</b>, or access 'Add Tree', 'My Trees', or 'Home' when viewing tree details.</font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: The 'Browse Trees' feature should be accessible to all visitors, regardless of their login status.
- [x] Criteria 2: All trees in the database should be displayed in an image-card format, similar to the 'My Trees' section, with each card linking to the tree's detailed page.
- [x] Criteria 3: Visitors who are not registered or logged in should be prompted to log in or sign up when viewing detailed tree information.
- [x] Criteria 4: Registered and logged-in users should have the ability to edit or delete their own tree entries from the detailed view.
- [x] Criteria 5: For trees not added by the logged-in user, options like 'Add Tree', 'My Trees', and 'Home' should be available for navigation.
- [x] Criteria 6: The interface for browsing trees should be intuitive and engaging, encouraging visitors to explore the tree collection.
- [x] Criteria 7: The feature should ensure a seamless transition from viewing to registration or login for new users.

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Develop the 'Browse Trees' section accessible from the website's main navigation for all visitors.
- [x] Task 2: Display trees in an image-card layout, with links to detailed information.
- [x] Task 3: Implement prompts for non-logged-in visitors to register/sign up.
- [x] Task 4: Enable edit and delete functionalities for logged-in users on their own tree entries.
- [x] Task 5: Provide navigation options for logged-in users to access 'Add Tree', 'My Trees', or 'Home' from tree's detail view.
- [x] Task 6: Design a user-friendly and engaging interface for the 'Browse Trees' section.
- [x] Task 7: Ensure the site's performance and speed are optimized for handling numerous tree entries.
- [x] Task 8: Test the feature thoroughly for different user scenarios and make adjustments based on feedback.

[Back to top ⇧](#table-of-contents)

***

<font size="5"><b>13.</b> As a <b>registered and logged-in user</b> of the Tree Enthusiast website, I want to <b>search and view trees with a specific common name added by any user</b>, while being able to <b>edit and delete only the trees that I have added</b>, and have access to 'My Trees', 'Add Tree', and 'Home' buttons when viewing trees added by others, so that I can <b>manage my contributions and navigate the site effectively without affecting other users' entries.</b></font>

***

##### ACCEPTANCE CRITERIA
_A set of predefined requirements that must be met to meet the user story needs (and mark it as complete)_.

- [x] Criteria 1: All users, upon logging in, should be able to search for trees by their common name and see results added by any user.
- [x] Criteria 2: The search results page should display all matching trees with relevant details like images and common names.
- [x] Criteria 3: 'Edit' and 'Delete' options should be visible and functional only next to the trees that the logged-in user has added.
- [x] Criteria 4: For trees not added by the user, buttons for 'My Trees', 'Add Tree', and 'Home' should be available for easy navigation. 

##### TASKS
_A single unit of work broken down from the defined user story_

- [x] Task 1: Implement frontend logic to display 'Edit' and 'Delete' buttons only for trees added by the logged-in user.
- [x] Task 2: Ensure 'My Trees', 'Add Tree', and 'Home' buttons are displayed when viewing trees added by other users.
- [x] Task 3: Conduct testing to ensure proper functionality and security across different user scenarios.

[Back to top ⇧](#table-of-contents)

## UX

### Refined Development Plan for Tree Enthusiast App

#### Strategy
- **Objective:** Craft a multi-faceted platform that serves as a hub for tree identification, educational growth, and mental wellness through nature, catering to the needs of a diverse community of tree enthusiasts and those seeking solace in nature.
- **User Research:** Expand surveys and user interviews to encompass individuals seeking outdoor-related mental wellness in addition to tree identification knowledge.
- **Competitor Analysis:** Examine other platforms that provide not just botanical information but also those that delve into the therapeutic aspects of nature.
- **Persona Creation:** Include personas such as nature therapy seekers, educators in botany and mental health professionals who recommend nature as therapy.
- **Goals:** Enrich goals to include the broadening of the app's resource base, fostering collaboration with mental health and environmental organizations, and creating a comprehensive guide to forest therapy techniques.

[Back to top ⇧](#table-of-contents)

### Target Audience

#### Roles:
- Beginners in Tree Identification
- Nature Therapy Participants
- Environmental Educators and Mental Health Professionals
- App Administrators, Content Creators, and Moderators

#### Demographics:
- Broad spectrum, from school-age children to seniors
- Individuals seeking therapeutic experiences through nature
- Professionals and volunteers in environmental and mental health sectors

### Psychographics:

#### Personality & Attitudes:
- Inquisitive about nature's diversity
- Advocates for mental health and well-being
- Believers in ecotherapy and the healing power of nature

### Values:
- Nature conservation and biodiversity
- Mental wellness and holistic health
- Education and the sharing of expertise

### Lifestyles:
- Outdoor enthusiasts and hikers
- Individuals practicing mindfulness and relaxation techniques
- Educators and therapists incorporating nature into their practice

[Back to top ⇧](#table-of-contents)

### User and Client Needs

***

| User Needs                         | Client Needs                 |
|------------------------------------|------------------------------|
| Register/Login to account          | Manage User Accounts         |
| Search for trees                   | Provide a Tree Database      |
| View Tree Details                  | Ensure Data Accuracy         |
| Add/Edit Own Tree Entries          | Accessible Tree Editing Tool |
| View Personal Tree Collection      | User Activity Insights       |
| Get in Contact with Admin          | Customer Support Management  |
| Share Tree Information             | Social Media Integration     |
| Accessible Navigation              | User Engagement              |

### Importance/Viability Tables

***

##### User Management Table
| Feature             | Importance | Viability | Notes                                       |
|---------------------|------------|-----------|---------------------------------------------|
| Register            | 5          | 5         | Allows users to create a new account.       |
| Log In              | 5          | 5         | Allows users to access their accounts.      |
| Log Out             | 5          | 5         | Allows users to securely exit their accounts. |
| Edit Profile        | 4          | 4         | Registered users can update personal information. |
| View User Profile   | 4          | 5         | Users can view their own and others' profiles. |
| Delete Profile      | 3          | 4         | Allows users to remove their account from the app. |

##### Tree Management Table
| Feature              | Importance | Viability | Notes                                       |
|----------------------|------------|-----------|---------------------------------------------|
| Add Tree Details     | 5          | 5         | Registered users can add new tree entries.  |
| Edit Tree Details    | 4          | 5         | Users can edit trees they've added.         |
| Delete Tree Record   | 4          | 4         | Users can delete trees they've added.       |
| Search Tree Records  | 5          | 5         | All visitors can search the tree database.  |
| Browse Tree Records  | 5          | 5         | All visitors can browse the tree collection.|
| View Individual Tree Details | 5  | 5         | All visitors can view tree details.         |
| Like/Dislike Tree    | 4          | 3         | Registered users can like or dislike trees. |
| Comment on Tree      | 4          | 3         | Registered users can comment on tree details.|

##### Other Features Table
| Feature                 | Importance | Viability | Notes                                    |
|-------------------------|------------|-----------|------------------------------------------|
| Welcoming Page          | 5          | 5         | First page visitors see, unregistered and registered. |
| Contact Page            | 3          | 5         | Allows users to contact admins.          |
| Social Media Integration| 3          | 4         | Lets users share trees on social media.  |

[Back to top ⇧](#table-of-contents)

## SCOPE

### Features:
- User registration
- Profile management
- Tree collection browsing
- Individual tree detail viewing
- Tree addition, editing, and deletion
- Comment functionality
- Like/dislike functionality
- Personal tree collection access
- Contact form
- Tree search

### Content:
- Tree Enthusiast will contain:
  - Tree names
  - Types
  - Origins
  - Images
  - Descriptions
  - Habitat information
  - User contributions

### User Flow:
- Unregistered visitors can:
  - Browse and search the tree collection
  - View tree details
- Registered users can:
  - Log in
  - Add trees to the collection
  - Manage their personal tree collection
  - Edit and delete tree information they have added
  - Utilize like/dislike and comment functionalities on tree details

[Back to top ⇧](#table-of-contents)

### Technical Requirements:
- **Front-End:**
  - HTML
  - CSS
  - JavaScript
  - Bootstrap 4.6
  - Font Awesome
- **Back-End:**
  - Python
  - Django 4.x
  - PostgreSQL
- **Deployment:**
  - Hosted on a platform like Heroku
  - Static and media files stored on Cloudinary
  - Database hosted on ElephantSQL
- **Version Control:**
  - Git
  - GitHub

### Milestones:
- Divided into phases:
  - Initial release
  - Feature additions
  - Final refinements
- Managed using Github Projects

[Back to top ⇧](#table-of-contents)

## Content Requirements

- Customisable user accounts with the ability to add, modify, and delete tree details.
- Intuitive navigation with a user-friendly theme (typography, imagery, color palette).
- **Tree Detail Page to include:**
  - Common Name
  - Tree Type
  - Origin
  - Image
  - Description
  - Habitat Information
  - Likes/Dislikes
  - Comments
- Searchable tree database
- Contact form for user inquiries
- Personal tree collection page for users to manage their added trees
- User profile page to view and edit profile details

[Back to top ⇧](#table-of-contents)

## Functionality Requirements

- Users will be able to:
  - Register and create a personalized account
  - Log in to and out of their account
  - Browse the entire tree collection without registration
  - Search for trees within the database
  - View detailed information about each tree
  - Add new trees to the database with details such as name, type, image, description, and habitat information
  - Edit and delete their own tree entries
  - Like/dislike trees and view the total number of likes/dislikes
  - Comment on tree details for interaction with other users
  - Access and manage their personal collection of added trees
  - Contact the admin through a form for support or inquiries
  - Customize their user profile, including uploading a profile picture and editing profile details
  - Delete their user profile
  - Encounter a custom 404 page when attempting to visit a nonexistent page

[Back to top ⇧](#table-of-contents)

## STRUCTURE

### Interaction Design:
- Users will interact with the Tree Enthusiast app through a combination of mouse clicks and keyboard inputs.
- Touchscreen-friendly features for mobile and tablet users.
- Interactive elements such as buttons, forms, and search field will provide visual feedback to facilitate user interaction.

### Information Architecture:
- Information will be hierarchically structured, emphasizing ease of access to key features like tree browsing, searching, and user profile management.
- Key information such as tree details will be prominently displayed.

### Navigation:
- Navigation will be straightforward and user-friendly, with a consistent and prominently placed navigation bar across the website.
- A responsive design to ensure seamless navigation on various devices, including desktops, tablets, and smartphones.
- Access to main features like 'Browse Trees', 'My Trees', and 'Add Tree' will be available from the main menu, with additional options accessible from related screens/forms.

### Information Design:
- Information will be presented in a clear, concise, and engaging manner.
- Information such as tree descriptions and habitat details will be organized into readable segments for ease of understanding.

### Interface Design:
- A clean and minimalist interface that highlights the app's features without overwhelming the user.
- Responsive design principles to ensure the interface is optimized for a variety of screen sizes and resolutions.
- Consistency in design elements such as color schemes, typography, and button styles across different pages for a cohesive user experience.

[Back to top ⇧](#table-of-contents)

### **Information Architecture and Navigation:**

The information architecture and navigation diagram for the Tree Enthusiast web application, depicted in the attachment, was crafted using the [Lucid app](https://www.lucidchart.com). The diagram serves as a testament to the CRUD (Create, Read, Update, Delete) functionality embedded within the application's framework.

Starting at the homepage, users are greeted with the option to delve into guided forest experiences. A decision node promptly distinguishes the pathways for visitors, who can choose to sign up or log in, and registered users, who have the facility to directly log into their accounts. The user profile is strategically placed as a central node that branches out into three distinct actions embodying the CRUD principles: viewing (Read), editing (Update), and deleting (Delete) their profile, which is indicative of the personalized experience the application offers.

The trees collection forms the heart of the Tree Enthusiast, showcasing an interactive array where visitors can browse (Read) and search for trees. Here, registered users are granted the capabilities to expand the collection by adding (Create) new trees, as well as curating their personal 'My Trees' collection through edit (Update) and delete (Delete) functions. This not only highlights the CRUD operations but also underscores user engagement and content management within the application.

Further enhancing the user interface, a contact route anchors the flowchart, extending users the courtesy to connect with the site administration or engage via social media, fostering a community-centric environment.

This meticulously constructed flowchart delineates the user journey within the Tree Enthusiast app, seamlessly integrating CRUD operations for an optimized user experience. It underscores the ease of navigation and intuitive interaction with the app's features, thereby ensuring a user-centric digital environment. 
<br>
<br>
For more details on the technologies used in the development of the Tree Enthusiast application, please refer to the [Technologies Used](#technologies-used) section or return to the [Table of Contents](#table-of-contents).

![Information Architecture and Navigation 1](./media/docs_images/architecture-and-navigation-diagram.png)

[Back to top ⇧](#table-of-contents)

#### SKELETON

- **Wireframes:** The wireframes were created using Balsamiq. The wireframes were created for desktop, tablet, and mobile devices. 

[Link to Wireframes](./media/docs_images/wireframes.png)

![Wireframes](./media/docs_images/wireframes.png)

_N.B. The wireframes were created before the project was started. The final project will abundantly differ from the wireframes._

[Back to top ⇧](#table-of-contents)

#### **SURFACE**

##### Imagery and Colour Scheme

The selection of images for the Tree Enthusiast app is a meticulous process that seeks to reinforce the application’s purpose of connecting nature lovers and providing a tranquil user experience. Each image is deliberately chosen for its visual appeal and its ability to evoke a sense of calm and serenity, mirroring the tranquility one might find in a forest. The images were created with DALL-E 3, a neural network that generates images from text descriptions.

![The selection of images for the Tree Enthusiast app](./media/docs_images/color-scheme-bg-imgs.png) 

[Back to top ⇧](#table-of-contents)

The overarching green palette, highlighted by the lush forest backgrounds, sets a thematic continuity that aligns with the app’s core subject—trees. This choice of imagery not only brings users closer to the subject matter but also serves as a constant visual reinforcement of the app’s theme. The incorporation of detailed macro photography, such as close-ups of sea buckthorn and vibrant foliage, further immerses users in the natural world, fostering a deeper connection with the content.

![The overlay, navbar and footer font colour](./media/docs_images/color-scheme-home.png)

The overlay colors on different screens and image cards are carefully chosen to not overpower the underlying images, ensuring that the content remains the focal point. These overlays utilize a subtle opacity that allows for legibility of text while maintaining the integrity of the images behind them. This delicate balance between visibility and aesthetics enhances user engagement without distracting from the app’s verdant imagery.

![The overlay, navbar and footer font colour](./media/docs_images/color-sceme-my_trees.png)

[Back to top ⇧](#table-of-contents)

In addition, the color of the font used in the navigation bar and the footer is optimized for readability against the variable backgrounds. The choice of a light-colored font on a darker background ensures legibility across diverse images, whether the backdrop is the dense green of a forest or the vivid oranges of sea buckthorn berries. This consistent color scheme across the app’s interface elements ensures a harmonious visual experience for users, regardless of the content they are viewing. To analise the colour palette developer used tools from [ColorSpace](https://mycolor.space/?hex=%23EFF4EB&sub=1).

![The overlay, navbar and footer font colour](./media/docs_images/colour-palette.png)


Favicons and profile images featuring silhouettes of trees and leaves reinforce the botanical focus of the app. They serve as a visual shorthand for the app’s purpose, providing a consistent and recognizable branding across various user interfaces.

![Favicon/App's Logo and prfile images](./media/docs_images/favicon-prof-imgs.png)

Overall, the design choices made in the Tree Enthusiast app are reflective of an intentional strategy to harmonize the visual elements with the user interface. By employing a consistent and nature-inspired color scheme, the app creates an immersive experience that is both visually cohesive and user-friendly. The seamless integration of imagery and interface elements contributes to a user experience that is both aesthetically pleasing and functionally intuitive, allowing users to navigate the app with ease while remaining engaged with its content.

[Back to top ⇧](#table-of-contents)

##### Typography

For the Tree Enthusiast application, we've embraced a typography approach that ensures clarity, accessibility, and optimal text rendering across various devices and operating systems. Instead of selecting custom typefaces, we've utilized the native font stack available in [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/content/reboot/), which adapts to the default system font of our users' operating systems. This not only provides a seamless user experience but also leverages the high-performance type rendering that users are accustomed to on their devices.

![Native font stack](./media/docs_images/fonts.png)

- For macOS and iOS devices, the UI will display in **San Francisco**, providing a crisp and adaptable interface that aligns with Apple's design aesthetics.
- **Segoe UI** will be used on Windows systems, which integrates smoothly with Microsoft's modern UI.
- Android devices will render the app in **Roboto**, Google's signature font that's been designed for legibility on digital screens.
- On Linux systems, **Noto Sans** offers a uniform appearance, supporting a wide range of scripts for international users.
- Fallback fonts, such as **Helvetica Neue**, **Arial**, and **sans-serif**, ensure that if the primary fonts are not available, the text still appears polished and readable.

Using the native font stack not only provides a comfortable and familiar reading experience but also aligns with our app's theme of natural elegance and simplicity. Our choice reflects our commitment to performance, sustainability, and user-centric design principles.

For more information on native font stacks and their benefits, please refer to this insightful [article by Smashing Magazine](https://www.smashingmagazine.com/2015/11/using-system-ui-fonts-practical-guide/).

##### Prototypes

For the development of the Tree Enthusiast app, a fully interactive prototype was not created due to the iterative nature of the development process. The application was built iteratively, with features being added and refined as needed. The initial wireframes served as a foundational guide, but the design evolved organically as the project progressed.

##### Feedback and Iteration

The development of Tree Enthusiast has been greatly informed by feedback from various sources. The guiding insights from a dedicated mentor provided the initial direction, while peer reviews contributed to refinements along the way. User feedback was invaluable, highlighting usability and design improvements that were iteratively integrated. This ongoing feedback loop has been crucial in shaping an app that meets the needs of tree enthusiasts while remaining agile and responsive to change. Each iteration has brought functional enhancements and design polish, ensuring that the app not only functions well but also provides a visually pleasing and intuitive user experience.

[Back to top ⇧](#table-of-contents)

## Accessibility

Ensuring website is accessible to all users is a core principle of the Tree Enthusiast app development. Developer have strived to meet accessibility standards to provide a user-friendly experience that is inclusive for individuals with disabilities.

To assess and enhance website's accessibility, developer utilized Lighthouse, an open-source, automated tool by Google that improves the quality of web pages. Lighthouse was instrumental in checking site's for accessibility issues.

The Tree Enthusiast app has been meticulously tested with Lighthouse Validation to ensure that it adheres to the best practices of web accessibility. As a result of commitment and continuous testing, the website currently holds a high accessibility score, reflecting its full accessibility for all users.

Developer is committed to maintaining and improving the accessibility of the Tree Enthusiast app as web standards evolve and as user feedback received. Developer's goal is to ensure that every user, regardless of their ability, can explore, share, and contribute to vast tree database effortlessly.

[Back to top ⇧](#table-of-contents)

## Database Design
Database design was made with [QuickDBD](https://www.quickdatabasediagrams.com/). The database is hosted on ElephantSQL and is a PostgreSQL database.

![Database Design](./media/docs_images/quickdbd-diagram.png)

![Database Design](./media/docs_images/quickdbd-diagram-1.png)

The database for the Tree Enthusiast app is designed to store user profiles, tree information, and contact messages. It utilizes the PostgreSQL database and the models are structured as follows:

- **Profile Model**: This model extends the built-in Django User model to store profile images using Cloudinary's cloud-based image management solution. It's linked to the User model with a one-to-one relationship, ensuring that each user has a single corresponding profile. The profile is automatically created or updated when a user registers or modifies their profile information.

- **Tree Model**: This model captures the details of individual trees. It includes fields for common names, tree types, origins, introductions, images, and habitats. Each tree is associated with a user through a foreign key relationship, allowing for easy tracking of which user added the tree. Timestamps for creation and updates are automatically managed by Django.

- **Message Model**: Designed to store contact form submissions, this model includes fields for the sender's name, email, optional subject, and the message body. Each message is timestamped upon creation to keep a record of when it was sent.

To visualize the relationships and structure, diagrams can be created using tools like [QuickDBD](https://www.quickdatabasediagrams.com/). The models are organized to facilitate the app's functionality in allowing users to manage their tree collection and communicate through the contact form.

[Back to top ⇧](#table-of-contents)

## Features

### Existing Features

#### Navbar
- The logo functions as a link to the homepage, ensuring users can always navigate back easily.
- Features a user-specific navigation experience; authenticated users can access options to add trees and manage their collections.
- Search functionality embedded in the navbar allows users to find specific trees.
- Adapts to different devices with a collapsible hamburger menu on smaller screens.

#### Footer
- Styled with Bootstrap for consistency and contains important links, including social media and contact information.
- Social media links open in new tabs to maintain user presence on the app.

#### User Authentication System
- Secure registration, login, and logout capabilities.
- Users can manage their profiles, with the option to update personal information or delete their account.
- Profile management includes a default profile image which can be replaced with a user-uploaded one.
- Show/Hide password functionality improves the user experience on authentication forms.

#### Home Page Features for Visitors and Users
- The **Home page** serves as an **inspirational gateway** into the app, highlighting the app's central theme of tree appreciation with a visually engaging design.
- **Visitors** are treated to **educational resources**, an **inspirational quote** related to the beauty of trees, and **links to guides** on tree identification and forest therapy.
- The page encourages exploration with quick access to resources about the benefits of forest bathing and outdoor therapy for mental health, complementing the information with links to authoritative external content.
- **Call-to-action buttons** prompt visitors to register or log in, offering a clear path to a more personalized experience, such as adding new trees or viewing their tree collection.
- **Registered users** receive a warm welcome by name and can navigate easily with tailored options like 'Add Tree' and 'My Trees', designed to enhance their interactive experience with the app.

#### Tree Management Features
- Users can add new tree entries with a form that accepts detailed information.
- Edit and delete capabilities allow users to manage their tree collection effectively.
- Individual tree detail pages offer comprehensive information and imagery.

#### Browsing Trees
- Visitors to the site can browse the tree collection without the need to register or log in, encouraging engagement with the app's content right from the start.
- Each tree is presented in a card layout with a clear image and the common name displayed, making it easy for users to visually scan and select trees of interest.
- Registered users have the added functionality of adding trees to their personal collection directly from the browse view, promoting interaction and personalized curation of content.
- The browsing page includes a user-friendly interface with pagination or infinite scroll (depending on implementation) to ensure a seamless browsing experience, even with a large number of entries.
- For both visitors and registered users, clicking on a tree card directs to a detailed view, offering a deeper dive into the information about the tree species, including its habitat, origin, and other engaging details.
- The browsing feature is fully responsive, ensuring that visitors and users have a consistent experience across all devices, whether they are at home on a desktop computer or on-the-go with a mobile device.

#### Search Functionality
- Allows for keyword searches throughout the tree database, displaying results in a visually pleasing card layout.

### Custom Error Pages
To enhance the user experience, our app includes customized error pages that guide users back to the app's main content when they encounter an error.

#### 404 Page Not Found
Our custom 404 page gently informs users that the page they are looking for cannot be found. It provides a clear and friendly message, assuring them that it's just a minor detour. The page features a serene forest background and offers a direct link to return to the homepage.

![404 Page](./media/docs_images/404_sc_sh.png)

#### 405 Method Not Allowed
When a user attempts an action that's not allowed, our 405 error page is there to guide them. It acknowledges the wrong turn with a calm forest backdrop and encourages users to return to the main path, offering a link back to the safety of the homepage.

#### 500 Internal Server Error
Unexpected server issues are addressed with our 500 error page. It reassures users that we are aware of the problem and are diligently working to fix it. While our digital environment recovers, users can click on the provided link to return to the homepage, which remains a bastion of tranquility and order amidst the chaos.

![500 Page](./media/docs_images/500_sc_sh.png)

Each error page maintains the app's theme, reflecting the natural and peaceful essence of our brand while providing users with a seamless and non-disruptive experience during their digital nature walks.

#### Responsive Layout
- Ensures a fluid experience on a variety of devices, with pages and components that adjust to screen sizes.

#### Additional UI Features
- Password visibility toggle for ease during authentication processes.
- Modal dialogs for critical actions:
  - Confirmations for logging out, deleting user profiles, and removing tree entries ensure intentional user interactions and prevent accidental data loss.
  - Modal forms for user and tree deletions include password confirmation to secure the process.

[Back to top ⇧](#table-of-contents)

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Issues and Bugs

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

[Back to top ⇧](#table-of-contents)

## Technologies Used

### Main Languages Used
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
    - HTML5 is used to structure the content of the website.
- [CSS3](https://en.wikipedia.org/wiki/CSS)
    - CSS3 is utilized for styling the website's content, with responsive design elements for mobile and desktop views.
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
    - JavaScript adds interactive elements to the website, enhancing user experience.
- [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
    - Python, combined with Django, forms the backbone of the website's backend logic.

### Frameworks, Libraries & Programs Used

#### Front-End
- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/)
    - Bootstrap 4.6 is used for its responsive design features and pre-designed components.
- [Font Awesome](https://fontawesome.com/)
    - Font Awesome provides icons used across the website.
- [Google Fonts](https://fonts.google.com/)
    - The project uses **Google Fonts** to style the website's fonts.

#### Back-End
- [Django](https://www.djangoproject.com/)
    - Django is the primary web framework used for rapid development and pragmatic design.
- [Cloudinary](https://cloudinary.com/)
    - Cloudinary is integrated for efficient image upload and management.
- [PostgreSQL](https://www.postgresql.org/)
    - PostgreSQL is used as the database for the website.
- [ElephantSQL](https://www.elephantsql.com/)
    - ElephantSQL for hosting of the database.
- [Heroku](https://www.heroku.com/)
    - Heroku for the website deployment.
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/)
    - For authentication, registration, and account management.
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
    - To manage Django forms rendering.
- [Pillow](https://pillow.readthedocs.io/en/stable/)
    - For image processing capabilities.
- [Python-Decouple](https://pypi.org/project/python-decouple/)
    - For managing sensitive configuration parameters.
- [Gunicorn](https://pypi.org/project/gunicorn/)
    - WSGI HTTP Server for running the Django application.
- [Psycopg2](https://pypi.org/project/psycopg2/)
    - PostgreSQL adapter for Python.
- [Python-Dotenv](https://pypi.org/project/python-dotenv/)
    - For managing environment variables.
- [Requests](https://pypi.org/project/requests/)
    - For sending HTTP requests.
- [DJ-Database-URL](https://pypi.org/project/dj-database-url/)
    - For database configuration.
- [OAuthlib](https://oauthlib.readthedocs.io/en/latest/)
    - For OAuth1 and OAuth2 functionalities.
- [PyJWT](https://pyjwt.readthedocs.io/en/latest/)
    - For encoding and decoding JSON Web Tokens.
- [Cryptography](https://pypi.org/project/cryptography/)
    - For cryptographic recipes and primitives.
- [EmailJS](https://www.emailjs.com/)
    - For creating a functional contact form.

#### Version Control and Deployment
- [Git](https://git-scm.com/)
    - Git for version control.
- [GitHub](https://github.com/)
    - For hosting the code repository.
- [Heroku](https://www.heroku.com/)
    - For deploying the website.

#### Design and Planning
- [Balsamiq](https://balsamiq.com/)
    - For creating wireframes.
- [QuickDBD](https://www.quickdatabasediagrams.com/)
    - For designing the database.

#### Testing and Validation
- [Lighthouse](https://developers.google.com/web/tools/lighthouse)
    - For checking website accessibility issues.
- [W3C Markup Validation Service](https://validator.w3.org/)
    - For validating HTML code.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - For validating CSS code.
- [JSHint](https://jshint.com/)
    - For checking JavaScript code.
- [CI Python Linter](https://pep8ci.herokuapp.com/)
    - For checking Python code compliance with PEP8.

#### Development Tools
- [Visual Studio Code](https://code.visualstudio.com/)
    - As a local IDE.
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)
    - For testing and debugging.
- [Mozilla Firefox](https://www.mozilla.org/en

[Back to top ⇧](#table-of-contents)

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

## Testing
For Testing details go to a separated file [TESTING.md](TESTING.md)


## Deployment
### Local Deployment

In order to make a local copy of this project, you can clone it. In your IDE Terminal, type the following command to clone the repository:

- `git clone https://github.com/tomdu3/books-for-life.git`

If done locally, the virtual environment needs to be created and activated. To do so, in your IDE Terminal, type the following commands:
```
python3 -m venv venv
```

If on Linux/MacOS, type the following command for activation:
```
source venv/bin/activate
```
On Windows type the following command for activation:
```
venv\Scripts\activate
```

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/tomdu3/books-for-life)

***

After cloning or opening the repository in Gitpod, you will need to:

1. Create your own `.env` file in the root level of the project:

```
SECRET_KEY=[your_secret_key]
DEBUG=True
DATABASE_URL=postgres://[username]:[password]@[host]:[port]/[database_name]
CLOUDINARY_URL=cloudinary://[api_key]:[api_secret]@[cloud_name]
```
**Ensure the `.env` file is added to your `.gitignore` file so it doesn't get pushed to a public repository.

If you don't have a Cloudinary account already, you will need to [Sign Up for Free](https://cloudinary.com/users/register/free) to host the static files in the project.

2. Run `pip3 install -r requirements.txt` to install required Python packages.

3. Migrate the database models using:
`python3 manage.py migrate`

4. Create a superuser with your own credentials:
`python3 manage.py migrate`

5. Run the Django sever:
`python manage.py runserver`
The address of the server will appear in the terminal window.
Add /admin to the address to access the Django admin panel using your superuser credentials.

### Heroku Deployment

Sign up to [Heroku](https://heroku.com/) for free if you don't already have an account.

1. Create a new app in Heroku.

2. In the Resources tab of your app in the Heroku dashboard, click Add-Ons and select Heroku Postgres. Select Hobby Dev - Free as your plan.

3. When Heroku Postgres is installed, click the Settings tab in the Heroku Dashboard.
Click Reveal Config Vars, and add the same variables from your `.env` file here, except for `DEBUG`, as you don't want debug mode on the deployed project.

4. Copy the value of `DATABASE_URL` from the Config Vars. In your `settings.py` file, comment out the default database configuration, and add a new one with the Postgres url.

```
DATABASES = {
    'default': dj_database_url.parse('your DATABASE_URL here'),
}
```

5. Migrate the database models using:
`python3 manage.py migrate`

6. Create a superuser with your own credentials:
`python3 manage.py migrate`

7. Create a file called `Procfile` (no extension) containing the following:
```
web: gunicorn core.wsgi
```

8. Run `pip3 install -r requirements.txt` to install required Python packages.

9. Add the url of your Heroku app ('https://books-4-life-2d26bdf04dec.herokuapp.com/') to your `settings.py` file:

```
ALLOWED_HOSTS = [
    'books-4-life-2d26bdf04dec.herokuapp.com',...
]
```

10. Disable collect static so that Heroku doesn't try to collect static files when you deploy by adding the following to your Heroku Config Vars in the Settings tab of Heroku dashboard:

```
DISABLE_COLLECTSTATIC=1
```

The same variable has to be removed from Heroku Config Vars when you want to collect static files (for the testing and final deployment).

11. Stage and commit your files to GitHub
```
git add . 
git commit -m "Commit message"
git push
```

12. In the Heroku dashboard for your App, select Deploy.
Under Deployment Method, choose GitHub and search for your repository and click Connect.

13. Select Enable Automatic Deployments, and then Deploy Branch. Heroku will build the App from the branch you selected.

14. Now whenever you push your commits to GitHub, Heroku will rebuild the application.

### Forking the GitHub Repository
The project can be forked in order to make a copy of the original repository and propose changes to the project owner using Pull Requests.
That can be done by following these steps:
First, log in to GitHub and locate the [Project's Repository](github.com/tomdu3/books-for-life).
At the top of the Repository, on the right side of the page, locate the "Fork" button.
A copy of the Repository should now be in your GitHub account.
You can now propose changes to the Repository by creating a Pull Request.

### Live deployment
The web site is deployed on Heroku and can be found [here](https://books-4-life-2d26bdf04dec.herokuapp.com/).


[Back to top ⇧](#table-of-contents)

## Credits

### Code
- Navbar code was adapted from [Bootstrap](https://getbootstrap.com/docs/5.0/examples/navbars/).
- The code for the contact form was adapted from [EmailJS](https://www.emailjs.com/).
- The code for the custom 404 page was adapted from [Django Docs](https://docs.djangoproject.com/en/3.2/ref/views/#error-views).

- The code for the text animations on the Homepage:
    - Main title:
    "Flip Text Animation" adapted from [https://alvarotrigo.com/blog/css-text-animations/](https://alvarotrigo.com/blog/css-text-animations/)
    - Second title:
    [https://codepen.io/andysanchez-dev/pen/GYPevV*/](https://codepen.io/andysanchez-dev/pen/GYPevV*/)
- The code for the footer social media links was adapted from:
[https://mdbootstrap.com/docs/standard/navigation/footer/](https://mdbootstrap.com/docs/standard/navigation/footer/)

- The code for the Password Validators was adapted from:
[https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators](https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators) and
[https://code.djangoproject.com/ticket/28163](https://code.djangoproject.com/ticket/28163)

For the rest of the code, the developer relied on Code Institute's course material,
the [stackoverflow](https://stackoverflow.com/), [Django documentation](https://docs.djangoproject.com/en/3.2/), and John Elder's [Codemy](https://codemy.com/).

### Content
- The content of the website was written by the developer.

### Media
- The images used in the website were obtained from [Unsplash](https://unsplash.com/).
- The site logo was created using [favicon.io](https://favicon.io/).
- The mockup image at the beginning of this file was created using [Am I Responsive](http://ami.responsivedesign.is/).
- The Shakespeare image and the default book image of a monk were generated by [DALL-E 2](https://openai.com/dall-e-2).

### Acknowledgements
- Seun Owonikoko, my mentor, for her guidance and support. Without her, this project wouldn't be possible or remotely as interesting.
- Rebecca Tracey-Timoney, our cohort lead, for her wise guidance and all the material she shared with me. All similarities between this project and her material are _**not coincidental**_.
- Code Institute's Slack community for their support and feedback.
- Code Institute's Tutor Support for their support and feedback (I don't want to give names. I hope that's ok with you, Rebecca :-)).
- My dear colleagues and friends from the Code Institute's Full Stack Web Development, especially Sirinya, Victoria, Richard, Lauren, Ho, for their support and testing services.
- My friends: Boris, Zeljka and Dragan for helping me with the testing.