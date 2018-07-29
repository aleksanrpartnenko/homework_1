var app = angular.module('toDo', []);
app.controller('toDoController', function($scope, $http) {
    // $scope.todoList = [{todoText: 'Finish this app', done: false}];
    $http.get('/plates').then(function(response) {
        $scope.todoList = [];
        for (var i = 0; i < response.data.length; i++) {

            var todo = {};
            todo.Name = response.data[i].NAME
            todo.Plate = response.data[i].PLATE
            //todo.Remove = false
            todo.id = response.data[i].id
            $scope.todoList.push(todo);
        }
        console.log (response.data)
        
    });
    $scope.saveData = function() {
        var data = {NAME: $scope.todoInput_NAME, PLATE: $scope.todoInput_PLATE, }
        $http.post('/plates', data)
        console.log (data)
    };
    $scope.todoAdd = function() {
        $scope.todoList.push({Name: $scope.todoInput_NAME, Plate: $scope.todoInput_PLATE, Remove: false});
        $scope.todoInput_NAME = '';
        $scope.todoInput_PLATE = '';
    };
    $scope.remove = function() {
        var oldList = $scope.todoList;
        //console.log (todo)
        $scope.todoList = [];
        angular.forEach(oldList, function(todo) {
            if (todo.Remove) {
                $http.delete('/plates/' + todo.id + '/');
            } else {
                $scope.todoList.push(todo);
                var new_data =  {NAME: todo.Name, PLATE: todo.Plate, }
                console.log (new_data)
                $http.put('/plates/' + todo.id + '/', new_data);
            }
        })
    };
})

var app = angular.module('ngMessagesExample', ['ngMessages']);

var app = angular.module('toUpdate', []);
app.controller('UpdateDoController', function($scope, $http, $location, $window) {
    var searchObject = $location.absUrl();
    var re = /\d+$/i;
    var DEV_ID =  searchObject.match(re);
    console.log (DEV_ID[0])
    $http.get('/plates/' + DEV_ID[0]  + '/').then(function(response) {
        $scope.UPDATE = [];
        var todo = {};
            todo.Name = response.data.NAME
            todo.Plate = response.data.PLATE
            todo.id = response.data.id
            $scope.UPDATE.push(todo);
        console.log (response.data)
        
    });
    $scope.todoUppdate= function() {
        $scope.UPDATE.push({Name: $scope.todoInput_NAME, Plate: $scope.todoInput_PLATE, Remove: false});
        
    };
    $scope.saveData = function() {
        
        var data = {NAME: $scope.todoInput_NAME, PLATE: $scope.todoInput_PLATE, }
        $http.put('/plates/'+ DEV_ID[0]  + '/', data)
        //$location.path('/success')
        $window.location.href ="/angular"
        
        
    };

}
);