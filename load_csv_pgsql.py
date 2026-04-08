import dlt
import pandas as pd

# 🔹 Extract + Transform
@dlt.resource
def csv_data():
    df = pd.read_csv(r"C:\MLakshmi\ML\backup\ML\Myself\Python practice\dlt_prac\dlt_mysql\data\sales.csv")
    # clean column names
    df.columns = df.columns.str.strip().str.lower()
    
    # remove duplicates
    df = df.drop_duplicates()
    
    yield df.to_dict(orient="records")


# 🔹 Pipeline
def run_pipeline():
    pipeline = dlt.pipeline(
        pipeline_name="csv_to_postgres",
        destination="postgres",
        dataset_name="etl_data"
    )

    load_info = pipeline.run(csv_data(), table_name="sales")
    print(load_info)



if __name__ == "__main__":
    run_pipeline()