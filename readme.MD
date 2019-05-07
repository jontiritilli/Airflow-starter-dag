# Workflow Management Using Airflow

## Introduction to Airflow Concepts

  ### **Directed Acyclic Graph (DAG):**
  > A DAG is a collection of the small tasks, which represent a larger more complex job, along with the relationships and dependencies between the tasks. A DAG can be expressed visually as a graph with nodes and edges, where the nodes represent tasks and the edges represent dependencies between tasks and the order in which the tasks must be completed. They represent the workflow that you want to orchestrate and monitor. “Acyclic” means that the graph does not work in cycles. This means means workflows must have a definitive beginning and end.
  ### **Operators:**
  > Represent the work being done within the tasks that compose a DAG. Specifically, an operator represents a single task in a DAG. Airflow provides many pre-defined classes and it's also flexible  with what you can run as tasks. This includes classes for common tasks, like BashOperator, PythonOperator, EmailOperator, OracleOperator, etc. On top of the multitude of operator classes available, Airflow provides the ability to define your own operators. As a result, a task in your DAG can do almost anything you want, and you can schedule and monitor it using Airflow.
  ### **Tasks:**
  > A running instance of an operator. During the instantiation, you can define specific parameters associated with the operator and the parameterized task becomes a node in a DAG.
---
## Airflow Installation

1. **Pull the image from the Docker repository**
    ```
    docker pull puckel/docker-airflow
    ```
1. **Verify image downloaded**
    ```
    docker images
    ```
1. **Run the image and link a volume for storing and editing our scripts. This will allow us to easily use an IDE or Git for versioning**
    ```
    docker run --name <give it a name> -d -p 8080:8080 -v /path/to/dags/on/your/local/machine/:/usr/local/airflow/dags puckel/docker-airflow webserver
    ```
1. Go to [the admin panel and see it running](http://localhost:8080/admin/)
---
## Access the Airflow Instance and Install NodeJS

1. **List all the running Docker images**
    ```
    docker ps
    ```
    * You will see a list of images (or one if no others exist), it should include `airflow-migration`
1. **SSH into the Docker image bash terminal**
    ```
    docker exec -ti airflow-migration bash
    ```
---
## Common Commands

### Backfill
    airflow backfill <DAG.py> -s <yyyy-mm-dd> -e <yyyy-mm-dd>
---