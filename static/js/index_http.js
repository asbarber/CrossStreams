function downloadResource(resourceId, numUsers, onCompleted) {
	var resourceData = "";
	var request = {
			"id": resourceId,
			"numUsers": numUsers,
			"sequenceNum": 0
	};

	var executeRequest = function () {
		$.get("http://localhost:8888/http/files", request, onMessage);
	};

	var onMessage = function (data, status) {
		resourceData += atob(data);
		request.sequenceNum++;

		if (request.sequenceNum < request.numUsers) {
			executeRequest();
		}
		else {
			onCompleted(btoa(resourceData));
		}
	};

	executeRequest();
}


function downloadImage(numUsers) {
	downloadResource("defaultImage", 3, function (data) {
		document.getElementById("streamedImage").src = "data:image/jpeg;base64," + data;
	});
}

function downloadVideo(numUsers) {
	downloadResource("defaultVideo", 1, function (data) {
		document.getElementById("streamedVideo").src = "data:video/mp4;base64," + data;
	});
}

function downloadText(numUsers) {
	downloadResource("defaultText", 2, function (data) {
		document.getElementById("streamedText").value = atob(data);
	});
}


function message(data, status) {
	alert(JSON.stringify(data));
}

function listFiles() {
	$.get("http://localhost:8888/http/files", {}, message);	
}

function addFile() {

}

function getFile() {

}

function updateFile() {

}

function deleteFile() {

}

function voteFile() {

}
