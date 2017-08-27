
console.log(`\n`);
var day_number = "day number";
var current_value = "Our Money";
for( let starting_dollar = 1, day = 1 ; day <= 31; starting_dollar = starting_dollar * 2, day++) {
    console.log(`${day_number} ${day} ${current_value} ${starting_dollar}`);
}
console.log(`\n`);