use clap::Parser;
use std::fs;
use std::io;
use std::io::BufRead;
use std::time::Instant;

/// A simple CLI example using clap
#[derive(Parser)]
struct Args {
    input: String,
    #[arg(long, short, default_value = "1")]
    part: Option<i32>,
}

fn part_one(list1: &[i32], list2: &[i32]) {
    let mut total_diff = 0;
    for (a, b) in list1.into_iter().zip(list2.into_iter()) {
        let diff = (a - b).abs();
        total_diff += diff
    }
    println!("total diff = {}", total_diff);
}

fn part_two(list1: &[i32], list2: &[i32]) {
    let mut total_count = 0;

    for num in list1 {
        let count = list2.iter().filter(|&x| x == num).count();
        let res = (count as i32) * num;
        println!("{} is {} times in list2", num, count);
        total_count += res;
    }
    println!("total diff = {}", total_count);
}

fn main() -> io::Result<()> {
    let start = Instant::now(); // start timer
    let args = Args::parse();

    // Open the file
    let file = fs::File::open(&args.input)?;

    // Collect all lines into a vector
    let reader = io::BufReader::new(file);

    let mut list1: Vec<i32> = Vec::new();
    let mut list2: Vec<i32> = Vec::new();

    for maybe_line in reader.lines() {
        let line = maybe_line.unwrap();
        let parts: Vec<&str> = line.split_whitespace().collect();
        assert_eq!(parts.len(), 2);
        if let (Ok(num1), Ok(num2)) = (parts[0].parse::<i32>(), parts[1].parse::<i32>()) {
            list1.push(num1);
            list2.push(num2);
        }
    }

    match args.part {
        Some(part) => match part {
            1 => {
                list1.sort();
                list2.sort();
                part_one(&list1, &list2);
            }
            2 => part_two(&list1, &list2),
            _ => {}
        },
        None => {}
    }

    println!("Program ran in: {:?}", start.elapsed());
    Ok(())
}
