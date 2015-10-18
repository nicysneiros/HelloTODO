
var baseURL = 'http://127.0.0.1:8000/'
var urlTODOList = baseURL + 'todolists'

todolist.factory('DataSrcTODOList', function($http) {
	return {
		getTODOLists: function (){
			return $http.get(urlTODOList);
		},
		
		saveTODOList: function (todolist) {
			if(todolist.id){
				return $http.put(urlTODOList + '/' + todolist.id + '/', todolist);
			} else {
				return $http.post(urlTODOList + '/', todolist);
			}
		},
		
		deleteTODOList: function (id){
			return $http.delete(urlTODOList + '/' + id + '/');
		}
	}
})