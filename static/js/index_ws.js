function downloadResource(resourceId, numUsers, onCompleted) {
	var ws = new WebSocket("ws://127.0.0.1:8888/ws/files");
	var resourceData = "";
	var command = "getSegment";

	var REQUEST_BODY = 1;
	var request = [
		command,
		{
			"id": resourceId,
			"numUsers": numUsers,
			"sequenceNum": 0
		}
	];

	var executeRequest = function () {
		ws.send(JSON.stringify(request));
	}

	ws.onopen = function () {
		executeRequest();
	};

	ws.onmessage = function (evt) {
		resourceData += atob(evt.data);
		request[REQUEST_BODY].sequenceNum++;

		if (request[REQUEST_BODY].sequenceNum < request[REQUEST_BODY].numUsers) {
			executeRequest();
		}
		else {
			onCompleted(btoa(resourceData));
		}
	};
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
