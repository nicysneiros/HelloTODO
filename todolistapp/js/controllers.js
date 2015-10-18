
todolist.controller('TODOListCtrl', function ($scope, DataSrcTODOList) {
	
	DataSrcTODOList.getTODOLists().then(function(response) {
		console.log(response);
	})
	
})