<h2>STACCC💵</h2>
  Backend: <a href="docs.djangoproject.com">Django</a><br>
  Frontend: <a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a>/
            <a href="https://developer.mozilla.org/en-US/docs/Web/CSS">CSS</a>/
            <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript">JS</a><br>
  Database: <a href="https://www.sqlite.org/docs.html">SQLite</a> (until MVP)<br>

  Database Schema: <a href="https://drawsql.app/teams/individual-69/diagrams/osac-forum">Click here.</a><br>
 
<h2>Contributing</h2>

Fork the repo
  ```sh
   Click the "Fork" button on the top right corner.
   ```

Clone the repo
   ```sh
   git clone https://github.com/"your-github-username"/OSAC-Forum 
   ```

To run project on your PC,

Install dependencies
  ```sh
  pip install -r requirements.txt
  #using virtual environment is highly recommended
  ```

Initialize the database and run server
  ```sh
  python manage.py migrate
  python manage.py runserver
  ```

Accessing Admin Dashboard

Create a superuser
  ```sh
  python manage.py createsuperuser
  ```
Navigate to `http://localhost:8000/admin` for admin login.

<h3>
Contribute on frontend without python knowledge:</h3>
<ul>
<li>Code a html file in your PC as you normally would. </li>
<li> Switch to dummy_template branch by running:   
    ```sh
    git switch dummy_template
    ```  
</li>
  <li>visit dummy_template folder and paste your code to the specified files.</li>
 <br> <i>Add the CSS inside the <b>style</b> tag and JS inside <b>script</b> tag in the same HTML file</i>.<br>
 Send Pull Request to the dummy_temp branch.
</ul>

