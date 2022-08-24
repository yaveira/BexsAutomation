# BexsAutomation
Project to testing a Fake API


#### Config the project
Environment
======
Create a virtual environment to installing dependencies of the project

    python -m venv venv

#### Behave Python API Testing


Tag
======
Use tags in feature files to indicate feature.

    @test

These tag will be used to indicate that BDD is in development.

    @wip

###### Example to run

    behave features/back_antecipation_duplicates -t @test


#### Allure Manual
======
1. First test run

        behave features/back_bank_accounts.features -t @authenticity -f allure_behave.formatter:AllureFormatter -o allure/results
    
2. Generate report for first test run

        allure generate allure/results/ -o allure/reports --clean
        
3. Remove old files

        rm -r allure/results
  
4. Open Allure Report

        allure open allure/reports