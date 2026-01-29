use polars::prelude::*;

pub fn process_data(mut df: DataFrame) -> DataFrame {
    // Example: fill nulls and normalize numeric columns
    for col in df.get_columns_mut() {
        if let Ok(float_col) = col.f64() {
            let filled = float_col.fill_null(FillNullStrategy::Mean).unwrap();
            let normalized = &filled / filled.max().unwrap();
            *col = Series::new(col.name(), normalized);
        }
    }
    df
}
