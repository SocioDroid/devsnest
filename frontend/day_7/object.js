//1.program to list the properties of a  JavaScript object

let student={
    firstName:"Aditi",
    sclass:"B. tech",
    rollno:"06",
}

console.log(student)

//2.program to delete the rollno property from the following object.
// let student={
//     firstName:"Aditi",
//     sclass:"B. tech",
//     rollno:"06", 
// }

console.log(student)
delete student.rollno
console.log(student)

//3.program to get the length of a JavaScript object
var library = [
    { author: 'Bill Gates', title: 'The Road Ahead',
    readingStatus: true }, 
    { author: 'Steve Jobs', title: 'Walter Isaacson', 
    readingStatus: true }, 
    { author: 'Suzanne Collins',title: 'Mockingjay: The Final Book of The Hunger Games', 
    readingStatus: false }
]
for(let book=0;book<library.length;book++){
    console.log(library[book].title,library[book].readingStatus)
    
}

//4.program to display the reading status (i.e. display book name, author name and reading status) of the following books.
var library = [ 
    {
        author: 'Bill Gates',
        title: 'The Road Ahead',
        readingStatus: true
    },
    {
        author: 'Steve Jobs',
        title: 'Walter Isaacson',
        readingStatus: true
    },
    {
        author: 'Suzanne Collins',
        title:  'Mockingjay: The Final Book of The Hunger Games', 
        readingStatus: false
    }];
 
//5.program to get the volume of a Cylinder with four decimal places using object classes.


//6.program to sort an array of JavaScript objects.
var library = [ 
   { author: 'Bill Gates', title: 'The Road Ahead', libraryID: 1254},
   { author: 'Steve Jobs', title: 'Walter Isaacson', libraryID: 4264},
   { author: 'Suzanne Collins', title: 'Mockingjay: The Final Book of The Hunger Games', libraryID: 3245}
   ];

function sort_by_title(a,b) 
 {
  if (a.title < b.title)
    return -1;
  if (a.title > b.title)
    return 1;
  return 0;
 }

console.log(library.sort(sort_by_title));