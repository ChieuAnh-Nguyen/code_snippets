import os


def install_airtable(AIRFLOW_VERSION, PYTHON_VERSION):
    """EX: AIRFLOW_VERSION = '2.2.2' 
    PYTHON_VERSION = '3.8' 
    """
    # Install Airflow using the constraints file
    CONSTRAINT_URL = f"https://raw.githubusercontent.com/apache/airflow/constraints-{AIRFLOW_VERSION}/constraints-{PYTHON_VERSION}.txt"
    # For example: https://raw.githubusercontent.com/apache/airflow/constraints-2.2.2/constraints-3.6.txt
    installer = f'pip install apache-airflow=={AIRFLOW_VERSION} --constraint {CONSTRAINT_URL}'
    os.system(installer)


def main():
    AIRFLOW_VERSION = "2.2.2"
    PYTHON_VERSION = "3.8"
    install_airtable(AIRFLOW_VERSION, PYTHON_VERSION)


if __name__ == "__main__":
    main()
