
todolist.controller('TODOListCtrl', function ($scope, $filter, DataSrcTODOList) {

	DataSrcTODOList.getTODOLists().then(function (response) {
		console.log(response);
		$scope.todolists = response.data;
	})

	$scope.addTODOList = function () {
		$scope.todolists.unshift({noTitle: true})
	}

	$scope.saveTODOList = function (todolist) {
		todolist.noTitle = false;
		
		console.log(todolist);
		
		if(!todolist.title){
			todolist.title = 'Undefined';
		}
		
		DataSrcTODOList.saveTODOList(todolist).then(function(response){
			
			if (!todolist.id){
				var newTodolist = response.data;
				for (var i = 0; i < $scope.todolists.length; i++){
					if ($scope.todolists[i].title === todolist.title){
						$scope.todolists[i] = newTodolist;
					}
				}
			}
			console.log(response);
			console.log($scope.todolists);	
		})
	}
	
	$scope.deleteTODOList = function (todolist) {
		$scope.todolists = $filter('filter')($scope.todolists, {id: '!' + todolist.id})
		
		DataSrcTODOList.deleteTODOList(todolist.id).then(function(response) {
			console.log(response);
		})
	}
})