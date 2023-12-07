chrome.runtime.onMessage.addListener((message, sender, sendResponse) => {
	if (!message) {
		sendResponse({
			status: false,
			reason: "message is missing",
		});
	} else if (message.contentScriptQuery === "post") {
		fetch(message.endpoint, {
			method: "POST",
			body: JSON.stringify({ destination: message.destination }),
			headers: {
				Accept: "application/json",
				"Content-Type": "application/json",
				mode: "cors",
				credentials: true,
			},
		}).catch(console.error);
	}

	return true;
});
