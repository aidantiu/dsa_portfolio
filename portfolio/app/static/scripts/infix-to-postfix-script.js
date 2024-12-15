// Clear button for clearing all contents
function clearAll() {
    document.getElementById('inputBox').value = '';
    document.querySelector('.postfix-result').innerHTML = '<span class="placeholder-text">Your postfix expression will appear here...</span>';
}