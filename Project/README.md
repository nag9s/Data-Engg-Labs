# Data Literacy Workshop - Day 1

Welcome to the Data Literacy Workshop! This workshop is designed to give you a hands-on experience with the initial stages of a data science project: Data Acquisition, Data Cleaning, and Data Validation.

## Workshop Overview

In this workshop, we will be working on a real-world scenario to understand the importance of data quality and how to achieve it. By the end of this workshop, you will be able to:

*   Understand the importance of data acquisition from various sources.
*   Perform data cleaning to handle inconsistencies, and missing values.
*   Validate the data to ensure its accuracy and reliability for analysis.
*   Gain hands-on experience with Python libraries like Pandas for data manipulation.

**Duration:** ~3 hours. This workshop is distributed on a preconfigured VM with the environment
already set up; `requirements.txt` at the repo root documents the exact dependencies for
reference (`pip install -r requirements.txt` if you ever need to rebuild the environment).

## Folder Structure

This repository is structured to help you navigate through the workshop resources easily. Here's a breakdown of the folders:

*   `DataSet/`: This folder contains the raw datasets we will be using during the workshop
    (`settlement.csv`, `api.csv`, `mongo.jsonl`), the field reference (`Dataset_Definitions.xlsx`),
    the mock API server (`mock_api.py`), and the generator script used to produce the data
    (`Generate_Data_Script_WithFault.py`).
    *   `DataSet/Practice/`: A second, distinct dataset (same schema, different seed/fault mix)
        generated for the practice notebooks, with its own mock API server so a practice run
        never touches the workshop's live data or outputs.
*   `SessionMaterials/`: Short, self-contained concept primers (`regex_validation_sample.ipynb`,
    `merge_sample.ipynb`, `coalesce_sample.ipynb`, `deduplication_sample.ipynb`). The workshop
    notebook links to the relevant primer right before the exercise that needs it.
*   `PracticeNotebooks/`: Two distinct practice notebooks for after the workshop, both using the
    `DataSet/Practice/` dataset so you aren't just replaying memorized answers:
    *   `PracticeNotebook_1.ipynb`: the full end-to-end pipeline again, on new data.
    *   `PracticeNotebook_2.ipynb`: a focused drill on the exercises learners find hardest
        (regex validation, coalescing, MCC/currency normalization, deduplication) —
        acquisition and merging are provided, so you can jump straight into the cleaning logic.
*   `ProcessedData/`: Any output generated from our data processing and cleaning will be saved in this folder.
*   `ReferenceNotebook.ipynb`: This notebook contains the complete code that will be covered in the workshop. You can use it as a reference.
*   `WorkshopNotebook.ipynb`: This is the main notebook we will be working on together during
    the workshop. Each function-writing exercise is scaffolded with a signature and docstring
    (fill in the body), and checkpoint cells after each major step confirm your answer before you
    build on it.

## Project Scenario: Global Mart's Transactional Data Unification

**Scenario:**

Global Mart, a (fictional) large retail company, needs to create a single, reliable source of truth for their customer transactions. This unified dataset is crucial for various business functions, including fraud detection, financial reconciliation, and customer analytics. The data is currently spread across three different systems, each representing a stage in the transaction lifecycle:

1.  **Settlement System (CSV):** This is the final, authoritative record of all transactions. It's used for financial settlement and reconciliation.
2.  **Authorization API (Real-time):** This system captures transaction data at the point of sale (POS), providing real-time information as a transaction is authorized.
3.  **Enrichment Database (MongoDB):** This database contains additional information related to risk, tokenization, and other classifications that are updated frequently.

**The Challenge:**

The data from these three sources is not consistent. There are overlapping fields with conflicting values, missing information, and different data formats. For example:
*   A transaction might have a different merchant category code (MCC) in the settlement file compared to the authorization API.
*   The real-time API might contain details about the point-of-sale environment that are not in the other systems.
*   The MongoDB database contains risk scores that are not available elsewhere.

**Our Goal:**

Our goal in this workshop is to act as data engineers for Global Mart. We will take the raw data from the `DataSet` folder and work through the following steps using the `WorkshopNotebook.ipynb`:

1.  **Data Acquisition:** Load data from the three sources: a CSV file, a paginated web API, and a MongoDB database.
2.  **Data Cleaning and Standardization:**
    *   Handle missing values and common placeholders (e.g., "NA", "9999").
    *   Normalize and standardize fields like merchant category codes, currency codes, and region codes.
    *   Validate key identifiers like transaction IDs and masked Primary Account Numbers (PANs).
3.  **Data Merging and Canonicalization:**
    *   Merge the three datasets based on a common transaction ID.
    *   Resolve conflicts between the sources by defining a clear order of precedence (e.g., the settlement data is the most reliable).
    *   Create a single, "canonical" dataset with a consistent schema.
4.  **Persist the Final Dataset:** Save the cleaned and unified dataset to a SQLite database for downstream use in analytics, dashboards, or machine learning models.

This final, cleaned dataset will be the single source of truth for all transactional data at Global Mart.

Let's get started!
