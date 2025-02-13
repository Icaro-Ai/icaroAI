document.getElementById("question-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    let question = document.getElementById("question").value;
    let responseDiv = document.getElementById("response");
    
    let response = await fetch("/ask", {
        method: "POST",
        headers: { "Content-Type": "application/x-www-form-urlencoded" },
        body: `question=${encodeURIComponent(question)}`
    });
    
    let data = await response.json();
    responseDiv.textContent = "Resposta: " + data.answer;
});
