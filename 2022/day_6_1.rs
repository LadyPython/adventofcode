use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut answer = 0;
    for line in read_lines("input.txt") {
        let str_line = line.unwrap();
        let bytes_line = str_line.as_bytes();
        for i in 0..bytes_line.len()-3 {
            if bytes_line[i] != bytes_line[i + 1] &&
                bytes_line[i] != bytes_line[i + 2] &&
                bytes_line[i] != bytes_line[i + 3] &&
                bytes_line[i + 1] != bytes_line[i + 2] &&
                bytes_line[i + 1] != bytes_line[i + 3] && 
                bytes_line[i + 2] != bytes_line[i + 3] {
                answer += i + 4;
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
