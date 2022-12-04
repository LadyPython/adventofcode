use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut answer = 0;
    for line in read_lines("input.txt") {
        let str_line = line.unwrap();
        let (first, second) = str_line.split_once(',').unwrap();
        let first_vec : Vec<i32> = first.split('-').map(|x| x.parse::<i32>().unwrap()).collect();
        let l1 = first_vec[0];
        let r1 = first_vec[1];
        let second_vec : Vec<i32> = second.split('-').map(|x| x.parse::<i32>().unwrap()).collect();
        let l2 = second_vec[0];
        let r2 = second_vec[1];
        answer += ((l2 - l1) * (r2 - r1) <= 0) as i32;
    }
    println!("{}", answer);
}

fn read_lines<P>(filename: P) -> io::Lines<io::BufReader<File>>
where P: AsRef<Path>, {
    let file = File::open(filename).unwrap();
    io::BufReader::new(file).lines()
}
