use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;
use std::collections::HashSet;

fn to_priorities(c: u8) -> i32 {
    if c < 91 {(c - 65 + 27) as i32} else {(c - 97 + 1) as i32}
}

fn main() {
    let mut total_score = 0;
    let mut lines = read_lines("input.txt");
    while let (Some(line1), Some(line2), Some(line3)) = (lines.next(), lines.next(), lines.next()) {
        let part1 : HashSet<u8> = line1.unwrap().bytes().collect();
        let part2 : HashSet<u8> = line2.unwrap().bytes().collect();
        let part3 : HashSet<u8> = line3.unwrap().bytes().collect();
        let common : HashSet<u8> = part1.intersection(&part2).copied().collect::<HashSet<u8>>().intersection(&part3).copied().collect();
        total_score += common.iter().map(|&i| to_priorities(i)).sum::<i32>();
    }

    println!("{}", total_score);
}

fn read_lines<P>(filename: P) -> io::Lines<io::BufReader<File>>
where P: AsRef<Path>, {
    let file = File::open(filename).unwrap();
    io::BufReader::new(file).lines()
}
