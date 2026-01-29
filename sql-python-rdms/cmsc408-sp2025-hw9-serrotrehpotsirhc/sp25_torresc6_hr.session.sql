DROP TABLE IF EXISTS wdi_data_stacked;

CREATE TABLE wdi_data_stacked AS
SELECT `Country Code`, `Indicator Code`, '1960' AS year_code, `1960` AS value
FROM world_bank_data.wdi_data
UNION
SELECT `Country Code`, `Indicator Code`, '1970', `1970` FROM world_bank_data.wdi_data
UNION
SELECT `Country Code`, `Indicator Code`, '1980', `1980` FROM world_bank_data.wdi_data
UNION
SELECT `Country Code`, `Indicator Code`, '1990', `1990` FROM world_bank_data.wdi_data
UNION
SELECT `Country Code`, `Indicator Code`, '2000', `2000` FROM world_bank_data.wdi_data
UNION
SELECT `Country Code`, `Indicator Code`, '2010', `2010` FROM world_bank_data.wdi_data
UNION
SELECT `Country Code`, `Indicator Code`, '2020', `2020` FROM world_bank_data.wdi_data;
