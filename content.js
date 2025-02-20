// List of abusive words (basic filtering before API call)
const abusiveWords = ["idiot", "stupid", "dumb", "moron", "loser", "clown", "pathetic", "trash",
    "worthless", "suck", "shut up", "ugly", "annoying", "disgusting", "failure",
    "nonsense", "awful", "terrible", "lame", "hopeless", "hate", "kill yourself",
    "dumbass", "jackass", "bullshit", "shithead", "piss off", "asshole",
    "bastard", "bitch", "fuck", "motherfucker", "cunt", "dickhead", "prick",
    "slut", "whore", "cock", "retard", "freak", "screw you" 
];

// Function to check for abusive words using the Flask API
async function checkAbuse(comment) {
    try {
        let response = await fetch("http://127.0.0.1:5000/detect", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ text: comment.innerText })
        });

        let result = await response.json();
        if (result.abusive) {
            comment.style.backgroundColor = "red"; // Highlight abusive comments
            comment.style.color = "white";
        }
    } catch (error) {
        console.error("Error calling API:", error);
    }
}

// Function to highlight abusive words (local detection)
function highlightAbusiveWords() {
    const comments = document.querySelectorAll("#content-text"); // YouTube comments selector

    comments.forEach(comment => {
        let containsBadWord = false;

        abusiveWords.forEach(word => {
            if (comment.innerText.toLowerCase().includes(word)) {
                containsBadWord = true;
                let regex = new RegExp(`\\b${word}\\b`, "gi"); // Match full words only
                comment.innerHTML = comment.innerHTML.replace(regex, match => {
                    return `<span style="background-color: red; color: white; padding: 2px; border-radius: 3px;">${match}</span>`;
                });
            }
        });

        // If no bad words were found locally, check with the Flask API
        if (!containsBadWord) {
            checkAbuse(comment);
        }
    });
}

// Function to observe new comments being loaded dynamically
function observeComments() {
    const targetNode = document.body; // Observing the whole body
    const config = { childList: true, subtree: true };

    const observer = new MutationObserver(() => {
        highlightAbusiveWords();
    });

    observer.observe(targetNode, config);
}

// Run function when page loads
setTimeout(() => {
    highlightAbusiveWords();
    observeComments();
}, 3000);
