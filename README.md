# auto_login
automatic login to riot client

<h1> Current Functionality </h1>
    - Hardcoded login script
    - Hardcoded sign out and sign in with different account
    - reads command line args

<h3> Issues </h3>
    [] how to wait for program to open, currently guessing using time.sleep(5)
    [] test if program is already open
    [] what to do if password is incorrect
    [] reading from file increases time complexity O(n) 

<h2> Goals </h2>
    [] Ultimate goal is for the program to maintain functionality on any computer (while making some assumptions about the environment)
    [] Have the program find and keep track of relevant coordinates automatically
    [] Login without hardcoded values using feature above
    [] Have a persisting settings file which contains passwords and relevant coordinates
    [] Hash and salt entered passwords for extra security


