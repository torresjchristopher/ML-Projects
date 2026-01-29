mod pipeline;
mod io;
mod schema;

use pipeline::process_data;
use io::{read_csv, write_csv};

fn main() {
    let input_path = "data/sample.csv";
    let output_path = "data/cleaned.csv";

    let df = read_csv(input_path).expect("Failed to read input file");
    let cleaned_df = process_data(df);
    write_csv(&cleaned_df, output_path).expect("Failed to write output");
}
