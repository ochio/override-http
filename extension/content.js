const links = document.querySelectorAll("[target='_blank']");

for (const link of links) {
	link.addEventListener("click", (e) => {
		e.preventDefault();
		chrome.runtime.sendMessage(
			{
				contentScriptQuery: "post",
				endpoint: "http://localhost:8080/",
				destination: link.getAttribute("href"),
			},
			(response) => {},
		);
	});
}
