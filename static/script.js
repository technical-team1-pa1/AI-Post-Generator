async function generatePost() {
    const topic = document.getElementById('topic').value.trim();
    const includeEmojis = document.getElementById('include-emojis').checked;
    const hashtagCount = document.getElementById('hashtag-count').value;

    if (!topic) {
        alert('Please enter a topic');
        return;
    }

    // Show loading
    document.getElementById('loading').classList.remove('hidden');
    document.getElementById('result').classList.add('hidden');

    try {
        const response = await fetch('/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 
                topic: topic,
                include_emojis: includeEmojis,
                hashtag_count: hashtagCount
            })
        });

        const data = await response.json();
        
        if (data.status === 'success') {
            document.getElementById('post-content').textContent = data.post;
            document.getElementById('result').classList.remove('hidden');
        } else {
            alert('Error generating post: ' + data.message);
        }
    } catch (error) {
        alert('Error generating post: ' + error.message);
    } finally {
        document.getElementById('loading').classList.add('hidden');
    }
}

function copyToClipboard() {
    const postContent = document.getElementById('post-content').textContent;
    navigator.clipboard.writeText(postContent)
        .then(() => alert('Post copied to clipboard!'))
        .catch(err => alert('Failed to copy: ' + err));
} 