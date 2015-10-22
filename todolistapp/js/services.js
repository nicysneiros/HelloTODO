
var baseURL = 'http://127.0.0.1:8000/'
var urlTODOList = baseURL + 'todolists/todolists/'
var urlTask = baseURL + 'todolists/task/'
var urlAccessToken = baseURL + 'users/register-by-token/'

todolist.factory('DataSrcTODOList', function($http) {
	return {
		getTODOLists: function (accessToken){
			var configAuth = {
                headers: {
                    'Authorization': 'Bearer ' + accessToken
                }
            }
			return $http.get(urlTODOList, configAuth);
		},
		
		saveTODOList: function (todolist, accessToken) {
			var configAuth = {
                headers: {
                    'Authorization': 'Bearer ' + accessToken
                }
            }
			
			if(todolist.id){
				return $http.put(urlTODOList + todolist.id + '/', todolist, configAuth);
			} else {
				return $http.post(urlTODOList, todolist, configAuth);
			}
		},
		
		deleteTODOList: function (id, accessToken){
			var configAuth = {
                headers: {
                    'Authorization': 'Bearer ' + accessToken
                }
            }
			return $http.delete(urlTODOList + id + '/', configAuth);
		},
		
		saveTask: function (task, accessToken) {
			var configAuth = {
                headers: {
                    'Authorization': 'Bearer ' + accessToken
                }
            }
			
			if(task.id){
				return $http.put(urlTask + task.id + '/', task, configAuth);
			} else {
				return $http.post(urlTask, task, configAuth);
			}
		},
		
		deleteTask: function (id, accessToken){
			var configAuth = {
                headers: {
                    'Authorization': 'Bearer ' + accessToken
                }
            }
			
			return $http.delete(urlTask + id + '/', configAuth);
		}
	}
});

todolist.factory('DataSrcUser', function ($http) {
	var accessToken;
	
	return {
		getExternalAccessToken: function (externalAccessToken, provider) {
			return $http.get(urlAccessToken + provider + '/?access_token=' + externalAccessToken);
		},
		
		setAccessToken: function(accessTokenInfo){
			accessToken = accessTokenInfo;
			window.localStorage.setItem("accessToken", accessToken);
		},
		
		getAccessToken: function() {
			accessToken = window.localStorage.getItem("accessToken");
			return accessToken;
		}
	}
})