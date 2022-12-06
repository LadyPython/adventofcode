use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    let mut arr : Vec<String> = vec![
        "VCWLRMFQ".to_string(),
        "LQD".to_string(),
        "BNCWGRSP".to_string(),
        "GQBHDCL".to_string(),
        "SZFLGV".to_string(),
        "PNGD".to_string(),
        "WCFVPZD".to_string(),
        "SMDPC".to_string(),
        "CPMVTWNZ".to_string()
    ];
    
    for line in read_lines("input.txt") {
        let str_line = line.unwrap();
        let tokens : Vec<&str> = str_line.split(' ').collect();
        let cnt = tokens[1].parse::<usize>().unwrap();
        let from = tokens[3].parse::<usize>().unwrap() - 1;
        let to = tokens[5].parse::<usize>().unwrap() - 1;

        let part : String = arr[from][..cnt].chars().rev().collect();
        arr[from] = arr[from][cnt..].to_string();
        arr[to] = format!("{}{}", part, arr[to]);
    }
    for s in arr {
        print!("{}", s.chars().nth(0).unwrap());
    }
}

fn read_lines<P>(filename: P) -> io::Lines<io::BufReader<File>>
where P: AsRef<Path>, {
    let file = File::open(filename).unwrap();
    io::BufReader::new(file).lines()
}
