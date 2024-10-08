# Test Cases for Login/Registration Functionality

## Test Case 1: Valid Registration
- **Objective**: Ensure that a user can register with valid details.
- **Preconditions**: The user is on the registration page.
- **Steps**:
  1. Enter valid username, email, and password.
  2. Click on the 'Register' button.
- **Expected Result**: User is successfully registered and redirected to the dashboard.

## Test Case 2: Registration with Existing Email
- **Objective**: Ensure that a user cannot register with an email that is already in use.
- **Preconditions**: The email is already registered.
- **Steps**:
  1. Enter a valid username, an existing email, and a password.
  2. Click on the 'Register' button.
- **Expected Result**: An error message is displayed indicating the email is already in use.

## Test Case 3: Invalid Email Format Registration
- **Objective**: Ensure that a user cannot register with an invalid email format.
- **Preconditions**: The user is on the registration page.
- **Steps**:
  1. Enter a valid username, an invalid email format (e.g., 'user@.com'), and a password.
  2. Click on the 'Register' button.
- **Expected Result**: An error message is displayed indicating the email format is incorrect.

## Test Case 4: Password Strength Requirement
- **Objective**: Ensure that the password meets the strength requirements.
- **Preconditions**: The user is on the registration page.
- **Steps**:
  1. Enter a valid username, a valid email, and a weak password (e.g., '12345').
  2. Click on the 'Register' button.
- **Expected Result**: An error message is displayed indicating the password does not meet the strength requirements.

## Test Case 5: Valid Login
- **Objective**: Ensure that a registered user can log in with valid credentials.
- **Preconditions**: The user is on the login page.
- **Steps**:
  1. Enter valid email and password.
  2. Click on the 'Login' button.
- **Expected Result**: User is successfully logged in and redirected to the dashboard.

## Test Case 6: Invalid Login (Wrong Password)
- **Objective**: Ensure that a user cannot log in with an incorrect password.
- **Preconditions**: The user is on the login page.
- **Steps**:
  1. Enter a valid email and an incorrect password.
  2. Click on the 'Login' button.
- **Expected Result**: An error message is displayed indicating the login credentials are incorrect.

## Test Case 7: Login with Unregistered Email
- **Objective**: Ensure that a user cannot log in with an unregistered email.
- **Preconditions**: The user is on the login page.
- **Steps**:
  1. Enter an unregistered email and any password.
  2. Click on the 'Login' button.
- **Expected Result**: An error message is displayed indicating the email is not registered.

## Test Case 8: Password Reset Request
- **Objective**: Ensure that a user can request a password reset.
- **Preconditions**: The user is on the login page.
- **Steps**:
  1. Click on the 'Forgot Password' link.
  2. Enter a registered email.
  3. Click on the 'Submit' button.
- **Expected Result**: A password reset email is sent to the user.

## Test Case 9: Password Reset Email
- **Objective**: Ensure that the password reset email is sent to the user.
- **Preconditions**: The user is on the 'Forgot Password' page.
- **Steps**:
  1. Enter a registered email address.
  2. Click on the 'Submit' button.
- **Expected Result**: A confirmation message is displayed, and a password reset email is sent to the user's email address.
