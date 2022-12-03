use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;

fn main() {
    let mut total_score = 0;
    for line in read_lines("input.txt") {
        let str_line = line.unwrap();
        let left : HashSet<u8> = str_line[..str_line.len() / 2].bytes().collect();
        let right : HashSet<u8> = str_line[str_line.len() / 2..].bytes().collect();
        let common : HashSet<u8> = left.intersection(&right).copied().collect();
        total_score += common.iter().map(|&i| if i < 91 {(i - 65 + 27) as i32} else {(i - 97 + 1) as i32}).sum::<i32>();
    }
    println!("{}", total_score);
}

fn read_lines<P>(filename: P) -> io::Lines<io::BufReader<File>>
where P: AsRef<Path>, {
    let file = File::open(filename).unwrap();
    io::BufReader::new(file).lines()
}
