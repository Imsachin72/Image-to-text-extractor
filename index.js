function copyText() {
    var text = document.getElementById("extractedText").textContent;
    navigator.clipboard.writeText(text).then(() => {
      alert("Text copied to clipboard!");
    });
  }