use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;

fn main() {
    let mut answer = 0;
    for line in read_lines("input.txt") {
        let str_line = line.unwrap();
        let bytes_line = str_line.as_bytes();
        for i in 0..bytes_line.len() - 14 {
            if bytes_line[i..i + 14]
                .into_iter()
                .collect::<HashSet<_>>()
                .len() == 14 {
                answer += i + 14;
                break;
            }
        }
    }
    println!("{answer}");
}

fn read_lines<P>(filename: P) -> io::Lines<io::BufReader<File>>
    where P: AsRef<Path>, {
    let file = File::open(filename).unwrap();
    io::BufReader::new(file).lines()
}
  
