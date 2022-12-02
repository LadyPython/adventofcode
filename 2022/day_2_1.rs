use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashMap;
use std::str;

fn score(c1: &str, c2: &str) -> i32 {
    let hm = HashMap::from([
        ("A", 1),
        ("B", 2),
        ("C", 3),
        ("X", 1),
        ("Y", 2),
        ("Z", 3),
    ]);
    let (t1, t2) = (hm[c1], hm[c2]);
    (t2 - t1 + 1 + 3) % 3 * 3 + t2
}

fn main() {
    let mut total_score = 0;
    for line in read_lines("input.txt") {
        let str_line = line.unwrap();
        let (c1, c2) = str_line.split_once(' ').unwrap();
        total_score += score(c1, c2);
    }
    println!("{}", total_score);
}

fn read_lines<P>(filename: P) -> io::Lines<io::BufReader<File>>
where P: AsRef<Path>, {
    let file = File::open(filename).unwrap();
    io::BufReader::new(file).lines()
}
