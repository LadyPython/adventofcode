use std::{io, io::prelude::*};
use std::cmp;

fn main() {
    let mut global_max = 0;
    let mut current_max = 0;
    for line in io::stdin().lock().lines() {
        let str_line = line.unwrap();
        if str_line.is_empty() {
            global_max = cmp::max(current_max, global_max);
            current_max = 0;
            continue;
        }
        current_max += str_line.parse::<i32>().unwrap();
    }
    println!("{}", global_max);
}
