use polars::prelude::*;
use std::error::Error;

pub fn read_csv(path: &str) -> Result<DataFrame, Box<dyn Error>> {
    let df = CsvReader::from_path(path)?
        .infer_schema(None)
        .has_header(true)
        .finish()?;
    Ok(df)
}

pub fn write_csv(df: &DataFrame, path: &str) -> Result<(), Box<dyn Error>> {
    let mut file = std::fs::File::create(path)?;
    CsvWriter::new(&mut file)
        .has_header(true)
        .finish(df)?;
    Ok(())
}
