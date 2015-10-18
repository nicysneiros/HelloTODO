
todolist.controller('TODOListCtrl', function ($scope, DataSrcTODOList) {

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
			console.log(response);	
		})
	}
	
})