var app = angular.module('toDo', []);
app.controller('toDoController', function($scope, $http) {
    // $scope.todoList = [{todoText: 'Finish this app', done: false}];
    $http.get('/plates').then(function(response) {
        $scope.todoList = [];
        for (var i = 0; i < response.data.length; i++) {

            var todo = {};
            todo.Name = response.data[i].NAME
            todo.Plate = response.data[i].PLATE
            todo.Remove = false
            todo.id = response.data[i].id
            $scope.todoList.push(todo);
        }
        console.log (response.data)
        
    });
    $scope.saveData = function() {
        var data = {NAME: $scope.todoInput_NAME, PLATE: $scope.todoInput_PLATE, }
        $http.post('/plates', data)
        console.log (data)
    }
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
            }
        })
    }
})