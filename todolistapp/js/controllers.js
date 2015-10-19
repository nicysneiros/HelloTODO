
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
	
	$scope.addTask = function(todolist, task) {
		if(!task.id){
			task.todolist = todolist.id;
			task.order_list = todolist.tasks.length + 1;
			task.done = false;
		}
		
		DataSrcTODOList.saveTask(task).then(function(response) {
			task.editting = false;
			
			if (!task.id){
				var newTask = response.data
				task.add = null;
				
				for(var i = 0; i < $scope.todolists.length; i++){
					if($scope.todolists[i].id === newTask.todolist){
						$scope.todolists[i].tasks.push(newTask);
					}
				}
			}
			
			console.log(response);
		})
	}
	
	$scope.checkTask = function(task){
		//task.done = !task.done;
		DataSrcTODOList.saveTask(task).then(function(response) {
			console.log(response);
		})
	}
	
	$scope.deleteTask = function(todolist, task){
		var tasks = $filter('filter')(todolist.tasks, {id: '!' + task.id});
		
		for (var i = 0; i < $scope.todolists.length; i++){
			if($scope.todolists[i].id === todolist.id){
				$scope.todolists[i].tasks = tasks;
			}
		}
		
		DataSrcTODOList.deleteTask(task.id).then(function(response) {
			console.log(response);
		})
	}
})