CREATE OR REPLACE PROCEDURE `speedy-coder-434214-t0.ETL_PROCESSING.sp_transform_and_load_smallcap`()
BEGIN
  -- Step 1: Data Transformation - Example 1: Filter out records with null values in key fields
  CREATE OR REPLACE TABLE `speedy-coder-434214-t0.ETL_PROCESSING.TRANSFORMED_SMALLCAP` AS
  SELECT
    Timestamp,
    `Stock Name`,
    Open,
    High,
    Low,
    Close,
    Volume,
    `Market Cap`,
    `PE Ratio`,
    CAST(`Industry PE` AS FLOAT64) AS `Industry PE`,
    `Debt to Equity`,
    `Dividend Yield`,
    ROE
  FROM
    `speedy-coder-434214-t0.ETL_PROCESSING.STAGING_SMALLCAP`
  WHERE
    `Stock Name` IS NOT NULL
    AND Timestamp IS NOT NULL;

  -- Step 2: Data Transformation - Example 2: Calculate additional metrics
  CREATE OR REPLACE TABLE `speedy-coder-434214-t0.ETL_PROCESSING.TRANSFORMED_SMALLCAP_FINAL` AS
  SELECT
    *,
    (Close - Open) AS Price_Change,  -- Example metric: Price Change
    CASE
      WHEN `PE Ratio` > `Industry PE` THEN 'Overvalued'
      WHEN `PE Ratio` < `Industry PE` THEN 'Undervalued'
      ELSE 'Fairly Valued'
    END AS Valuation,  -- Example metric: Valuation classification
    SAFE_DIVIDE(`Market Cap`, `Debt to Equity`) AS Capital_Leverage_Ratio  -- Example metric: Capital Leverage Ratio
  FROM
    `speedy-coder-434214-t0.ETL_PROCESSING.TRANSFORMED_SMALLCAP`;

  -- Step 3: Check if the target table exists; if not, create it
  BEGIN
    DECLARE target_table_exists BOOL DEFAULT FALSE;

    -- Check if the table exists in the dataset's __TABLES__ view
    SET target_table_exists = (
      SELECT COUNT(*)
      FROM `speedy-coder-434214-t0.ETL_PROCESSING.__TABLES__`
      WHERE table_id = 'TARGET_SMALLCAP'
    ) > 0;

    -- Create the table if it doesn't exist
    IF NOT target_table_exists THEN
      CREATE TABLE `speedy-coder-434214-t0.ETL_PROCESSING.TARGET_SMALLCAP` (
        Timestamp TIMESTAMP,
        `Stock Name` STRING,
        Open FLOAT64,
        High FLOAT64,
        Low FLOAT64,
        Close FLOAT64,
        Volume FLOAT64,
        `Market Cap` INT64,
        `PE Ratio` FLOAT64,
        `Industry PE` FLOAT64,
        `Debt to Equity` FLOAT64,
        `Dividend Yield` FLOAT64,
        ROE FLOAT64,
        Price_Change FLOAT64,
        Valuation STRING,
        Capital_Leverage_Ratio FLOAT64
      );
    END IF;
  END;

  -- Step 4: Load transformed data into the target table
  INSERT INTO `speedy-coder-434214-t0.ETL_PROCESSING.TARGET_SMALLCAP`
  SELECT
    Timestamp,
    `Stock Name`,
    Open,
    High,
    Low,
    Close,
    Volume,
    `Market Cap`,
    `PE Ratio`,
    `Industry PE`,
    `Debt to Equity`,
    `Dividend Yield`,
    ROE,
    Price_Change,
    Valuation,
    Capital_Leverage_Ratio
  FROM
    `speedy-coder-434214-t0.ETL_PROCESSING.TRANSFORMED_SMALLCAP_FINAL`;

END;