CI/CD Classroom Demo — SauceDemo Automation Project (v4.0)
----------------------------------------------------------

1️⃣ Objective:
   Demonstrate how to:
   - Run Selenium tests automatically via GitHub Actions
   - Use API calls for initialization and verification
   - Generate and upload HTML reports

2️⃣ Prerequisites:
   - GitHub account
   - This repository pushed to a GitHub repo
   - Docker Desktop installed and running

3️⃣ Steps to Demonstrate:

   LOCAL:
   -------
   1. Start Selenium Grid:
        docker compose up -d
   2. Run tests manually:
        pytest -n 2 -v --html=src/reports/report.html --self-contained-html
   3. Observe HTML report in src/reports/

   GITHUB ACTIONS (CI/CD):
   -----------------------
   1. Commit and push any change to the 'main' branch.
   2. Open the "Actions" tab in your GitHub repository.
   3. Watch:
        - Grid starting in Docker
        - Tests running (parallel)
        - HTML report being uploaded
   4. Download and review report artifact ("test-report.zip").

4️⃣ Test Explanation:
   - 'test_login_with_api.py' uses both API and UI testing.
   - API: verifies mock backend user data.
   - UI: performs SauceDemo login.
   - API: verifies session via mock endpoint.

Enjoy showing your students a full CI/CD + API + Selenium integration demo!
