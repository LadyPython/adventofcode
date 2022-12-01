use std::{io, io::prelude::*};

fn main() {
    let mut global_max_1 = 0;
    let mut global_max_2 = 0;
    let mut global_max_3 = 0;
    let mut current_max = 0;
    for line in io::stdin().lock().lines() {
        let str_line = line.unwrap();
        if str_line.is_empty() {
            if current_max > global_max_1 {
                global_max_3 = global_max_2;
                global_max_2 = global_max_1;
                global_max_1 = current_max;
            }
            else if current_max > global_max_2 {
                global_max_3 = global_max_2;
                global_max_2 = current_max;
            }
            else if current_max > global_max_3 {
                global_max_3 = current_max;
            }
            current_max = 0;
            continue;
        }
        current_max += str_line.parse::<i32>().unwrap();
    }
    println!("{}", global_max_1 + global_max_2 + global_max_3);
}
