var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
];


function names(){
    console.log("Students:")
    counter = 0;
    for(var i = 0;i < students.length; i++){
        counter += 1;
        console.log(counter + " - " + students[i].first_name + " " + students[i].last_name + " " + (students[i].first_name.length + students[i].last_name.length));
    }
}

names();
