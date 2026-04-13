# FirecREST Operators for Airflow

## Goal

Write custom [Apache Airflow operators](https://airflow.apache.org/docs/apache-airflow/stable/howto/custom-operator.html) that use FirecREST to execute compute-intensive DAG tasks on an HPC cluster.

The DAG combines tasks that run locally on a laptop with tasks that must run on a supercomputer. Your operators extend Airflow's `BaseOperator` and use PyFirecREST in their `execute` method:

```python
class FirecRESTCustomOperator(BaseOperator):
    def __init__(self, system, script, working_dir, **kwargs):
        super().__init__(**kwargs)
        self.system = system
        self.script = script
        self.working_dir = working_dir

    def execute(self, context):
        # PyFirecREST operations
        ...
```

## Installation

Create a virtual environment and install the required packages:

```bash
python -m venv .demo-env
source .demo-env/bin/activate
pip install apache-airflow pyfirecrest==3.7.1
```

Set your credentials as environment variables (the base operator reads these):

```bash
export FIRECREST_CLIENT_ID=<client-id>
export FIRECREST_CLIENT_SECRET=<client-secret>
export AUTH_TOKEN_URL=https://<token-url>
export FIRECREST_URL=https://<firecrest-url>
```

## Launch Airflow

Initialize the database and start Airflow in standalone mode:

```bash
export AIRFLOW_HOME=$HOME/airflow-demo
airflow db migrate
airflow standalone
```

The dashboard is available at <http://127.0.0.1:8080>. Credentials are printed at startup and saved to `$AIRFLOW_HOME/standalone_admin_password.txt`.

!!! tip
    Set `load_examples = False` in `$AIRFLOW_HOME/airflow.cfg` to start with a clean dashboard.

    To change the port, set `web_server_port` under the `[api]` section in `airflow.cfg`.

## Deploy the DAG

Register the DAG and install the custom operators:

```bash
mkdir -p $AIRFLOW_HOME/dags
cp use-case-airflow-operator/airflow-dag.py $AIRFLOW_HOME/dags/

# Install the custom operators into the Python path
pip install -e use-case-airflow-operator/
```

Open `airflow-dag.py` and set `workdir` to the absolute path of the `airflow-operators` directory and `username` to your Piz Daint username.

## Exercise

The provided DAG (`firecrest_example`) models a crystal structure simulation workflow with these tasks:

1. Detect that a new structure has been produced
2. Upload the structure and its pseudopotential to Piz Daint
3. Submit a job to compute its properties
4. Download the output
5. Log relevant values to a table
6. Delete the structure file

The file [`firecrest_airflow_operators.py`](https://github.com/eth-cscs/firecrest-training/blob/main/use-case-airflow-operator/firecrest_airflow_operators.py) contains the operator implementations to complete.

Trigger the DAG from the Airflow dashboard by clicking the **Play** button next to `firecrest_example`.
