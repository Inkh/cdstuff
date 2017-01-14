var students = [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
];

var users = {
 'Students': [
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }

function names(){
    console.log("Students:")
    counter = 0;
    for(var i = 0;i < students.length; i++){
        counter += 1;
        console.log(counter + " - " + students[i].first_name + " " + students[i].last_name + " " + (students[i].first_name.length + students[i].last_name.length));
    }
}

names();

function combine(){
    students = users[0];
    teachers = users[1];
    counter = 0;
    for(var i = 0;i < students.length; i++){
        counter += 1;
        console.log(counter + " - " + students[i].first_name + " " + students[i].last_name + " " + (students[i].first_name.length + students[i].last_name.length));
    }

}
combine();
