app = angular.module 'example.app.basic', []

app.controller 'AppController', ['$scope', '$http', ($scope, $http) ->
    $scope.posts = []
    $http.get('/plates').then (result) ->
        angular.forEach result.data, (item) ->
            $scope.posts.push item
]